import os
import sys
from matplotlib import pyplot as plt

sys.path.append('../')
from analysis import analyse_file, gen_pair_graphs


for rept in [1,2,3]:
    deg = 30
    csv_filename = f'{deg}deg_{rept}_repeat'
    groups_filename = 'group1'
    output_folder = 'lysis_curve_3_repeats/'

    df = analyse_file(
        opticalDense_path = f'./csv/{csv_filename}.csv',
        triplicates_path  = f'./groups/{groups_filename}.csv',
        blanks            = ['A3', 'A9']
    )
    figs = {}

    ## WT ##
    title = f'Lysis Curve - {deg}°C\nWT'
    cols = [ c for c in df.columns if 'WT' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
    title = title.split('\n')
    figs[title[1]] = fig
    ## WT ##

    wt_cols = [ c for c in df.columns if 'WT' in c and 'OE' not in c ]
    wt_oe_cols = [ c for c in df.columns if 'WT' in c and 'OE' in c ]

    ## all ##
    title = f'Lysis Curve - {deg}°C\nΔzaga'
    cols = df.columns.tolist()
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
    title = title.split('\n')
    figs[title[1]] = fig
    ## all ##
    
    ## all (no -AT) ##
    title = f'Lysis Curve - {deg}°C\nΔzaga (no -AT)'
    cols = [ c for c in df.columns if '-AT' not in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
    title = title.split('\n')
    figs[title[1]] = fig
    ## all (no -AT) ##

    # save dict
    for title,fig in figs.items():
        path = f'./figs/{output_folder}/{csv_filename}'
        os.makedirs(path, exist_ok=True)
        print(f'saving {title} figure..')
        fig.savefig(f'{path}/{title}.png')

    # show
    # plt.show()
