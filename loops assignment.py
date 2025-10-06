#menu prices1
menu = ["Taco", "Burrito", "Nachos", "Soft Drink"]
prices = [2.50, 4.25, 3.75, 1.95]

def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")

print("Welcome to Taco Palace! Please view the menu below and make a selection.")

order = []
total = 0.0
running = True

while running:
    print_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("You selected a Taco.")
        order.append("Taco")
        total += 2.50
    elif choice == "2":
        print("You selected a Burrito.")
        order.append("Burrito")
        total += 4.25
    elif choice == "3":
        print("You selected Nachos.")
        order.append("Nachos")
        total += 3.75
    elif choice == "4":
        print("You selected a Soft Drink.")
        order.append("Soft Drink")
        total += 1.95
    elif choice == "5":
        running = False
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

if len(order) > 0:
    print("\nYou ordered:")
    for item in order:
        print(f"- {item}")
    print(f"Your total is ${total:.2f}")
else:
    print("\nYou did not order anything.")