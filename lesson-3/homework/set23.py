import random
size = int(input())
start = int(input())
end = int(input())
result = set(random.sample(range(start, end+1), size))
print(result)