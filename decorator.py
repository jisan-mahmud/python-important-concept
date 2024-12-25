import time

def execution_time():
    def decorat(func):
        def wrapper(*args, **kwargs):
            started_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f'Total execution time: {end_time - started_time}')
            return result
        return wrapper
    return decorat

@execution_time()
def sum1(n):
    time.sleep(2)
    print(sum(range(n+1)))

if __name__ == '__main__':
    sum1(10)