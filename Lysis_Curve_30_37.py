import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

#####################
##     GROUP 1     ##
#####################

# deg = 30
deg = 37
rept = 1
csv_filename = f'{deg}deg_{rept}_repeat'
groups_filename = 'group1'
output_folder = 'lysis_curve_3_repeats/v3'

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
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## WT ##

wt_cols = [ c for c in df.columns if 'WT' in c and 'OE' not in c ]
wt_oe_cols = [ c for c in df.columns if 'WT' in c and 'OE' in c ]

## CURED not OE ##
title = f'Lysis Curve - {deg}°C\nCURED'
cols = wt_cols + [ c for c in df.columns if ('CURED' in c and 'OE' not in c) and 'Zaga' not in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## CURED not OE ##

## CURED OE ##
title = f'Lysis Curve - {deg}°C\nCURED OE LMRG_01556'
cols = wt_oe_cols + [ c for c in df.columns if ('CURED' in c and 'OE' in c) and 'Zaga' not in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## CURED OE ##

## zaga not OE ##
title = f'Lysis Curve - {deg}°C\nCURED ΔZaga'
cols = wt_cols + [ c for c in df.columns if 'Zaga' in c and 'OE' not in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## zaga not OE ##

## zaga OE ##
title = f'Lysis Curve - {deg}°C\nCURED ΔZaga OE LMRG_01556'
cols = wt_oe_cols + [ c for c in df.columns if 'Zaga' in c and 'OE' in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## zaga OE ##

## struc not OE ##
title = f'Lysis Curve - {deg}°C\nΔStruc'
cols = wt_cols + [ c for c in df.columns if 'Struc' in c and 'OE' not in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## struc not OE ##

## struc OE ##
title = f'Lysis Curve - {deg}°C\nΔStruc OE LMRG_01556'
cols = wt_oe_cols + [ c for c in df.columns if 'Struc' in c and 'OE' in c ]
fig,axs = gen_pair_graphs(df, cols, title)
figs += [fig]
## struc OE ##


# save
for i,fig in enumerate(figs):
    path = f'./figs/{output_folder}/{csv_filename}'
    os.makedirs(path, exist_ok=True)
    fig.savefig(f'{path}/{i}.png')

# show
# plt.show()