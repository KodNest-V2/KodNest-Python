limit = int(input())
target = int(input())

count = 0
total = 0
found = False

for i in range(1, limit + 1):
    if i % 3 == 0:
        count += 1
        total += i
        if i == target:
            found = True

print(f"Count: {count}")
print(f"Sum: {total}")

if found:
    print("Target Found: Yes")
else:
    print("Target Found: No")