# Given an array of integers nums, 
# a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: nums = [2,2,3,4]					
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: nums = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# def solution(nums):
#     frequency = {}
    
#     # Count the frequency of each number
#     for num in nums:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1
    
#     lucky_num = -1
    
#     # Find the largest lucky number
#     for num, freq in frequency.items():
#         if num == freq:
#             if num > lucky_num:
#                 lucky_num = num
    
#     return lucky_num
def solution(nums):
    freq = {}  # Dictionary to store the frequency of each number

    # Count the frequency of each number
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    lucky_numbers = []

    # Find lucky numbers
    for num, frequency in freq.items():
        if num == frequency:
            lucky_numbers.append(num)

    if not lucky_numbers:
        return -1

    return max(lucky_numbers)

def solution(li):
    di = {}
    numbers = []
    
    if li:
        for i in range(len(li)):
            if li[i] not in di:
                di[li[i]] = 1
            else:
                di[li[i]] += 1
        
        for k,v in di.items():
            if k == v:
                numbers.append(k)
        if numbers:
            return max(numbers)
        else:
            return -1
    else:
        return -1
