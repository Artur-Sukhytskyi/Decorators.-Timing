import time

class Timing:
    def __init__(self, function_to_run):
        self.num_runs = input("введите число запусков: ")
        self.num_runs = int(self.num_runs)
        self.func_to_run = function_to_run

    def __call__(self, *args, **kwargs):
        avg = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        fn = self.func_to_run.__name__
        print(
            "Среднее время выполнения %s за %s запусков: %.5f секунд" % (
                fn,
                self.num_runs,
                avg
            )
        )
        return self.func_to_run(*args, **kwargs)
        
@Timing
###Некоторая функция
def f():
    for _ in range(1000000):
        pass
f()