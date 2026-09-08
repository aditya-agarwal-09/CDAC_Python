bag = input("Enter the contents of the bag: ").split()

new_item = input("Enter the new item: ")

bag.append(new_item)
ejected_item = bag.pop(0)

print("Portal transition activated!")
print(f"Ejected oldest item: {ejected_item}")
print(f"Updated contents of the bag: {bag}")