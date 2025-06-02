import csv

file_name = "grades.csv"

with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(["Name", "Subject", "Grade"])
    
    # Writing some sample data
    writer.writerow(["Alice", "Math", 85])
    writer.writerow(["Bob", "Science", 78]) 
    writer.writerow(["Carol", "Math", 92])
    writer.writerow(["Dave", "History", 74])

subject_grades = {}

with open(file_name, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header
    
    for row in reader:
        subject = row[1]
        grade = int(row[2])
        
        if subject not in subject_grades:
            subject_grades[subject] = [grade]
        else:
            subject_grades[subject].append(grade)

for subject, grades in subject_grades.items():
    subject_grades[subject] = sum(grades) / len(grades)

with open("average_grades.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, average in subject_grades.items():
        writer.writerow([subject, average])
