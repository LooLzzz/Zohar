import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

for rept in [1,2,3,4]:
    deg = 30
    # deg = 37
    # rept = 2
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

    ## Δzaga ##
    title = f'Lysis Curve - {deg}°C\nΔzaga'
    cols = wt_cols + [ c for c in df.columns if 'zaga' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## Δzaga ##

    ## Δ01555 ##
    title = f'Lysis Curve - {deg}°C\nΔ01555'
    cols = wt_cols + wt_oe56_cols + [ c for c in df.columns if 'd_01555' in c or 'd_struc OE' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## Δ01555 ##

    ## cured Δstruc ##
    title = f'Lysis Curve - {deg}°C\ncured Δstruc'
    cols = wt_cols + [ c for c in df.columns if 'cured' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## cured Δstruc ##




    # save dict
    for title,fig in figs.items():
        path = f'./figs/{output_folder}/{csv_filename}'
        os.makedirs(path, exist_ok=True)
        print(f'saving {title} figure..')
        fig.savefig(f'{path}/{title}.png')

    print('done')

    # show
    # plt.show()
