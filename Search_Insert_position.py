nums=[1,3,5,6]
target=int(input("Enter target value: "))
a=0
for i in range(len(nums)):
    if nums[i]==target:
        print(f"Target found at index: {i}")
        a=1
        break
if a!=1:
    for i in range(len(nums)):
        if nums[i]>target and target<nums[len(nums)-1]:
            print(f"Target not found. It can be inserted at index: {i}")
            break  
        elif target>nums[len(nums)-1]:
            print(f"Target not found. It can be inserted at index: {len(nums)}")
            break