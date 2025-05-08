txt = input("Enter the full sentence: ").split()
start = input("starts with: ")
ends = input("Ends with: ")

if txt[0] == start and txt[-1] == ends:
    print("YES")
else:
    print("NO")