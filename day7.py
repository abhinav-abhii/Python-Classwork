
grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append(item)
    print(f'"{item}" has been added to the grocery list.')

def remove_last_item():
    if grocery_list:
        removed = grocery_list.pop()
        print(f'"{removed}" has been removed from the grocery list.')
    else:
        print("The grocery list is already empty.")

display_item = lambda item: print(f"Item: {item}")

def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])


print("Initial List:", grocery_list)
add_item("butter")
add_item("rice")

remove_last_item()

print("\nGrocery List Items:")
for i in grocery_list:
    display_item(i)

total_chars = count_characters(grocery_list)
print(f"\nTotal number of characters in all item names: {total_chars}")
