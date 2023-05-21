def maxAir(arr, n):
	res = 0
	for i in range(1, n - 1):
		left = arr[i]
		for j in range(i):
			left = max(left, arr[j])
		right = arr[i]
		for j in range(i + 1, n):
			right = max(right, arr[j])
		res = res + (min(left, right) - arr[i])
	return res

if __name__ == "__main__":
	n=int(input())
	arr = list(map(int, input().split()))
	print(maxAir(arr, n))
	