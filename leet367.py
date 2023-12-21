class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        y = num
        x = y**(0.5)
        if x//1 == x:
            return True
        else:
            return False