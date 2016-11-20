from time import sleep
import os
import numpy

filename = "/home/pi/Documents/temp_range.txt"
avgfile = open("/home/pi/Documents/range_median_value.txt","w")

def median(lst):
    return numpy.median(numpy.array(lst))

def read():
    with open(filename,"r") as infile:
        try:
            data = [float(n) for n in infile.read().split()]
            gooddata = median(data[(len(data)-15):len(data)])
            return gooddata
    
        except (IOError, ValueError):
            destroy()
def loop():
    while True:
        if read() != None:
            avgfile.write("%0.2f\n" % read())
            avgfile.flush()
            os.fsync(avgfile)
            sleep(10)

def destroy():
    data = []
    avgfile.close()
    pass

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
