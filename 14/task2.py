final_price = 0
with open('prices.txt', encoding = 'utf-8') as file:
    for line in file:
        name, vol, price = line.split()
        final_price += int(vol)*int(price)
print(final_price)
        
