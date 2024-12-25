def iterate(n):
    for i in range(n):
        yield i
    
generator = iterate(100)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))