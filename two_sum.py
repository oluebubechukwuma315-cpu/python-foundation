def twoSum(nums, target):
        result = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp not in result:
                result[nums[i]] = i
            else:
                return result[temp],i
nums = [1,1,456,5,3]
target = 459
print(twoSum(nums,target))