from calendar import c


maplist = [34,56,67,98,90]

mydict_list = map(lambda a : {'data': a}, maplist)

for item in mydict_list:
    print(item)


# single line function 

sumsum = lambda a, b, c : a + b + c

print("sum:", sumsum(1, 1, 1))

tupler  = lambda a : a * 2
tripler = lambda a : a * 3

myf = tupler(120)
trip = tripler(100)

print(myf, trip)