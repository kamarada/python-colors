# Material Design color palette:
# https://material.io/design/color/the-color-system.html
# https://github.com/buschtoens/material-colors-json/blob/master/colors.json

# openSUSE color palette:
# https://en.opensuse.org/Help:Colors

from scipy.spatial import distance
import json

# Distance between two 3D points
# https://stackoverflow.com/a/21986532/1657502

def distance_rgb(color1, color2):
    return distance.euclidean(color1, color2)

# Converting hex color to RGB and vice-versa
# https://stackoverflow.com/a/214657/1657502

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# Getting values from JSON using Python
# https://linuxconfig.org/how-to-parse-data-from-json-into-python
# https://stackoverflow.com/a/12353363/1657502

def closest_color(reference_color_rgb, target_color_palette):
    closest_color_name = "Black"
    closest_color_hex = "#000000"
    closest_color_rgb = (0, 0, 0)
    closest_color_distance = distance_rgb(reference_color_rgb, closest_color_rgb)
    for palette_color_name, palette_color_hex in target_color_palette:
        palette_color_rgb = hex_to_rgb(palette_color_hex)
        palette_color_distance = distance_rgb(reference_color_rgb, palette_color_rgb)
        if palette_color_distance < closest_color_distance:
            closest_color_name = palette_color_name
            closest_color_hex = palette_color_hex
            closest_color_rgb = palette_color_rgb
            closest_color_distance = palette_color_distance
    return (closest_color_name, closest_color_hex, closest_color_rgb)

# Printing the content of a text file in Python
# https://stackoverflow.com/a/18256401/1657502

def compare_color_palettes(reference_color_palette_filename, target_color_palette_filename):
    with open('template-begin.html') as template:
        print(template.read())

    with open(reference_color_palette_filename) as reference_color_palette_file:
        reference_color_palette = json.load(reference_color_palette_file)
        with open(target_color_palette_filename) as target_color_palette_file:
            target_color_palette = json.load(target_color_palette_file)
            for reference_color_name, reference_color_hex in reference_color_palette.items():
                reference_color_rgb = hex_to_rgb(reference_color_hex)
                (target_color_name, target_color_hex, target_color_rgb) = closest_color(reference_color_rgb, target_color_palette.items())
                (reference_color_r, reference_color_g, reference_color_b) = reference_color_rgb
                (target_color_r, target_color_g, target_color_b) = target_color_rgb

                print('        <tr>')
                print('          <td><div class="square" style="background:', reference_color_hex ,';"/></td>')
                print('          <td>', reference_color_name, '</td>')
                print('          <td style="text-align: center">', reference_color_hex ,'</td>')
                print('          <td style="text-align: center">', reference_color_r ,'</td>')
                print('          <td style="text-align: center">', reference_color_g ,'</td>')
                print('          <td style="text-align: center">', reference_color_b ,'</td>')
                print('          <td><div class="square" style="background:', target_color_hex ,';"/></td>')
                print('          <td>', target_color_name, '</td>')
                print('          <td style="text-align: center">', target_color_hex ,'</td>')
                print('          <td style="text-align: center">', target_color_r ,'</td>')
                print('          <td style="text-align: center">', target_color_g ,'</td>')
                print('          <td style="text-align: center">', target_color_b ,'</td>')
                print('        </tr>')

    with open('template-end.html') as template:
        print(template.read())

compare_color_palettes('opensuse-colors.json', 'material-colors.json')

