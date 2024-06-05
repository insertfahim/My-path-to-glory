class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr,start,mid,end):
            first = arr[start:mid+1]
            second=arr[mid+1:end+1]
            k=start
            i,j=0,0
            while i<len(first) and j<len(second):
                if first[i]<=second[j]:
                    arr[k]=first[i]
                    i+=1
                    k+=1
                else:
                    arr[k]=second[j]
                    j+=1
                    k+=1
            while i<len(first):
                arr[k]=first[i]
                i+=1
                k+=1
            while j<len(second):
                arr[k]=second[j]
                j+=1
                k+=1
        
        def mergesort(arr,start,end):
            if (end-start)+1<=1:
                return arr
            mid = (start+end)//2
            mergesort(arr,start,mid)
            mergesort(arr,mid+1,end)
            merge(arr,start,mid,end)
            return arr
        return mergesort(nums,0,len(nums)-1)