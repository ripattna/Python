def addNumbers(num1, num2):
    try:
        print(num1 + num2)
    except TypeError:
        print('Invalid Number')
    except Exception as e:
        print(e)
    else:
        print('Successfull...')
    finally:
        print('THE END... ')


addNumbers(5,'a')