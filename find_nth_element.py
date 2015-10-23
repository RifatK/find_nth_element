
def find_nth_element(list,n,start=None,end=None):
    if  start is None:
        start = 0
    if end is None:
        end = len(list)-1

    if start < end :
        pivot = get_pivot(list,start,end)
        if pivot == n-1:
           return list[pivot]
        elif pivot > n-1:
           return find_nth_element(list,n,start=start,end=pivot)
        else:
           return find_nth_element(list,n,start=pivot+1,end=end)

def get_pivot(list,start,end):
    pivot = start
    i = start + 1
    j = end
    while i < j:
        while list[i] < list[pivot] and i < end:
            i += 1
        while list[j] > list[pivot] and j > start:
            j-= 1
        if i < j:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    temp = list[j]
    list[j] = list[pivot]
    list[pivot] = temp

    if i == j:
        return j-1

    return j

def main():
   #Test Cases
   #list=[0,3,2,1]
   list=[4,2,1,3,8,7,10,9,6]
   print(find_nth_element(list,3))
   print(find_nth_element(list,5))

