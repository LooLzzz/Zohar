import os
import sys
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

sys.path.append('../../')
from analysis import analyse_file, gen_pair_graphs

#############
## GROUP 2 ##
#############

deg = 37
# deg = 30
csv_filename = f'{deg}deg_with_AT'
groups_filename = 'group2'
output_folder = 'lysis_curve_at_only/v4'

df = analyse_file(
    opticalDense_path = f'./csv/{csv_filename}.csv',
    triplicates_path  = f'./groups/{groups_filename}.csv'
)
figs = []

## WT ##
title = f'Lysis Curve - {deg}°C\nWT'
wt_cols = [ c for c in df.columns if 'WT' in c ]
fig,axs = gen_pair_graphs(df, wt_cols, title, '+AT', xticks=range(13))
figs += [fig]
## WT ##

## cured ##
title = f'Lysis Curve - {deg}°C\ncured'
cols = wt_cols + [ c for c in df.columns if 'cured' in c and 'zaga' not in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## cured ##

## cured Δzaga ##
title = f'Lysis Curve - {deg}°C\ncured Δzaga'
cols = wt_cols + [ c for c in df.columns if 'zaga' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## cured Δzaga ##

## Δstruc ##
title = f'Lysis Curve - {deg}°C\nΔstruc'
cols = wt_cols + [ c for c in df.columns if 'struc' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δstruc ##

## Δ01552-54 ##
title = f'Lysis Curve - {deg}°C\nΔ01552-54'
cols = wt_cols + [ c for c in df.columns if '01552-54' in c and '02377-78' not in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ01552-54 ##

## Δ02377-78 ##
title = f'Lysis Curve - {deg}°C\nΔ02377-78'
cols = wt_cols + [ c for c in df.columns if '01552-54' not in c and '02377-78' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ02377-78 ##

## Δ01552-54 Δ02377-78 ##
title = f'Lysis Curve - {deg}°C\nΔ01552-54 Δ02377-78'
cols = wt_cols + [ c for c in df.columns if '01552-54' in c and '02377-78' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ01552-54 Δ02377-78 ##

## Δ01555-56 ##
title = f'Lysis Curve - {deg}°C\nΔ01555-56'
cols = [ c for c in df.columns if ('01555-56' in c or 'WT' in c) and 'OE' not in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ01555-56 ##

## Δ01552-54 Δ02377-78 ##
title = f'Lysis Curve - {deg}°C\nΔ01552-54 Δ02377-78'
cols = wt_cols + [ c for c in df.columns if '01552-54' in c or '02377-78' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ01552-54 Δ02377-78 ##

# save
for i,fig in enumerate(figs):
    path = f'./figs/{output_folder}/{csv_filename}'
    os.makedirs(path, exist_ok=True)
    fig.savefig(f'{path}/{i}.png')
# show
# plt.show()