# take a number as inputs from the user one by one
# . skip negative numbers and keep adding the positive ones.
# stop when the user enter 0 and print the total uses both continue and break

total=0
while True:
    number=int(input("Enter Your Number : "))
    if number==0:
        break
    if number<0:
        continue
    total+=number
print( 'Total number are :' , total)
