lst = []
for i in range(0, 101, 2):
    lst.append(i)
for i, num in enumerate(lst, start=1):
    print(f"{i}:{num}")
