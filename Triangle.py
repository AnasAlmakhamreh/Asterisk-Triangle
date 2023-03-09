

#First nested loops to print the first half of the triangle
for i in range(6): # this first loop is to set the range for the collums 
    for j in range(i): # The second loop is to set the range for the rows
        print("*", end=" ")#Here i use the end=" "  in order to print the Asterisks on the same line
    print()
    
#Second nested loops to print the second half of the triangle
for i in range(4, 0, -1): 
    for j in range(i):
        print("*", end=" ")
    print()
   
    
   
    