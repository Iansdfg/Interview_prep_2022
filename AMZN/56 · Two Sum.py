class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers, target):
        # write your code here
        num2index = dict()
        for index, number in enumerate(numbers):
            if number not in num2index:
                num2index[target - number] = index
            else:
                return [num2index[number], index]
            
