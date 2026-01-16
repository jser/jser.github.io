#!/usr/bin/env python3
"""
JSer.info 15th Anniversary Chart Generation Script (English Version)

Usage:
    python generate_15th_charts_en.py

Output:
    15th_*_en.png files will be generated
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D
import numpy as np

# Output directory
OUTPUT_DIR = '.'

# =============================================================================
# Data Definition
# =============================================================================

# Yearly data (2011-2025)
YEARS_FULL = list(range(2011, 2026))
ARTICLES = [915, 1126, 1269, 1147, 1043, 1078, 1068, 921, 790, 810, 789, 712, 737, 638, 552]
POSTS = [65, 57, 57, 59, 56, 59, 54, 58, 53, 53, 53, 54, 53, 47, 41]
PER_POST = [14.1, 19.8, 22.3, 19.4, 18.6, 18.3, 19.8, 15.9, 14.9, 15.3, 14.9, 13.2, 13.9, 13.6, 13.5]
AVG_CHARS = [61.9, 52.5, 57.6, 69.7, 64.5, 61.7, 78.6, 82.9, 90.2, 97.8, 101.1, 101.9, 106.4, 101.3, 108.2]
JP_RATE = [22.2, 18.0, 15.0, 10.0, 7.7, 6.5, 5.5, 4.5, 3.3, 3.5, 4.0, 4.2, 4.5, 4.5, 4.7]


# =============================================================================
# Individual Chart Functions
# =============================================================================

def create_yearly_posts():
    """Yearly article and post count trends"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax_twin = ax.twinx()

    bars = ax.bar(YEARS_FULL, ARTICLES, color='#3498db', alpha=0.7, label='Articles', width=0.7)
    line = ax_twin.plot(YEARS_FULL, POSTS, 'o-', color='#e74c3c', linewidth=2, markersize=6, label='Posts')

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Number of Articles', color='#3498db', fontsize=12)
    ax_twin.set_ylabel('Number of Posts', color='#e74c3c', fontsize=12)
    ax.set_title('Yearly Article and Post Count Trends', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 1500)
    ax_twin.set_ylim(30, 75)
    ax.set_xticks(YEARS_FULL)
    ax.set_xticklabels(YEARS_FULL, rotation=45, ha='right')

    legend_elements = [mpatches.Patch(facecolor='#3498db', alpha=0.7, label='Articles'),
                       Line2D([0], [0], color='#e74c3c', marker='o', label='Posts')]
    ax.legend(handles=legend_elements, loc='upper right')
    ax.annotate('Peak\n1,269', xy=(2013, 1269), xytext=(2015, 1350),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_yearly_posts_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_yearly_posts_en.png")


def create_quantity_quality():
    """Quality over Quantity shift"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax_twin = ax.twinx()

    bars = ax.bar(YEARS_FULL, PER_POST, color='#9b59b6', alpha=0.7, width=0.7, label='Items per Post')
    line = ax_twin.plot(YEARS_FULL, AVG_CHARS, 's-', color='#27ae60', linewidth=2, markersize=6, label='Avg Characters')

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Items per Post', color='#9b59b6', fontsize=12)
    ax_twin.set_ylabel('Avg Description Length (chars)', color='#27ae60', fontsize=12)
    ax.set_title('Quality over Quantity: The Shift', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 30)
    ax_twin.set_ylim(40, 130)
    ax.set_xticks(YEARS_FULL)
    ax.set_xticklabels(YEARS_FULL, rotation=45, ha='right')

    legend_elements = [mpatches.Patch(facecolor='#9b59b6', alpha=0.7, label='Items per Post'),
                       Line2D([0], [0], color='#27ae60', marker='s', label='Avg Characters')]
    ax.legend(handles=legend_elements, loc='upper right')
    ax.annotate('2013 Peak\n22.3 items/post', xy=(2013, 22.3), xytext=(2015, 26),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_quantity_quality_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_quantity_quality_en.png")


def create_japanese_rate():
    """Japanese source ratio trends"""
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.fill_between(YEARS_FULL, JP_RATE, alpha=0.3, color='#e74c3c')
    ax.plot(YEARS_FULL, JP_RATE, 'o-', color='#e74c3c', linewidth=2, markersize=6)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Japanese Source Rate (%)', fontsize=12)
    ax.set_title('Japanese Source Ratio Trends', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 25)
    ax.set_xticks(YEARS_FULL)
    ax.set_xticklabels(YEARS_FULL, rotation=45, ha='right')
    ax.axhline(y=5, color='gray', linestyle='--', alpha=0.5)
    ax.text(2023, 6.5, 'Stable at ~5%', fontsize=10, color='gray')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_japanese_rate_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_japanese_rate_en.png")


def create_summary_stats():
    """15 Years of Records (Summary Cards)"""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')

    stats = [
        ('Total Posts', '820', '#3498db'),
        ('Total Articles', '13,606', '#27ae60'),
        ('Years Running', '15 years', '#9b59b6'),
        ('Update Frequency', 'Weekly', '#e74c3c'),
    ]

    for i, (label, value, color) in enumerate(stats):
        y_pos = 0.85 - i * 0.22
        ax.add_patch(mpatches.FancyBboxPatch((0.05, y_pos-0.08), 0.9, 0.18,
                                              boxstyle="round,pad=0.02",
                                              facecolor=color, alpha=0.15,
                                              edgecolor=color, linewidth=2))
        ax.text(0.5, y_pos+0.02, value, fontsize=24, fontweight='bold',
                 ha='center', va='center', color=color)
        ax.text(0.5, y_pos-0.04, label, fontsize=12, ha='center', va='center', color='#555')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('15 Years of Records', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_summary_stats_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_summary_stats_en.png")


def create_info_sources():
    """Information Source Changes (Early, Mid, Late)"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.suptitle('Information Source Evolution: From Personal Blogs to Official Docs', fontsize=16, fontweight='bold', y=1.02)

    # Early
    sources_early = ['github.com', 'd.hatena.ne.jp', 'slideshare.net', 'amazon.co.jp', 'amazon.com']
    values_early = [327, 154, 147, 98, 83]
    colors_early = ['#2c3e50', '#27ae60', '#9b59b6', '#9b59b6', '#9b59b6']

    # Mid
    sources_mid = ['github.com', 'medium.com', 'developers.google.com', 'webkit.org', 'nodejs.org']
    values_mid = [828, 134, 103, 69, 64]
    colors_mid = ['#2c3e50', '#27ae60', '#3498db', '#3498db', '#e67e22']

    # Late
    sources_late = ['github.com', 'nodejs.org', 'bun.sh', 'zenn.dev', 'developer.chrome.com']
    values_late = [568, 98, 62, 56, 55]
    colors_late = ['#2c3e50', '#e67e22', '#e67e22', '#27ae60', '#3498db']

    def create_bar_chart(ax, sources, values, colors, title, period_desc):
        y_pos = np.arange(len(sources))
        bars = ax.barh(y_pos, values, color=colors, alpha=0.8)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(sources, fontsize=10)
        ax.invert_yaxis()
        ax.set_xlabel('Count', fontsize=10)
        ax.set_title(title, fontsize=12, fontweight='bold')

        for i, (bar, val) in enumerate(zip(bars, values)):
            ax.text(val + 5, bar.get_y() + bar.get_height()/2, str(val),
                    va='center', fontsize=9)

        ax.text(0.5, -0.12, period_desc, transform=ax.transAxes, fontsize=9,
                ha='center', style='italic', color='#666')

    create_bar_chart(axes[0], sources_early, values_early, colors_early,
                     'Early (2011-2013)', 'Personal blogs, slides, books dominant')
    create_bar_chart(axes[1], sources_mid, values_mid, colors_mid,
                     'Mid (2017-2019)', 'Medium rises, vendor docs in top')
    create_bar_chart(axes[2], sources_late, values_late, colors_late,
                     'Late (2023-2025)', 'Official docs & primary sources central')

    category_colors = {
        'GitHub': '#2c3e50',
        'Blog Platform': '#27ae60',
        'Official Docs': '#3498db',
        'Project Official': '#e67e22',
        'Slides/Books': '#9b59b6',
    }
    legend_patches = [mpatches.Patch(color=v, label=k, alpha=0.8)
                      for k, v in list(category_colors.items())]
    fig.legend(handles=legend_patches, loc='lower center', ncol=5, fontsize=9,
               bbox_to_anchor=(0.5, -0.02))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_info_sources_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_info_sources_en.png")


def create_jp_platforms():
    """Japanese Blog Platform Transition"""
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('Japanese Blog Platform Transition', fontsize=16, fontweight='bold')

    years = [2011, 2014, 2016, 2018, 2020, 2021, 2024]
    hatena = [92, 29, 10, 5, 3, 1, 2]
    qiita = [0, 19, 45, 30, 4, 1, 1]
    zenn = [0, 0, 0, 0, 3, 22, 24]

    ax.stackplot(years, hatena, qiita, zenn,
                 labels=['Hatena', 'Qiita', 'Zenn'],
                 colors=['#e74c3c', '#55c500', '#3ea8ff'],
                 alpha=0.8)

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Article Count', fontsize=11)
    ax.legend(loc='upper right')

    ax.axvline(x=2015, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=2020, color='gray', linestyle='--', alpha=0.5)

    ax.text(2012.5, 80, 'Hatena Era', fontsize=10, ha='center', style='italic', color='#666')
    ax.text(2017.5, 50, 'Qiita Era', fontsize=10, ha='center', style='italic', color='#666')
    ax.text(2022.5, 30, 'Zenn Era', fontsize=10, ha='center', style='italic', color='#666')

    ax.set_xlim(2011, 2024)
    ax.set_ylim(0, 120)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_jp_platforms_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_jp_platforms_en.png")


def create_ui_frameworks():
    """UI Framework Trends"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [2011, 2013, 2015, 2017, 2019, 2021, 2023, 2025]
    jquery = [109, 86, 29, 7, 9, 8, 3, 1]
    angular = [1, 44, 30, 34, 9, 6, 5, 4]
    react = [0, 6, 103, 153, 84, 84, 90, 82]
    vue = [0, 0, 10, 28, 20, 23, 12, 4]

    ax.plot(years, jquery, 'o-', label='jQuery', color='#0769ad', linewidth=2, markersize=8)
    ax.plot(years, angular, 's-', label='Angular', color='#dd0031', linewidth=2, markersize=8)
    ax.plot(years, react, '^-', label='React', color='#61dafb', linewidth=2, markersize=8)
    ax.plot(years, vue, 'D-', label='Vue', color='#42b883', linewidth=2, markersize=8)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Mentions', fontsize=12)
    ax.set_title('UI Frameworks: jQuery → Angular → React', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11)
    ax.set_ylim(0, 180)
    ax.annotate('jQuery Era', xy=(2011, 109), xytext=(2012.5, 140),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)
    ax.annotate('React Peak\n153', xy=(2017, 153), xytext=(2019, 165),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_ui_frameworks_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_ui_frameworks_en.png")


def create_build_tools():
    """Build Tool Trends"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years_build = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    webpack = [33, 43, 35, 26, 26, 16, 11, 13, 10, 8]
    rollup = [2, 8, 5, 7, 7, 5, 3, 10, 5, 2]
    esbuild = [0, 0, 0, 0, 5, 7, 9, 16, 8, 6]
    vite = [0, 0, 0, 0, 1, 10, 28, 36, 28, 23]

    ax.fill_between(years_build, webpack, alpha=0.3, color='#8dd6f9')
    ax.plot(years_build, webpack, 'o-', label='webpack', color='#8dd6f9', linewidth=2, markersize=8)
    ax.plot(years_build, rollup, 's-', label='Rollup', color='#ff6633', linewidth=2, markersize=8)
    ax.plot(years_build, esbuild, '^-', label='esbuild', color='#ffcf00', linewidth=2, markersize=8)
    ax.plot(years_build, vite, 'D-', label='Vite', color='#646cff', linewidth=2, markersize=8)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Mentions', fontsize=12)
    ax.set_title('Build Tools: webpack → Vite', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11)
    ax.annotate('webpack Peak', xy=(2017, 43), xytext=(2018.5, 48),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)
    ax.annotate('Vite Rises', xy=(2022, 28), xytext=(2020, 35),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_build_tools_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_build_tools_en.png")


def create_runtimes():
    """Runtime Diversification"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years_runtime = [2020, 2021, 2022, 2023, 2024, 2025]
    deno = [13, 21, 21, 19, 18, 15]
    bun = [0, 1, 5, 27, 26, 20]

    ax.bar([y - 0.2 for y in years_runtime], deno, width=0.4, label='Deno', color='#000000', alpha=0.8)
    ax.bar([y + 0.2 for y in years_runtime], bun, width=0.4, label='Bun', color='#fbf0df', edgecolor='#f9c144', linewidth=2)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Mentions', fontsize=12)
    ax.set_title('Runtime Diversification: From Node.js Dominance to Competition', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=11)
    ax.text(0.95, 0.95, 'Node.js remains the\nfoundation with many\nmentions throughout',
             transform=ax.transAxes, fontsize=10, ha='right', va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_runtimes_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_runtimes_en.png")


def create_tech_changes():
    """Technologies That Changed Over 15 Years"""
    fig, ax = plt.subplots(figsize=(10, 7))

    not_mentioned = ['Backbone.js', 'CoffeeScript', 'AMD/RequireJS', 'Grunt', 'PhantomJS', 'Bower']
    not_mentioned_2011 = [75, 71, 74, 49, 37, 13]
    not_mentioned_2025 = [0, 0, 3, 0, 0, 0]

    emerged = ['ESM/import', 'Rust', 'WebAssembly', 'monorepo']
    emerged_2011 = [2, 1, 0, 0]
    emerged_2025 = [117, 40, 51, 14]

    y_pos = np.arange(len(not_mentioned))
    y_pos2 = np.arange(len(emerged)) + len(not_mentioned) + 1

    ax.barh(y_pos, [-x for x in not_mentioned_2011], color='#e74c3c', alpha=0.5, label='2011-13')
    ax.barh(y_pos, [-x for x in not_mentioned_2025], color='#e74c3c', alpha=1.0, label='2023-25')
    ax.barh(y_pos2, emerged_2011, color='#27ae60', alpha=0.5)
    ax.barh(y_pos2, emerged_2025, color='#27ae60', alpha=1.0)

    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_yticks(list(y_pos) + list(y_pos2))
    ax.set_yticklabels(not_mentioned + emerged, fontsize=11)
    ax.set_xlabel('Count (Left: Decreased / Right: Increased)', fontsize=11)
    ax.set_title('Technologies That Changed Over 15 Years', fontsize=14, fontweight='bold')

    ax.axhline(y=len(not_mentioned) + 0.5, color='gray', linestyle='--', alpha=0.5)
    ax.text(-60, len(not_mentioned) + 0.5, 'Faded Away', fontsize=10, color='#e74c3c', va='center')
    ax.text(60, len(not_mentioned) + 0.5, 'Emerged', fontsize=10, color='#27ae60', va='center')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_tech_changes_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_tech_changes_en.png")


def create_cross_topics():
    """Cross-cutting Topic Trends"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [2011, 2014, 2017, 2020, 2021, 2025]
    types_data = [30, 52, 108, 123, 129, 88]
    test = [46, 87, 86, 44, 59, 47]
    performance = [27, 58, 93, 80, 64, 42]
    security = [10, 14, 15, 13, 28, 15]
    a11y = [6, 9, 15, 16, 17, 23]

    ax.plot(years, types_data, 'o-', label='Types (TypeScript)', color='#3178c6', linewidth=2, markersize=8)
    ax.plot(years, test, 's-', label='Testing', color='#27ae60', linewidth=2, markersize=8)
    ax.plot(years, performance, '^-', label='Performance', color='#e74c3c', linewidth=2, markersize=8)
    ax.plot(years, security, 'D-', label='Security', color='#9b59b6', linewidth=2, markersize=8)
    ax.plot(years, a11y, 'p-', label='a11y', color='#f39c12', linewidth=2, markersize=8)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Mentions', fontsize=12)
    ax.set_title('Cross-cutting Topic Trends', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.set_ylim(0, 150)

    ax.annotate('TypeScript Peak\n(became standard)', xy=(2021, 129), xytext=(2017.5, 140),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)
    ax.annotate('a11y: Only\nrising trend', xy=(2025, 23), xytext=(2022.5, 45),
                arrowprops=dict(arrowstyle='->', color='#f39c12'), fontsize=10, color='#f39c12')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_cross_topics_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_cross_topics_en.png")


def create_dev_practices():
    """Development Practice Changes"""
    fig, ax = plt.subplots(figsize=(10, 6))

    practices = ['CI/CD', 'Migration', 'RFC/Proposal', 'Breaking Change']
    early = [31, 10, 2, 3]
    mid = [56, 32, 73, 15]
    late = [67, 56, 45, 17]

    x = np.arange(len(practices))
    width = 0.25

    ax.bar(x - width, early, width, label='2011-13', color='#3498db', alpha=0.6)
    ax.bar(x, mid, width, label='2017-19', color='#3498db', alpha=0.8)
    ax.bar(x + width, late, width, label='2023-25', color='#3498db', alpha=1.0)

    ax.set_xlabel('Topic', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title('Development Practice Changes', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(practices, fontsize=11)
    ax.legend(loc='upper right', fontsize=11)

    ax.text(0.02, 0.95, 'CI/CD: Rise of continuous integration\nMigration: Sign of ecosystem maturity',
             transform=ax.transAxes, fontsize=10, va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_dev_practices_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_dev_practices_en.png")


def create_publisher_types():
    """Information Source Composition Changes (Official/GitHub/Personal)"""
    fig, ax = plt.subplots(figsize=(10, 6))

    periods = ['2011-13', '2023-25']
    x = np.arange(len(periods))

    # New data: Official/GitHub/Personal blog classification
    official = [204, 479]
    github = [506, 596]
    personal = [213, 70]

    width = 0.25

    bars1 = ax.bar(x - width, official, width, label='Official', color='#27ae60')
    bars2 = ax.bar(x, github, width, label='GitHub', color='#2c3e50')
    bars3 = ax.bar(x + width, personal, width, label='Personal Blog', color='#3498db')

    ax.set_xlabel('Period', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title('Information Source Changes: Personal Blog vs Official', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(periods, fontsize=12)
    ax.legend(loc='upper right', fontsize=10)

    # Add value labels
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{int(height)}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Change rate annotation
    ax.text(0.5, 0.95, 'Official: +135%  GitHub: Stable  Personal: -67%',
            transform=ax.transAxes, fontsize=11, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_publisher_types_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_publisher_types_en.png")


def create_content_types_bar():
    """Article Type Trends (Tag + Keyword Hybrid Classification)"""
    fig, ax = plt.subplots(figsize=(12, 6))

    years = ['2011-13', '2017-19', '2023-25']
    release_notes = [560, 862, 986]
    articles = [719, 813, 526]
    books = [192, 135, 45]
    slides = [292, 170, 49]
    tutorials = [97, 93, 14]

    x = np.arange(len(years))
    width = 0.15

    bars1 = ax.bar(x - 2*width, release_notes, width, label='Release Notes', color='#27ae60')
    bars2 = ax.bar(x - width, articles, width, label='Articles', color='#3498db')
    bars3 = ax.bar(x, books, width, label='Books', color='#e74c3c')
    bars4 = ax.bar(x + width, slides, width, label='Slides/Videos', color='#9b59b6')
    bars5 = ax.bar(x + 2*width, tutorials, width, label='Tutorials', color='#f39c12')

    ax.set_xlabel('Period', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title('Article Type Trends', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=12)
    ax.legend(loc='upper right', fontsize=10)

    for bars in [bars1, bars2, bars3, bars4, bars5]:
        for bar in bars:
            height = bar.get_height()
            if height > 80:
                ax.annotate(f'{int(height)}',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3), textcoords="offset points",
                            ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_content_types_bar_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_content_types_bar_en.png")


def create_content_change_rate():
    """Article Type Change Rate (Tag + Keyword Hybrid Classification)"""
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['Release Notes', 'Articles', 'Books', 'Slides/Videos', 'Tutorials']
    # 2011-13 → 2023-25 change rate
    changes = [
        (986-560)/560*100,   # Release Notes: +76%
        (526-719)/719*100,   # Articles: -27%
        (45-192)/192*100,    # Books: -77%
        (49-292)/292*100,    # Slides/Videos: -83%
        (14-97)/97*100,      # Tutorials: -86%
    ]
    colors = ['#27ae60' if c > 0 else '#e74c3c' for c in changes]

    bars = ax.barh(categories, changes, color=colors, alpha=0.8, height=0.6)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_xlabel('Change Rate (%)', fontsize=12)
    ax.set_title('Article Type Change Rate (Early → Late)', fontsize=14, fontweight='bold')

    # Display % inside bars with white text
    for bar, val in zip(bars, changes):
        x_pos = val / 2
        ax.text(x_pos, bar.get_y() + bar.get_height()/2,
                f'{val:+.0f}%', va='center', ha='center', fontsize=12, fontweight='bold',
                color='white')

    ax.text(0.95, 0.05, 'From learning content\nto release notes',
             transform=ax.transAxes, fontsize=11, ha='right', va='bottom',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_content_change_rate_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_content_change_rate_en.png")


def create_summary():
    """Before/After Comparison (Summary)"""
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.axis('off')
    fig.suptitle('JSer.info: 15 Years of Change', fontsize=28, fontweight='bold', y=0.97)

    # Left side (2011)
    ax.add_patch(FancyBboxPatch((0.02, 0.05), 0.38, 0.88,
                                 boxstyle="round,pad=0.02",
                                 facecolor='#e74c3c', alpha=0.10,
                                 edgecolor='#e74c3c', linewidth=3))
    ax.text(0.21, 0.95, '2011', fontsize=32, fontweight='bold', ha='center', color='#c0392b')

    # Right side (2025)
    ax.add_patch(FancyBboxPatch((0.60, 0.05), 0.38, 0.88,
                                 boxstyle="round,pad=0.02",
                                 facecolor='#3498db', alpha=0.10,
                                 edgecolor='#3498db', linewidth=3))
    ax.text(0.79, 0.95, '2025', fontsize=32, fontweight='bold', ha='center', color='#2980b9')

    # Comparison items
    comparisons = [
        {'label': 'Sources', 'left': 'Hatena, SlideShare\nBooks, Personal Blogs',
         'right': 'GitHub, Official Docs\nRelease Notes', 'y': 0.78, 'color': '#3498db'},
        {'label': 'UI Framework', 'left': 'jQuery\nBackbone.js',
         'right': 'React\n(Stable Era)', 'y': 0.63, 'color': '#0769ad'},
        {'label': 'Build Tools', 'left': 'Grunt / Gulp',
         'right': 'Vite / esbuild', 'y': 0.50, 'color': '#646cff'},
        {'label': 'Curation Style', 'left': '22 items/post\nAvg 62 chars',
         'right': '13 items/post\nAvg 108 chars', 'y': 0.35, 'color': '#27ae60'},
        {'label': 'JP Source Rate', 'left': '22%', 'right': '5%', 'y': 0.22, 'color': '#e67e22'},
        {'label': 'Sources', 'left': 'Personal Blog\nCentric',
         'right': 'Official Sites\n& Projects Centric', 'y': 0.09, 'color': '#9b59b6'},
    ]

    for i, comp in enumerate(comparisons):
        y = comp['y']
        color = comp['color']

        # Divider line
        if i > 0:
            line_y = (comp['y'] + comparisons[i-1]['y']) / 2
            ax.axhline(y=line_y, xmin=0.05, xmax=0.95, color='#ddd', linestyle='-', linewidth=1.5)

        # Label
        ax.add_patch(FancyBboxPatch((0.41, y - 0.03), 0.18, 0.06,
                                     boxstyle="round,pad=0.008",
                                     facecolor=color, alpha=0.95))
        ax.text(0.5, y, comp['label'], fontsize=14, ha='center', va='center',
                fontweight='bold', color='white')

        # Left value
        ax.text(0.21, y, comp['left'], fontsize=16, ha='center', va='center',
                color='#922b21', fontweight='bold', linespacing=1.5)

        # Right value
        ax.text(0.79, y, comp['right'], fontsize=16, ha='center', va='center',
                color='#1a5276', fontweight='bold', linespacing=1.5)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_summary_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_summary_en.png")


# =============================================================================
# Combined Charts
# =============================================================================

def create_basic_stats_combined():
    """Basic Stats Dashboard (4 in 1)"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('JSer.info 15th Anniversary: Basic Stats', fontsize=18, fontweight='bold', y=0.98)

    # 1-1: Yearly articles and posts
    ax1 = axes[0, 0]
    ax1_twin = ax1.twinx()
    ax1.bar(YEARS_FULL, ARTICLES, color='#3498db', alpha=0.7, label='Articles', width=0.7)
    ax1_twin.plot(YEARS_FULL, POSTS, 'o-', color='#e74c3c', linewidth=2, markersize=6)
    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Articles', color='#3498db', fontsize=11)
    ax1_twin.set_ylabel('Posts', color='#e74c3c', fontsize=11)
    ax1.set_title('Yearly Article and Post Trends', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 1500)
    ax1_twin.set_ylim(30, 75)
    ax1.set_xticks(YEARS_FULL[::2])
    legend_elements = [mpatches.Patch(facecolor='#3498db', alpha=0.7, label='Articles'),
                       Line2D([0], [0], color='#e74c3c', marker='o', label='Posts')]
    ax1.legend(handles=legend_elements, loc='upper right')
    ax1.annotate('Peak\n1,269', xy=(2013, 1269), xytext=(2014.5, 1350),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

    # 1-2: Quality over Quantity
    ax2 = axes[0, 1]
    ax2_twin = ax2.twinx()
    ax2.bar(YEARS_FULL, PER_POST, color='#9b59b6', alpha=0.7, width=0.7)
    ax2_twin.plot(YEARS_FULL, AVG_CHARS, 's-', color='#27ae60', linewidth=2, markersize=6)
    ax2.set_xlabel('Year', fontsize=11)
    ax2.set_ylabel('Items per Post', color='#9b59b6', fontsize=11)
    ax2_twin.set_ylabel('Avg Description Length', color='#27ae60', fontsize=11)
    ax2.set_title('Quality over Quantity', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 30)
    ax2_twin.set_ylim(40, 130)
    ax2.set_xticks(YEARS_FULL[::2])
    legend_elements2 = [mpatches.Patch(facecolor='#9b59b6', alpha=0.7, label='Items/Post'),
                        Line2D([0], [0], color='#27ae60', marker='s', label='Avg Chars')]
    ax2.legend(handles=legend_elements2, loc='upper right')
    ax2.annotate('2013 Peak', xy=(2013, 22.3), xytext=(2015, 26),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

    # 1-3: Japanese source rate
    ax3 = axes[1, 0]
    ax3.fill_between(YEARS_FULL, JP_RATE, alpha=0.3, color='#e74c3c')
    ax3.plot(YEARS_FULL, JP_RATE, 'o-', color='#e74c3c', linewidth=2, markersize=6)
    ax3.set_xlabel('Year', fontsize=11)
    ax3.set_ylabel('Japanese Rate (%)', fontsize=11)
    ax3.set_title('Japanese Source Ratio Trends', fontsize=12, fontweight='bold')
    ax3.set_ylim(0, 25)
    ax3.set_xticks(YEARS_FULL[::2])
    ax3.axhline(y=5, color='gray', linestyle='--', alpha=0.5)
    ax3.text(2023, 6.5, 'Stable at ~5%', fontsize=9, color='gray')

    # 1-4: 15 year summary
    ax4 = axes[1, 1]
    ax4.axis('off')
    stats = [
        ('Total Posts', '820', '#3498db'),
        ('Total Articles', '13,606', '#27ae60'),
        ('Years Running', '15 years', '#9b59b6'),
        ('Update Frequency', 'Weekly', '#e74c3c'),
    ]
    for i, (label, value, color) in enumerate(stats):
        y_pos = 0.85 - i * 0.22
        ax4.add_patch(mpatches.FancyBboxPatch((0.1, y_pos-0.08), 0.8, 0.18,
                                              boxstyle="round,pad=0.02",
                                              facecolor=color, alpha=0.15,
                                              edgecolor=color, linewidth=2))
        ax4.text(0.5, y_pos+0.02, value, fontsize=20, fontweight='bold',
                 ha='center', va='center', color=color)
        ax4.text(0.5, y_pos-0.04, label, fontsize=11, ha='center', va='center', color='#555')
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.set_title('15 Years of Records', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_basic_stats_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_basic_stats_en.png (combined)")


def create_tech_trends_combined():
    """Tech Trends Dashboard (4 in 1)"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Technology Trend Evolution', fontsize=18, fontweight='bold', y=0.98)

    # 2-1: UI Frameworks
    ax1 = axes[0, 0]
    years = [2011, 2013, 2015, 2017, 2019, 2021, 2023, 2025]
    jquery = [109, 86, 29, 7, 9, 8, 3, 1]
    angular = [1, 44, 30, 34, 9, 6, 5, 4]
    react = [0, 6, 103, 153, 84, 84, 90, 82]
    vue = [0, 0, 10, 28, 20, 23, 12, 4]
    ax1.plot(years, jquery, 'o-', label='jQuery', color='#0769ad', linewidth=2, markersize=6)
    ax1.plot(years, angular, 's-', label='Angular', color='#dd0031', linewidth=2, markersize=6)
    ax1.plot(years, react, '^-', label='React', color='#61dafb', linewidth=2, markersize=6)
    ax1.plot(years, vue, 'D-', label='Vue', color='#42b883', linewidth=2, markersize=6)
    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Mentions', fontsize=11)
    ax1.set_title('UI Frameworks: jQuery → Angular → React', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right')
    ax1.set_ylim(0, 180)
    ax1.annotate('jQuery Era', xy=(2011, 109), xytext=(2012, 130),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
    ax1.annotate('React Peak\n153', xy=(2017, 153), xytext=(2018.5, 165),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

    # 2-2: Build Tools
    ax2 = axes[0, 1]
    years_build = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    webpack = [33, 43, 35, 26, 26, 16, 11, 13, 10, 8]
    rollup = [2, 8, 5, 7, 7, 5, 3, 10, 5, 2]
    esbuild = [0, 0, 0, 0, 5, 7, 9, 16, 8, 6]
    vite = [0, 0, 0, 0, 1, 10, 28, 36, 28, 23]
    ax2.fill_between(years_build, webpack, alpha=0.3, color='#8dd6f9')
    ax2.plot(years_build, webpack, 'o-', label='webpack', color='#8dd6f9', linewidth=2)
    ax2.plot(years_build, rollup, 's-', label='Rollup', color='#ff6633', linewidth=2)
    ax2.plot(years_build, esbuild, '^-', label='esbuild', color='#ffcf00', linewidth=2)
    ax2.plot(years_build, vite, 'D-', label='Vite', color='#646cff', linewidth=2)
    ax2.set_xlabel('Year', fontsize=11)
    ax2.set_ylabel('Mentions', fontsize=11)
    ax2.set_title('Build Tools: webpack → Vite', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right')
    ax2.annotate('webpack Peak', xy=(2017, 43), xytext=(2018, 50),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
    ax2.annotate('Vite Rises', xy=(2022, 28), xytext=(2020.5, 35),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

    # 2-3: Runtimes
    ax3 = axes[1, 0]
    years_runtime = [2020, 2021, 2022, 2023, 2024, 2025]
    deno = [13, 21, 21, 19, 18, 15]
    bun = [0, 1, 5, 27, 26, 20]
    ax3.bar([y - 0.2 for y in years_runtime], deno, width=0.4, label='Deno', color='#000000', alpha=0.8)
    ax3.bar([y + 0.2 for y in years_runtime], bun, width=0.4, label='Bun', color='#fbf0df', edgecolor='#f9c144', linewidth=2)
    ax3.set_xlabel('Year', fontsize=11)
    ax3.set_ylabel('Mentions', fontsize=11)
    ax3.set_title('Runtime Diversification', fontsize=12, fontweight='bold')
    ax3.legend(loc='upper left')
    ax3.text(0.95, 0.95, 'Node.js remains the\nfoundation throughout',
             transform=ax3.transAxes, fontsize=9, ha='right', va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    # 2-4: Tech Changes
    ax4 = axes[1, 1]
    not_mentioned = ['Backbone.js', 'CoffeeScript', 'AMD/RequireJS', 'Grunt', 'PhantomJS', 'Bower']
    not_mentioned_2011 = [75, 71, 74, 49, 37, 13]
    not_mentioned_2025 = [0, 0, 3, 0, 0, 0]
    emerged = ['ESM/import', 'Rust', 'WebAssembly', 'monorepo']
    emerged_2011 = [2, 1, 0, 0]
    emerged_2025 = [117, 40, 51, 14]
    y_pos = np.arange(len(not_mentioned))
    y_pos2 = np.arange(len(emerged)) + len(not_mentioned) + 1
    ax4.barh(y_pos, [-x for x in not_mentioned_2011], color='#e74c3c', alpha=0.5, label='2011-13')
    ax4.barh(y_pos, [-x for x in not_mentioned_2025], color='#e74c3c', alpha=1.0, label='2023-25')
    ax4.barh(y_pos2, emerged_2011, color='#27ae60', alpha=0.5)
    ax4.barh(y_pos2, emerged_2025, color='#27ae60', alpha=1.0)
    ax4.axvline(x=0, color='black', linewidth=0.5)
    ax4.set_yticks(list(y_pos) + list(y_pos2))
    ax4.set_yticklabels(not_mentioned + emerged)
    ax4.set_xlabel('Count (Left: Decreased / Right: Increased)', fontsize=10)
    ax4.set_title('Technologies That Changed', fontsize=12, fontweight='bold')
    ax4.axhline(y=len(not_mentioned) + 0.5, color='gray', linestyle='--', alpha=0.5)
    ax4.text(-60, len(not_mentioned) + 0.5, 'Faded', fontsize=9, color='#e74c3c', va='center')
    ax4.text(60, len(not_mentioned) + 0.5, 'Emerged', fontsize=9, color='#27ae60', va='center')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_tech_trends_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_tech_trends_en.png (combined)")


def create_topics_combined():
    """Cross-cutting Topics Dashboard (2 in 1)"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Cross-cutting Topic Changes', fontsize=16, fontweight='bold', y=1.02)

    # Cross-cutting topic trends
    ax1 = axes[0]
    years = [2011, 2014, 2017, 2020, 2021, 2025]
    types_data = [30, 52, 108, 123, 129, 88]
    test = [46, 87, 86, 44, 59, 47]
    performance = [27, 58, 93, 80, 64, 42]
    security = [10, 14, 15, 13, 28, 15]
    a11y = [6, 9, 15, 16, 17, 23]
    ax1.plot(years, types_data, 'o-', label='Types (TypeScript)', color='#3178c6', linewidth=2, markersize=8)
    ax1.plot(years, test, 's-', label='Testing', color='#27ae60', linewidth=2, markersize=8)
    ax1.plot(years, performance, '^-', label='Performance', color='#e74c3c', linewidth=2, markersize=8)
    ax1.plot(years, security, 'D-', label='Security', color='#9b59b6', linewidth=2, markersize=8)
    ax1.plot(years, a11y, 'p-', label='a11y', color='#f39c12', linewidth=2, markersize=8)
    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Mentions', fontsize=11)
    ax1.set_title('Cross-cutting Topic Trends', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right')
    ax1.set_ylim(0, 150)
    ax1.annotate('TypeScript Peak\n(became standard)', xy=(2021, 129), xytext=(2018, 140),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
    ax1.annotate('a11y: Only\nrising trend', xy=(2025, 23), xytext=(2023, 40),
                arrowprops=dict(arrowstyle='->', color='#f39c12'), fontsize=9, color='#f39c12')

    # Development practice changes
    ax2 = axes[1]
    practices = ['CI/CD', 'Migration', 'RFC/Proposal', 'Breaking Change']
    early = [31, 10, 2, 3]
    mid = [56, 32, 73, 15]
    late = [67, 56, 45, 17]
    x = np.arange(len(practices))
    width = 0.25
    ax2.bar(x - width, early, width, label='2011-13', color='#3498db', alpha=0.6)
    ax2.bar(x, mid, width, label='2017-19', color='#3498db', alpha=0.8)
    ax2.bar(x + width, late, width, label='2023-25', color='#3498db', alpha=1.0)
    ax2.set_xlabel('Topic', fontsize=11)
    ax2.set_ylabel('Count', fontsize=11)
    ax2.set_title('Development Practice Changes', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(practices, rotation=15, ha='right')
    ax2.legend(loc='upper right')
    ax2.text(0.05, 0.95, 'CI/CD: Rise of continuous integration\nMigration: Sign of ecosystem maturity',
             transform=ax2.transAxes, fontsize=9, va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_topics_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_topics_en.png (combined)")


def create_publishers_combined():
    """Information Sources Dashboard (2 in 1)"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Information Source Changes', fontsize=16, fontweight='bold', y=1.02)

    # Left: Official/GitHub/Personal comparison
    ax1 = axes[0]
    periods = ['2011-13', '2023-25']
    x = np.arange(len(periods))
    official = [204, 479]
    github = [506, 596]
    personal = [213, 70]
    width = 0.25
    bars1 = ax1.bar(x - width, official, width, label='Official', color='#27ae60')
    bars2 = ax1.bar(x, github, width, label='GitHub', color='#2c3e50')
    bars3 = ax1.bar(x + width, personal, width, label='Personal Blog', color='#3498db')
    ax1.set_xlabel('Period', fontsize=11)
    ax1.set_ylabel('Count', fontsize=11)
    ax1.set_title('Information Source Composition Changes', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(periods)
    ax1.legend(loc='upper right')
    # Value labels
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax1.annotate(f'{int(height)}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Right: Flow diagram showing changes
    ax2 = axes[1]
    ax2.axis('off')
    categories = ['Personal Blog', 'GitHub', 'Official']
    colors = ['#3498db', '#2c3e50', '#27ae60']
    changes = ['-67%', 'Stable', '+135%']
    ax2.text(0.1, 0.85, '2011-13', fontsize=12, fontweight='bold', ha='center')
    ax2.add_patch(mpatches.FancyBboxPatch((0.02, 0.55), 0.16, 0.25,
                                           boxstyle="round,pad=0.02",
                                           facecolor='#3498db', alpha=0.8))
    ax2.text(0.1, 0.675, 'Personal\n≒ Official', fontsize=10, ha='center', va='center', color='white')
    for i, (cat, color, change) in enumerate(zip(categories, colors, changes)):
        y = 0.7 - i * 0.22
        ax2.annotate('', xy=(0.65, y), xytext=(0.35, y),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))
        ax2.text(0.5, y + 0.05, change, fontsize=11, ha='center', va='bottom',
                fontweight='bold', color=color)
    ax2.text(0.9, 0.85, '2023-25', fontsize=12, fontweight='bold', ha='center')
    ax2.add_patch(mpatches.FancyBboxPatch((0.72, 0.55), 0.26, 0.25,
                                           boxstyle="round,pad=0.02",
                                           facecolor='#27ae60', alpha=0.8))
    ax2.text(0.85, 0.675, 'Official is\n7x Personal\nBlogs', fontsize=10,
             ha='center', va='center', color='white')
    ax2.text(0.1, 0.38, 'Personal Blog', fontsize=10, ha='center', color='#3498db')
    ax2.text(0.1, 0.18, 'GitHub', fontsize=10, ha='center', color='#2c3e50')
    ax2.text(0.9, 0.38, 'Official', fontsize=10, ha='center', color='#27ae60')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_title('Information Source Shift', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_publishers_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_publishers_en.png (combined)")


def create_content_types_combined():
    """Article Types Dashboard (2 in 1, Tag + Keyword Hybrid Classification)"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('Article Type Changes: How We Learn JavaScript', fontsize=16, fontweight='bold', y=1.02)

    # Article type trends
    ax1 = axes[0]
    years = ['2011-13', '2017-19', '2023-25']
    release_notes = [560, 862, 986]
    articles = [719, 813, 526]
    books = [192, 135, 45]
    slides = [292, 170, 49]
    tutorials = [97, 93, 14]
    x = np.arange(len(years))
    width = 0.15
    bars1 = ax1.bar(x - 2*width, release_notes, width, label='Release Notes', color='#27ae60')
    bars2 = ax1.bar(x - width, articles, width, label='Articles', color='#3498db')
    bars3 = ax1.bar(x, books, width, label='Books', color='#e74c3c')
    bars4 = ax1.bar(x + width, slides, width, label='Slides/Videos', color='#9b59b6')
    bars5 = ax1.bar(x + 2*width, tutorials, width, label='Tutorials', color='#f39c12')
    ax1.set_xlabel('Period', fontsize=11)
    ax1.set_ylabel('Count', fontsize=11)
    ax1.set_title('Article Type Trends', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.legend(loc='upper right', fontsize=9)
    for bars in [bars1, bars2, bars3, bars4, bars5]:
        for bar in bars:
            height = bar.get_height()
            if height > 100:
                ax1.annotate(f'{int(height)}',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3), textcoords="offset points",
                            ha='center', va='bottom', fontsize=8)

    # Change rate
    ax2 = axes[1]
    categories = ['Release Notes', 'Articles', 'Books', 'Slides/Videos', 'Tutorials']
    changes = [
        (986-560)/560*100,   # +76%
        (526-719)/719*100,   # -27%
        (45-192)/192*100,    # -77%
        (49-292)/292*100,    # -83%
        (14-97)/97*100,      # -86%
    ]
    colors = ['#27ae60' if c > 0 else '#e74c3c' for c in changes]
    bars = ax2.barh(categories, changes, color=colors, alpha=0.8)
    ax2.axvline(x=0, color='black', linewidth=0.5)
    ax2.set_xlabel('Change Rate (%)', fontsize=11)
    ax2.set_title('Early → Late Change Rate', fontsize=12, fontweight='bold')
    # Display % inside bars with white text
    for bar, val in zip(bars, changes):
        x_pos = val / 2
        ax2.text(x_pos, bar.get_y() + bar.get_height()/2,
                 f'{val:+.0f}%', va='center', ha='center', fontsize=10, fontweight='bold',
                 color='white')
    ax2.text(0.95, 0.05, 'From learning content\nto release notes',
             transform=ax2.transAxes, fontsize=10, ha='right', va='bottom',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_content_types_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_content_types_en.png (combined)")


# =============================================================================
# Bookmark Correlation Chart
# =============================================================================

def create_bookmark_correlation():
    """Bookmark and JSer.info Update Correlation"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Bookmark and JSer.info Update Correlation (2020-2025)', fontsize=18, fontweight='bold', y=0.98)

    # Data
    years = [2020, 2021, 2022, 2023, 2024, 2025]
    bookmarks = [2473, 2862, 2536, 2373, 1752, 1033]  # Bookmark count
    jser_items = [810, 789, 712, 737, 638, 552]  # JSer.info articles

    # Conversion rate (JSer.info / Bookmark)
    conversion_rate = [j/b*100 for j, b in zip(jser_items, bookmarks)]

    # 1-1: Bookmarks vs JSer.info
    ax1 = axes[0, 0]
    x = np.arange(len(years))
    width = 0.35
    ax1.bar(x - width/2, bookmarks, width, label='Bookmarks', color='#3498db', alpha=0.8)
    ax1.bar(x + width/2, jser_items, width, label='JSer.info', color='#e74c3c', alpha=0.8)
    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Count', fontsize=11)
    ax1.set_title('Bookmarks vs JSer.info Articles', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.legend(loc='upper right')
    for i, (b, j) in enumerate(zip(bookmarks, jser_items)):
        ax1.text(i - width/2, b + 50, str(b), ha='center', fontsize=9)
        ax1.text(i + width/2, j + 50, str(j), ha='center', fontsize=9)

    # 1-2: Conversion efficiency trends
    ax2 = axes[0, 1]
    ax2.fill_between(years, conversion_rate, alpha=0.3, color='#27ae60')
    ax2.plot(years, conversion_rate, 'o-', color='#27ae60', linewidth=2, markersize=8)
    ax2.set_xlabel('Year', fontsize=11)
    ax2.set_ylabel('Conversion Rate (%)', fontsize=11)
    ax2.set_title('Bookmark → JSer.info Conversion Efficiency', fontsize=12, fontweight='bold')
    ax2.set_ylim(20, 60)
    for i, (y, r) in enumerate(zip(years, conversion_rate)):
        ax2.annotate(f'{r:.1f}%', xy=(y, r), xytext=(0, 10), textcoords='offset points',
                     ha='center', fontsize=10, fontweight='bold')
    ax2.text(0.05, 0.95, f'2020: {conversion_rate[0]:.1f}% → 2025: {conversion_rate[-1]:.1f}%\nEfficiency +{(conversion_rate[-1]/conversion_rate[0]-1)*100:.0f}%',
             transform=ax2.transAxes, fontsize=10, va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    # 1-3: Relative change (2020=100)
    ax3 = axes[1, 0]
    bookmarks_rel = [b/bookmarks[0]*100 for b in bookmarks]
    jser_rel = [j/jser_items[0]*100 for j in jser_items]
    ax3.plot(years, bookmarks_rel, 'o-', label='Bookmarks', color='#3498db', linewidth=2, markersize=8)
    ax3.plot(years, jser_rel, 's-', label='JSer.info', color='#e74c3c', linewidth=2, markersize=8)
    ax3.axhline(y=100, color='gray', linestyle='--', alpha=0.5)
    ax3.set_xlabel('Year', fontsize=11)
    ax3.set_ylabel('Relative Value (2020=100)', fontsize=11)
    ax3.set_title('Relative Change Comparison', fontsize=12, fontweight='bold')
    ax3.legend(loc='upper right')
    ax3.set_ylim(30, 130)
    ax3.annotate(f'{bookmarks_rel[-1]:.0f}', xy=(2025, bookmarks_rel[-1]), xytext=(5, 0),
                 textcoords='offset points', fontsize=10, color='#3498db')
    ax3.annotate(f'{jser_rel[-1]:.0f}', xy=(2025, jser_rel[-1]), xytext=(5, 0),
                 textcoords='offset points', fontsize=10, color='#e74c3c')

    # 1-4: Summary
    ax4 = axes[1, 1]
    ax4.axis('off')

    # Summary data
    bookmark_change = (bookmarks[-1] - bookmarks[0]) / bookmarks[0] * 100
    jser_change = (jser_items[-1] - jser_items[0]) / jser_items[0] * 100
    efficiency_change = (conversion_rate[-1] / conversion_rate[0] - 1) * 100

    summary_data = [
        ('Input (Bookmarks)', f'{bookmark_change:+.0f}%', '#3498db'),
        ('Output (JSer.info)', f'{jser_change:+.0f}%', '#e74c3c'),
        ('Conversion Efficiency', f'{efficiency_change:+.0f}%', '#27ae60'),
    ]

    ax4.text(0.5, 0.95, '5 Year Changes', fontsize=16, fontweight='bold', ha='center', va='top')

    for i, (label, value, color) in enumerate(summary_data):
        y_pos = 0.75 - i * 0.25
        ax4.add_patch(mpatches.FancyBboxPatch((0.1, y_pos-0.08), 0.8, 0.18,
                                              boxstyle="round,pad=0.02",
                                              facecolor=color, alpha=0.15,
                                              edgecolor=color, linewidth=2))
        ax4.text(0.5, y_pos+0.02, value, fontsize=24, fontweight='bold',
                 ha='center', va='center', color=color)
        ax4.text(0.5, y_pos-0.04, label, fontsize=11, ha='center', va='center', color='#555')

    ax4.text(0.5, 0.08, 'Maintaining output quality\neven as input decreases',
             fontsize=11, ha='center', va='bottom', style='italic', color='#666')

    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_bookmark_correlation_en.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_bookmark_correlation_en.png")


# =============================================================================
# Main Execution
# =============================================================================

def main():
    print("=" * 60)
    print("JSer.info 15th Anniversary Chart Generation (English)")
    print("=" * 60)

    print("\n--- Individual Charts ---")
    create_yearly_posts()
    create_quantity_quality()
    create_japanese_rate()
    create_summary_stats()
    create_info_sources()
    create_jp_platforms()
    create_ui_frameworks()
    create_build_tools()
    create_runtimes()
    create_tech_changes()
    create_cross_topics()
    create_dev_practices()
    create_publisher_types()
    create_content_types_bar()
    create_content_change_rate()
    create_summary()
    create_bookmark_correlation()

    print("\n--- Combined Charts ---")
    create_basic_stats_combined()
    create_tech_trends_combined()
    create_topics_combined()
    create_publishers_combined()
    create_content_types_combined()

    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)


if __name__ == '__main__':
    main()
