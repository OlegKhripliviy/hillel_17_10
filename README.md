```bash
   _     _  _  _  _         _                                            
  | |   | |(_)| || |       | |                                           
  | |__ | | _ | || |  ____ | |    ____  ___   _   _   ____  ____  ____   
  |  __)| || || || | / _  )| |   / ___)/ _ \ | | | | / ___)/ ___)/ _  )  
  | |   | || || || |( (/ / | |  ( (___| |_| || |_| || |   ( (___( (/ /   
  |_|   |_||_||_||_| \____)|_|   \____)\___/  \____||_|    \____)\____)  
                                                                         
              __   ______    ______    ______  ______   ______           
             /  | / __   |  (_____ \  / __   |(_____ \ (_____ \          
            /_/ || | //| |    ____) )| | //| |  ____) )  ____) )         
              | || |// | |   /_____/ | |// | | /_____/  /_____/          
              | ||  /__| |_  _______ |  /__| | _______  _______          
              |_| \_____/(_)(_______) \_____/ (_______)(_______)         
     
```   

## About

### Classwork and homework

## Quick start

### Install deps

```bash
# Install pipenv
pip install pipenv

# Activate virtual env
pipenv shell

#Install deps
pipenv sync
```

#### Additional
```bash
# Regenerate Pipfile.lock file
pipenv lock

# pipenv lock & pipenv sync
pipenv update
```

## Homeworks

### Homework 2 (GitHub)

<details><summary>Homework assignment</summary>
<p>

* Create a profile on GitHub
* Create a repository hillel_10_2022 that is public
* Create a folder for lesson_02

</p>
</details>

### Homework 3 (Setup code quality tools)

<details><summary>Homework assignment</summary>
<p>

* Setup GitHub Actions
* Setup black, isort, flake8 in GitHub Actions
* Setup pre-commit hooks

</p>
</details>

### Homework 4 (Generators)

<details><summary>Homework assignment</summary>
<p>

* Complete the examples on a classwork

* Download rockyou file

* Generate a new file that has only lines that include requested parameter by user

* This file should not be in the GitHub repo

* README.md is updated in order to give the information about where to download this file

* After creating as a customer I want to see

  * total lines of each file
  * total size of each file (use Pympler library to get the total size)
</p>
</details>


* __Download [rockyou file](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwisgfT2-ZT4AhVJxIsKHR9wB4IQFnoECAgQAQ&url=https%3A%2F%2Fgithub.com%2Fbrannondorsey%2Fnaive-hashcat%2Freleases%2Fdownload%2Fdata%2Frockyou.txt&usg=AOvVaw3snAERl1mU6Ccr4WFEazBd) for this homework__

### Homework 5 (Context manager and frange)

<details><summary>Homework assignment</summary>
<p>

* Create a Context Manager! In order to print colored text in the terminal using print, you can use the so-called. 
  escape sequences: https://www.skillsugar.com/how-to-print-coloured-text-in-python . The desired color is "turned on" 
  by printing a specific string and turned off as well.
  
  Example:
```ruby
  print('\033[93m', end='')
  print('aaa')
  print('bbb')
  print('\033[0m', end='')
  print('ccc')
```
  Create a colorizer context manager that will print the specified color in an arbitrary block of code. After leaving 
  the block, the text is printed in the usual way:

```ruby
  with colorizer('red'):
      print('printed in red')
  print('printed in default color')
```

* There is no frange class in Python that works with floats. Create your own version of such a class that would support 
  the standard range interface, but work with float at the same time.
```ruby
  class frange:
      pass
  
  for i in frange(1, 100, 3.5):
      print(i)
```
  The code above should output:
```ruby
  1
  4.5
  8.0
  ...
```
  The type of all class parameters is float. The number of supported parameters is the same as in range: 
  from 1 (only the right border of the range) to 3 (left border, right border, step).

  Before PR, make sure you pass the following tests:
```ruby
  assert(list(frange(5)) == [0, 1, 2, 3, 4])
  assert(list(frange(2, 5)) == [2, 3, 4])
  assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
  assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
  assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
  assert(list(frange(1, 5)) == [1, 2, 3, 4])
  assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
  assert(list(frange(0, 0)) == [])
  assert(list(frange(100, 0)) == [])
  
  print('SUCCESS!')
```

</p>
</details>

### Homework 6 (Decorators)

<details><summary>Homework assignment</summary>
<p>

* Realize reverse string decorator

```ruby
# MODIFY THIS DECORATOR
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year() -> int:
    return 1957

# TEST OUPUT
print(
    get_university_name(),
    get_university_founding_year(),
    sep="\n"
)
```

* Replace dict value decorator
```ruby
# MODIFY THIS DECORATOR
def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }

# TEST OUPUT
print(
    get_user(name="Alice", age=30),
    get_user(name="Bob", age=25),
    sep="\n"
)
```
</p>
</details>

### Homework 8 (Abstract classes)

<details><summary>Homework assignment</summary>
<p>

* Comlete this piece of a code

```ruby

from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    """Change me"""


class Circle(Shape):
    """Change me"""


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    options: list[Shape] = [change_me]
    return choice(options)


def main():
    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()

```

</p>
</details>

### Homework 9 (Dunder methods)

<details><summary>Homework assignment</summary>
<p>

* Create a class Price

```ruby

class Price:
        def __init__(self, amount: int, currency: str) -> None:
            self.amount: int = amount
            self.currency: str = currency

```

* Acceptance criterias:

  * If I create 2 instances of a Price class I want to do operations between them:
    * add prices with same currency 
    * do a subtricttion of prices with same currency
  
* Additional: operations between prices with different currencies:

  * If price instances currencies are different I want to do a double convertion 
    * USD is a middle currency 
    * If right price is USD the regular convertation (not double) is happening 
    * If prices currencies is the same convertion is not happening 
    * Result currency after the operation is a currency of the price that is on the left or USD (for your decision)
  * Use @dataclass decorator instead of a regular class
</p>
</details>

### Homework 11 (Threads)

<details><summary>Homework assignment</summary>
<p>

* You have a very unoptimized method to find prime numbers (below).
* Let's imagine that user passes a huge numbers range - [start=100, end=10_000]
* You have to make this huge range be run in 5 threads P.S. Think about how would you split this huge range

```ruby

def get_primes(start: int, end: int) -> list[int]:
    results = []
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            results.append(number)
    return results


data = get_primes(10, 20)
print(data)

>>> [11, 13, 17, 19]

```


</p>
</details>