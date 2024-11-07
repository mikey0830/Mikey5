def read_grades(file_name):
   
    students = []
    try:
        with open(file_name, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                name = data[0]
                grades = list(map(int, data[1:]))
                students.append((name, grades))
    except FileNotFoundError:
        print(f"Error")
    return students

def calculate_averages(students):
    
    student_averages = []
    total_sum = 0
    total_count = 0
    for student in students:
        name, grades = student
        avg = sum(grades) / len(grades)
        student_averages.append((name, avg))
        total_sum += sum(grades)
        total_count += len(grades)
    
    class_average = total_sum / total_count
    return student_averages, class_average

def find_highest_lowest(students):
   
    highest_score = -float('inf')
    lowest_score = float('inf')
    highest_student = ""
    lowest_student = ""
    
    for student in students:
        name, grades = student
        highest = max(grades)
        lowest = min(grades)
        
        if highest > highest_score:
            highest_score = highest
            highest_student = name
        
        if lowest < lowest_score:
            lowest_score = lowest
            lowest_student = name
    
    return highest_student, highest_score, lowest_student, lowest_score

def write_results(file_name, student_averages, class_average, highest_student, highest_score, lowest_student, lowest_score):
   
    with open(file_name, 'w') as f:
        f.write("Grade Analyser Results\n")
        f.write("========================\n")
        f.write(f"Class Average: {class_average:.2f}\n\n")
        
        f.write("Student Averages:\n")
        for name, avg in student_averages:
            f.write(f"{name}: {avg:.2f}\n")
        
        f.write("\nHighest Score:\n")
        f.write(f"{highest_student}: {highest_score}\n")
        
        f.write("\nLowest Score:\n")
        f.write(f"{lowest_student}: {lowest_score}\n")
        
    print(f"Results have been written to {file_name}")

def main():
   
    input_file = input("Please enter the name of the grades file (e.g., grades.txt): ")
    
   
    students = read_grades(input_file)
    
   
    if not students:
        print("No student data found, exiting.")
        return
    
   
    student_averages, class_average = calculate_averages(students)
    
    
    highest_student, highest_score, lowest_student, lowest_score = find_highest_lowest(students)
    
    
    output_file = input_file.replace('.txt', '_results.txt')
    
   
    write_results(output_file, student_averages, class_average, highest_student, highest_score, lowest_student, lowest_score)

if __name__ == "__main__":
    main()