## Initialize the dictionary which has all the check boxes

def initChecked(m):
    checked = {}
    for i in range(2,m+1):
        checked[i] = 0
    i = 2
    while i <= m:
        checked[i] = 1
        i = i * 2
    return checked

## Here's the main function we'll call in the script

def main(n,flag,m):
    count = 0 ## Initialize the number of iterations of the loop to zero
    numIterations = [] ## Initialize an empty array to store the number of iterations at each step
    checked = initChecked(m) ## Initialize the dictionary with check boxes
    for num in range(2,n+1):
        if checked[num] == 1:
            numIterations.append(count)
            continue
        x = num ## Copy the number for later
        aList = []
        while x != 2: ## x has to equal 2 first before it equals 1 so we cut it out
            aList.append(x)
            if x % 2: ## odd
                x = 3 * x + 1
            else: ## even
                x = x / 2
            count = count + 1 ## Increase the count each time
            if x <= m and checked[x] == 1: ## If the number has been checked we're done
                while num <= m:
                    checked[num] = 1 ## Check the original number off (this is why we copied it)
                    num = num * 2 ## Also check off the original number times all possible powers of 2
                for i in aList:
                    if i <= m:
                        checked[i] = 1
                break
        numIterations.append(count) ## Add the number of iterations to this point so we can plot them
    if flag: ## Flag in script to decide whether or not to plot
        plt.plot(range(2,n+1),numIterations) ## Set up the plot
        plt.grid(b=True) ## Show the grid
        plt.show() ## Plot the number of iterations
        plt.savefig('rileyBecker_part3' + str(mult) + '.png') ## Save the plot
    print count ## Print the final counter (mostly for the case when we don't plot)

## This just sets up the scripting by importing and taking arguments from the command line.
## First argument is n and the second is a flag to decide whether or not we should plot
## the number of iterations.

if __name__ == "__main__": ## Do the sccripting
    import sys, matplotlib.pyplot as plt ## Import sys to read arguments, pyplot to plot
    args = sys.argv[1:] ## Take in all the command line arguments after filename
    n = int(args[0]) ## Cast first argument
    flag = int(args[1]) ## Cast second argument
    mult = int(args[2]) ## Cast third argument
    m = n*mult
    main(n,flag,m) ## Now we're set up, so call the main function
