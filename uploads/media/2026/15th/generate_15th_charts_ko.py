#!/usr/bin/env python3
"""
JSer.info 15주년 기사용 차트 생성 스크립트 (한국어판)

Usage:
    python generate_15th_charts_ko.py

Output:
    15th_*_ko.png 파일이 생성됩니다
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches

# 한국어 폰트 설정 (NotoSansKR)
font_path = '/sessions/adoring-sharp-ramanujan/mnt/dataset/NotoSansKR-Regular.ttf'
fm.fontManager.addfont(font_path)
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D
import numpy as np

# 출력 디렉토리
OUTPUT_DIR = '/sessions/adoring-sharp-ramanujan/mnt/dataset'


# =============================================================================
# 데이터 정의
# =============================================================================

# 연도별 기본 데이터 (2011-2025)
YEARS_FULL = list(range(2011, 2026))
ARTICLES = [915, 1126, 1269, 1147, 1043, 1078, 1068, 921, 790, 810, 789, 712, 737, 638, 552]
POSTS = [65, 57, 57, 59, 56, 59, 54, 58, 53, 53, 53, 54, 53, 47, 41]
PER_POST = [14.1, 19.8, 22.3, 19.4, 18.6, 18.3, 19.8, 15.9, 14.9, 15.3, 14.9, 13.2, 13.9, 13.6, 13.5]
AVG_CHARS = [61.9, 52.5, 57.6, 69.7, 64.5, 61.7, 78.6, 82.9, 90.2, 97.8, 101.1, 101.9, 106.4, 101.3, 108.2]
JP_RATE = [22.2, 18.0, 15.0, 10.0, 7.7, 6.5, 5.5, 4.5, 3.3, 3.5, 4.0, 4.2, 4.5, 4.5, 4.7]


# =============================================================================
# 개별 차트 생성 함수
# =============================================================================

def create_yearly_posts():
    """연도별 소개 기사 수와 게시물 수 추이"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax_twin = ax.twinx()

    bars = ax.bar(YEARS_FULL, ARTICLES, color='#3498db', alpha=0.7, label='소개 기사 수', width=0.7)
    line = ax_twin.plot(YEARS_FULL, POSTS, 'o-', color='#e74c3c', linewidth=2, markersize=6, label='게시물 수')

    ax.set_xlabel('연도', fontsize=12)
    ax.set_ylabel('소개 기사 수', color='#3498db', fontsize=12)
    ax_twin.set_ylabel('게시물 수', color='#e74c3c', fontsize=12)
    ax.set_title('연도별 소개 기사 수와 게시물 수 추이', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 1500)
    ax_twin.set_ylim(30, 75)
    ax.set_xticks(YEARS_FULL)
    ax.set_xticklabels(YEARS_FULL, rotation=45, ha='right')

    legend_elements = [mpatches.Patch(facecolor='#3498db', alpha=0.7, label='소개 기사 수'),
                       Line2D([0], [0], color='#e74c3c', marker='o', label='게시물 수')]
    ax.legend(handles=legend_elements, loc='upper right')
    ax.annotate('피크\n1,269건', xy=(2013, 1269), xytext=(2015, 1350),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_yearly_posts_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_yearly_posts_ko.png")


def create_quantity_quality():
    """'양보다 질'로의 변화"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax_twin = ax.twinx()

    bars = ax.bar(YEARS_FULL, PER_POST, color='#9b59b6', alpha=0.7, width=0.7, label='게시물당 건수')
    line = ax_twin.plot(YEARS_FULL, AVG_CHARS, 's-', color='#27ae60', linewidth=2, markersize=6, label='평균 글자 수')

    ax.set_xlabel('연도', fontsize=12)
    ax.set_ylabel('게시물당 건수', color='#9b59b6', fontsize=12)
    ax_twin.set_ylabel('소개문 평균 글자 수', color='#27ae60', fontsize=12)
    ax.set_title("'양보다 질'로의 변화", fontsize=14, fontweight='bold')
    ax.set_ylim(0, 30)
    ax_twin.set_ylim(40, 130)
    ax.set_xticks(YEARS_FULL)
    ax.set_xticklabels(YEARS_FULL, rotation=45, ha='right')

    legend_elements = [mpatches.Patch(facecolor='#9b59b6', alpha=0.7, label='게시물당 건수'),
                       Line2D([0], [0], color='#27ae60', marker='s', label='평균 글자 수')]
    ax.legend(handles=legend_elements, loc='upper right')
    ax.annotate('2013년 피크\n22.3건/게시물', xy=(2013, 22.3), xytext=(2015, 26),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_quantity_quality_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_quantity_quality_ko.png")


def create_japanese_rate():
    """일본어 소스 비율 추이"""
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.fill_between(YEARS_FULL, JP_RATE, alpha=0.3, color='#e74c3c')
    ax.plot(YEARS_FULL, JP_RATE, 'o-', color='#e74c3c', linewidth=2, markersize=6)
    ax.set_xlabel('연도', fontsize=12)
    ax.set_ylabel('일본어 비율 (%)', fontsize=12)
    ax.set_title('일본어 소스 비율 추이', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 25)
    ax.set_xticks(YEARS_FULL)
    ax.set_xticklabels(YEARS_FULL, rotation=45, ha='right')
    ax.axhline(y=5, color='gray', linestyle='--', alpha=0.5)
    ax.text(2023, 6.5, '약 5%로 안정', fontsize=10, color='gray')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_japanese_rate_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_japanese_rate_ko.png")


def create_summary_stats():
    """15년간의 기록 (요약 카드)"""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')

    stats = [
        ('총 게시물 수', '820회', '#3498db'),
        ('총 소개 기사 수', '13,606건', '#27ae60'),
        ('운영 기간', '15년', '#9b59b6'),
        ('평균 업데이트 빈도', '주 1회', '#e74c3c'),
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
    ax.set_title('15년간의 기록', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_summary_stats_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_summary_stats_ko.png")


def create_info_sources():
    """정보 소스의 변화 (초기/중기/후기)"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.suptitle('정보 소스의 변화: 개인 블로그에서 공식 문서로', fontsize=16, fontweight='bold', y=1.02)

    # 초기
    sources_early = ['github.com', 'd.hatena.ne.jp', 'slideshare.net', 'amazon.co.jp', 'amazon.com']
    values_early = [327, 154, 147, 98, 83]
    colors_early = ['#2c3e50', '#e74c3c', '#9b59b6', '#f39c12', '#f39c12']

    # 중기
    sources_mid = ['github.com', 'medium.com', 'developers.google.com', 'webkit.org', 'nodejs.org']
    values_mid = [828, 134, 103, 69, 64]
    colors_mid = ['#2c3e50', '#27ae60', '#3498db', '#3498db', '#27ae60']

    # 후기
    sources_late = ['github.com', 'nodejs.org', 'bun.sh', 'zenn.dev', 'developer.chrome.com']
    values_late = [568, 98, 62, 56, 55]
    colors_late = ['#2c3e50', '#27ae60', '#e67e22', '#3498db', '#3498db']

    def create_bar_chart(ax, sources, values, colors, title, period_desc):
        y_pos = np.arange(len(sources))
        bars = ax.barh(y_pos, values, color=colors, alpha=0.8)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(sources, fontsize=10)
        ax.invert_yaxis()
        ax.set_xlabel('건수', fontsize=10)
        ax.set_title(title, fontsize=12, fontweight='bold')

        for i, (bar, val) in enumerate(zip(bars, values)):
            ax.text(val + 5, bar.get_y() + bar.get_height()/2, str(val),
                    va='center', fontsize=9)

        ax.text(0.5, -0.12, period_desc, transform=ax.transAxes, fontsize=9,
                ha='center', style='italic', color='#666')

    create_bar_chart(axes[0], sources_early, values_early, colors_early,
                     '초기 (2011-2013)', '개인 블로그/슬라이드/서적이 주류')
    create_bar_chart(axes[1], sources_mid, values_mid, colors_mid,
                     '중기 (2017-2019)', 'Medium 부상, 벤더 공식이 상위로')
    create_bar_chart(axes[2], sources_late, values_late, colors_late,
                     '후기 (2023-2025)', '공식 문서/1차 정보가 중심')

    category_colors = {
        'GitHub': '#2c3e50',
        '개인 블로그/플랫폼': '#e74c3c',
        '공식 문서/벤더': '#3498db',
        '신흥 플랫폼': '#27ae60',
        '슬라이드/서적': '#9b59b6',
    }
    legend_patches = [mpatches.Patch(color=v, label=k, alpha=0.8)
                      for k, v in list(category_colors.items())]
    fig.legend(handles=legend_patches, loc='lower center', ncol=5, fontsize=9,
               bbox_to_anchor=(0.5, -0.02))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_info_sources_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_info_sources_ko.png")


def create_jp_platforms():
    """일본어 블로그 플랫폼의 변천"""
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('일본어 블로그 플랫폼의 변천', fontsize=16, fontweight='bold')

    years = [2011, 2014, 2016, 2018, 2020, 2021, 2024]
    hatena = [92, 29, 10, 5, 3, 1, 2]
    qiita = [0, 19, 45, 30, 4, 1, 1]
    zenn = [0, 0, 0, 0, 3, 22, 24]

    ax.stackplot(years, hatena, qiita, zenn,
                 labels=['Hatena', 'Qiita', 'Zenn'],
                 colors=['#e74c3c', '#55c500', '#3ea8ff'],
                 alpha=0.8)

    ax.set_xlabel('연도', fontsize=11)
    ax.set_ylabel('기사 수', fontsize=11)
    ax.legend(loc='upper right')

    ax.axvline(x=2015, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=2020, color='gray', linestyle='--', alpha=0.5)

    ax.text(2012.5, 80, 'Hatena 시대', fontsize=10, ha='center', style='italic', color='#666')
    ax.text(2017.5, 50, 'Qiita 시대', fontsize=10, ha='center', style='italic', color='#666')
    ax.text(2022.5, 30, 'Zenn 시대', fontsize=10, ha='center', style='italic', color='#666')

    ax.set_xlim(2011, 2024)
    ax.set_ylim(0, 120)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_jp_platforms_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_jp_platforms_ko.png")


def create_ui_frameworks():
    """UI 프레임워크 추이"""
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

    ax.set_xlabel('연도', fontsize=12)
    ax.set_ylabel('언급 수', fontsize=12)
    ax.set_title('UI 프레임워크: jQuery → Angular → React', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11)
    ax.set_ylim(0, 180)
    ax.annotate('jQuery 시대', xy=(2011, 109), xytext=(2012.5, 140),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)
    ax.annotate('React 피크\n153건', xy=(2017, 153), xytext=(2019, 165),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_ui_frameworks_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_ui_frameworks_ko.png")


def create_build_tools():
    """빌드 도구 추이"""
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

    ax.set_xlabel('연도', fontsize=12)
    ax.set_ylabel('언급 수', fontsize=12)
    ax.set_title('빌드 도구: webpack → Vite', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11)
    ax.annotate('webpack 피크', xy=(2017, 43), xytext=(2018.5, 48),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)
    ax.annotate('Vite 부상', xy=(2022, 28), xytext=(2020, 35),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_build_tools_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_build_tools_ko.png")


def create_runtimes():
    """런타임 다양화"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years_runtime = [2020, 2021, 2022, 2023, 2024, 2025]
    deno = [13, 21, 21, 19, 18, 15]
    bun = [0, 1, 5, 27, 26, 20]

    ax.bar([y - 0.2 for y in years_runtime], deno, width=0.4, label='Deno', color='#000000', alpha=0.8)
    ax.bar([y + 0.2 for y in years_runtime], bun, width=0.4, label='Bun', color='#fbf0df', edgecolor='#f9c144', linewidth=2)

    ax.set_xlabel('연도', fontsize=12)
    ax.set_ylabel('언급 수', fontsize=12)
    ax.set_title('런타임 다양화: Node.js 독주에서 경쟁 시대로', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=11)
    ax.text(0.95, 0.95, 'Node.js는 기반으로서\n항상 다수 언급됨',
             transform=ax.transAxes, fontsize=10, ha='right', va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_runtimes_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_runtimes_ko.png")


def create_tech_changes():
    """언급이 변화한 기술"""
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
    ax.set_xlabel('건수 (좌: 언급 감소 / 우: 언급 증가)', fontsize=11)
    ax.set_title('15년간 언급이 변화한 기술', fontsize=14, fontweight='bold')

    ax.axhline(y=len(not_mentioned) + 0.5, color='gray', linestyle='--', alpha=0.5)
    ax.text(-60, len(not_mentioned) + 0.5, '사라진 기술', fontsize=10, color='#e74c3c', va='center')
    ax.text(60, len(not_mentioned) + 0.5, '부상한 기술', fontsize=10, color='#27ae60', va='center')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_tech_changes_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_tech_changes_ko.png")


def create_cross_topics():
    """횡단적 토픽의 추이"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [2011, 2014, 2017, 2020, 2021, 2025]
    types_data = [30, 52, 108, 123, 129, 88]
    test = [46, 87, 86, 44, 59, 47]
    performance = [27, 58, 93, 80, 64, 42]
    security = [10, 14, 15, 13, 28, 15]
    a11y = [6, 9, 15, 16, 17, 23]

    ax.plot(years, types_data, 'o-', label='타입(TypeScript)', color='#3178c6', linewidth=2, markersize=8)
    ax.plot(years, test, 's-', label='테스트', color='#27ae60', linewidth=2, markersize=8)
    ax.plot(years, performance, '^-', label='퍼포먼스', color='#e74c3c', linewidth=2, markersize=8)
    ax.plot(years, security, 'D-', label='보안', color='#9b59b6', linewidth=2, markersize=8)
    ax.plot(years, a11y, 'p-', label='a11y', color='#f39c12', linewidth=2, markersize=8)

    ax.set_xlabel('연도', fontsize=12)
    ax.set_ylabel('언급 수', fontsize=12)
    ax.set_title('횡단적 토픽의 추이', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.set_ylim(0, 150)

    ax.annotate('TypeScript 피크\n(당연해진 시점)', xy=(2021, 129), xytext=(2017.5, 140),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)
    ax.annotate('a11y만 유일하게\n상승 트렌드', xy=(2025, 23), xytext=(2022.5, 45),
                arrowprops=dict(arrowstyle='->', color='#f39c12'), fontsize=10, color='#f39c12')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_cross_topics_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_cross_topics_ko.png")


def create_dev_practices():
    """개발 프랙티스의 변화"""
    fig, ax = plt.subplots(figsize=(10, 6))

    practices = ['CI/CD', 'Migration/이행', 'RFC/Proposal', 'Breaking Change']
    early = [31, 10, 2, 3]
    mid = [56, 32, 73, 15]
    late = [67, 56, 45, 17]

    x = np.arange(len(practices))
    width = 0.25

    ax.bar(x - width, early, width, label='2011-13', color='#3498db', alpha=0.6)
    ax.bar(x, mid, width, label='2017-19', color='#3498db', alpha=0.8)
    ax.bar(x + width, late, width, label='2023-25', color='#3498db', alpha=1.0)

    ax.set_xlabel('토픽', fontsize=12)
    ax.set_ylabel('건수', fontsize=12)
    ax.set_title('개발 프랙티스의 변화', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(practices, fontsize=11)
    ax.legend(loc='upper right', fontsize=11)

    ax.text(0.02, 0.95, 'CI/CD: 지속적 통합의 보급\nMigration: 에코시스템 성숙의 증거',
             transform=ax.transAxes, fontsize=10, va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_dev_practices_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_dev_practices_ko.png")


def create_publisher_types():
    """정보 소스 구성 변화 (공식/GitHub/개인 블로그)"""
    fig, ax = plt.subplots(figsize=(10, 6))

    periods = ['2011-13', '2023-25']
    x = np.arange(len(periods))

    # 데이터: 공식/GitHub/개인 블로그 3분류
    official = [204, 479]
    github = [506, 596]
    personal = [213, 70]

    width = 0.25

    bars1 = ax.bar(x - width, official, width, label='공식', color='#27ae60')
    bars2 = ax.bar(x, github, width, label='GitHub', color='#2c3e50')
    bars3 = ax.bar(x + width, personal, width, label='개인 블로그', color='#3498db')

    ax.set_xlabel('기간', fontsize=12)
    ax.set_ylabel('건수', fontsize=12)
    ax.set_title('정보 소스의 변화: 개인 블로그 vs 공식', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(periods, fontsize=12)
    ax.legend(loc='upper right', fontsize=10)

    # 수치 라벨 추가
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{int(height)}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

    # 변화율 주석
    ax.text(0.5, 0.95, '공식: +135%  GitHub: 안정  개인 블로그: -67%',
            transform=ax.transAxes, fontsize=11, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_publisher_types_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_publisher_types_ko.png")


def create_content_types_bar():
    """콘텐츠 타입별 추이"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years = ['2011-13', '2017-19', '2023-25']
    release_notes = [23, 305, 349]
    official_docs = [31, 68, 328]
    books = [257, 73, 18]
    slides = [179, 63, 13]

    x = np.arange(len(years))
    width = 0.2

    bars1 = ax.bar(x - 1.5*width, release_notes, width, label='릴리스 노트', color='#27ae60')
    bars2 = ax.bar(x - 0.5*width, official_docs, width, label='공식 문서', color='#3498db')
    bars3 = ax.bar(x + 0.5*width, books, width, label='서적', color='#e74c3c')
    bars4 = ax.bar(x + 1.5*width, slides, width, label='슬라이드', color='#9b59b6')

    ax.set_xlabel('기간', fontsize=12)
    ax.set_ylabel('건수', fontsize=12)
    ax.set_title('콘텐츠 타입별 추이', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=12)
    ax.legend(loc='upper right', fontsize=10)

    for bars in [bars1, bars2, bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            if height > 50:
                ax.annotate(f'{int(height)}',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3), textcoords="offset points",
                            ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_content_types_bar_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_content_types_bar_ko.png")


def create_content_change_rate():
    """콘텐츠 타입 변화율"""
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['릴리스 노트', '공식 문서', '서적', '슬라이드']
    changes = [
        (349-23)/23*100,
        (328-31)/31*100,
        (18-257)/257*100,
        (13-179)/179*100
    ]
    colors = ['#27ae60' if c > 0 else '#e74c3c' for c in changes]

    bars = ax.barh(categories, changes, color=colors, alpha=0.8, height=0.6)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_xlabel('변화율 (%)', fontsize=12)
    ax.set_title('콘텐츠 타입 변화율 (초기→후기)', fontsize=14, fontweight='bold')

    # 바 내부에 흰색 텍스트로 % 표시
    for bar, val in zip(bars, changes):
        if val > 0:
            x_pos = val / 2
            ax.text(x_pos, bar.get_y() + bar.get_height()/2,
                    f'{val:+.0f}%', va='center', ha='center', fontsize=12, fontweight='bold',
                    color='white')
        else:
            x_pos = val / 2
            ax.text(x_pos, bar.get_y() + bar.get_height()/2,
                    f'{val:+.0f}%', va='center', ha='center', fontsize=12, fontweight='bold',
                    color='white')

    ax.text(0.95, 0.05, '스터디/서적에서\n공식 문서/\n릴리스 노트로',
             transform=ax.transAxes, fontsize=11, ha='right', va='bottom',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_content_change_rate_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_content_change_rate_ko.png")


def create_summary():
    """Before/After 비교 (총괄)"""
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.axis('off')
    fig.suptitle('JSer.info 15년간의 변화', fontsize=28, fontweight='bold', y=0.97)

    # 좌측 (2011)
    ax.add_patch(FancyBboxPatch((0.02, 0.05), 0.38, 0.88,
                                 boxstyle="round,pad=0.02",
                                 facecolor='#e74c3c', alpha=0.10,
                                 edgecolor='#e74c3c', linewidth=3))
    ax.text(0.21, 0.95, '2011', fontsize=32, fontweight='bold', ha='center', color='#c0392b')

    # 우측 (2025)
    ax.add_patch(FancyBboxPatch((0.60, 0.05), 0.38, 0.88,
                                 boxstyle="round,pad=0.02",
                                 facecolor='#3498db', alpha=0.10,
                                 edgecolor='#3498db', linewidth=3))
    ax.text(0.79, 0.95, '2025', fontsize=32, fontweight='bold', ha='center', color='#2980b9')

    # 비교 항목 (나란히)
    comparisons = [
        {'label': '정보 소스', 'left': 'Hatena/SlideShare\n서적/개인 블로그',
         'right': 'GitHub/공식 문서\n릴리스 노트', 'y': 0.78, 'color': '#3498db'},
        {'label': 'UI 프레임워크', 'left': 'jQuery\nBackbone.js',
         'right': 'React\n(안정기)', 'y': 0.63, 'color': '#0769ad'},
        {'label': '빌드 도구', 'left': 'Grunt / Gulp',
         'right': 'Vite / esbuild', 'y': 0.50, 'color': '#646cff'},
        {'label': '소개 스타일', 'left': '22건/게시물\n평균 62자',
         'right': '13건/게시물\n평균 108자', 'y': 0.35, 'color': '#27ae60'},
        {'label': '일본어 비율', 'left': '22%', 'right': '5%', 'y': 0.22, 'color': '#e67e22'},
        {'label': '정보 소스', 'left': '개인 블로그 중심',
         'right': '공식 사이트/프로젝트 중심', 'y': 0.09, 'color': '#9b59b6'},
    ]

    for i, comp in enumerate(comparisons):
        y = comp['y']
        color = comp['color']

        # 구분선
        if i > 0:
            line_y = (comp['y'] + comparisons[i-1]['y']) / 2
            ax.axhline(y=line_y, xmin=0.05, xmax=0.95, color='#ddd', linestyle='-', linewidth=1.5)

        # 라벨
        ax.add_patch(FancyBboxPatch((0.41, y - 0.03), 0.18, 0.06,
                                     boxstyle="round,pad=0.008",
                                     facecolor=color, alpha=0.95))
        ax.text(0.5, y, comp['label'], fontsize=14, ha='center', va='center',
                fontweight='bold', color='white')

        # 좌측 값
        ax.text(0.21, y, comp['left'], fontsize=16, ha='center', va='center',
                color='#922b21', fontweight='bold', linespacing=1.5)

        # 우측 값
        ax.text(0.79, y, comp['right'], fontsize=16, ha='center', va='center',
                color='#1a5276', fontweight='bold', linespacing=1.5)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_summary_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_summary_ko.png")


# =============================================================================
# 통합 버전 (여러 차트를 하나로)
# =============================================================================

def create_basic_stats_combined():
    """기본 통계 대시보드 (4개 통합)"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('JSer.info 15주년: 기본 통계', fontsize=18, fontweight='bold', y=0.98)

    # 1-1: 연도별 소개 기사 수와 게시물 수
    ax1 = axes[0, 0]
    ax1_twin = ax1.twinx()
    ax1.bar(YEARS_FULL, ARTICLES, color='#3498db', alpha=0.7, label='소개 기사 수', width=0.7)
    ax1_twin.plot(YEARS_FULL, POSTS, 'o-', color='#e74c3c', linewidth=2, markersize=6)
    ax1.set_xlabel('연도', fontsize=11)
    ax1.set_ylabel('소개 기사 수', color='#3498db', fontsize=11)
    ax1_twin.set_ylabel('게시물 수', color='#e74c3c', fontsize=11)
    ax1.set_title('연도별 소개 기사 수와 게시물 수 추이', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 1500)
    ax1_twin.set_ylim(30, 75)
    ax1.set_xticks(YEARS_FULL[::2])
    legend_elements = [mpatches.Patch(facecolor='#3498db', alpha=0.7, label='소개 기사 수'),
                       Line2D([0], [0], color='#e74c3c', marker='o', label='게시물 수')]
    ax1.legend(handles=legend_elements, loc='upper right')
    ax1.annotate('피크\n1,269건', xy=(2013, 1269), xytext=(2014.5, 1350),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

    # 1-2: '양보다 질'로의 변화
    ax2 = axes[0, 1]
    ax2_twin = ax2.twinx()
    ax2.bar(YEARS_FULL, PER_POST, color='#9b59b6', alpha=0.7, width=0.7)
    ax2_twin.plot(YEARS_FULL, AVG_CHARS, 's-', color='#27ae60', linewidth=2, markersize=6)
    ax2.set_xlabel('연도', fontsize=11)
    ax2.set_ylabel('게시물당 건수', color='#9b59b6', fontsize=11)
    ax2_twin.set_ylabel('소개문 평균 글자 수', color='#27ae60', fontsize=11)
    ax2.set_title("'양보다 질'로의 변화", fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 30)
    ax2_twin.set_ylim(40, 130)
    ax2.set_xticks(YEARS_FULL[::2])
    legend_elements2 = [mpatches.Patch(facecolor='#9b59b6', alpha=0.7, label='게시물당 건수'),
                        Line2D([0], [0], color='#27ae60', marker='s', label='평균 글자 수')]
    ax2.legend(handles=legend_elements2, loc='upper right')
    ax2.annotate('2013년 피크', xy=(2013, 22.3), xytext=(2015, 26),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

    # 1-3: 일본어 비율 추이
    ax3 = axes[1, 0]
    ax3.fill_between(YEARS_FULL, JP_RATE, alpha=0.3, color='#e74c3c')
    ax3.plot(YEARS_FULL, JP_RATE, 'o-', color='#e74c3c', linewidth=2, markersize=6)
    ax3.set_xlabel('연도', fontsize=11)
    ax3.set_ylabel('일본어 비율 (%)', fontsize=11)
    ax3.set_title('일본어 소스 비율 추이', fontsize=12, fontweight='bold')
    ax3.set_ylim(0, 25)
    ax3.set_xticks(YEARS_FULL[::2])
    ax3.axhline(y=5, color='gray', linestyle='--', alpha=0.5)
    ax3.text(2023, 6.5, '약 5%로 안정', fontsize=9, color='gray')

    # 1-4: 15년간 누적 요약
    ax4 = axes[1, 1]
    ax4.axis('off')
    stats = [
        ('총 게시물 수', '820회', '#3498db'),
        ('총 소개 기사 수', '13,606건', '#27ae60'),
        ('운영 기간', '15년', '#9b59b6'),
        ('평균 업데이트 빈도', '주 1회', '#e74c3c'),
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
    ax4.set_title('15년간의 기록', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_basic_stats_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_basic_stats_ko.png (combined)")


def create_tech_trends_combined():
    """기술 트렌드 대시보드 (4개 통합)"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('기술 트렌드의 변천', fontsize=18, fontweight='bold', y=0.98)

    # 2-1: UI 프레임워크
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
    ax1.set_xlabel('연도', fontsize=11)
    ax1.set_ylabel('언급 수', fontsize=11)
    ax1.set_title('UI 프레임워크: jQuery → Angular → React', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right')
    ax1.set_ylim(0, 180)
    ax1.annotate('jQuery 시대', xy=(2011, 109), xytext=(2012, 130),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
    ax1.annotate('React 피크\n153건', xy=(2017, 153), xytext=(2018.5, 165),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

    # 2-2: 빌드 도구
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
    ax2.set_xlabel('연도', fontsize=11)
    ax2.set_ylabel('언급 수', fontsize=11)
    ax2.set_title('빌드 도구: webpack → Vite', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right')
    ax2.annotate('webpack 피크', xy=(2017, 43), xytext=(2018, 50),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
    ax2.annotate('Vite 부상', xy=(2022, 28), xytext=(2020.5, 35),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

    # 2-3: 런타임
    ax3 = axes[1, 0]
    years_runtime = [2020, 2021, 2022, 2023, 2024, 2025]
    deno = [13, 21, 21, 19, 18, 15]
    bun = [0, 1, 5, 27, 26, 20]
    ax3.bar([y - 0.2 for y in years_runtime], deno, width=0.4, label='Deno', color='#000000', alpha=0.8)
    ax3.bar([y + 0.2 for y in years_runtime], bun, width=0.4, label='Bun', color='#fbf0df', edgecolor='#f9c144', linewidth=2)
    ax3.set_xlabel('연도', fontsize=11)
    ax3.set_ylabel('언급 수', fontsize=11)
    ax3.set_title('런타임 다양화: Node.js 독주에서 경쟁 시대로', fontsize=12, fontweight='bold')
    ax3.legend(loc='upper left')
    ax3.text(0.95, 0.95, 'Node.js는 기반으로서\n항상 다수 언급됨\n(별도 스케일)',
             transform=ax3.transAxes, fontsize=9, ha='right', va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    # 2-4: 언급이 변화한 기술
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
    ax4.set_xlabel('건수 (좌: 감소 / 우: 증가)', fontsize=10)
    ax4.set_title('15년간 언급이 변화한 기술', fontsize=12, fontweight='bold')
    ax4.axhline(y=len(not_mentioned) + 0.5, color='gray', linestyle='--', alpha=0.5)
    ax4.text(-60, len(not_mentioned) + 0.5, '사라진 기술', fontsize=9, color='#e74c3c', va='center')
    ax4.text(60, len(not_mentioned) + 0.5, '부상한 기술', fontsize=9, color='#27ae60', va='center')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_tech_trends_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_tech_trends_ko.png (combined)")


def create_topics_combined():
    """횡단적 토픽 대시보드 (2개 통합)"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('횡단적 토픽의 변화', fontsize=16, fontweight='bold', y=1.02)

    # 횡단적 토픽의 추이
    ax1 = axes[0]
    years = [2011, 2014, 2017, 2020, 2021, 2025]
    types_data = [30, 52, 108, 123, 129, 88]
    test = [46, 87, 86, 44, 59, 47]
    performance = [27, 58, 93, 80, 64, 42]
    security = [10, 14, 15, 13, 28, 15]
    a11y = [6, 9, 15, 16, 17, 23]
    ax1.plot(years, types_data, 'o-', label='타입(TypeScript)', color='#3178c6', linewidth=2, markersize=8)
    ax1.plot(years, test, 's-', label='테스트', color='#27ae60', linewidth=2, markersize=8)
    ax1.plot(years, performance, '^-', label='퍼포먼스', color='#e74c3c', linewidth=2, markersize=8)
    ax1.plot(years, security, 'D-', label='보안', color='#9b59b6', linewidth=2, markersize=8)
    ax1.plot(years, a11y, 'p-', label='a11y', color='#f39c12', linewidth=2, markersize=8)
    ax1.set_xlabel('연도', fontsize=11)
    ax1.set_ylabel('언급 수', fontsize=11)
    ax1.set_title('횡단적 토픽의 추이', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right')
    ax1.set_ylim(0, 150)
    ax1.annotate('TypeScript 피크\n(당연해진 시점)', xy=(2021, 129), xytext=(2018, 140),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
    ax1.annotate('a11y만 유일하게\n상승 트렌드', xy=(2025, 23), xytext=(2023, 40),
                arrowprops=dict(arrowstyle='->', color='#f39c12'), fontsize=9, color='#f39c12')

    # 개발 프랙티스의 변화
    ax2 = axes[1]
    practices = ['CI/CD', 'Migration/이행', 'RFC/Proposal', 'Breaking Change']
    early = [31, 10, 2, 3]
    mid = [56, 32, 73, 15]
    late = [67, 56, 45, 17]
    x = np.arange(len(practices))
    width = 0.25
    ax2.bar(x - width, early, width, label='2011-13', color='#3498db', alpha=0.6)
    ax2.bar(x, mid, width, label='2017-19', color='#3498db', alpha=0.8)
    ax2.bar(x + width, late, width, label='2023-25', color='#3498db', alpha=1.0)
    ax2.set_xlabel('토픽', fontsize=11)
    ax2.set_ylabel('건수', fontsize=11)
    ax2.set_title('개발 프랙티스의 변화', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(practices, rotation=15, ha='right')
    ax2.legend(loc='upper right')
    ax2.text(0.05, 0.95, 'CI/CD: 지속적 통합의 보급\nMigration: 에코시스템 성숙의 증거',
             transform=ax2.transAxes, fontsize=9, va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_topics_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_topics_ko.png (combined)")


def create_publishers_combined():
    """정보 소스 대시보드 (2개 통합)"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('정보 소스의 변화', fontsize=16, fontweight='bold', y=1.02)

    # 좌: 공식/GitHub/개인 블로그 비교
    ax1 = axes[0]
    periods = ['2011-13', '2023-25']
    x = np.arange(len(periods))
    official = [204, 479]
    github = [506, 596]
    personal = [213, 70]
    width = 0.25
    bars1 = ax1.bar(x - width, official, width, label='공식', color='#27ae60')
    bars2 = ax1.bar(x, github, width, label='GitHub', color='#2c3e50')
    bars3 = ax1.bar(x + width, personal, width, label='개인 블로그', color='#3498db')
    ax1.set_xlabel('기간', fontsize=11)
    ax1.set_ylabel('건수', fontsize=11)
    ax1.set_title('정보 소스 구성 변화', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(periods)
    ax1.legend(loc='upper right')
    # 수치 라벨
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax1.annotate(f'{int(height)}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=9, fontweight='bold')

    # 우: 변화를 보여주는 플로우 다이어그램
    ax2 = axes[1]
    ax2.axis('off')
    categories = ['개인 블로그', 'GitHub', '공식']
    colors = ['#3498db', '#2c3e50', '#27ae60']
    changes = ['-67%', '안정', '+135%']
    ax2.text(0.1, 0.85, '2011-13', fontsize=12, fontweight='bold', ha='center')
    ax2.add_patch(mpatches.FancyBboxPatch((0.02, 0.55), 0.16, 0.25,
                                           boxstyle="round,pad=0.02",
                                           facecolor='#3498db', alpha=0.8))
    ax2.text(0.1, 0.675, '개인 블로그\n≒ 공식', fontsize=10, ha='center', va='center', color='white')
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
    ax2.text(0.85, 0.675, '공식이\n개인 블로그의\n7배', fontsize=10,
             ha='center', va='center', color='white')
    ax2.text(0.1, 0.38, '개인 블로그', fontsize=10, ha='center', color='#3498db')
    ax2.text(0.1, 0.18, 'GitHub', fontsize=10, ha='center', color='#2c3e50')
    ax2.text(0.9, 0.38, '공식', fontsize=10, ha='center', color='#27ae60')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_title('정보 소스 주체의 변화', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_publishers_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_publishers_ko.png (combined)")


def create_content_types_combined():
    """콘텐츠 타입 대시보드 (2개 통합)"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("콘텐츠 타입의 변화: 'JavaScript 학습 방법'의 변화", fontsize=16, fontweight='bold', y=1.02)

    # 콘텐츠 타입별 추이
    ax1 = axes[0]
    years = ['2011-13', '2017-19', '2023-25']
    release_notes = [23, 305, 349]
    official_docs = [31, 68, 328]
    books = [257, 73, 18]
    slides = [179, 63, 13]
    x = np.arange(len(years))
    width = 0.2
    bars1 = ax1.bar(x - 1.5*width, release_notes, width, label='릴리스 노트', color='#27ae60')
    bars2 = ax1.bar(x - 0.5*width, official_docs, width, label='공식 문서', color='#3498db')
    bars3 = ax1.bar(x + 0.5*width, books, width, label='서적', color='#e74c3c')
    bars4 = ax1.bar(x + 1.5*width, slides, width, label='슬라이드', color='#9b59b6')
    ax1.set_xlabel('기간', fontsize=11)
    ax1.set_ylabel('건수', fontsize=11)
    ax1.set_title('콘텐츠 타입별 추이', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.legend(loc='upper right')
    for bars in [bars1, bars2, bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            if height > 50:
                ax1.annotate(f'{int(height)}',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3), textcoords="offset points",
                            ha='center', va='bottom', fontsize=8)

    # 변화율
    ax2 = axes[1]
    categories = ['릴리스 노트', '공식 문서', '서적', '슬라이드']
    changes = [(349-23)/23*100, (328-31)/31*100, (18-257)/257*100, (13-179)/179*100]
    colors = ['#27ae60' if c > 0 else '#e74c3c' for c in changes]
    bars = ax2.barh(categories, changes, color=colors, alpha=0.8)
    ax2.axvline(x=0, color='black', linewidth=0.5)
    ax2.set_xlabel('변화율 (%)', fontsize=11)
    ax2.set_title('초기→후기 변화율', fontsize=12, fontweight='bold')
    # 바 내부에 흰색 텍스트로 % 표시
    for bar, val in zip(bars, changes):
        x_pos = val / 2
        ax2.text(x_pos, bar.get_y() + bar.get_height()/2,
                 f'{val:+.0f}%', va='center', ha='center', fontsize=10, fontweight='bold',
                 color='white')
    ax2.text(0.95, 0.05, '스터디/서적에서\n공식 문서/\n릴리스 노트로',
             transform=ax2.transAxes, fontsize=10, ha='right', va='bottom',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_content_types_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_content_types_ko.png (combined)")


# =============================================================================
# 메인 실행
# =============================================================================

def create_bookmark_correlation():
    """북마크 수와 JSer.info 업데이트 수의 상관관계"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('북마크와 JSer.info 업데이트의 상관관계 (2020-2025)', fontsize=18, fontweight='bold', y=0.98)

    # 데이터
    years = [2020, 2021, 2022, 2023, 2024, 2025]
    bookmarks = [2473, 2862, 2536, 2373, 1752, 1033]  # 북마크 수
    jser_items = [810, 789, 712, 737, 638, 552]  # JSer.info 소개 기사 수

    # 변환율 (JSer.info / 북마크)
    conversion_rate = [j/b*100 for j, b in zip(jser_items, bookmarks)]

    # 1-1: 북마크 vs JSer.info
    ax1 = axes[0, 0]
    x = np.arange(len(years))
    width = 0.35
    ax1.bar(x - width/2, bookmarks, width, label='북마크', color='#3498db', alpha=0.8)
    ax1.bar(x + width/2, jser_items, width, label='JSer.info', color='#e74c3c', alpha=0.8)
    ax1.set_xlabel('연도', fontsize=11)
    ax1.set_ylabel('건수', fontsize=11)
    ax1.set_title('북마크 수 vs JSer.info 소개 기사 수', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.legend(loc='upper right')
    for i, (b, j) in enumerate(zip(bookmarks, jser_items)):
        ax1.text(i - width/2, b + 50, str(b), ha='center', fontsize=9)
        ax1.text(i + width/2, j + 50, str(j), ha='center', fontsize=9)

    # 1-2: 변환 효율 추이
    ax2 = axes[0, 1]
    ax2.fill_between(years, conversion_rate, alpha=0.3, color='#27ae60')
    ax2.plot(years, conversion_rate, 'o-', color='#27ae60', linewidth=2, markersize=8)
    ax2.set_xlabel('연도', fontsize=11)
    ax2.set_ylabel('변환율 (%)', fontsize=11)
    ax2.set_title('북마크 → JSer.info 변환 효율', fontsize=12, fontweight='bold')
    ax2.set_ylim(20, 60)
    for i, (y, r) in enumerate(zip(years, conversion_rate)):
        ax2.annotate(f'{r:.1f}%', xy=(y, r), xytext=(0, 10), textcoords='offset points',
                     ha='center', fontsize=10, fontweight='bold')
    ax2.text(0.05, 0.95, f'2020년: {conversion_rate[0]:.1f}% → 2025년: {conversion_rate[-1]:.1f}%\n효율 +{(conversion_rate[-1]/conversion_rate[0]-1)*100:.0f}%',
             transform=ax2.transAxes, fontsize=10, va='top',
             bbox=dict(boxstyle='round', facecolor='#ecf0f1', alpha=0.8))

    # 1-3: 상대 변화 (2020년=100)
    ax3 = axes[1, 0]
    bookmarks_rel = [b/bookmarks[0]*100 for b in bookmarks]
    jser_rel = [j/jser_items[0]*100 for j in jser_items]
    ax3.plot(years, bookmarks_rel, 'o-', label='북마크', color='#3498db', linewidth=2, markersize=8)
    ax3.plot(years, jser_rel, 's-', label='JSer.info', color='#e74c3c', linewidth=2, markersize=8)
    ax3.axhline(y=100, color='gray', linestyle='--', alpha=0.5)
    ax3.set_xlabel('연도', fontsize=11)
    ax3.set_ylabel('상대값 (2020년=100)', fontsize=11)
    ax3.set_title('상대 변화 비교', fontsize=12, fontweight='bold')
    ax3.legend(loc='upper right')
    ax3.set_ylim(30, 130)
    ax3.annotate(f'{bookmarks_rel[-1]:.0f}', xy=(2025, bookmarks_rel[-1]), xytext=(5, 0),
                 textcoords='offset points', fontsize=10, color='#3498db')
    ax3.annotate(f'{jser_rel[-1]:.0f}', xy=(2025, jser_rel[-1]), xytext=(5, 0),
                 textcoords='offset points', fontsize=10, color='#e74c3c')

    # 1-4: 요약
    ax4 = axes[1, 1]
    ax4.axis('off')

    # 요약 데이터
    bookmark_change = (bookmarks[-1] - bookmarks[0]) / bookmarks[0] * 100
    jser_change = (jser_items[-1] - jser_items[0]) / jser_items[0] * 100
    efficiency_change = (conversion_rate[-1] / conversion_rate[0] - 1) * 100

    summary_data = [
        ('인풋 (북마크)', f'{bookmark_change:+.0f}%', '#3498db'),
        ('아웃풋 (JSer.info)', f'{jser_change:+.0f}%', '#e74c3c'),
        ('변환 효율', f'{efficiency_change:+.0f}%', '#27ae60'),
    ]

    ax4.text(0.5, 0.95, '5년간의 변화', fontsize=16, fontweight='bold', ha='center', va='top')

    for i, (label, value, color) in enumerate(summary_data):
        y_pos = 0.75 - i * 0.25
        ax4.add_patch(mpatches.FancyBboxPatch((0.1, y_pos-0.08), 0.8, 0.18,
                                              boxstyle="round,pad=0.02",
                                              facecolor=color, alpha=0.15,
                                              edgecolor=color, linewidth=2))
        ax4.text(0.5, y_pos+0.02, value, fontsize=24, fontweight='bold',
                 ha='center', va='center', color=color)
        ax4.text(0.5, y_pos-0.04, label, fontsize=11, ha='center', va='center', color='#555')

    ax4.text(0.5, 0.08, '인풋이 줄어도\n아웃풋의 질을 유지',
             fontsize=11, ha='center', va='bottom', style='italic', color='#666')

    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/15th_bookmark_correlation_ko.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 15th_bookmark_correlation_ko.png")


def main():
    print("=" * 60)
    print("JSer.info 15주년 기사용 차트 생성 (한국어판)")
    print("=" * 60)

    print("\n--- 개별 차트 ---")
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

    print("\n--- 통합 차트 ---")
    create_basic_stats_combined()
    create_tech_trends_combined()
    create_topics_combined()
    create_publishers_combined()
    create_content_types_combined()

    print("\n" + "=" * 60)
    print("완료!")
    print("=" * 60)


if __name__ == '__main__':
    main()
