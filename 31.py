from  functools import  reduce
horrible=lambda x:reduce(lambda x,y:x+y,list(map(lambda x:x*x,list(filter(lambda  x:x%2==0,x)))))

arr=[1,2,3,4,5,6,7]
print(horrible(arr))