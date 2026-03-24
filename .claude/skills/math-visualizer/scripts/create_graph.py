#!/usr/bin/env python3
"""
Graph Generator Script
Creates mathematical graphs using matplotlib.
"""

import sys
import argparse
import json
from pathlib import Path

try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    import numpy as np
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib not installed. Install with: pip install matplotlib numpy", file=sys.stderr)


def create_graph(function_str, x_range, y_range, output_path, title="", xlabel="x", ylabel="y"):
    """Create a graph of a mathematical function."""
    if not HAS_MATPLOTLIB:
        print("Error: matplotlib not installed", file=sys.stderr)
        return False

    try:
        # Parse function string
        # Expected format: "lambda x: x**2" or just "x**2"
        if not function_str.startswith("lambda"):
            function_str = f"lambda x: {function_str}"

        func = eval(function_str)

        # Generate x values
        x = np.linspace(x_range[0], x_range[1], 500)
        y = np.array([func(xi) for xi in x])

        # Create plot
        plt.figure(figsize=(8, 6), dpi=150)
        plt.plot(x, y, 'b-', linewidth=2)
        plt.grid(True, alpha=0.3)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)

        if title:
            plt.title(title, fontsize=14)

        if y_range:
            plt.ylim(y_range)

        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)

        # Save
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, bbox_inches='tight', dpi=150)
        plt.close()

        print(f"Graph saved to: {output_path}")
        return True

    except Exception as e:
        print(f"Error creating graph: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description='Create mathematical graphs')
    parser.add_argument('--function', required=True, help='Function to plot (e.g., "x**2" or "lambda x: x**2")')
    parser.add_argument('--xrange', nargs=2, type=float, default=[-10, 10], help='X-axis range')
    parser.add_argument('--yrange', nargs=2, type=float, default=None, help='Y-axis range')
    parser.add_argument('--output', required=True, help='Output file path')
    parser.add_argument('--title', default='', help='Graph title')
    parser.add_argument('--xlabel', default='x', help='X-axis label')
    parser.add_argument('--ylabel', default='y', help='Y-axis label')

    args = parser.parse_args()

    success = create_graph(
        args.function,
        args.xrange,
        args.yrange,
        args.output,
        args.title,
        args.xlabel,
        args.ylabel
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
