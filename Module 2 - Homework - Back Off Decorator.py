"""
Tri Phan
13 March 2023
CS 399 - Intermediate Python Programming
Module 2
Back Off Decorator
"""
from random import randint
from time import sleep, asctime

def backoff(initial_delay = 0.1, back_off_factor = 1.5, max_delay=2.5):

    def decorator(function):
        
        def inner(*args, **kwargs):
            delay = initial_delay
            success = False
            while not success:
                func = function(*args, **kwargs)
                if func == None or func == False:
                    delay *= back_off_factor
                    if delay > max_delay:
                        delay = max_delay  
                elif func == True:
                    success = True
                else:
                    raise ValueError(f"{function.__name__} has something this code doesnt know how to handle")
                print(f"{asctime()}: will be calling {function.__name__} after {delay:.4f} sec delay")
                sleep(delay)
                if not success:
                    print(func)
            return func
        return inner
    return decorator
           
@backoff()
def call_shaky_service():
    return 6 == randint(1, 6)

while True:
    print(call_shaky_service())
    
"""
For the future, i would write out that the process failed or succeeded and if it would re-try based on that. I would also program a loop to try to access the function (in this caase call_shaky_service) a certain number of times, so the code would just retry until the number of successes is enough
"""