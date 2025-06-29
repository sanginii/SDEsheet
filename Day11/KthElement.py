def kthElement(nums1, nums2, k):
    n1 = len(nums1) 
    n2 = len(nums2) 
    
    if n1 > n2:
        return kthElement(nums2, nums1, k) 
    
    low = max(0, k - n2)
    high = min(k, n1)

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = k - mid1

        l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
        r1 = nums1[mid1] if mid1 < n1 else float("inf")
        l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
        r2 = nums2[mid2] if mid2 < n2 else float("inf")

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
