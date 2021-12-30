def addNumbers(num1, num2):
    try:
        return (num1 + num2)
    
    except TypeError:
        return ('Invalid Number')
    except NameError:
       return('Invalid parameter')

    except Exception as e:
        return(e)



print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers(7,'a'))
print(addNumbers(99,1))
print('Execution Completed!')