import time

def execution_time(timer_value):
    print(timer_value)
    def decorat(func):
        def wrapper(*args, **kwargs):
            started_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(end_time - started_time)
            return result
        return wrapper
    return decorat

@execution_time(timer_value= 10)
def sum1(n):
    time.sleep(2)
    print(sum(range(n+1)))

sum1(10)