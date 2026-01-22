#largest odd from 10 numbers
import array as arr
large=arr.array('i',[10,20,40,1,30,5,130,80,50,25])
m=0
#loop 
for l in large:
    if m<l:#condition for large
        if l%2!=0: # condition for Odd number
            m=l
        
print(m)
