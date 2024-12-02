#python program for printing the table of numbers from 1 to 10 by using the inner for loop
#This is the best example for inner for loop in the python code.
#Most of the cases we use inner loop for the pattern matching.
for num in range(1,11):
    #Using for-loop for a values from 1-10
    for i in range(1,11):
        #using for-loop for values from 1-10
        print(num,"*",i,"=",num*i)
        #printing the result
        if i==10:
            print("\n")
            #The space in between the one loop to the another loop