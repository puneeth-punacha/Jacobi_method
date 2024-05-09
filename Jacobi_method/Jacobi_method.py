# Code to solve linear system of equation using Jacobi Method

# Author: PUNEETHA KUMAR D
# MTech in Mechanical Engineering IISc Bangalore
# Date: 09/05/2024

# Consider a linear system of equation in the form Ax= b

# Let Rhs be unit vector


import numpy as np


N= 3 # size of vector

b= np.ones(N)
#b[10-1]=10
# Consider the Matrix A = [ 2 -1 0......0
#                           -1 2 -1 0.....0
#                           0 -1 2 -1 0...0] (N)X(N)
A = np.array(np.zeros((N,N)))

for i in range(0,N):
    A[i,i]=2
    
for i in range(0,N-1): 
    A[i,i+1]=-1

for i in range(1,N): 
    A[i,i-1]=-1
   
# Now solving through Jacobi method

threshold_error=.4
x_prev_iter= np.zeros_like(b)
x_new_iter= np.zeros_like(b)
error=np.zeros_like(b)
temp_error= 0
while True:
    
    x_new_iter[1:-1]= (b[1:-1]- x_prev_iter[0:-2]-x_prev_iter[2:])/2
    error= abs(x_new_iter[0:]-x_prev_iter[0:])
    
    for i in range(np.shape(error)[0]):
        temp_error= temp_error+error[i]**2   
    rms_error= np.sqrt(temp_error/np.shape(error)[0])
    if rms_error< threshold_error:
        break
    x_prev_iter= x_new_iter
    print(rms_error)
print(x_new_iter)
    
A_inv= np.linalg.inv(A)
#print(np.shape(A_inv))

x_exact= np.zeros_like(b)


x_exact= np.dot(A_inv,b)
#print(x_exact)    
    
