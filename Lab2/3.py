#Lists
thislist = ["abc", 34, True, 40, "male"]
thislist.insert(2, "watermelon")
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist.pop(1)
[print(x) for x in thislist] 


newlist = [x for x in fruits if "a" in x]
print(newlist)
print([x if x != "banana" else "orange" for x in fruits])

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist.extend(newlist)
print(thislist) 
