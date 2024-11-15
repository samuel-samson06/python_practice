nums = [7, 2, 8]
target = 10
for i in range(len(nums)):
    x = nums[i]+nums[i+1]
    if x == target:
        into_list = [nums[i], nums[i+1]]
        print(into_list)
        break
    else:
        print(i)
        continue

