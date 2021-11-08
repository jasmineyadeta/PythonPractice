def twoSum(nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in hashmap and hashmap[other_num] != i:
                return [i, hashmap[other_num]]

print twoSum([2,11,7,15], 9)