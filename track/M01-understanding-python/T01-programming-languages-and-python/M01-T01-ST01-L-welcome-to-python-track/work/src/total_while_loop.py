n = int(input())

counter = 1
total = 0

while counter <= n:
    total = total + counter
    counter = counter + 1

print(f"Total: {total}")