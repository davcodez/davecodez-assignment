n = int(input("Enter a number: ")) 

print(f"The multiples of {n} are:")

count = 1
i = 1  

while count <= 10:  
    multiple = n * i
    print(multiple)
    i += 1
    count += 1
