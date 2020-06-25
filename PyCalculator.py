import re
import operator as op

# Assign the operators to their string counterparts
ops = {
  '+' : op.add,
  '-' : op.sub,
  '*' : op.mul,
  '/' : op.truediv
}

def start(equ):
  # Create global variable that will be used called and edited inside the calculate() function.
    global index
    global numbers
    global result
    result = 0

    # The var equation is stripped of it's spaces.
    # The var numbers gathers and add all numbers in the string to an array.
    # The var operators gathers and add all operators in the string to an array.
    equation = equ.replace(" ", "")
    numbers = re.findall(r'\d+', equation)
    operators = re.findall(r'\D', equation)
    
    index = 0
    num_len = len(numbers)

    
    while num_len != operators:
      try:
        # The var result will equal to the value the calculate() function returns.
        result = calculate(numbers, operators[index])
        index += 1
      except:
        break
    
    return result

# Calculates the equation the user enters.
def calculate(val, operator):
  try:
    num_1 = int(val[0])
    num_2 = int(val[1])

    # If the index is less than zero then this statement takes num_1 and num_2 and calulates it based on it's operator.
    # del number[value] delete the number or numbers from the array once its calculation took place this avoids repeatedly calculating the same value.
    if index < 1:
      new_val = ops[operator](num_1, num_2) 
      del numbers[0:2]


    else:
      new_val = ops[operator](result, num_1)
      del numbers[0]
    
    return new_val
  
  # If an error arise the except method will continue to calculate the final sum and return its value.
  except:
    new_val = ops[operator](result, num_1)
    del numbers[0]
    return new_val

def main():
    user_equ = str(input("[*] Enter your equation here: "))
    answer = start(user_equ)
    print(answer)
    
#   This prevents the script from automatically running when it is imported in to another python script or program.
if __name__ == "__main__":
    main()