print("📚 Welcome To Results Portal 📚")

name = str(input("Enter your name"))
mark = int(input("Enter your mark"))
subject = str(input("Enter your subject"))

if mark > 100: 
    print("Error")
elif mark >= 75:
    print("Grade A Excellent its a pass congratulations🎉😌")
elif mark >= 60:
    print("Grade B Vey Good its pass congratulations🎉😌")
elif mark >= 50:
    print("Grade C Fairly its a pass well tried 😌 ")
elif mark >= 45:
    print("Grade D its a Fail😩")
elif mark >= 39:
    print("Grade F its a Fail 😔")
elif mark >= 0:
    print("Grade U Sorry you have failed😔")
     
else:
    print("❌Error mark is between 0 and 100 ❌")
print(f"{name}, your  mark is {mark} for {subject}")
