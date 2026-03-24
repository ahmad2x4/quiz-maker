#!/usr/bin/env python3
"""
Create statistical visualizations for data investigation quiz.
"""

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def create_column_graph(output_path):
    """Create a simple column graph showing favorite sports."""
    sports = ['Soccer', 'Basketball', 'Tennis', 'Swimming']
    frequencies = [8, 12, 6, 10]

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

    bars = ax.bar(sports, frequencies, color='#3b82f6', edgecolor='#1f2937', linewidth=2)

    ax.set_xlabel('Sport', fontsize=12, weight='bold')
    ax.set_ylabel('Frequency (Number of Students)', fontsize=12, weight='bold')
    ax.set_title('Favorite Sports Survey', fontsize=14, weight='bold')
    ax.set_ylim(0, 15)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_dot_plot(output_path):
    """Create a dot plot showing test scores."""
    # Test scores: 4, 5, 5, 6, 6, 6, 7, 7, 8, 9, 10
    scores = [4, 5, 5, 6, 6, 6, 7, 7, 8, 9, 10]

    fig, ax = plt.subplots(figsize=(10, 4), dpi=150)

    # Count frequency of each score
    from collections import Counter
    counts = Counter(scores)

    # Plot dots
    for score, count in counts.items():
        for i in range(count):
            ax.plot(score, i, 'o', color='#3b82f6', markersize=12,
                   markeredgecolor='#1f2937', markeredgewidth=1.5)

    ax.set_xlabel('Test Score', fontsize=12, weight='bold')
    ax.set_ylabel('Frequency', fontsize=12, weight='bold')
    ax.set_title('Dot Plot of Test Scores', fontsize=14, weight='bold')
    ax.set_xlim(3, 11)
    ax.set_ylim(-0.5, 4)
    ax.set_xticks(range(4, 11))
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_histogram(output_path):
    """Create a frequency histogram showing age groups."""
    age_groups = ['10-14', '15-19', '20-24', '25-29', '30-34']
    frequencies = [12, 25, 18, 10, 8]

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

    x_pos = np.arange(len(age_groups))
    bars = ax.bar(x_pos, frequencies, width=0.9, color='#3b82f6',
                   edgecolor='#1f2937', linewidth=2)

    ax.set_xlabel('Age Group (years)', fontsize=12, weight='bold')
    ax.set_ylabel('Frequency', fontsize=12, weight='bold')
    ax.set_title('Age Distribution Histogram', fontsize=14, weight='bold')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(age_groups)
    ax.set_ylim(0, 30)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_back_to_back_stemleaf(output_path):
    """Create a back-to-back stem-and-leaf plot visualization."""
    fig, ax = plt.subplots(figsize=(10, 8), dpi=150)
    ax.axis('off')

    # Title
    ax.text(0.5, 0.95, 'Back-to-Back Stem-and-Leaf Plot',
            ha='center', fontsize=16, weight='bold', transform=ax.transAxes)
    ax.text(0.5, 0.90, 'Team A vs Team B Scores',
            ha='center', fontsize=12, transform=ax.transAxes)

    # Headers
    ax.text(0.25, 0.80, 'Team A', ha='center', fontsize=14, weight='bold', transform=ax.transAxes)
    ax.text(0.5, 0.80, 'Stem', ha='center', fontsize=14, weight='bold', transform=ax.transAxes)
    ax.text(0.75, 0.80, 'Team B', ha='center', fontsize=14, weight='bold', transform=ax.transAxes)

    # Data
    data = [
        ('7  5', '4', '2  8'),
        ('3  1', '5', '2  5  8'),
        ('8  4  2', '6', '0  3  7'),
    ]

    y_start = 0.70
    y_step = 0.10

    for i, (team_a, stem, team_b) in enumerate(data):
        y = y_start - i * y_step
        ax.text(0.25, y, team_a, ha='center', fontsize=12, family='monospace', transform=ax.transAxes)
        ax.text(0.5, y, stem, ha='center', fontsize=12, weight='bold', family='monospace', transform=ax.transAxes)
        ax.text(0.75, y, team_b, ha='left', fontsize=12, family='monospace', transform=ax.transAxes)

    # Draw vertical lines
    ax.plot([0.42, 0.42], [0.40, 0.85], 'k-', linewidth=2, transform=ax.transAxes)
    ax.plot([0.58, 0.58], [0.40, 0.85], 'k-', linewidth=2, transform=ax.transAxes)

    # Note
    ax.text(0.5, 0.20, 'Example: Team A: 45, 47, 51, 53, 56, 62, 64, 68',
            ha='center', fontsize=10, style='italic', transform=ax.transAxes)
    ax.text(0.5, 0.15, 'Team B: 42, 48, 52, 55, 58, 60, 63, 67',
            ha='center', fontsize=10, style='italic', transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_frequency_polygon(output_path):
    """Create a frequency polygon."""
    # Class midpoints
    midpoints = [15, 25, 35, 45, 55, 65]
    frequencies = [5, 12, 15, 10, 6, 2]

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

    # Plot polygon
    ax.plot(midpoints, frequencies, 'o-', color='#3b82f6', linewidth=2.5,
            markersize=8, markeredgecolor='#1f2937', markeredgewidth=1.5)

    # Fill under the curve
    ax.fill_between(midpoints, frequencies, alpha=0.3, color='#93c5fd')

    ax.set_xlabel('Value (Class Midpoint)', fontsize=12, weight='bold')
    ax.set_ylabel('Frequency', fontsize=12, weight='bold')
    ax.set_title('Frequency Polygon', fontsize=14, weight='bold')
    ax.set_xlim(10, 70)
    ax.set_ylim(0, 18)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Add value labels
    for x, y in zip(midpoints, frequencies):
        ax.text(x, y + 0.5, str(y), ha='center', va='bottom', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_bimodal_distribution(output_path):
    """Create a bimodal distribution histogram."""
    # Create bimodal data
    np.random.seed(42)
    group1 = np.random.normal(30, 5, 100)
    group2 = np.random.normal(60, 5, 100)
    data = np.concatenate([group1, group2])

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

    # Create histogram
    n, bins, patches = ax.hist(data, bins=20, color='#3b82f6', edgecolor='#1f2937',
                               linewidth=1.5, alpha=0.7)

    ax.set_xlabel('Value', fontsize=12, weight='bold')
    ax.set_ylabel('Frequency', fontsize=12, weight='bold')
    ax.set_title('Bimodal Distribution', fontsize=14, weight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add annotations for peaks
    ax.annotate('Peak 1', xy=(30, max(n)*0.8), xytext=(20, max(n)*0.9),
                fontsize=11, weight='bold', color='#ef4444',
                arrowprops=dict(arrowstyle='->', color='#ef4444', lw=2))
    ax.annotate('Peak 2', xy=(60, max(n)*0.8), xytext=(70, max(n)*0.9),
                fontsize=11, weight='bold', color='#ef4444',
                arrowprops=dict(arrowstyle='->', color='#ef4444', lw=2))

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_skewed_distribution(output_path):
    """Create a positively skewed distribution."""
    np.random.seed(42)
    data = np.random.gamma(2, 2, 1000)

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

    n, bins, patches = ax.hist(data, bins=25, color='#3b82f6', edgecolor='#1f2937',
                               linewidth=1.5, alpha=0.7)

    # Calculate statistics
    mean_val = np.mean(data)
    median_val = np.median(data)

    # Add vertical lines for mean and median
    ax.axvline(mean_val, color='#ef4444', linestyle='--', linewidth=2, label=f'Mean = {mean_val:.1f}')
    ax.axvline(median_val, color='#10b981', linestyle='--', linewidth=2, label=f'Median = {median_val:.1f}')

    ax.set_xlabel('Value', fontsize=12, weight='bold')
    ax.set_ylabel('Frequency', fontsize=12, weight='bold')
    ax.set_title('Positively Skewed Distribution', fontsize=14, weight='bold')
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add annotation
    ax.text(0.65, 0.85, 'Tail extends to the right →',
            transform=ax.transAxes, fontsize=11, style='italic')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

if __name__ == "__main__":
    output_dir = "quizzes/statistics/data-investigation"

    if len(sys.argv) > 1:
        output_dir = sys.argv[1]

    os.makedirs(output_dir, exist_ok=True)

    print("Generating statistics visualizations...")

    create_column_graph(f"{output_dir}/graph-column-simple.png")
    create_dot_plot(f"{output_dir}/graph-dot-plot.png")
    create_histogram(f"{output_dir}/graph-histogram.png")
    create_back_to_back_stemleaf(f"{output_dir}/graph-back-to-back.png")
    create_frequency_polygon(f"{output_dir}/graph-frequency-polygon.png")
    create_bimodal_distribution(f"{output_dir}/graph-bimodal.png")
    create_skewed_distribution(f"{output_dir}/graph-skewed.png")

    print(f"\nAll diagrams created in: {output_dir}")
