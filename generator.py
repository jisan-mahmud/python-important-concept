from decorator import execution_time
# def iterate(n):
#     for i in range(n):
#         yield i
    
# generator = iterate(100)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

N = 10000000

## Without use generator

@execution_time()
def iterator(n):
    return [i for i in range(n)]

# print(sum(iterator(N)))

## Using generator
def generator(n):
    for i in range(n):
        yield i

@execution_time()
def times():
    return sum(generator(N))

# print(times())

##Generator using expresion
sequence = (i for i in range(N))

# print(next(sequence))
# print(next(sequence))

##use close method

sequence = (i for i in range(N))

print(next(sequence))
# sequence.close
# print(next(sequence))