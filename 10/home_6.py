def analyze_data(*numbers):
    numbers = list(numbers)
    if not numbers:
        return 0.0, 0.0
    numbers.sort()
    Sred = sum(numbers)/len(numbers)
    if len(numbers)%2 == 0:
        Med = (numbers[int(len(numbers)/2)]+
               numbers[int(-1+len(numbers)/2)])/2
    else:
        Med = numbers[int((len(numbers)-1)/2)]
    return Sred, Med
