choosenum = input("Which number of the Fibonacci sequence would you like to find?")+1
choosestart = input("What number would you like the sequence to start from(default Fibonacci is 1)")
start = 0
currentnum = choosestart
counter = 1

nextnum = (start + currentnum)

print(nextnum)

for counter in range(1,choosenum):
    print(counter)
    #this adds moves the counter up by one
    counter = (counter + 1) 
    previousnum = currentnum
    currentnum = nextnum
    nextnum = (currentnum + previousnum)
    print(nextnum)
    print((nextnum)/(currentnum))
