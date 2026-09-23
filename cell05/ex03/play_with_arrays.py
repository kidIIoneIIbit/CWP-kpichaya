original = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()

for number in original:
    if number > 5:
        new_array.add(number + 2)

print(original)
print(new_array)