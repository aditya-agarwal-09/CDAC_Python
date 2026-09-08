vip_list = ["Esha", "Vinod", "Rajan", "Kishor", "Rahul"]

print(f"Current VIP list: {vip_list}")

while True:
    guest_name = input("Enter the guest name: ")

    if(guest_name == "exit"):
        break

    if(guest_name in vip_list):
        vip_list.remove(guest_name)
        vip_list.insert(0, guest_name)
        print(f"{guest_name} moved to the front!")
        print(f"Updated VIP list: {vip_list}")

    else:
        print("Access denied. Not on the VIP list")
        print(f"Current VIP list: {vip_list}")



