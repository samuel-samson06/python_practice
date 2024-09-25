import time
initial_time = time.time()
nums = [1, 1, 2, 3, 4, 4, 4, 5, 1, 5, 6, 7, 7, 7]
nums_t = set(nums)
print(f"k={len(nums_t)} values={list(nums_t)}")
end_time = time.time()
print(f"Program Ran in {end_time-initial_time}s")
