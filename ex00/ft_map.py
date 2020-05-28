def ft_map(function_to_apply, list_of_inputs):
	res = []
	for elem in list_of_inputs:
		res.append(function_to_apply(elem))
	return res


def double(n): 
    return n + n 
  

# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = ft_map(double, numbers)
print(list(result))