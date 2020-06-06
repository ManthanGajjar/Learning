class Solution:
    def sortArrayByParityII(self, A):
        for i in range(0, len(A)):
            if(A[i] % 2 != i % 2):
                getSwapIndex = Solution.getNextSelectedVal(self, A, i, i % 2)
                tempValue = A[i];
                A[i] = A[getSwapIndex];
                A[getSwapIndex] = tempValue;
        return A

    def getNextSelectedVal(self, A, index,  modIndex):
        for i in range ( index + 1, len(A)):
            if( A[i] % 2 == modIndex):
                return i;

solution = Solution()
inputArray = [4,2,5,7]
result = solution.sortArrayByParityII(inputArray)
print(result)