## if statement


intthree = 3
intfour = 4
print( intthree < intfour )

if intthree > intfour:
    print('if 3 is not greater then 4 then this wont show')


## while loop

while intthree < intfour:
    # infinte unless you change the values
    intthree += 1
    print('nonnii')

## for loop

## lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# array list
array = [1,2,3,4]

# array length funtion = len(array) # return length of the array

# add elements to an array
array.append(40)

# remove element by index from an array
array.pop(1)

# remove element by the value
array.remove(3)

# remove all elements from an array
array.clear()

# check datatype of variable
name = "myname"
type(name)