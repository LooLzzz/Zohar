import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from analysis import analyse_file, gen_pair_graphs


sns.set_palette('gray', n_colors=20)
sns.color_palette()





# df = pd.DataFrame(columns=['a','b'], index=range(10))
# df['a'][:2] = [0,1]


# deg = 37
# rept = 3
# csv_filename = f'{deg}deg_{rept}_repeat'
# groups_filename = 'group1'
# output_folder = 'lysis_curve_3_repeats'

# df = analyse_file(
#     opticalDense_path = f'./csv/{csv_filename}.csv',
#     triplicates_path  = f'./groups/{groups_filename}.csv',
#     # blanks            = ['A3'] # for deg30-rept1
#     blanks            = ['A3', 'A9'] # for all else
# )

# vals = df.drop(columns=['Time']).values
# val_max = vals[~np.isnan(vals)].max()
# std_max = df.drop(columns=['Time']).std().max()

# ymax = max(val_max, std_max)

# (0, ymax)

# d = {}
# d = {'a':1, 'b':2}

# d if d else {}



# a = [1,2]
# b = [3,4]

# for (i,j) in zip(a,b):
#     print(i,j)
