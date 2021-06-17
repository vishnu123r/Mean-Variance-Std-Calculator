import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    np_list = np.array(list).reshape(3,3)
    mean_0 = np.mean(np_list, axis = 0).tolist()
    mean_1 = np.mean(np_list, axis = 1).tolist()
    mean = np.mean(np_list).tolist()
    mean_list = [mean_0, mean_1,mean]

    var_0 = np.var(np_list, axis = 0).tolist()
    var_1 = np.var(np_list, axis = 1).tolist()
    var = np.var(np_list).tolist()
    var_list = [var_0, var_1, var]

    std_0 = np.std(np_list, axis = 0).tolist()
    std_1 = np.std(np_list, axis = 1).tolist()
    std = np.std(np_list).tolist()
    std_list = [std_0, std_1, std]

    max_0 = np.max(np_list, axis = 0).tolist()
    max_1 = np.max(np_list, axis = 1).tolist()
    max = np.max(np_list).tolist()
    max_list = [max_0, max_1, max]

    min_0 = np.min(np_list, axis = 0).tolist()
    min_1 = np.min(np_list, axis = 1).tolist()
    min = np.min(np_list).tolist()
    min_list = [min_0, min_1, min]

    sum_0 = np.sum(np_list, axis = 0).tolist()
    sum_1 = np.sum(np_list, axis = 1).tolist()
    sum = np.sum(np_list).tolist()
    sum_list = [sum_0, sum_1, sum]
 

    calculations = {"mean": mean_list, "variance": var_list, "standard deviation": std_list, "max": max_list, "min": min_list, "sum": sum_list}

    return calculations


if __name__ == '__main__':
    print(calculate([0,1,2,3,4,5,6,7,8]))