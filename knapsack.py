def knapsack(arr, weight, w, n):
    if (w ==0 or n == 0):
        return 0
    print("w",w)
    print("n",n)
    if matrix[n][w] != -1:
        return matrix[n][w]
    
    elif weight[n-1] <= w:
        matrix[n][w] = max(arr[n-1] + knapsack(arr, weight, w - weight[n-1], n-1), knapsack(arr, weight, w, n-1))
        return matrix[n][w]
        
    elif weight[n-1] > w:
        matrix[n][w] = knapsack(arr, weight, w, n-1)
        return matrix[n][w]
    

arr = [1, 3, 4, 5]
weight = [1, 4, 5, 7]
w = 5
n = 4

matrix = [[-1 for i in range(w+1)] for i in range(n+1)]

print(matrix)

print(knapsack(arr, weight, w, n))
        
        
    
    