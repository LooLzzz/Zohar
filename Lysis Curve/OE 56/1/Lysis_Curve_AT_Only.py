import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

#############
## GROUP 2 ##
#############

# deg = 37
deg = 30
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

## Cured ##
title = f'Lysis Curve - {deg}°C\nCured'
cols = wt_cols + [ c for c in df.columns if 'Cured' in c and 'Zaga' not in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Cured ##

## Cured ΔZaga ##
title = f'Lysis Curve - {deg}°C\nCured ΔZaga'
cols = wt_cols + [ c for c in df.columns if 'Zaga' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Cured ΔZaga ##

## ΔStruc ##
title = f'Lysis Curve - {deg}°C\nΔStruc'
cols = wt_cols + [ c for c in df.columns if 'Struc' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## ΔStruc ##

## Δ1552-54 ##
title = f'Lysis Curve - {deg}°C\nΔ1552-54'
cols = wt_cols + [ c for c in df.columns if '1552-54' in c and '2377-78' not in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ1552-54 ##

## Δ2377-78 ##
title = f'Lysis Curve - {deg}°C\nΔ2377-78'
cols = wt_cols + [ c for c in df.columns if '1552-54' not in c and '2377-78' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ2377-78 ##

## Δ1552-54 Δ2377-78 ##
title = f'Lysis Curve - {deg}°C\nΔ1552-54 Δ2377-78'
cols = wt_cols + [ c for c in df.columns if '1552-54' in c and '2377-78' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ1552-54 Δ2377-78 ##

## Δ1555-56 ##
title = f'Lysis Curve - {deg}°C\nΔ1555-56'
cols = [ c for c in df.columns if ('1555-56' in c or 'WT' in c) and 'OE' not in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ1555-56 ##

## Δ1552-54 Δ2377-78 ##
title = f'Lysis Curve - {deg}°C\nΔ1552-54 Δ2377-78'
cols = wt_cols + [ c for c in df.columns if '1552-54' in c or '2377-78' in c ]
fig,axs = gen_pair_graphs(df, cols, title, '+AT', xticks=range(13))
figs += [fig]
## Δ1552-54 Δ2377-78 ##

# save
for i,fig in enumerate(figs):
    path = f'./figs/{output_folder}/{csv_filename}'
    os.makedirs(path, exist_ok=True)
    fig.savefig(f'{path}/{i}.png')
# show
# plt.show()