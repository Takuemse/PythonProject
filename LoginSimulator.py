print("\n🎉 Welcome  to Python 🐍 Software Development Bootcamp 2026 🎉")
   
   
User_data = {
    "username": "Takudzwa W Musemwa",
    "password": "takue@056" 
}

name = input("\n Enter your username: ")
password = input("Enter your password: ")

def login(name, password):
    if name == User_data["username"] and password == User_data["password"]:
        print(f" 🎉 Login successful Welcome,{name}  🎉 ")
    else:
        print(f"Invalid details.")
login(name, password)             