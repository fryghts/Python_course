db = dict()
while text:=input():
    customer, item, volume = text.split()
    volume = int(volume)
    customer_dict = db.setdefault(customer, dict())
    customer_dict.setdefault(item, 0)
    customer_dict[item] += volume

for customer, customer_dict in db.items():
    for item, vol in customer_dict.items():
        print(f'{customer} {item} {vol}')

        
