shopping_list = []

while True:
    print("\nShopping List Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")
    elif choice == '2':
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")
    elif choice == '3':
        if not shopping_list:  # Check if the list is empty
            print("Your shopping list is empty.")
        else:
            print("\nCurrent Shopping List:")
            for i, item in enumerate(shopping_list):  # Use enumerate for cleaner output
                print(f"{i+1}. {item}") # Numbering the items
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
