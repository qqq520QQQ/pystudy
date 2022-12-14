class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        res_list = []
        for n1 in nums1:
            if (n1 in nums2) | (n1 in nums3):
                if n1 not in res_list:
                    res_list.append(n1)

        for n2 in nums2:
            if (n2 in nums3) | (n2 in nums1):
                if n2 not in res_list:
                    res_list.append(n2)

        for n3 in nums3:
            if (n3 in nums2) | (n3 in nums1):
                if n3 not in res_list:
                    res_list.append(n3)
        return res_list
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        freq = Counter(nums)   # 每个元素出现次数哈希表
        for num in nums:
            if freq[num-1] == 0 and freq[num+1] == 0 and freq[num] == 1:
                res.append(num)
        return res
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
ss = Solution()
ss.twoOutOfThree(nums1, nums2, nums3)
