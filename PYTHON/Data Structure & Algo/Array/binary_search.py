def binary_search(arr,target):
	left=0
	right=len(arr)-1
	
	while left<=right:
		mid = (left+right)//2
		if arr[mid]==target:
			return  mid

		elif arr[mid]<target:
			left = mid + 1

		else:
			right = mid -1

	return -1


arr = [1,2,3,4,5,6]
target = 6
result = binary_search(arr,target)
if binary_search!=-1:
	print(f'{target} is found at index',result)

else:
	print('target not found!')

