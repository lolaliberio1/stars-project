# Star Chart Project

This repository contains code for a Python project focused on creating a visual representation of star locations using data from a cleaned-up star catalog. 
This is an academic project (assignment), some base code was provided by the professor.

## Overview

Astronomers gather extensive data about stars, often cataloging their locations in various star catalogs. This project utilizes data from the `stars.txt` file, which contains information about the brightest stars in the northern hemisphere. Each star entry in the file includes fields such as the Henry Draper number, coordinates, magnitude, and name(s) of the star.

## Functions Implemented

### Translate Coordinates

- `coords_to_pixel(star_x, star_y, size)`: Converts star coordinates to pixel coordinates.

### Read Data

- `read_stars(fp)`: Reads star data from the provided file and returns dictionaries containing coordinates, magnitudes, and names.

### Plot Stars

- `plot_by_magnitude(size, coords, magnitudes)`: Plots stars based on their magnitudes using the provided function `draw_star(x, y, radius, color)`.

### Read Constellations

- `read_constellation_lines(fp)`: Reads constellation data from provided files and returns a dictionary.

### Draw Constellations

- `plot_constellation(coords, lines, names, color, size)`: Draws constellations based on provided data using the provided function `draw_line(x0, y0, x1, y1, color)`.

## Main Program

The main program utilizes the implemented functions to read star data and constellation files, and then draws the associated stars and constellations. 
Some code was already provided.

## Instructions

1. Run star_chart.py file.

## Credits

- Code snippets and specifications were provided as part of the assignment.

