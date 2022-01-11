class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=s.split()
        arr1=[""]*9
        for i in arr:
            
            arr1[int(i[-1])-1]=i[:-1]
        for i in arr1:
            if i=="":
                arr1.remove(i)
                
        return " ".join(arr1).rstrip()
