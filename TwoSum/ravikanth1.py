def twosum(nums, target):
    output=[]
    for i in nums:
        for j in nums:
            if i+j ==target and nums.index(i)!=nums.index(j):
                output.append(nums.index(i))
                output.append(nums.index(j))
                return output


print(twosum([3,4,5,6,7],10))                