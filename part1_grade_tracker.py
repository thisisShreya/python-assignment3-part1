raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

for student in raw_students:
    name = student["name"].strip().title()
    roll = int(student["roll"])
    marks = list(map(int, student["marks_str"].split(",")))
    
    # Name validation 
    valid = True
    for word in name.split():  
        if not word.isalpha():   
            valid = False
            
    # Profile card
    print("="*32)
    print(f"Student  : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("="*32)
    
    if valid:    
        print("Valid name")
    else:    
        print("Invalid name")
        
    print()

#------ TASK-2 ------

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print("\n--- Marks Analysis ---\n")

#loop through subject & marks
for sub, mark in zip(subjects, marks):

    #assigning grade based on marks
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{sub} : {mark} -> {grade}")

#calculate total & average
total = sum(marks)
average = round(total / len(marks), 2)
print("\nTotal Marks:",total)
print("Average Marks:",average)

#highest & lowest scoring subject
max_mark = max(marks)
min_mark = min(marks)
max_sub = subjects[marks.index(max_mark)]
min_sub = subjects[marks.index(min_mark)]

print("\nHighest Scoring Subject: ", max_sub, "-", max_mark)
print("Lowest Scoring Subject: ", min_sub, "-", min_mark)

#---- Task-3 ----
count=0
while True:
    sub = input("Enter subject name (or 'done' to stop): ")
    if sub.lower() == "done":
        break

    mark_input = input("Enter marks: ")
    
    #numeric validation
    if not mark_input.isdigit():
        print("Invalid input. Enter numeric value")
        continue

    mark = int(mark_input)

    #range validation
    if mark<0 or mark>100:
        print("Marks must be between 0 and 100")
        continue
    #add valid data
    subjects.append(sub)
    marks.append(mark)

    count += 1

print("\nNew subjects added:", count)
new_avg = round(sum(marks) / len(marks), 2)
print("Updated Average:", new_avg)

class_data = [
    {"name": "Ayesha Sharma", "marks": [88, 72, 95, 60, 78]},
    {"name": "Rohit Verma",   "marks": [55, 68, 49, 72, 61]},
    {"name": "Priya Nair",    "marks": [91, 85, 88, 94, 79]},
    {"name": "Karan Mehta",   "marks": [40, 55, 38, 62, 50]},
    {"name": "Sneha Pillai",  "marks": [75, 80, 70, 68, 85]},
]

print("\n--- Class Summary ---\n")
print(f"{'Name':<20} {'Average':<10} {'Status':<10}")

for student in class_data:
    name = student["name"]
    marks = student["marks"]
    total = sum(marks)
    avg = round(total / len(marks), 2)
    #status 
    if avg >= 50:
        result = "Pass"
    else:
        result = "Fail"
    print(f"{name:<20}\t{avg:<10}\t{result:<10}")


#---- Task-4 ----
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

#strip
clean_essay = essay.strip()
print("\n1. Clean Essay:", clean_essay)
#convert
print("\n2. Title Case:", clean_essay.title())
#count
print("\n3. Count of 'python':", clean_essay.count("python"))
#replace
replaced_essay = clean_essay.replace("python", "Python 🐍")
print("\n4. Replaced essay:", replaced_essay)
#split
print("\n5. Sentences list:", clean_essay.split(". "))
#numbered sentences
print("\n6. Numbered Sentences:")
sentences = clean_essay.split(". ")
i=1
for s in sentences:
    if not s.endswith("."):
        s += "."
    print(str(i) + ". " + s)
    i += 1