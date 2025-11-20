def fun(*args):
    try:
        #10/0
        raise BlockingIOError('blablabla')
        'qwerty'*'werty'
        sum(args)/args[1]
    except ZeroDivisionError:
        return 0
    except Exception as err:
        print(err)
    else:
        print('else')
    finally:
        print('finally')

print(fun(0,5,10,15))

