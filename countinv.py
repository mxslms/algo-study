#countinv.py
def merge_and_count_split_inv(arr1, arr2):
    i = 0
    j = 0
    combolen = len(arr1) + len(arr2)
    k = 0
    invs=0
    arr3 = []
    while k < combolen: 
        if arr1[i] <= arr2[j]:
             arr3.append(arr1[i])
             if i == len(arr1)-1:
                 return (arr3 + arr2[j:]),invs
             i = i+1
        else:
            arr3.append(arr2[j])
            invs=invs+len(arr1)-i
            if j == len(arr2)-1:
                return (arr3 + arr1[i:]), invs
            j = j+1
            
        k=k+1
    return arr3, invs

def sort_and_count_inv(a_list):
    if len(a_list) <= 1:
        return a_list, 0
    else:
        half = len(a_list)//2
        left, leftinvs = sort_and_count_inv(a_list[:half])
        right, rightinvs = sort_and_count_inv(a_list[half:])
        final, splitinvs = merge_and_count_split_inv(left,right)
        return final, (leftinvs+rightinvs+splitinvs)

######
#Main#
######
'''
num = input('Enter a list of integers: ')
#convert to list
intlist = list(map(int, str(num)))
print(sort_and_count_inv(intlist))

'''
import urllib.request
from bs4 import BeautifulSoup

url = "https://algorithmsilluminated.org/datasets/problem3.5.txt"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
lines = str(soup).splitlines()
total = 0
for line in lines:
    arr, invs = sort_and_count_inv(list(line))
    print (arr, invs)
    total = total + invs
print (total)