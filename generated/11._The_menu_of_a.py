# Write an algorithm that reads the code of the item ordered,
# the quantity and calculates the amount to be paid for that snack Consider that for each run, only one item will be calculated

# Description Code Price
# Cachorro Quente 100 1.20
# Bauru Simples 101 1.30
# Bauru com Ovo 102 1.50
# Hambúrguer 103 1.20
# Cheeseburguer 104 1.30
# Refrigerante 105 1.00


# use a dictionary to store the prices
prices = {
    100: 1.20,
    101: 1.30,
    102: 1.50,
    103: 1.20,
    104: 1.30,
    105: 1.00
}

code = int(input('Type the code of the item ordered: '))
quantity = int(input('Type the quantity of the item ordered: '))

# get the price of the item ordered
price = prices[code]

# calculate the total amount to be paid
total = price * quantity

print(f'The total amount to be paid is {total:.2f}')

