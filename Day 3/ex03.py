train = ["coal", "gold", "iron", "gold", "iron", "copper"]

res = input("Enter a resource type: ")

print(f"Number of {res} wagons: {train.count(res)}")

if(res in train):
    print(f"The first {res} wagon is at: {train.index(res)}")
else:
    print("resource not found!")


