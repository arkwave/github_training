"""
This is our brand new stats module
"""

def mean(x):
    raise NotImplementedError()

def median(data):
	#finds the median value of a given range of values.
	data.sort()
	index = len(data)
	return data(index//2)
	