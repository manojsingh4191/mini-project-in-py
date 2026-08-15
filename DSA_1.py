nums = [2,2,1,1,1,2,2]

def majorityElement(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    majority_count = len(nums) // 2
    for num, cnt in count.items():
        if cnt > majority_count:
            return num

print(majorityElement(nums))