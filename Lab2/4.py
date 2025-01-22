# Tuples
thistuple = ("apple",)
print(type(thistuple))

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
