import random

# Generate list of 20 arr of 3 random integers between 0 and 99
arr = []
for i in range(20):
    nums = [random.randint(0, 99) for j in range(3)]
    arr.append(nums)

# Write arr to text file
with open('arr20.txt', 'w') as file_out:
    for nums in arr:
        line = ' '.join(str(x) for x in nums) + '\n'
        file_out.write(line)


# Generate list of 100 arr of 3 random integers between 0 and 99
arr = []
for i in range(100):
    nums = [random.randint(0, 99) for j in range(3)]
    arr.append(nums)

# Write arr to text file
with open('arr100.txt', 'w') as file_out:
    for nums in arr:
        line = ' '.join(str(x) for x in nums) + '\n'
        file_out.write(line)

# Generate list of 2000 arr of 3 random integers between 0 and 99
arr = []
for i in range(2000):
    nums = [random.randint(0, 99) for j in range(3)]
    arr.append(nums)

# Write arr to text file
with open('arr2000.txt', 'w') as file_out:
    for nums in arr:
        line = ' '.join(str(x) for x in nums) + '\n'
        file_out.write(line)

# Generate list of 6000 arr of 3 random integers between 0 and 99
arr = []
for i in range(6000):
    nums = [random.randint(0, 99) for j in range(3)]
    arr.append(nums)

# Write arr to text file
with open('arr6000.txt', 'w') as file_out:
    for nums in arr:
        line = ' '.join(str(x) for x in nums) + '\n'
        file_out.write(line)

#insertion sort algorithm
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i- 1
        arr[i + 1] = key


with open("arr20.txt", "r") as f:
    arr20 = []
    for line in f:
        line = line.strip() # removing whitespaces from beginning and end from the text file
        if line: 
            convert = [int(x) for x in line.split()] # converting the line to list of integers
            insertion_sort(convert) # sort the list using insertion sort
            arr20.append(convert) # append sorted list to arr

# opening the text file arr100 and sorting it 
with open("arr100.txt", "r") as f:
    arr100 = []
    for line in f:
        line = line.strip() # removing whitespaces from beginning and end from the text file
        if line: 
            convert = [int(x) for x in line.split()] # converting the line to list of integers
            insertion_sort(convert) # sort the list using insertion sort
            arr100.append(convert) # append sorted list to arr
#opening the text file arr2000 and sortingit
with open("arr2000.txt", "r") as f:
    arr2000 = []
    for line in f:
        line = line.strip() # removing whitespaces from beginning and end from the text file
        if line: 
            convert = [int(x) for x in line.split()] # converting the line to list of integers
            insertion_sort(convert) # sort the list using insertion sort
            arr2000.append(convert) # append sorted list to arr

#opening the text file arr6000 and sorting it
with open("arr6000.txt", "r") as f:
    arr6000 = []
    for line in f:
        line = line.strip() # removing whitespaces from beginning and end from the text file
        if line: 
            convert = [int(x) for x in line.split()] # converting the line to list of integers
            insertion_sort(convert) # sort the list using insertion sort
            arr6000.append(convert) # append sorted list to arr


def insertion_sort_last_column(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][2] > key[2]:
            arr[j + 1] = arr[j]
            j =j - 1
        arr[j + 1] = key
    return arr

# Sort the list based on the last number using insertion sort
arr_sorted = insertion_sort_last_column(arr20)

# Print the sorted list
for column in arr_sorted:
    print(column)

# Open the output file and write the sorted lines
# Save sorted data to file
with open('arrIS_O_20.txt', 'w') as f:
    for row in arr20:
        f.write(' '.join(str(x) for x in row) + '\n')


# Sort the list based on the last number using insertion sort
arr_sorted = insertion_sort_last_column(arr100)

# Print the sorted list
for column in arr_sorted:
    print(column)

# Open the output file and write the sorted lines
# Save sorted data to file
with open('arrIS_O_100.txt', 'w') as f:
    for row in arr100:
        f.write(' '.join(str(x) for x in row) + '\n')


# Sort the list based on the last number using insertion sort
arr_sorted = insertion_sort_last_column(arr2000)

# Print the sorted list
for column in arr_sorted:
    print(column)

# Open the output file and write the sorted lines
# Save sorted data to file
with open('arrIS_O_2000.txt', 'w') as f:
    for row in arr2000:
        f.write(' '.join(str(x) for x in row) + '\n')

# Sort the list based on the last number using insertion sort
arr_sorted = insertion_sort_last_column(arr6000)

# Print the sorted list
for column in arr_sorted:
    print(column)

# Open the output file and write the sorted lines
# Save sorted data to file
with open('arrIS_O_6000.txt', 'w') as f:
    for row in arr6000:
        f.write(' '.join(str(x) for x in row) + '\n')

