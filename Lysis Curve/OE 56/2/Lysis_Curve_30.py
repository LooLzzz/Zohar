import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs


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
    blanks            = ['A3', 'A9'],
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

wt_cols      = [ c for c in df.columns if 'WT' in c and 'OE' not in c ]
wt_oe56_cols = [ c for c in df.columns if 'WT' in c and 'OE' in c ]

## ΔZaga ##
title = f'Lysis Curve - {deg}°C\nΔZaga'
cols = wt_cols + [ c for c in df.columns if 'Zaga' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## ΔZaga ##

## Δ1555 ##
title = f'Lysis Curve - {deg}°C\nΔ1555'
cols = wt_cols + [ c for c in df.columns if 'd_55' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## Δ1555 ##

## cured ΔStruc ##
title = f'Lysis Curve - {deg}°C\ncured ΔStruc'
cols = wt_cols + [ c for c in df.columns if 'cured' in c ]
fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
title = title.split('\n')
figs[title[1]] = fig
## cured ΔStruc ##




# save dict
for title,fig in figs.items():
    path = f'./figs/{output_folder}/{csv_filename}'
    os.makedirs(path, exist_ok=True)
    print(f'saving {title} figure..')
    fig.savefig(f'{path}/{title}.png')

print('done')

# show
# plt.show()
