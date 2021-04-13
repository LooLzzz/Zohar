import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

#############
## GROUP 3 ##
#############

deg = 30
rept = 1
csv_filename = f'{deg}deg_OEMpaR_{rept}_repeat'
groups_filename = 'group3'
output_folder = 'lysis_curve_OEMpaR/v2'

df = analyse_file(
    opticalDense_path = f'./csv/{csv_filename}.csv',
    triplicates_path  = f'./groups/{groups_filename}.csv',
    blanks            = [],
    drop_wells        = ['A6', 'E5', 'B8', 'B9'],
    drop_neg          = True,
    parse_time        = False
)
figs = []

## WT ##
title = f'Lysis Curve - {deg}°C\nWT'
wt_cols = [ c for c in df.columns if 'WT' in c ]
fig,axs = gen_pair_graphs(df, wt_cols, title)
figs += [fig]
## WT ##

## CURED ##
title = f'Lysis Curve - {deg}°C\nCURED'
cols = wt_cols + [ c for c in df.columns if 'CURED' in c and 'Struc' not in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## CURED ##

## ΔStruc ##
title = f'Lysis Curve - {deg}°C\nΔStruc Compared to Δ1555-56'
cols = wt_cols + [ c for c in df.columns if ('Struc' in c or 'd_1555-56' in c) and 'CURED' not in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## ΔStruc ##

## CURED ΔStruc ##
title = f'Lysis Curve - {deg}°C\nCURED ΔStruc'
cols = wt_cols + [ c for c in df.columns if 'CURED d_Struc' in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## CURED ΔStruc ##



## not OE ##
title = f'Lysis Curve - {deg}°C\n'
cols = [ c for c in df.columns if 'OE' not in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## not OE ##

## OE ##
title = f'Lysis Curve - {deg}°C\nOver Expression MpaR'
cols = [ c for c in df.columns if 'OE' in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## OE ##


# save
for i,fig in enumerate(figs):
    path = f'./figs/{output_folder}/{csv_filename}'
    os.makedirs(path, exist_ok=True)
    fig.savefig(f'{path}/{i}.png')

# show
# plt.show()