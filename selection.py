def selectionsort(a):
    n=len(a)
    for i in range(n-1):
       min=i
       for j in range(i+1,n-1):
           if a[j]<a[min]:
               min=j
       temp=a[i]
       a[i]=a[min]
       a[min]=temp
x=[34,46,43,27,57,41,45,21,70]
print("before sort : ",x)
selectionsort(x)
print("after sort : ",x)
