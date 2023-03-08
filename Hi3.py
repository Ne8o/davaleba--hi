'''
შექმენი პროგრამის ისეთი ვერსია რომელიც სხვა და სხვა სახელის მქონე ადამიანებს განსხვავებული მისალმებით პასუხობს.

'''

#for diferent users diferent answer
import random
#ask name
name = input("What is you name? ").title().strip()
# greetings list
greetings = ("nice to meet you!", "you have nice smile!", "have a nice day!")
a = random.choice(greetings)
#print function
print("Hello,", name, a)
#finish