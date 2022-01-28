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

    ## OE 01523 ##
    title = f'Lysis Curve - {deg}°C\nOE 01523'
    cols = wt_cols + [ c for c in df.columns if 'OE 01523' in c or 'd_01556' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
    title = title.split('\n')
    figs[title[1]] = fig
    ## OE 01523 ##
    
    ## OE 01523 (+AT) ##
    title = f'Lysis Curve - {deg}°C\nOE 01523 (+AT)'
    cols = [ c for c in df.columns if '+AT' in c and ( ('OE 01523' in c or 'd_01556' in c) or ('WT' in c) ) ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
    title = title.split('\n')
    figs[title[1]] = fig
    ## OE 01523 (+AT) ##
    
    ## ΔlmaA ##
    title = f'Lysis Curve - {deg}°C\nΔlmaA'
    cols = wt_cols + [ c for c in df.columns if 'd_lmaA' in c or 'OE 01556' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
    title = title.split('\n')
    figs[title[1]] = fig
    ## ΔlmaA ##
    
    ## ΔlmaA (+AT) ##
    title = f'Lysis Curve - {deg}°C\nΔlmaA (+AT)'
    cols = [ c for c in df.columns if '+AT' in c and ( ('d_lmaA' in c or 'OE 01556' in c) or ('WT' in c) ) ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(13))
    title = title.split('\n')
    figs[title[1]] = fig
    ## ΔlmaA (+AT) ##
    

    # save dict
    for title,fig in figs.items():
        path = f'./figs/{output_folder}/{csv_filename}'
        os.makedirs(path, exist_ok=True)
        print(f'saving {title} figure..')
        fig.savefig(f'{path}/{title}.png')

    # show
    # plt.show()
