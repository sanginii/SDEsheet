n = 4
a1 = [1, 3, 5,7 ] 
m = 3
a2 = [0, 2, 6, 8, 9]
i=n-1 
j=0
while a1[i]>a2[j]:
    a1[i],a2[j]=a2[j],a1[i]
    i-=1
    j+=1
a1.sort()
a2.sort()
print (a1,a2)


#gap method 
def merge(a1, a2):
    import math
    n, m = len(a1), len(a2)

    def next_gap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)  # ceil(gap / 2)

    gap = next_gap(n + m)

    while gap > 0:
        i = 0
        j = gap

        while j < n + m:
            # i and j are positions in the combined virtual array

            # Case 1: both in a1
            if i < n and j < n:
                if a1[i] > a1[j]:
                    a1[i], a1[j] = a1[j], a1[i]

            # Case 2: i in a1, j in a2
            elif i < n and j >= n:
                if a1[i] > a2[j - n]:
                    a1[i], a2[j - n] = a2[j - n], a1[i]

            # Case 3: both in a2
            elif i >= n:
                if a2[i - n] > a2[j - n]:
                    a2[i - n], a2[j - n] = a2[j - n], a2[i - n]

            i += 1
            j += 1

        gap = next_gap(gap)

    



