import csv
import json

# Reads superheroes.json (in this folder)
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

# Creates an empty array called powers
powers = []

# Loop thorough the members of the squad, and 
# append the powers of each to the powers array.
for member in superheroes["members"]:
	powers.append(member["powers"])

# Prints those powers to the terminal
print(powers)