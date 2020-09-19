def binarySearchRecursive(mylist, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high)//2
		if target == mylist[mid]:
			return True
		elif target < mylist[mid]:
			return binarySearchRecursive(mylist, target, low, mid-1)
		else:
			return binarySearchRecursive(mylist, target, mid+1, high)

def binarySearch(mylist, target):
	low = 0
	high = len(mylist) - 1
	mid = 0
	while low <= high:
		mid = (low + high) // 2
		if mylist[mid] == target:
			return True
			#return mid to return its index
		elif target < mylist[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False

def linearSearch(mylist, target):
	for i in mylist:
		if target == mylist[i]:
			return True
	return False

def linearSearchRecursive(mylist, i, target):
	if i > len(mylist)-1:
		return False
	if mylist[i] == target:
		return True
	return linearSearchRecursive(mylist, i+1, target)


mylist = [i for i in range(0,20)]
print(mylist)

print(binarySearchRecursive(mylist, 0, 0, len(mylist)-1))
print(binarySearchRecursive(mylist, 20, 0, len(mylist)-1))

print(binarySearch(mylist, 0))
print(binarySearch(mylist, 20))

print(linearSearch(mylist, 0))
print(linearSearch(mylist, 20))

print(linearSearchRecursive(mylist, 0, 0))
print(linearSearchRecursive(mylist, 0, 20))

