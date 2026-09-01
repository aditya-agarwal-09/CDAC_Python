scores = map(int, input("Enter the test scores(space-seperated): ").split())

revised = [min(score + 10, 100) if score < 50 else min(score + 5, 100) for score in scores]

print(f"Original: {scores}")
print(f"Revised: {revised}")