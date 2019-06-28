
#1)
import numpy as np
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(np.where(arr%2==1, -1, arr))


#2)
import numpy as np
arr = np.arange(10).reshape(2,5)
arr
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])

#3)
import numpy as np
arr = np.array([1,2,3])
np.concatenate((np.repeat(arr,3),np.tile(arr,3)))
array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

#4)
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)
array([2, 4])
#5)
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a==b)
(array([1, 3, 5, 7]),)


#6)
import numpy as np
5 * np.random.random_sample((5, 3)) + 5
array([[6.17820352, 7.15456359, 9.58391835],
       [5.71413865, 6.38803935, 7.74265941],
       [9.21080484, 6.65698472, 7.59302277],
       [7.42482711, 8.43480418, 6.8226245 ],
       [5.89774903, 5.13907131, 9.91470558]])


#7)
import numpy as np
np.set_printoptions(threshold=3)
arr = np.arange(15)
arr
array([ 0,  1,  2, ..., 12, 13, 14])


#8)
import numpy as np
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(suppress=True, precision=6)
rand_arr
array([[0.000543, 0.000278, 0.000425],
       [0.000845, 0.000005, 0.000122],
       [0.000671, 0.000826, 0.000137]])


#9)
import numpy as np
arr = np.arange(9).reshape(3,3)
arr[:,[0, 1]] = arr[:,[1, 0]]
arr
array([[1, 0, 2],
       [4, 3, 5],
       [7, 6, 8]])

#10)
import numpy as np
arr = np.arange(9).reshape(3,3)
arr[[0, 1],:] = arr[[1, 0],:]
arr
array([[3, 4, 5],
       [0, 1, 2],
       [6, 7, 8]])

