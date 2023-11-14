import os
import csv
import logging

# Define the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define folder paths
csv_folder = os.path.join(current_directory, 'csvs')
logs_folder = os.path.join(current_directory, 'logs')

# Create the csvs and logs folders if they don't exist
os.makedirs(csv_folder, exist_ok=True)
os.makedirs(logs_folder, exist_ok=True)

# Configure the logging module
log_file_path = os.path.join(logs_folder, 'myLog.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the CSV file path
csv_file_path = os.path.join(csv_folder, 'myCsv.csv')

# Create myCsv.csv if it doesn't exist and write some data
if not os.path.isfile(csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Name', 'Age'])
        csv_writer.writerow(['Alice', 30])
        csv_writer.writerow(['Bob', 25])

# Read the CSV into a data structure
csv_data = []
with open(csv_file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        csv_data.append(row)

# Save a dummy log
logging.debug('This is a sample log entry.')

# Print the read CSV data
for row in csv_data:
    print(row)
