# Code to solve linear system of equation using Jacobi Method

# Author: PUNEETHA KUMAR D
# MTech in Mechanical Engineering IISc Bangalore
# Date: 09/05/2024

# Consider a linear system of equation in the form Ax= b

# Let Rhs be unit vector


import numpy as np


N= 100 # size of vector

b= np.ones(N)

b_exact= np.ones(N-2)
#b[10-1]=10
# Consider the Matrix A = [ 2 -1 0......0
#                           -1 2 -1 0.....0
#                           0 -1 2 -1 0...0] (N)X(N)
A = np.array(np.zeros((N-2,N-2)))

for i in range(0,np.shape(A)[0]):
    A[i,i]=2
    
for i in range(0,np.shape(A)[0]-1): 
    A[i,i+1]=-1

for i in range(1,np.shape(A)[0]): 
    A[i,i-1]=-1
   
# Now solving through Jacobi method

threshold_error=0.00001 
threshold_iteration= 10000 # Maximum number of iteration to be run 
                            # irrespective of threshold error
x_prev_iter= np.zeros_like(b)

k=0
while True:
    
    x_new_iter= np.zeros_like(b)
    error= np.zeros_like(b)
    x_new_iter[1:-1]= (b[1:-1]+ x_prev_iter[0:-2]+x_prev_iter[2:])/2
        
    sum_error= 0
    for i in range(0,np.shape(error)[0]):
       error[i]= x_new_iter[i]-x_prev_iter[i]
       sum_error= sum_error+error[i]**2   
    rms_error= np.sqrt(sum_error/(np.shape(error)[0]-2))
    
    #print(error)
    #print(sum_error)
    print("The rms error is ",rms_error)
    print("The number of iteration ",k)
    
    k=k+1
    if k>threshold_iteration:
       break
    if rms_error< threshold_error:
       break 
    
    x_prev_iter= x_new_iter
    
# Using Inverse matrix ( Direct method)
A_inv= np.linalg.inv(A)
x_exact= np.zeros(N-2)
x_exact= np.dot(A_inv,b_exact)

print("Solution using Direct Method ", x_exact)    
print("Solution using Iterative Jacobi Method",x_new_iter)    
