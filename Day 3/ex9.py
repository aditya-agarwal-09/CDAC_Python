"""
Scenario: A group of 
N
 soldiers (numbered 1 to 
N
) stand in a circle. Starting from the first soldier, every 
K
-th soldier is eliminated from the circle. The count continues with the next remaining soldier, moving clockwise. This process repeats until only one soldier remains. Write a program that prompts the user to enter 
N
 (number of soldiers) and 
K
 (elimination interval). Simulate the game using a list and print the order of eliminations and the final survivor.

Sample Input: N = 5, K = 2
Sample Output:
Soldier circle initialized: [1, 2, 3, 4, 5]
Eliminated soldier: 2 (Remaining: [1, 3, 4, 5])
Eliminated soldier: 4 (Remaining: [1, 3, 5])
Eliminated soldier: 1 (Remaining: [3, 5])
Eliminated soldier: 5 (Remaining: [3])
The sole survivor is: 3

"""

n = int(input("Enter N (number of soldiers): "))
k = int(input("Enter K (elimination interval): "))

soldiers = list(range(1, n + 1))
print(f"Soldier circle initialized: {soldiers}")

index = 0

while len(soldiers) > 1:
    index = (index + k - 1) % len(soldiers)
    eliminated = soldiers.pop(index)
    print(f"Eliminated soldier: {eliminated} (Remaining: {soldiers})")

print(f"The sole survivor is: {soldiers[0]}")