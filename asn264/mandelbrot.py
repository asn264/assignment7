'''
Aditi Nair (asn264)
Introduction to Programming for Data Science: Assignment 7
November 3 2015
'''

import numpy as np
import matplotlib.pyplot as plt

class mandelbrot(object):

    
	def __init__(self, n_max, n_threshold, x_range, y_range, grid_size):
		'''
		The Mandelbrot object is tied to a threshold value, a max value, and a grid/set of points in the complex plane such that
		there are (grid_size x grid_size) number of points and they are evenly spaced between x-range values and y-range values.
		'''
		self.max = n_max
		self.threshold = n_threshold
        	x, y = np.meshgrid(np.linspace(x_range[0],x_range[1],grid_size),np.linspace(y_range[0],y_range[1],grid_size))
		self.z = x + 1j * y
		
	def iterate(self,c):
		'''Mandelbrot iteration function as defined in the homework assignment.'''
		np.seterr(all='ignore') #Ignore out of bounds errors
		n = c
		for v in range(self.max):
			n = n**2 + c
		return n
		
	def get_mask(self,iter_array):
		'''Pass an array that has had the iteration applied to it, and get a boolean mask of values below the threshold'''
		mask = np.abs(iter_array) < self.threshold
		return mask
		
	def get_im(self,bool_mask):
		'''Use the mask of the Mandelbrot iteration to get an image via matplotlib'''
		plt.imshow(bool_mask, extent=[-2,1,-1.5,1.5])
		plt.gray()
		plt.savefig('mandelbrot.png')

