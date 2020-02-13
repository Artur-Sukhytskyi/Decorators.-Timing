import time

number_of_runs = input("введите число запусков: ")
number_of_runs = int(number_of_runs)

def time_this(NUM_RUNS = number_of_runs):
    def decorator(func_to_run):
        def func(*args, **kwargs):
            avg = 0
            for _ in range(NUM_RUNS):
                t0 = time.time()
                func_to_run(*args, **kwargs)
                t1 = time.time()
                avg += (t1 - t0)
            avg /= NUM_RUNS
            fn = func_to_run.__name__
            print("Среднее время выполнения %s за %s запусков: %.5f секунд" % (fn, NUM_RUNS, avg))
        return func

    return decorator

@time_this()
###Некоторая функция
def f(number_of_runs):
    for j in range(1000000):
        pass

f(number_of_runs)