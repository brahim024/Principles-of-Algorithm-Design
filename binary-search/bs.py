def binary_search(list,item):
	low=0
	high=len(list)-1
	while low <= high:
		mid=(low+high)
		guess=list[mid]
		if guess== item:
			return mid
		if guess > item:
			high =mid-1
		else:
			high=mid +1
	return None

my_list=[-1,0,1,3,5,7,8]

print(binary_search(my_list,3))
print(binary_search(my_list,-1))