import csv

# построчно списком
# with open('file.csv') as csvfile:
#     country_reader = csv.reader(csvfile, delimiter=';')
#     for row in country_reader:
#         print(int(row[2]+2))

# построчно словарём
with open('test.csv') as csvfile:
    country_reader = csv.DictReader(csvfile, delimiter=',')
    for row in country_reader:
         print(row)

