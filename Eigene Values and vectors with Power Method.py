# comparing three approaches for calculating eigene value and vectors using For- loop , numpy funtions and inbuilt numpy implementation
import numpy as np
import math
import time
import matplotlib.pyplot as plt
tol = 10e-6
max_iter = 1000

#Function for scalar division
def div_scalar(vector_1, divisor):
    div_scalar_list = []
    for i in range (len (vector_1)):
        div_scalar_list.append (vector_1 [i] / divisor)
    return div_scalar_list

#function for vector subtraction
def diff_vector(vector_a, vector_b):
    diff_vector_list = []
    for i in range (len (vector_a)):
        diff_vector_list.append (vector_a [i] - vector_b [i])
    return diff_vector_list

#function for vector multiplication
def dot_product(mat_a, mat_b):
    mat_result = []
    for row_index in range (len (mat_a)):
        sum = 0
        for col_index in range (len (mat_b)):
            sum = sum + mat_a [row_index] [col_index] * mat_b [col_index]
        mat_result.append (sum)
    return mat_result

#function to compute euclidean norm
def L2_norm(x):
    sum = 0
    for i in range (len (x)):
        sum = sum + x [i] * x [i]
    return math.sqrt (sum)

# Controlling function that uses all above function for computing eigene vector and value
def power_method_appr1(input_matrix, max_iter):
    X = np.ones (N)
    for i in range (max_iter):
        y = dot_product (input_matrix, X)
        # calculate the norm
        y_norm = L2_norm (y)
        X_new = div_scalar (y, y_norm)
        if L2_norm(diff_vector(X, X_new)) < tol:
            error_1.append(L2_norm(diff_vector(X, X_new)))
            index_k1.append (i)
            break
        X = X_new
    return X, y_norm

# controlling function for computing using numpy functions
def power_method_appr2(input_matrix, max_iter):
    X = np.ones(N)
    for i in range (max_iter):
        y =np.dot(input_matrix, X)
        # calculate the norm
        y_norm = np.linalg.norm (y)
        X_new = np.divide(y, y_norm)
        if np.linalg.norm((np.subtract(X, X_new))) < tol:
            error_2.append (np.linalg.norm ((np.subtract (X, X_new))))
            index_k2.append(i)
            break
        X = X_new
    return X, y_norm

index_k1 = []  #list of index k corresponding to error_1 list
index_k2 = []  #list of index k corresponding to error_2 list

# error e after computing the eulidean difference between new X and Previous X
error_1 =[]
error_2 =[]
# different value of N list
Ns = []
#list of the time taken to compute the three approach
times_1 =[]
times_2 =[]
times_3 =[]
for N in [50,100,150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]:

    # Approach 1 time measurement after calling the controlling functioins
    t_o = time.time()
    input_matrix = np.random.random ((N, N))
    eig_vect_1, eig_value_1 = power_method_appr1(input_matrix, max_iter)
    t_1 = time.time()
    total_1 = t_1 - t_o
    times_1.append (total_1)
    Ns.append (N)
    print(f'Approach 1 eig vector is {eig_vect_1} and eig value is {eig_value_1}')

    #Approach 2 time measurement after calling the approach 2 control function
    t_2 = time.time ()
    eig_vector_2, eig_value_2 = power_method_appr2 (input_matrix, max_iter)
    t_3 = time.time ()
    total_2 = t_3 - t_2
    times_2.append(total_2)
    print (f'Approach 2 eig vector is {eig_vector_2} and eig value is {eig_value_2}')

    #Approach 3 computation time after calling the inbuilt function
    t_4 = time.time ()
    eig_values, eig_vects = np.linalg.eig (input_matrix)
    t_5 = time.time ()
    total_3 = t_5 - t_4
    times_3.append(total_3)
    print (f'Approach 3 eig vector is {eig_vects} and eig value is {eig_values}')

# Performance characteristics plot of the three approach- number of iteration(Ns) against time
fig, ax = plt.subplots ()
ax.plot (times_1, Ns, 'b', label='For loops Approach')
ax.plot (times_2, Ns, 'k:', label='NumPy Functions Approach')
ax.plot (times_3, Ns, 'r', alpha = 0.5, label='NumPy Implementation Approach')
ax.set_ylabel('Number of iteration')
ax.set_xlabel ('Time')
ax.set_title ('Performance Characteristics of Eigenvalues Model')
ax.legend(loc='best')
plt.savefig ('Power_method_eigene4.png')
plt.show ()

# error e against index k
fig, ax = plt.subplots ()
ax.plot (index_k1, error_1, 'p', label='Error-For loops Appr.')
ax.plot (index_k2, error_2,  'k:', alpha = 0.5, label='Error-NumPy Functions Appr.')
ax.set_ylabel('Error')
ax.set_xlabel ('Number of index')
ax.set_title ('Error of Eigenvalues Model')
ax.legend(loc='best')
plt.axhline(tol, color = 'r', label = 'Tolerance' )
plt.savefig ('error_plot_3.png')
plt.show ()
