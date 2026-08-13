first_number = int(input())
second_number = int(input())
if second_number == 0:
    print("second_number must not be zero")
else:
    result = first_number / second_number
    res = first_number // second_number
    print(result)
    print(res)