# Online Python - IDE, Editor, Compiler, Interpreter
# 1 2 5 4 3
def check_sorted(nums):
    
    i = 0
    flagged = False
    while i<len(nums):
        if i==0 or nums[i]>nums[i-1]:
            i+=1
            continue
        if flagged:
            return False
        flagged = True
        j = i
        to_swap = i
        for j in range(i,len(nums)):
            if nums[j]<nums[i]:
                to_swap = j
                break
        nums[i-1],nums[to_swap]=nums[to_swap],nums[i-1]
    
    return True
lst = [1,2,5,4,3]
print(check_sorted(lst))
lst = [1,2,5,4]
print(check_sorted(lst))
lst = [1,2,5,4,7,6]
print(check_sorted(lst))

        