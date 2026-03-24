#!/usr/bin/env python3
"""
Create 3D shape visualizations for geometry quiz questions.
Generates diagrams of rectangular prisms, cylinders, spheres, and composite shapes.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import sys
import os

def create_rectangular_prism(length, width, height, output_path, show_dimensions=True):
    """Create a 3D visualization of a rectangular prism."""
    fig = plt.figure(figsize=(8, 6), dpi=150)
    ax = fig.add_subplot(111, projection='3d')

    # Define the vertices of the rectangular prism
    vertices = np.array([
        [0, 0, 0], [length, 0, 0], [length, width, 0], [0, width, 0],  # bottom
        [0, 0, height], [length, 0, height], [length, width, height], [0, width, height]  # top
    ])

    # Define the 6 faces
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # front
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # back
        [vertices[0], vertices[3], vertices[7], vertices[4]],  # left
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # right
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # bottom
        [vertices[4], vertices[5], vertices[6], vertices[7]]   # top
    ]

    # Create the 3D polygon collection
    face_collection = Poly3DCollection(faces, linewidths=1.5, edgecolors='#1f2937', alpha=0.7)
    face_collection.set_facecolor('#3b82f6')
    ax.add_collection3d(face_collection)

    # Add dimension labels if requested
    if show_dimensions:
        ax.text(length/2, -0.5, 0, f'{length} cm', fontsize=10, ha='center', color='#ef4444', weight='bold')
        ax.text(-0.5, width/2, 0, f'{width} cm', fontsize=10, ha='center', color='#ef4444', weight='bold')
        ax.text(-0.5, 0, height/2, f'{height} cm', fontsize=10, ha='center', color='#ef4444', weight='bold')

    # Set the aspect ratio and limits
    max_dim = max(length, width, height)
    ax.set_xlim([-0.5, max_dim + 0.5])
    ax.set_ylim([-0.5, max_dim + 0.5])
    ax.set_zlim([0, max_dim + 0.5])

    ax.set_xlabel('Length', fontsize=10)
    ax.set_ylabel('Width', fontsize=10)
    ax.set_zlabel('Height', fontsize=10)
    ax.set_title('Rectangular Prism', fontsize=12, weight='bold')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_cylinder(radius, height, output_path, show_dimensions=True):
    """Create a 3D visualization of a cylinder."""
    fig = plt.figure(figsize=(8, 6), dpi=150)
    ax = fig.add_subplot(111, projection='3d')

    # Create cylinder
    theta = np.linspace(0, 2*np.pi, 100)
    z = np.linspace(0, height, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)

    # Plot the cylinder surface
    ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.7, color='#3b82f6', edgecolor='none')

    # Plot top and bottom circles
    x_circle = radius * np.cos(theta)
    y_circle = radius * np.sin(theta)
    ax.plot(x_circle, y_circle, 0, color='#1f2937', linewidth=2)
    ax.plot(x_circle, y_circle, height, color='#1f2937', linewidth=2)

    # Add dimension labels if requested
    if show_dimensions:
        ax.text(0, 0, -0.3, f'r = {radius} cm', fontsize=10, ha='center', color='#ef4444', weight='bold')
        ax.text(-radius-0.5, 0, height/2, f'h = {height} cm', fontsize=10, ha='center', color='#ef4444', weight='bold')

    # Set the aspect ratio and limits
    max_dim = max(radius * 2, height)
    ax.set_xlim([-max_dim/2, max_dim/2])
    ax.set_ylim([-max_dim/2, max_dim/2])
    ax.set_zlim([0, max_dim])

    ax.set_xlabel('X', fontsize=10)
    ax.set_ylabel('Y', fontsize=10)
    ax.set_zlabel('Height', fontsize=10)
    ax.set_title('Cylinder', fontsize=12, weight='bold')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_sphere(radius, output_path, show_dimensions=True):
    """Create a 3D visualization of a sphere."""
    fig = plt.figure(figsize=(8, 6), dpi=150)
    ax = fig.add_subplot(111, projection='3d')

    # Create sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the sphere surface
    ax.plot_surface(x, y, z, alpha=0.7, color='#3b82f6', edgecolor='none')

    # Add dimension label if requested
    if show_dimensions:
        ax.text(0, 0, -radius-0.5, f'r = {radius} cm', fontsize=10, ha='center', color='#ef4444', weight='bold')

    # Set the aspect ratio and limits
    ax.set_xlim([-radius*1.2, radius*1.2])
    ax.set_ylim([-radius*1.2, radius*1.2])
    ax.set_zlim([-radius*1.2, radius*1.2])

    ax.set_xlabel('X', fontsize=10)
    ax.set_ylabel('Y', fontsize=10)
    ax.set_zlabel('Z', fontsize=10)
    ax.set_title('Sphere', fontsize=12, weight='bold')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_composite_shape_lshape(output_path):
    """Create a 2D L-shaped composite figure with dimensions."""
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)

    # Define L-shape vertices
    vertices = [(0, 0), (8, 0), (8, 3), (3, 3), (3, 6), (0, 6), (0, 0)]

    # Create polygon
    polygon = patches.Polygon(vertices, closed=True, fill=True,
                             facecolor='#93c5fd', edgecolor='#1f2937', linewidth=2)
    ax.add_patch(polygon)

    # Add dimension labels
    ax.annotate('', xy=(8.2, 0), xytext=(8.2, 3),
                arrowprops=dict(arrowstyle='<->', color='#ef4444', lw=2))
    ax.text(8.7, 1.5, '3 m', fontsize=11, color='#ef4444', weight='bold', va='center')

    ax.annotate('', xy=(0, -0.5), xytext=(8, -0.5),
                arrowprops=dict(arrowstyle='<->', color='#ef4444', lw=2))
    ax.text(4, -1, '8 m', fontsize=11, color='#ef4444', weight='bold', ha='center')

    ax.annotate('', xy=(-0.5, 0), xytext=(-0.5, 6),
                arrowprops=dict(arrowstyle='<->', color='#ef4444', lw=2))
    ax.text(-1.2, 3, '6 m', fontsize=11, color='#ef4444', weight='bold', ha='center')

    ax.annotate('', xy=(3, 6.5), xytext=(8, 6.5),
                arrowprops=dict(arrowstyle='<->', color='#10b981', lw=1.5, linestyle='dashed'))
    ax.text(5.5, 7, '5 m', fontsize=10, color='#10b981', weight='bold', ha='center')

    ax.annotate('', xy=(3.5, 3), xytext=(3.5, 6),
                arrowprops=dict(arrowstyle='<->', color='#10b981', lw=1.5, linestyle='dashed'))
    ax.text(4.2, 4.5, '3 m', fontsize=10, color='#10b981', weight='bold', va='center')

    ax.set_xlim([-2, 10])
    ax.set_ylim([-2, 8])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('L-Shaped Composite Figure', fontsize=14, weight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_circle_with_sector(radius, angle_degrees, output_path):
    """Create a circle with a shaded sector."""
    fig, ax = plt.subplots(figsize=(8, 8), dpi=150)

    # Draw the full circle
    circle = plt.Circle((0, 0), radius, fill=False, edgecolor='#1f2937', linewidth=2)
    ax.add_patch(circle)

    # Draw the sector
    theta = np.linspace(0, np.radians(angle_degrees), 100)
    x = np.concatenate([[0], radius * np.cos(theta), [0]])
    y = np.concatenate([[0], radius * np.sin(theta), [0]])
    ax.fill(x, y, color='#93c5fd', alpha=0.7, edgecolor='#3b82f6', linewidth=2)

    # Draw radii
    ax.plot([0, radius], [0, 0], 'k-', linewidth=2)
    ax.plot([0, radius * np.cos(np.radians(angle_degrees))],
            [0, radius * np.sin(np.radians(angle_degrees))], 'k-', linewidth=2)

    # Add labels
    ax.text(radius/2, -0.3, f'r = {radius} cm', fontsize=11, ha='center', color='#ef4444', weight='bold')
    ax.text(1, 1, f'{angle_degrees}°', fontsize=12, color='#1f2937', weight='bold')

    # Draw center point
    ax.plot(0, 0, 'ko', markersize=6)
    ax.text(0.2, -0.5, 'O', fontsize=12, weight='bold')

    ax.set_xlim([-radius*1.3, radius*1.3])
    ax.set_ylim([-radius*1.3, radius*1.3])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Circle with Sector', fontsize=14, weight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

def create_composite_rectangle_triangle(output_path):
    """Create a composite shape made of rectangle and triangle."""
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)

    # Rectangle
    rect = patches.Rectangle((0, 0), 12, 8, linewidth=2,
                             edgecolor='#1f2937', facecolor='#93c5fd', alpha=0.7)
    ax.add_patch(rect)

    # Triangle on top
    triangle = patches.Polygon([(0, 8), (12, 8), (6, 13)], closed=True,
                              linewidth=2, edgecolor='#1f2937',
                              facecolor='#fbbf24', alpha=0.7)
    ax.add_patch(triangle)

    # Add dimension labels
    ax.annotate('', xy=(0, -0.5), xytext=(12, -0.5),
                arrowprops=dict(arrowstyle='<->', color='#ef4444', lw=2))
    ax.text(6, -1.2, '12 cm', fontsize=11, color='#ef4444', weight='bold', ha='center')

    ax.annotate('', xy=(-0.5, 0), xytext=(-0.5, 8),
                arrowprops=dict(arrowstyle='<->', color='#ef4444', lw=2))
    ax.text(-1.5, 4, '8 cm', fontsize=11, color='#ef4444', weight='bold', ha='center')

    ax.annotate('', xy=(12.5, 8), xytext=(12.5, 13),
                arrowprops=dict(arrowstyle='<->', color='#10b981', lw=2))
    ax.text(13.5, 10.5, '5 cm', fontsize=11, color='#10b981', weight='bold', va='center')

    ax.set_xlim([-3, 15])
    ax.set_ylim([-2, 15])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Composite Shape: Rectangle + Triangle', fontsize=14, weight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f"Created: {output_path}")

if __name__ == "__main__":
    # Default output directory
    output_dir = "quizzes/geometry/area-and-volume-measurement"

    if len(sys.argv) > 1:
        output_dir = sys.argv[1]

    os.makedirs(output_dir, exist_ok=True)

    # Generate all diagrams
    print("Generating 3D shape visualizations...")

    create_rectangular_prism(6, 4, 5, f"{output_dir}/diagram-rectangular-prism-001.png")
    create_rectangular_prism(8, 3, 4, f"{output_dir}/diagram-rectangular-prism-002.png")
    create_cylinder(4, 10, f"{output_dir}/diagram-cylinder-001.png")
    create_cylinder(5, 8, f"{output_dir}/diagram-cylinder-002.png")
    create_sphere(6, f"{output_dir}/diagram-sphere-001.png")
    create_composite_shape_lshape(f"{output_dir}/diagram-composite-lshape.png")
    create_circle_with_sector(8, 90, f"{output_dir}/diagram-circle-sector.png")
    create_composite_rectangle_triangle(f"{output_dir}/diagram-composite-rect-tri.png")

    print(f"\nAll diagrams created in: {output_dir}")
