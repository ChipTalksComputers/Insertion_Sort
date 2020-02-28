#Input
print("Enter your array")

array = list(map(int, input().split()))

n = len(array)

#Sorting
for i in range(1,n):
    j = i
    while (j>=1):
        if array[j] < array[j-1]:
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp


        j-=1

#Output
for element in array:
    print(element, end= " ")
