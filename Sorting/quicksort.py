import random

numbers = list(range(1,4)) #Generates List of Nums
random.shuffle(numbers)

def quickSort(nums):
    if len(nums) > 2:
        pivot = nums[-1] # Pivot is last in list
        i = 0
        numLen = len(nums)
        while i < numLen:
            print(nums[i], pivot)
            if nums[i] > pivot:
                nums.append(nums[i])
                nums.pop(i)
                numLen -= 1
            else:
                i+= 1

        print(nums)
        print("Pivot:", pivot)
        piPos = nums.index(pivot)
        print("Pivot Position:", piPos)
        print("Slice:", nums[0::piPos])
        if piPos > 0:
            leftSlice = [quickSort(nums[0::piPos])]
        if piPos < len(nums):
            rightSlice = [quickSort(nums[piPos::])]
        print("LeftSlice:", leftSlice)
        pivot = [pivot]
        print("")
        return [leftSlice + pivot + rightSlice]
    return nums


print(quickSort(numbers))