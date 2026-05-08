import csv 

data1 = "NAME,AGE,MARKS\n"
data2 = """
AMIT,20,85
RIYA,21,90
PIYUSH,20,93
"""

with open("Data.csv", "w") as file:
    file.write(data1)
    file.write(data2)

empty_list = []

    
with open("Data.csv", newline="") as file:
    content = csv.DictReader(file)
    for row in content:
        empty_list.append(row)
    
print(empty_list)

total = 0

for child in empty_list:
    total += int(child['MARKS'])
    
print(total)

average = total / int(len(child['MARKS']))

print(average)