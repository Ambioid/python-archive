import math
import random

inNums = list(range(1,21)) #Generates List of Nums
random.shuffle(inNums)

nums = []
for x in inNums:
    nums.append([x])
print(nums, "\n")

# Run through enough to merge everything
for o in range(int(math.log(len(nums), 2))+1):  # Log finds how many line repeats
    for i in range(0, len(nums) // 2, 1):  # Run through each line's sublists
        nums.insert(i + 2, [])  # Add an empty replacement list

        while nums[i] or nums[i + 1]:  # Keep iterating until both empty

            # Empties both lists out to replacement, in order
            if (nums[i+1] < nums[i] and nums[i+1]) or nums[i] == []:

                nums[i + 2].insert(len(nums[i+2]), nums[i + 1][0])
                nums[i + 1].pop(0)
            else:
                nums[i + 2].insert(len(nums[i+2]), nums[i][0])
                nums[i].pop(0)

        nums = [x for x in nums if x]  # After that, clear the 2 lists
        #print(nums,"\n")
    print(o, nums)

print((nums[0] == sorted(nums[0])))