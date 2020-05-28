import time
from random import randint
import functools
import getpass


def log(func):
    """Print info about the decorated function"""
    @functools.wraps(func)
    def wrapper_log(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        time_unit = 's'
        if run_time < 1:
            run_time /= 1000
            time_unit = 'ms'
        func_name = ' '.join(func.__name__.split('_')).title()
        with open("machine.log", "a") as f:
        	f.write("({})Running: {:20}[ exec-time = {:.3f} {:2} ]\n".
                	format(getpass.getuser(), func_name, run_time, time_unit))
        return value
    return wrapper_log


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
            self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
