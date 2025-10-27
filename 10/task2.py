def rec():
    num = int(input())
    if num != 0:
        rec()
    print(num)
