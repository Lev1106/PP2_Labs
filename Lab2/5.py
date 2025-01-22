# Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
thisset.discard("banana")
print(thisset) 


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)
