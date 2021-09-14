import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

#####################
##     GROUP 1     ##
#####################

deg = 30
# deg = 37
rept = 4
time_in_oven = 12
csv_filename = f'{deg}deg_{rept}_repeat'
groups_filename = 'group1'
output_folder = f'lysis_curve_4_repeats'

df = analyse_file(
    opticalDense_path = f'./csv/{csv_filename}.csv',
    triplicates_path  = f'./groups/{groups_filename}.csv',
    blanks            = ['F1', 'F2', 'F3'],
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

wt_cols = [ c for c in df.columns if 'WT' in c ]

## OE LmaC ##
title = f'Lysis Curve - {deg}°C\nOE LmaC'
cols = wt_cols + [ c for c in df.columns if 'OE LmaC' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## OE LmaC ##

## OE LmaD+C ##
title = f'Lysis Curve - {deg}°C\nOE LmaD+C'
cols = wt_cols + [ c for c in df.columns if 'OE LmaD+C' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## OE LmaD+C ##

## d_LmaC ##
title = f'Lysis Curve - {deg}°C\nΔLmaC'
cols = wt_cols + [ c for c in df.columns if 'd_LmaC' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## d_LmaC ##

## d_LmaD ##
title = f'Lysis Curve - {deg}°C\nΔLmaD'
cols = wt_cols + [ c for c in df.columns if 'd_LmaD' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## d_LmaD ##



# save dict
for title,fig in figs.items():
    path = f'./figs/{output_folder}/{csv_filename}'
    os.makedirs(path, exist_ok=True)
    print(f'saving {title} figure..')
    fig.savefig(f'{path}/{title}.png')

print('done')

# show
# plt.show()