import csv
import re

def validate_and_transform_data(input_file, output_file):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    exceptions = []
    clean_data = []

    with open(input_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            emp_id = row['id']
            name = row['name']
            email = row['email']
            salary = row['salary']
            
            if not email or not re.match(email_pattern, email):
                exceptions.append({"id": emp_id, "name": name, "error": "Invalid or Missing Email"})
                continue
            
            try:
                if int(salary) <= 0:
                    exceptions.append({"id": emp_id, "name": name, "error": "Salary must be positive"})
                    continue
            except ValueError:
                exceptions.append({"id": emp_id, "name": name, "error": "Salary must be a number"})
                continue
                
            clean_data.append(row)

    with open(output_file, mode='w') as report:
        report.write("=== DATA EXCEPTION REPORT ===\n\n")
        if not exceptions:
            report.write("No errors found! Data is 100% clean.\n")
        else:
            for error in exceptions:
                report.write(f"Employee ID {error['id']} ({error['name']}) -> Error: {error['error']}\n")
                
    print(f"Process Complete! Clean records: {len(clean_data)}, Errors found: {len(exceptions)}")
    print(f"Exception report saved as: {output_file}")

validate_and_transform_data('employees.csv', 'exception_report.txt')
