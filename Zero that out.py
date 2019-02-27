#Complete Solution
n = int(input())
nums = []

for x in range(n):
    num = int(input())
    if num == 0:
        nums = nums[:len(nums)-1]
    else:
        nums.append(num)

print(sum(nums))