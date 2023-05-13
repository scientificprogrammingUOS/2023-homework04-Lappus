import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array1, array2, axis=0):
    new_array1 = array1.squeeze()
    new_array2 = array2.squeeze()

    if new_array1.ndim == new_array2.ndim:
        final_array = np.concatenate((new_array1,new_array2), axis)
        return final_array    
    else:
        raise ValueError('The arrays must have the same dimension for combination.')




if __name__ == "__main__":
    # use this for your own testing!
    array1 = np.arange(9).reshape(3,3)
    array2 = np.arange(9,18).reshape(3,3)
    print(combination(array1, array2, axis=1))
    pass
