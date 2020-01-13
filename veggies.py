# By Abdullah and Ryuichiro
import csv

# make a list of dictionaries
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# 1. Loops through each vegetable
with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)

    writer.writerow(['name', 'color', 'length']) # write headers
    for vegetable in vegetables: # write the name, color, and name's length of each vegetable
    	writer.writerow([vegetable["name"], vegetable["color"], len(vegetable["name"])])