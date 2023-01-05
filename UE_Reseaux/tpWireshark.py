import csv
with open('randomDog.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    total = 0
    for row in spamreader:
        total += int(row['Length'])
        print(row['Length'])

print(spamreader)
print(total)