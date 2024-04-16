num_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "ninteen": 19,
    "twenty": 20,
}
print("Keys:")
for key in num_dict.keys():
    print(key)
print("\nValues:")
for value in num_dict.values():
    print(value)
print("\nKey + 'two' and Value + 2:")
for key, value in num_dict.items():
    print(key + " + two :", value + 2)
