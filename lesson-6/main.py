def simple_generator():
    print("first running")
    yield 1
    print("second running")
    yield 2
    print("third running")
    yield 3

GEN = simple_generator()    
print(next(GEN))    
print(next(GEN))    
print(next(GEN))
# print(next(GEN))  # Uncommenting this line will raise a StopIteration exception