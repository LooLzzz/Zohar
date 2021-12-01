import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

#####################
##     GROUP 1     ##
#####################

for rept in [1,2,3]:
    deg = 30
    # deg = 37
    # rept = 3
    time_in_oven = 12
    csv_filename = f'{deg}deg_{rept}_repeat'
    groups_filename = 'group1'
    output_folder = 'lysis_curve_3_repeats'

    df = analyse_file(
        opticalDense_path = f'./csv/{csv_filename}.csv',
        triplicates_path  = f'./groups/{groups_filename}.csv',
        blanks            = ['A3', 'A9']
    )
    figs = []

    ## WT ##
    title = f'Lysis Curve - {deg}°C\nWT'
    cols = [ c for c in df.columns if 'WT' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    figs += [fig]
    ## WT ##

    wt_cols = [ c for c in df.columns if 'WT' in c and 'OE' not in c ]
    wt_cols_minus_at = [ c for c in df.columns if 'WT' in c and 'OE' not in c and '-AT' in c ]
    wt_oe_cols = [ c for c in df.columns if 'WT' in c and 'OE' in c ]

    ## cured  ##
    title = f'Lysis Curve - {deg}°C\ncured'
    cols = wt_cols + [ c for c in df.columns if 'cured' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    figs += [fig]
    ## cured ##

    ## struc ##
    title = f'Lysis Curve - {deg}°C\nΔstruc'
    cols = wt_cols + wt_oe_cols + [ c for c in df.columns if 'struc' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    figs += [fig]
    ## struc ##

    ## Δ01555-56 ##
    title = f'Lysis Curve - {deg}°C\nΔ01555-56'
    cols = wt_cols + [ c for c in df.columns if '01555-56' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    figs += [fig]
    ## Δ01555-56 ##

    ## Δ01555-56 ##
    title = f'Lysis Curve - {deg}°C\nΔ01555-56'
    cols = wt_cols_minus_at + [ c for c in df.columns if '01555-56' in c and 'OE' not in c and '-AT' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    figs += [fig]
    ## Δ01555-56 ##


    # save
    for i,fig in enumerate(figs):
        path = f'./figs/{output_folder}/{csv_filename}'
        os.makedirs(path, exist_ok=True)
        fig.savefig(f'{path}/{i}.png')

    # show
    # plt.show() 