#shopping cart example to add total value of products
cart={
    "apple":2.5,
    "banana":1.2,
    "milk":3.0
}

total=0
for item,price in cart.items():
    print(f"(item):${price}")
    total+=price   #total=total+price

print(f"total:${total}")
print("total:",total,"$")
print(f"total shopping cost is{total}")
