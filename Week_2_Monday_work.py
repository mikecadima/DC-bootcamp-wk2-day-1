#Week 2 Monday work
#1 small Madlib function-Write a function that accepts two arguments: a name and a subject.
# The function should return a String with the name and subject interpolated in.
'''
def mad_lib(name, subject):
    print(name + "'s favorite subject is " + subject)
mad_lib("mike", "lunch") 
'''
#2 small celcius to fahrenheit convert-F = (C * 9/5) + 32.
# Write a function that takes a temperature in Celsius, converts it Fahrenheit, and returns the value
'''
def Celsius_to_Fahrenheit(c) :  
    f = (9/5)*c + 32  
    return f
#3 small fahrenheit to Celsius conversion
def Fahrenheit_to_Celsius(f) :   
    c = (5/9)*(f - 32)    
    return c
if __name__ == "__main__" :    
    c = 36
    print(c, "degree celsius is equal to:",Celsius_to_Fahrenheit(c),"Fahrenheit")    
    f = 98
    print(f,"Fahrenheit is equal to:",Fahrenheit_to_Celsius(f),"degree celsius")
'''
#4 is_even function
'''
def is_even(x):
    if x % 2 == 0:
        print "True"
        return True
    else:
        print "False"
        return False
is_even(2)
'''
#5 is_odd function
'''
def is_odd(x):
    if x % 2 == 1:
        print "True"
        return True

    else:
        print("False")
        return False
is_odd(5)
'''
#6 only evens function
'''
def only_even(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(only_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
'''
#7 only odds function
'''
def only_odd(l):
    enum = []
    for n in l:
        if n % 2 == 1:
            enum.append(n)
    return enum
print(only_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))
'''
#1 medium find the smallest number
'''
num_list = [3,2,6,3,1,8,]
minimum = min(num_list)
print(minimum)
'''

#2 medium find the largest number
'''
num_list = [3,2,6,3,1,8,]
maximum = max(num_list)
print(maximum)
'''
#3 medium Find the shortest String
'''
test_list = ['the', 'board', 'longest'] 

res = min(len(ele) for ele in test_list) 
print("Length of minimum string is : " + str(res)) 
'''
#4 medium Find the longest string--fix function
'''
test_list = max(['the', 'board', 'longest']) 
print(test_list)
'''