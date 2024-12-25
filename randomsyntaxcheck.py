# data=[("daddy",51),("akhi",24),("Mani",46),("Sai",26)]
# mid=len(data)//2


# def adding(a,b):
#     def add(c):
#         d=a*b+c
#         return d
#     return add
# closure=adding(2,3)
# #print(closure(5))


# def my_decorator(methodname):
#     def my_logic(a,b):
#         if a<b:
#             print("Before Swaping:",a,b)
#             a,b=b,a
#             print("After Swaping:",a,b)
#         return methodname(a,b)
#     return my_logic

# @my_decorator
# def divison(a,b):
#     c=a/b
#     return c
# #print(divison(2,6))



# from collections import defaultdict

# # Create a defaultdict with a default value of 0
# dd = defaultdict(int)

# # Add items to the defaultdict
# dd['apple'] += 1
# dd['banana'] += 2

#print(dd)  # Output: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})

# Accessing a missing key will not raise an error
# print(dd['akhi']) 
# print(dd['sai']) # Output: 0 (default value)


# def palindrome_check(num):
#     target=num
#     sum=0
#     while num>0:
#         rem=num%10 
#         sum=sum*10+rem
#         print(sum)
#         num=num//10
#     if(target==sum):
#         return "It's a palindrome"
#     else:
#         return "Not palindrome"
# if __name__=="__main__":
#     num=int(input("enter a number to check palindrome or not"))
#     print(palindrome_check(num))

# list1=[1,4,6,7]
# iter_=iter(list1)
# def my_generators():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# gen=my_generators()
# print(next(gen))
# print(next(iter_))
# print(next(gen))
# print(next(iter_))
# print(next(gen))
# print(next(iter_))
# print(next(gen))
# print(next(iter_))
# print(next(iter_))

# def palidrome_check(given_input):
#     special_characters = " !@#$:%^&*()',.?"
#     reverse=""
#     cleaned_input= "".join(char.lower() for char in given_input if char not in special_characters)
#     print(cleaned_input)
#     for char in cleaned_input:
#         reverse=char+reverse
#     print(reverse)
#     if(cleaned_input==reverse):
#         return "palindrome"
#     else:
#         return "not palindrome"

# if __name__=="__main__":
#     input_= "ma $la, :y a ,l'am@@@$#%"
#     print(palidrome_check(input_))



# def my_decorator(method):
#     def logic(a,b):
#         if a<b:
#             a,b=b,a
#         return method(a,b)
#     return logic

# @my_decorator
# def substraction(a,b):
#     return a-b

# @my_decorator
# def division(a,b):
#     return a//b

# if __name__=="__main__":
#     print(substraction(2,6))
#     print(division(2,6))


# import threading
# import time

# # A simple function to run in a thread
# def print_numbers():
#     for i in range(5):
#         time.sleep(1)
#         print(i)

# # Create threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_numbers)

# # Start threads
# thread1.start()
# thread2.start()

# # Wait for threads to complete
# thread1.join()
# thread2.join()

# print("Both threads have finished.")


# def fibonacci(num):
#     fibonacci_series=[]
#     num1=0
#     num2=1
#     for i in range(num):
#         num3=num1+num2
#         fibonacci_series.append(num3)
#         num1=num2
#         num2=num3
#     return f"fibonacci Series{fibonacci_series}"

# if __name__=="__main__":
#     print(fibonacci(10))



from pandas import DataFrame
data= [8, 8, 3, 3, 1, 4, 5, 5, 9, 6]
df=DataFrame(data, columns=['nums'])

max_group=df.groupby('nums').size()
max_count=DataFrame(max_group)
print(max_count)
sort_desc=max_count.sort_values(by='nums',ascending=False)
filtered=sort_desc.loc[(sort_desc['count'] == 1)]
print("the highest non repeated number",sort_desc.columns)

query_check=max_count.query('count<3')
print(query_check)

