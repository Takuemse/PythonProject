print(" 📚 Welcome to Student Score Tracker 📚")

students = {}

# Add multiple students
while True: 
    name = input("Enter student name: ")
    students[name] = []

    # Add multiple scores for this student
    while True:
        score = int(input(f"Enter score for {name}: "))
        students[name].append(score)

        more_scores = input("Add another score for this student? (yes/no): ")
        if more_scores.lower() == "no":
            break

    more_students = input("Add another student? (yes/no): ")
    if more_students.lower() == "no":
        break

while True:
    search = input("Search student (or type 'exit' to quit): ")

    if search.lower() == "exit":
        print("Exiting program...")
        break

    if search in students:
        print(f"{search} scores:", students[search])
        average = sum(students[search]) / len(students[search])
        print(f"{search} average:", average)
    else:
        print("Student not found")

    
    more_search = input("Search another student? (yes/no): ")
    if more_search.lower() == "no":
        print("Exiting program...")
        break

