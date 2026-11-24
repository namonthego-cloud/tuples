#create a tuple with diffrent data types 
tuplex = ("tuple",False,3.2,1)
print(tuplex)

#create a tupletuplex = (4,6,3,8,1,7)
print(tuplex)
#tuples are immutable,so it can not be changed.
#usingmerge of tuples with the+operator you can add an element and it wil create a new tuple
tuplex = tuplex +(9,)
print(tuplex)

#counts the number of occurrences of item 50 from a tuple
tuple1 =(50 ,10,60,70,50)
print(tuple1.count(50))

#create a tuple
tuplex = (2,4,3,5,4,6,7,0,1,9)
#used tuple[start:stop]the start index is inclusive and the stop index
_slice = tuplex[3:6]
#is exclusive
print(_slice)
#if the start index isn't defined, is taken from the beinning of the tuple
_slice = tuplex[:6]
print(_slice)
