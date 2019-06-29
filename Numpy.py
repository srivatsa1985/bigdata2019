#1
import numpy as np
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(np.where(arr%2==1, -1, arr))

#2
import numpy as np
arr = np.arange(10).reshape(2,5)

#3
import numpy as np
arr = np.array([1,2,3])
np.concatenate((np.repeat(arr,3),np.tile(arr,3)))

#4

import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

#5)
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a==b)


#6
import numpy as np
5 * np.random.random_sample((5, 3)) + 5

#7
import numpy as np
np.set_printoptions(threshold=3)
arr = np.arange(15)
arr

#8
import numpy as np
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(suppress=True, precision=6)
rand_arr

#9
import numpy as np
arr = np.arange(9).reshape(3,3)
arr[:,[0, 1]] = arr[:,[1, 0]]
arr
array([[1, 0, 2],
       [4, 3, 5],
       [7, 6, 8]])
#10
import numpy as np
arr = np.arange(9).reshape(3,3)
arr[[0, 1],:] = arr[[1, 0],:]
arr
