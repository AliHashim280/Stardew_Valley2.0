import random

# Set the dimensions of the tilemap to cover the 800x600 screen
num_columns = 23
num_rows = 25

# Maximum tile value
max_tile_value = 49

# Generate the tilemap array with random values from 0 to 15
tilemap = [
    [random.randint(0, max_tile_value) for _ in range(num_columns)]
    for _ in range(num_rows)
]

import json

# Assuming the tilemap is already generated
tilemap = [[random.randint(0, 15) for _ in range(25)] for _ in range(19)]

# Open the file in write mode
with open("tile_map.json", "w") as f:
    # Write the tilemap to the JSON file
    json.dump({"tilemap": tilemap}, f)

print("Tilemap saved to tile_map.json")
