price1 = 14.2223
price2 = 92.3344
price3 = 34.5543

# .2f represent from decimel how many values need to show
print(f"Price 1 is ${price1 : .3f}")
print(f"Price 1 is ${price1 : .2f}")
print(f"Price 1 is ${price1 : .4f}")

# to make this value of size 10
print(f"Price 1 is ${price1 : 10}")
print(f"Price 2 is ${price2 : 10}")
print(f"Price 3 is ${price3 : 10}")

print(f"Price 1 is ${price1 : 010}")
print(f"Price 2 is ${price2 : 010}")
print(f"Price 3 is ${price3 : 010}")

print(f"Price 1 is ${price1 : <10}")
print(f"Price 2 is ${price2 : <10}")
print(f"Price 3 is ${price3 : <10}")

# to center numbers
print(f"Price 1 is ${price1 : ^10}")
print(f"Price 2 is ${price2 : ^10}")
print(f"Price 3 is ${price3 : ^10}")

price1 = 140000
price2 = 2000
price3 = 90000

print(f"Price 1 is ${price1 : ,}")
print(f"Price 2 is ${price2 : ,}")
print(f"Price 3 is ${price3 : ,}")

print(f"Price 1 is ${price1 : }")
print(f"Price 2 is ${price2 : }")
print(f"Price 3 is ${price3 : }")
