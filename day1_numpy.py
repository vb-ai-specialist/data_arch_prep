import numpy as np
arr = np.array([1, 2, 3])
#print ("Test Array:", arr)

#print ("Orignal Array: ", arr)

squared = arr **2
#print("Square of Array: ", squared)

new_values = [8,2,7,20,23,41,634]
arr_extended = np.append(arr,new_values)
#print("Updated Array: ", arr_extended)

matrix = arr_extended.reshape(5,2)
#print("Reshaped Array: ", matrix)

matrix_transpose = np.transpose(matrix)
#print("Transposed Array: ", matrix_transpose)


test_data = np.array([23,45,56,12,74,22,88,54,1,85])

data_mean = np.mean(test_data)
#print("Mean for Data: ", data_mean)

data_stdiv = np.std(test_data)
#print("Standard Deviation :", data_stdiv)

two_d_arr = np.array([[1,34,45,12,55],[66,3,56,23,7]])
#print("2-D Array :", two_d_arr)

three_d_arr = np.array([[[4,44,62,65,22],[56,2,7,22,85]],[[53,27,52,77,62],[66,2,7,83,82]],[[26,15,12,44,76],[73,75,88,95,54]],[[3,88,83,99,25],[11,52,63,77,26]]])
print("3-D Array :", three_d_arr)

five_d_arr = np.array([[[[[1,3],[6,3]],[[2,5],[7,2]],[[0,3],[8,8]],[[3,6],[1,4]]],[[[6,4],[8,3]],[[7,8],[6,3]],[[2,9],[0,0]],[[2,1],[3,7]]]],[[[[2,7],[9,3]],[[9,0],[0,8]],[[2,1],[1,0]],[[2,9],[3,8]]],[[[4,5],[5,4]],[[6,3],[7,2]],[[8,1],[9,0]],[[7,7],[2,2]]]]])
#print("5-D Array :", five_d_arr)

slice_thr_d_arr = three_d_arr[1:,:1]
print("Sliced Array :", slice_thr_d_arr)

