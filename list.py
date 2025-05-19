city = ["satna","bhopa","indore","katni"]
number = [1,2,3,4,5]
w =[1,11,1,1,1,1,1,1]
y =[2,2,2,2,2,2,2,2,2]
c =[3,3,3,3,3,3,3,3,3]
for citise in city:
    print(citise,":", min(number))
    nubers = min(number)
    number.remove(nubers)
combined = w + y + c
print(combined)
print(w.index(1))
print(w.sort())
def math():
        squares = [x*2 for x in range(1,10)]
        print(squares)
math()
matrix = [
    [1,2,3],
    [4,5,6],
]
for row in matrix:
    print(row)
for  col in row:
    print(col)
for col in matrix:
    print(col)
transposed = [[row[i] for row in matrix]  for i in range(3)]
print(transposed)

        