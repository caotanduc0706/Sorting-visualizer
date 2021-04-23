def insertionSort(a):
	for i in range(1, len(arr)):
		temp = a[i]
		j = i
		while (j > 0 and a[j - 1] > temp):
			a[j] = a[j - 1]
			j -= 1
		a[j] = temp
def bubbleSort(a):
	for i in range(len(a) - 1):
		for j in range(0, len(a) - i - 1):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]


def partition(a, start, end):
	pivotIndex = start
	pivotValue = a[end]
	for i in range(start, end):
		if a[i] < pivotValue:
			a[i], a[pivotIndex] = a[pivotIndex], a[i]
			pivotIndex += 1
	a[pivotIndex], a[end] = a[end], a[pivotIndex]
	return pivotIndex

def quickSort(a, start, end):
	if start >= end:
		return
	index = partition(a, start, end)
	quickSort(a, start, index - 1)
	quickSort(a, index + 1, end)

