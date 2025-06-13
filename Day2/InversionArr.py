inversion_count = 0  # Global variable to track inversion count

def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        b = a[:mid]
        c = a[mid:]
        
        merge_sort(b)
        merge_sort(c)
        
        merge(b, c, a)  # merge into original array

def merge(b, c, a):
    global inversion_count 
    i = j = k = 0
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            inversion_count += len(b) - i  # All remaining elements in b are > c[j]
            j += 1
        k += 1

    while i < len(b):
        a[k] = b[i]
        i += 1
        k += 1

    while j < len(c):
        a[k] = c[j]
        j += 1
        k += 1

# Example usage
a = [5, 3, 2, 1, 4]
merge_sort(a)
print("Sorted Array:", a)
print("Inversion Count:", inversion_count)
