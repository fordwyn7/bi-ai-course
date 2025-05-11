a = set(map(int, input().split()))
element = int(input())
if element in a:
    a.remove(element)
print(a)