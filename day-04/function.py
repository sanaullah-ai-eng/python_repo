# write a function that ask a number from user and print the odd or even numbers 
def oddeven():
    num=int(input("Enter Your Number : "))
    if num %2==0:
        print(f"{num} is Even ")
    else:
        print(f"{num} is odd ")
oddeven()
oddeven()






# write a function that shows all the factor of the numebrs entered byuser 
def factorial():
    number = int(input("Enter Your Number "))
    for i in range(1 , number+1):
        if number%i==0 :
            print(i,end=" ")
factorial()







#discount function 
def discount_price(original , dicount):
    discount_amount = (dicount/100) *original
    final = original-discount_amount
    print(f" you wil get a {final} discount ")
discount_price(50 , 50)