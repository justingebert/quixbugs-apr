import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 14})

df = pd.read_json('aggregated_metrics.json')

# Aggregate to ensure one row per (model, max_attempts)
df_grouped = df.groupby(['model', 'max_attempts']).agg({
    'repair_success_rate': 'mean',
    'avg_execution_time_per_issue': 'mean',
    'avg_cost_per_issue': 'mean'
}).reset_index()

metrics = [
    ('repair_success_rate', 'Repair Success Rate (%)', 'Success Rate (%)'),
    ('avg_execution_time_per_issue', 'Average Time per Issue (s)', 'Time (s)'),
    ('avg_cost_per_issue', 'Average Cost per Issue ($)', 'Cost ($)')
]

# Custom model order
custom_order = [
    "gemini-2.0-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.5-flash-lite-preview-06-17",
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "gpt-4.1-nano",
    "gpt-4.1-mini",
    "gpt-4.1",
    "o4-mini",
    "claude-3-5-haiku-latest",
    "claude-3-7-sonnet-latest",
    "claude-sonnet-4-0"
]

# Custom abbreviations
custom_abbr = {
    "gemini-2.0-flash-lite": "G20F-L",
    "gemini-2.0-flash": "G20F",
    "gemini-2.5-flash-lite-preview-06-17": "G25F-L",
    "gemini-2.5-flash": "G25F",
    "gemini-2.5-pro": "G25P",
    "gpt-4.1-nano": "GPT4N",
    "gpt-4.1-mini": "GPT4M",
    "gpt-4.1": "GPT4",
    "o4-mini": "O4M",
    "claude-3-5-haiku-latest": "C35H",
    "claude-3-7-sonnet-latest": "C37S",
    "claude-sonnet-4-0": "CS40"
}

# Filter only models present in the data and keep custom order
model_names = [name for name in custom_order if name in df_grouped['model'].unique()]
abbr_labels = [custom_abbr[name] for name in model_names]

attempts = [1, 3]
colors = sns.color_palette("Set2", n_colors=2)

for metric, title, ylabel in metrics:
    values = []
    for attempt in attempts:
        vals = []
        for model in model_names:
            row = df_grouped[(df_grouped['model'] == model) & (df_grouped['max_attempts'] == attempt)]
            if not row.empty:
                vals.append(row.iloc[0][metric])
            else:
                vals.append(0)
        values.append(vals)

    x = np.arange(len(model_names))
    width = 0.35

    fig, ax = plt.subplots(figsize=(16, 8 if metric == 'avg_cost_per_issue' else 7))
    bars1 = ax.bar(x - width/2, values[0], width, label='1', color=colors[0])
    bars2 = ax.bar(x + width/2, values[1], width, label='3', color=colors[1])
    ax.set_xticks(x)
    ax.set_xticklabels(abbr_labels)
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_ylabel(ylabel)
    ax.set_xlabel('Model')
    ax.legend(title='Attempts', loc='upper left')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # # Use log scale for cost diagram
    # if metric == 'avg_cost_per_issue':
    #     ax.set_yscale('log')
    #     ax.text(
    #         0.99, 0.95, "Log scale", ha='right', va='top', transform=ax.transAxes,
    #         fontsize=12, color='gray', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=0.2)
    #     )

    # Annotate bars for all diagrams, horizontal numbers with requested formatting
    for rects in [bars1, bars2]:
        for rect in rects:
            height = rect.get_height()
            if height > 0:
                if metric == 'avg_execution_time_per_issue':
                    label = f'{round(height):d}'
                elif metric == 'avg_cost_per_issue':
                    label = f'{height:.4f}'
                elif metric == 'repair_success_rate':
                    label = f'{height:.1f}'
                else:
                    label = str(height)
                # For cost, place label above the bar for better fit
                y_offset = 8 if metric == 'avg_cost_per_issue' else 5
                ax.annotate(label,
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, y_offset),
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=9 if metric == 'avg_cost_per_issue' else 10, rotation=0)

    # Model abbreviation legend below the plot, left-aligned and compact
    # abbr_text = "\n".join([f"{custom_abbr[name]}: {name}" for name in model_names])
    # plt.gcf().text(
    #     0.0, 0.0, abbr_text, ha='left', va='top', fontsize=12,
    #     bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.2')
    # )

    plt.tight_layout(rect=[0, 0.08, 1, 1])
    plt.savefig(f'{metric}_per_model_grouped.png', bbox_inches='tight')
    plt.close()

# --- diagrams: CI run duration vs total execution time (stacked bar), split by attempts ---

for attempt in [1, 3]:
    ci_df = df[df['max_attempts'] == attempt].copy()
    ci_df['run_label'] = ci_df.apply(
        lambda row: f"{custom_abbr.get(row['model'], row['model'])}", axis=1
    )
    model_order_map = {name: i for i, name in enumerate(custom_order)}
    ci_df['model_order'] = ci_df['model'].map(model_order_map)
    ci_df = ci_df.sort_values(['model_order'])

    x = np.arange(len(ci_df))
    width = 0.6

    ci_overhead = ci_df['ci_run_duration'] - ci_df['total_execution_time']
    exec_time = ci_df['total_execution_time']

    # Use the same color palette as above
    stacked_colors = [colors[0], colors[1]]

    fig, ax = plt.subplots(figsize=(max(12, len(ci_df)*0.7), 7))
    bars_exec = ax.bar(x, exec_time, width, label='APR Core Execution Time', color=stacked_colors[0])
    bars_overhead = ax.bar(x, ci_overhead, width, bottom=exec_time, label='CI Overhead', color=stacked_colors[1])

    ax.set_xticks(x)
    ax.set_xticklabels(ci_df['run_label'], rotation=0, ha='center')
    ax.set_title(f'CI Run Duration: APR Core Execution Time + CI Overhead  (40 Bugs, Attempts={attempt})', fontsize=18, fontweight='bold')
    ax.set_ylabel('Seconds')
    ax.set_xlabel('Model')
    ax.legend(loc='upper left')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Annotate total bar height and execution time only (omit overhead annotation if too small)
    for i, (exec_h, overhead_h) in enumerate(zip(exec_time, ci_overhead)):
        total_h = exec_h + overhead_h
        if exec_h > 0:
            ax.annotate(f'{round(exec_h):d}', xy=(x[i], exec_h/2), ha='center', va='center', fontsize=10, color='white')
        ax.annotate(f'{round(total_h):d}', xy=(x[i], total_h), xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

    plt.tight_layout()
    plt.savefig(f'ci_vs_exec_time_per_run_stacked_attempts_{attempt}.png', bbox_inches='tight')
    plt.close()
