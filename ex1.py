import matplotlib.pyplot as plt
import numpy as np
import time
start= time.time()
def binary_search(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1
arr=[]
n=int(input("enter the number of element:"))
for i in range(n):
    arr.append(int(input("enter the element")))
print("sorted array",arr)
x=int(input("enter the element to search of element:"))
result=binary_search(arr,0,len(arr),x)
if result!=-1:
    print("element is found in index :",str(result))
else:
    print("element is not found")
end=time.time()
print({end-start})
xpoints=np.array([500,1000,1500,2000,2500,5000])
ypoints=np.array([0.00009,0.0010,0.0020,0.0030,0.0040,0.0050])
plt.plot(xpoints,ypoints)
plt.show()