import numpy as np 

x = [[2], 
        [4], 
        [6],
          [10]]  
y = [[2], 
        [8], 
        [9],
          [23]] 

z=[[5], 
      [7], 
        [10],
          [25]] 
p=[[6], 
      [9], 
        [17],
          [28]] 
   

cow_A_vctr = np.array(x) 
cow_B_vctr = np.array(y) 
cow_c_vctr = np.array(z)
cow_test_vctr=np.array(p) 
print("Vector created from a list:") 
print("cow_A_vctr =",cow_A_vctr) 
print("cow_B_vctr=",cow_B_vctr) 
print("cow_c_vctr=",cow_c_vctr) 
print("cow_test_vctr=",cow_test_vctr) 

final_matrix=np.concatenate((cow_A_vctr,cow_B_vctr,cow_c_vctr), axis=1)
print("final_matrix",final_matrix)
import time
start = time.time()
distance1=np.sqrt((np.square(final_matrix-cow_test_vctr).sum(0)))
print("With matrix",distance1)
end =time.time()
seconds=end-start
print("Seconds1 =", seconds)	
start2 = time.time()
distance2=np.sqrt((np.square(cow_A_vctr-cow_test_vctr).sum()))
distance3=np.sqrt((np.square(cow_B_vctr-cow_test_vctr).sum()))
distance4=np.sqrt((np.square(cow_c_vctr-cow_test_vctr).sum()))
print(distance2)
print(distance3)
print(distance4)
end2 =time.time()
seconds2=end2-start2
print("Seconds2 =", seconds2)
print("Difference between two is ","{:.10f}".format(seconds2-seconds))