#sine :
import math
def sin(x,n):
    s = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        s = s + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return s
x=int(input("x in degrees: "))
n=int(input("number of terms "+"'n'" ": "))
print(round(sin(x,n),2))

#cosine
import math
def cos(x,n):
    s = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        s = s + ((y**(2.0*i))/math.factorial(2*i))*sign
    return s
x=int(input("x in degrees: "))
n=int(input("number of terms "+"'n'" ": "))
print(round(cos(x,n),2))

#exp
import math
exp = 0
x = int(input("Enter the value of x: "))
n = int(input("Number of terms is : "))
for i in range (n):
    exp = exp + ((x**i)/math.factorial(i)) 
print(exp)

#pi
# Initialize denominator
k = 1
 
# Initialize sum
s = 0
 
for i in range(1000000):
 
    # even index elements are positive
    if i % 2 == 0:
        s += 4/k
    else:
 
        # odd index elements are negative
        s -= 4/k
 
    # denominator is odd
    k += 2
     
print(s)
