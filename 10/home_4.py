
#conditions_dict = {
#    "условие: число чётное": lambda x: x % 2 == 0,
#    "условие: число нечётное": lambda x: x % 2 != 0,
#    "условие: число положительное": lambda x: x > 0,
#    "условие: число отрицательное": lambda x: x < 0,
#    "условие: число целое": lambda x: int(x) == x,
#    "условие: число дробное": lambda x: int(x) != x
#}

def filter_list(numbers, condition):
  #func = conditions_dict[condition]
  return [elem for elem in numbers if condition(elem)]
