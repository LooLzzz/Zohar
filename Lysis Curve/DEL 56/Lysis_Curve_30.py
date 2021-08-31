import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

#####################
##     GROUP 1     ##
#####################

deg = 30
# deg = 37
rept = 2
time_in_oven = 12
csv_filename = f'{deg}deg_{rept}_repeat'
groups_filename = 'group1'
output_folder = f'lysis_curve_3_repeats'

df = analyse_file(
    opticalDense_path = f'./csv/{csv_filename}.csv',
    triplicates_path  = f'./groups/{groups_filename}.csv',
    blanks            = ['A3', 'A9'], # 2nd repeat
    parse_time        = True,
)
figs = {}

## WT ##
title = f'Lysis Curve - {deg}°C\nWT'
cols = [ c for c in df.columns if 'WT' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## WT ##

wt_cols = [ c for c in df.columns if 'WT' in c and 'Del' not in c ]
wt_del_cols = [ c for c in df.columns if 'WT' in c and 'Del' in c ]

## struc ##
title = f'Lysis Curve - {deg}°C\nΔStruc'
cols = wt_cols + [ c for c in df.columns if 'Struc' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## struc ##

## ΔΔholin-lysin ##
title = f'Lysis Curve - {deg}°C\nΔΔholin-lysin'
cols = wt_cols + [ c for c in df.columns if 'holin-lysin' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## Δ55-6 ##


# save dict
for title,fig in figs.items():
    path = f'./figs/{output_folder}/{csv_filename}'
    os.makedirs(path, exist_ok=True)
    print(f'saving {title} figure..')
    fig.savefig(f'{path}/{title}.png')

print('done')

# show
# plt.show()