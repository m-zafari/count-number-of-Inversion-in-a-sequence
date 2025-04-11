
def mergeSort1(arr1, m): 
	temp_arr = [0]*m 
	return tmerge_Sort(arr1, temp_arr, 0, m-1) 

def tmerge_Sort(arr1, temp_arr, left, right): 


	in_count = 0

	if left < right: 

		mid1 = (left + right)//2


		in_count = tmerge_Sort(arr1, temp_arr, left, mid1) 

		in_count += tmerge_Sort(arr1, temp_arr, mid1 + 1, right) 


		in_count += mergefinal(arr1, temp_arr, left, mid1, right) 
	return in_count 
def mergefinal(arr1, temp_arr, left, mid1, right): 
	i = left	 
	j = mid1 + 1 
	k = left	  
	inv_count = 0
 
	while i <= mid1 and j <= right:  

		if arr1[i] <= arr1[j]: 
			temp_arr[k] = arr1[i] 
			k += 1
			i += 1
		else: 
 
			temp_arr[k] = arr1[j] 
			inv_count += (mid1-i + 1) 
			k += 1
			j += 1

	while i <= mid1: 
		temp_arr[k] = arr1[i] 
		k += 1
		i += 1

	while j <= right: 
		temp_arr[k] = arr1[j] 
		k += 1
		j += 1

	for var in range(left, right + 1): 
		arr1[var] = temp_arr[var] 
		
	return inv_count 
N = int(input())
numbers =[]
for i in range(N):
    numbers.append(int(input()))
result = mergeSort1(numbers,len(numbers)) 
print(result%100000)