'''
Write a decorator that will calculate the execution time of a function.

    Example:

    ```python
    @calculate_execution_time
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)
    > 3
    > Execution time: 0.0005 seconds
    ```
'''
import time


def calculate_execution_time(func):

  def wraper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    dt_time = end_time - start_time
    print('Execute time',dt_time)
    return  result

  return wraper


@calculate_execution_time
def add(a: int, b: int) -> int:
  return a + b


@calculate_execution_time
def print_hello():
  print('Hello, world')


print('Result of summing', add(100, 150))
print_hello()

# calculate_execution_time(add)  (100, 150)

