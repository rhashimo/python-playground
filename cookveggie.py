# By Abdullah and Ryuichiro
import csv
import json

# read vegetable.csv and assign it to "vegetables"
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    vegetables = [dict(veggie) for veggie in vegetables]

# print vegetables
print(vegetables)

# turn vegetables into json file
with open('vegetables.json', 'w') as f:
	json.dump(vegetables, f, indent = 2)