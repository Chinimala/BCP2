from functools import reduce
from collections.abc import Iterable

def ft_reduce(function_to_apply, list_of_inputs):
	if not isinstance(list_of_inputs, Iterable):
		raise TypeError("ft_reduce() arg 2 must support iteration")
	if len(list_of_inputs) == 0:
		raise TypeError("ft_reduce() of empty sequence with no initial value")
	elif len(list_of_inputs) == 1:
		return list_of_inputs[0]
	res = function_to_apply(list_of_inputs[0], list_of_inputs[1])
	for elem in list_of_inputs[2:]:
		res = function_to_apply(res, elem)
	return res

# python code to demonstrate working of reduce() 
  
# importing functools for reduce() 
import functools 

# initializing list 
lis = [ 1 , 3, 5, 6, 2, ]
  
# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (ft_reduce(lambda a,b : a+b,lis))
  
# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (ft_reduce(lambda a,b : a if a > b else b,lis))
