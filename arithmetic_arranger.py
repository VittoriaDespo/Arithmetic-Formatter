import re

def arithmetic_arranger(problems, solve = False):
  num = ''
  den = ''
  line = ''
  sum = ''
  
  if len(problems)>5:
    return "Error: Too many problems."
  for problem in problems:
    digit = (problem.split())
    first_operand = digit[0]
    operator = digit[1]
    second_operand = digit[2]
    if(re.search("[/]",problem) or re.search("[*]",problem)):
      return "Error: Operator must be '+' or '-'."
    elif(re.search("[^\s0-9+-]",problem)):
      return "Error: Numbers must only contain digits."
    elif ((len(first_operand)) > 4 or (len(second_operand) > 4)):
      return "Error: Numbers cannot be more than four digits."
    
    if (operator == '+'):
      result = int(first_operand) + int(second_operand)
    elif(operator == '-'):
      result = int(first_operand) - int(second_operand)

    length = max(len(first_operand),len(second_operand)) + 2
    numerator = (first_operand).rjust(length)
    denominator = operator + second_operand.rjust(length - 1)
    res_string = str(result)
    res = res_string.rjust(length)
    dashes = ''
    for n in range(length):
      dashes = dashes + '-'

    if problem != problems[-1]:
      num += numerator + '    '
      den += denominator + '    ' 
      line += dashes + '    '
      sum += res + '    '
    else:
      num += numerator
      den += denominator
      line += dashes
      sum += res

  if solve:
    arranged_problems = num + '\n' + den + '\n' + line + '\n' + sum
  else:
    arranged_problems = num + '\n' + den + '\n' + line
  
  return arranged_problems
    

    
    
  
   
    
      
   
    
    
    
    
    
  

  