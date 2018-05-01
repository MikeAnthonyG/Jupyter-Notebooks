import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.random.seed(26)

def find_correlations(number_variables=5, var_size=100, var_width= 100, r_cutoff=0.2):
    data_matrix = []
    corr_above_cutoff = 0
    for x in range(number_variables):
        data_matrix.append(np.random.randint(0, var_width, var_size))
    
    #Check correlations across all variables
    for i in range(0, number_variables-1):
        for j in range(i+1, number_variables):
            corr_r = np.corrcoef(data_matrix[i], data_matrix[j])
            if corr_r[0][1] > r_cutoff or corr_r[0][1] < (-1.0 * r_cutoff): 
                corr_above_cutoff += 1
    i
    return corr_above_cutoff

#number of variables check for variables 2 to 1000
def check_var():
    var_check = []
    for i in range(2, 100):
        var_check.append(find_correlations(number_variables = i))
    plt.plot(list(range(2,100)), var_check) 
    plt.show()   

def pandas_correlation(num_var= 5, var_size=100, var_range=100, r_cutoff=0.2):
    df = pd.DataFrame()
    _helper = 'a'
    _total = 0
    greatest_coef = 0
    for i in range(2, num_var+1):
        row_name = str(i) + _helper
        df[row_name] = np.random.randint(0, var_range, var_size)        
    df_corr = df.corr()
    col_names = df_corr.columns
    for i in range(len(df_corr)):
        for j in range(len(col_names)):
            if df_corr.iloc[i][j] > r_cutoff or df_corr.iloc[i][j] < (-1.0 * r_cutoff):
                if df_corr.iloc[i][j] != 1:
                    _total += 1
                    if abs(df_corr.iloc[i][j]) > greatest_coef:
                        greatest_coef = abs(df_corr.iloc[i][j])
    return _total, greatest_coef


#Analysis with num_vars changing   , with var_size    and var_range    and r_cutoff
    