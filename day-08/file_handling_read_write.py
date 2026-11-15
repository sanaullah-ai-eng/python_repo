with open("day-08/rough.txt", "r") as f:
    content = f.read(10)
    print(content)


#working like loop and more efficent then other methods 
try:
    print()
    with open("day-08/rough.txt" , "r") as f : 
        for line in f : 
            print(line.strip())  # no memory ziyda usage . 
except Exception :
    print('Some error occur .')





