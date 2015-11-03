'''
Aditi Nair (asn264)
Introduction to Programming for Data Science: Assignment 7
November 3 2015
'''

import numpy as np
#import matplotlib.pyplot as plt
from mandelbrot import *

print "PROBLEM ONE\n"

#create 1x15 array with entries from 1-15. reshape to 3x5 then transpose
orig = (np.arange(15)+1).reshape((3,5)).transpose()
print "The array is:\n", orig, "\n\n"

#a new array containing the 2nd and 4th rows
second_and_fourth = orig[1:4:2]
print "The second and fourth rows are:\n", second_and_fourth, "\n\n"

#a new array containing the 2nd column
second_col = orig[:,1:2]
print "The 2nd column is:\n", second_col, "\n\n"

#elements from the rectangular section between [1,0] and [3,2]
rect_section = orig[1:4,:] 
print "The elements in the rectangular section between the coordinates [1,0] and [3,2]:\n", rect_section, "\n\n"

#array of zeros with length = number of elements between 3 and 11
li_between_3_11 = []
for index, value in np.ndenumerate(orig):
	if value > 3 and value < 11:
		li_between_3_11.append(orig.item(index))
between_3_11 = np.array(li_between_3_11)
print "The elements between 3 (non-inclusive) and 11 (non-inclusive) are: \n", between_3_11, "\n\n"




print "PROBLEM TWO\n"
a = np.arange(25).reshape(5,5)

#Take the transpose to divide each row element-wise
a_transpose = a.transpose()
b = np.array([1.,5,10,15,20])

#This is the transpose of the solution
c = np.divide(a_transpose, b)
print "The array: \n", a, "\n\nwith each column divided element-wise by the array:\n", b, "\n\nis:\n", c.transpose(), "\n\n"




print "PROBLEM THREE\n"
#A 10x3 array with entries in the range [0,1]
arr = np.random.rand(10,3)
print "A 10x3 array with random values in the range [0,1]:\n", arr, "\n\n"

#find the abs difference between values and 0.5. then do argsort to get the ordering
arr_diff = np.argsort(np.abs(arr-0.5))

#the 0th column in arr_diff the closest value to 0.5
col = arr_diff[:,0:1].ravel().tolist()

#use fancy indexing to pull the correct values
print "The values closest to 0.5 in each row are:\n", arr[np.arange(arr.shape[0]),col], "\n\n" 




print "PROBLEM FOUR\n"
print "See directory for \'mandelbrot.png\'.\n"

#Create a Mandelbrot object with max = 50, threshold = 50 and range [-2,1]x[-1.5,1.5]. I chose to use grid size 1000x1000.
mandel = mandelbrot(50, 50, [-2,1], [-1.5,1.5], 1000)

#Returns the grid with the Mandelbrot iteration applied to it
iter_mandel = mandel.iterate(mandel.z)

#Get the mask of the iteration below the threshold 50
mandel_mask = mandel.get_mask(iter_mandel)

#Get the image in png format
mandel.get_im(mandel_mask)

