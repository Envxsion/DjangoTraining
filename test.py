import random
import operator

ops = {
           "+": operator.add,
           "-": operator.sub, 
           "*": operator.mul,
           "/": operator.truediv
           }
def randquestion(ops): 
    op = random.choice(list(ops))
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    question = (f'{num1} {op} {num2}')
    return question, ops[op](num1, num2)

prob = randquestion(ops)
print(f"Answer to the question: {prob[0]} is  {prob[1]}") 

