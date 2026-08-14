number_count = int(input())

positive_count = 0
negative_count = 0
zero_count = 0
total = 0

for _ in range(number_count):
    number = int(input())
    total = total + number

    if number > 0:
        positive_count = positive_count + 1
    elif number < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1

print(f"Positive Count: {positive_count}")
print(f"Negative Count: {negative_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")