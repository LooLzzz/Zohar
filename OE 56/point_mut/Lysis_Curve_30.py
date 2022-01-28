import sys
import os
from matplotlib import pyplot as plt

sys.path.append('../../')
from analysis import analyse_file, gen_pair_graphs


def to_latex(cols):
    return [r'$\mathrm{' + c.replace(' ', r'\ ') + '}$'
            for c in cols]


for rept in [1, 2, 3, 4]:
    deg = 30
    # deg = 37
    time_in_oven = 12
    csv_filename = f'{deg}deg_{rept}_repeat'
    groups_filename = 'group1'
    output_folder = f'lysis_curve_4_repeats'

    df = analyse_file(
        opticalDense_path=f'./csv/{csv_filename}.csv',
        triplicates_path=f'./groups/{groups_filename}.csv',
        blanks=['A3', 'A9'],
        parse_time=True,
    )
    figs = {}

    ## WT ##
    title = f'Lysis Curve - {deg}°C\nWT'
    cols = [c for c in df.columns if 'WT' in c]
    lbls = to_latex(cols)
    fig, axs = gen_pair_graphs(df, cols, title, legend_labels=lbls, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## WT ##

    wt_cols = [c for c in df.columns if 'WT' in c and 'OE' not in c and 'Y163F' not in c]
    wt_oe56_cols = [c for c in df.columns if 'WT' in c and 'OE' in c and 'Y163F' not in c]

    ## cured PM ##
    title = f'Lysis Curve - {deg}°C\ncured'
    cols = wt_cols + wt_oe56_cols + [c for c in df.columns if 'cured' in c and 'd_zaga' not in c]
    lbls = to_latex(cols)
    fig, axs = gen_pair_graphs(df, cols, title, legend_labels=lbls, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## cured PM ##

    ## cured Δzaga PM ##
    title = f'Lysis Curve - {deg}°C\ncured Δzaga'
    cols = wt_cols + wt_oe56_cols + [c for c in df.columns if 'cured d_zaga' in c]
    lbls = to_latex(cols)
    fig, axs = gen_pair_graphs(df, cols, title, legend_labels=lbls, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## cured Δzaga PM ##

    ## Δstruc ##
    title = f'Lysis Curve - {deg}°C\nΔstruc'
    cols = wt_cols + wt_oe56_cols + [c for c in df.columns if 'd_struc' in c]
    lbls = to_latex(cols)
    fig, axs = gen_pair_graphs(df, cols, title, legend_labels=lbls, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## Δstruc ##

    # save dict
    for title, fig in figs.items():
        path = f'./figs/{output_folder}/{csv_filename}'
        os.makedirs(path, exist_ok=True)
        print(f'saving {title} figure..')
        fig.savefig(f'{path}/{title}.png')

    print('done')

    # show
    # plt.show()
