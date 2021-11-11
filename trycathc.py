try :
    age = int(input('age: '))
    income = 2000
    risk = income/age
    print(risk)
except ZeroDivisionError : 
    print('number cannot be zero')
except ValueError: 
    print('Invalid value')