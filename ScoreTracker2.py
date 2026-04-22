students = {}

def add_student():
    while True:
        name = input("Student name: ")
        subject = input("Subject: ")
        
        scores = input("Enter Scores (comma-separated): ").split(',')
        scores = [int(s) for s in scores]

        average = sum(scores) / len(scores)

        students[name] = {
            "subject": subject,
            "scores": scores,
            "average": round(average, 2)
        }

        print(f" Added {name}")

        more = input("Add another student? (yes/no): ")
        if more.lower() != "yes":
            break


def find_student():
    while True:
        name = input("\nEnter student name to search: ")

        if name in students:
            print(f"\n📚 {name}'s Details:")
            print("Subject:", students[name]["subject"])
            print("Scores:", students[name]["scores"])
            print("Average:", students[name]["average"])
        else:
            print(f"{name} not found!")

        search_again = input("Search again? (yes/no): ")
        if search_again.lower() != "yes":
            break


# Run program
add_student()
find_student()