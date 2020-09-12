def towerofhanoi(n, start, end, middle):
	if n == 1:
		print("Move disk %i from tower %s to tower %s" %(n, start, end))
	else:
		towerofhanoi(n-1, start, middle, end)
		print("Move disk %i from tower %s to tower %s" %(n, start, end))
		towerofhanoi(n-1, middle, end, start)

n = 4
towerofhanoi(n, 'A', 'C', 'B')