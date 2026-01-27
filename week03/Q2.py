# Lists - Searching and Removal
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print("We have ", apple_count, " apples")

milk_position = cart.index("milk")
print("The milk position is at ", milk_position)

cart.remove("apple")
print(cart)

print("Remove item using pop: ", cart.pop())
print(cart)

print("Is the banana in the cart? ", "banana" in cart)

