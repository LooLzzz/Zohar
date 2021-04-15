import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

#####################
##     GROUP 1     ##
#####################

# deg = 30
deg = 37
rept = 3
csv_filename = f'{deg}deg_{rept}_repeat'
groups_filename = 'group1'
output_folder = 'lysis_curve_3_repeats/v4'

df = analyse_file(
    opticalDense_path = f'./csv/{csv_filename}.csv',
    triplicates_path  = f'./groups/{groups_filename}.csv',
    # blanks            = ['A3'] # for deg30-rept1
    blanks            = ['A3', 'A9'] # for all else
)
figs = []

## WT ##
title = f'Lysis Curve - {deg}°C\nWT'
cols = [ c for c in df.columns if 'WT' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
figs += [fig]
## WT ##

wt_cols = [ c for c in df.columns if 'WT' in c and 'OE' not in c ]
wt_oe_cols = [ c for c in df.columns if 'WT' in c and 'OE' in c ]

## Cured ##
title = f'Lysis Curve - {deg}°C\nCured'
cols = wt_oe_cols + [ c for c in df.columns if 'Cured' in c and 'Zaga' not in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
figs += [fig]
## Cured ##

## zaga ##
title = f'Lysis Curve - {deg}°C\nCured ΔZaga'
cols = wt_oe_cols + [ c for c in df.columns if 'Zaga' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
figs += [fig]
## zaga ##

## struc ##
title = f'Lysis Curve - {deg}°C\nΔStruc'
cols = wt_oe_cols + [ c for c in df.columns if 'Struc' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
figs += [fig]
## struc ##


# save
for i,fig in enumerate(figs):
    path = f'./figs/{output_folder}/{csv_filename}'
    os.makedirs(path, exist_ok=True)
    fig.savefig(f'{path}/{i}.png')

# show
# plt.show()