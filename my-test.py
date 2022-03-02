from prefect import task, Task, Flow
import random

@task
def random_number():
    return random.randint(0, 100)

@task
def plus_one(x):
    return x + 1

with Flow('My Functional Flow') as flow:
    r = random_number()
    y = plus_one(x=r)