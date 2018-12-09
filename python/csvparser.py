'''
Reading CSV files and Parsing
'''
import csv

# with open('names.csv', 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file)

# 	with open('newnames.csv', 'w') as new_file:
# 		csv_writer = csv.writer(new_file, delimiter='-')

# 		# Print out each line
# 		for line in csv_reader:
# 			csv_writer.writerow(line)

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	
	with open('new_names.csv', 'w') as new_file:
		fieldnames = ['id', 'first_name' ,'gender']
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
		csv_writer.writeheader()

		# Print out each line
		for line in csv_reader:
			csv_writer.writerow(line)