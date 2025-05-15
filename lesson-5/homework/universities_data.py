universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    students = [univ[1] for univ in data]
    tuitions = [univ[2] for univ in data]
    return students, tuitions

def mean(values):
    return sum(values) / len(values)

def median(values):
    sorted_values = sorted(values)
    length = len(sorted_values)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]

students, tuitions = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuitions)

student_mean = mean(students)
student_median = median(students)

tuition_mean = mean(tuitions)
tuition_median = median(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print("")
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print("")
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("******************************")
