import pylab
import numpy as np

#open and read in the file 
xydat_file = open("../data/xy.dat", "r")

# The file has data from line 1 onwards, with two collumns

# Set empty lists for storing x and y data (x is first, y second in each row)
xdat = []
ydat = []

# Note the number of data points
n = 0

while True:

    # Use a try/except block to navigate the lines and exit when at the end

    try:
        line = xydat_file.readline()
        words = line.split()

        # if we have not got two words, we have an unwanted line so exit
        if len(words) != 2:
            break

    except:
        break

    # Add 1 to the number of data points seen
    n += 1

    
    # Add data to each list
    x = float(words[0])
    y = float(words[1]) 
    xdat.append(x)
    ydat.append(y)

# Print to screen the max and min y data
print "Max y val = ", max(ydat)
print "Min y val = ", min(ydat)

# Plot y against x, but we need to change lists to arrays first
xdat = np.array(xdat)
ydat = np.array(ydat)
pylab.plot(xdat, ydat)
pylab.xlabel("x")
pylab.ylabel("y")
pylab.show()


