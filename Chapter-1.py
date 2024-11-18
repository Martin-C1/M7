#Martin C

import random
import resources

#Chapter1-P1

def say_my_name(string):
    value = [0,1]
    choice = random.choice(value)
    if choice == 0:
        print(f"hiya {string}")
    else:
        print(f"go away {string}")

say_my_name("jim") 

#Chapter1-P3
resources.lets_see(10)

def multiply_if():
   numbers = []
   for _ in range(10):
      num =random.randint(1,50)
      if resources.lets_see(num):
         num *= 5
      numbers.append(num)
   return numbers
print(multiply_if())

#P5
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    unique_list.sort()
    return unique_list
print(unique_elements ([1,3,8,7,6,2,3,5]))