#merge-sort.py
def merge(arr1, arr2):
    i = 0
    j = 0
    combolen = len(arr1) + len(arr2)
    k = 0
    arr3 = []
    while k < combolen: 
        if arr1[i] < arr2[j]:
             arr3.append(arr1[i])
             if i == len(arr1)-1:
                 return arr3 + arr2[j:]
             i = i+1
        else:
            arr3.append(arr2[j])
            if j == len(arr2)-1:
                return arr3 + arr1[i:]
            j = j+1
        k=k+1
    return arr3

def sort(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        half = len(a_list)//2
        left = sort(a_list[:half])
        right = sort(a_list[half:])
        final = merge(left,right)
        return final

######
#Main#
######

num = input('Enter a list of integers: ')
#convert to list
intlist = list(map(int, str(num)))
print(sort(intlist))