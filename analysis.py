from cycler import cycler
import seaborn as sns
from typing import Iterable, List, Tuple
from matplotlib.ticker import FormatStrFormatter
from matplotlib import pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np


def strtime_to_floattime(value: str) -> str:
    """converts strtime `h:m:s` to hours in float"""
    h, m, s = [int(item) for item in value.split(':')]
    return h + (m / 60) + (s / (60**2))


class CircularList(list):
    def __getitem__(self, slice):
        if isinstance(slice, int) and slice > len(self) - 1:
            slice = slice % len(self)
        return super().__getitem__(slice)


def analyse_file(opticalDense_path: str, triplicates_path: str,
                 blanks: List[str] = None,
                 parse_time: bool = True,
                 drop_neg: bool = False,
                 drop_wells: List[str] = []) -> pd.DataFrame:
    # od dataframe #
    opticalDense_df: pd.DataFrame = pd.read_csv(opticalDense_path)

    if parse_time:
        opticalDense_df['Time'] = opticalDense_df['Time'].apply(strtime_to_floattime)

    # triplicates dataframe #
    triplicates_df: pd.DataFrame = pd.read_csv(triplicates_path)
    if not blanks and 'blanks' not in triplicates_df:
        blanks = []
        blanks_means = 0
    else:
        if 'blanks' in triplicates_df:
            blanks = triplicates_df['blanks'].dropna()
            triplicates_df = triplicates_df.drop(columns=['blanks'])
        blanks_means = opticalDense_df[blanks].values.mean(axis=1)  # .repeat(3)

    res = pd.DataFrame(opticalDense_df['Time'].repeat(3)).reset_index(drop=True)

    for tri_name in triplicates_df:
        wells = list(triplicates_df[tri_name].dropna())
        # wells = triplicates_df[tri_name]
        # for w in wells:
        #     if w in drop_tris:
        #         wells[w] = np.nan
        # wells = [ w for w in wells if w not in drop_tris ]

        od_values = opticalDense_df[wells]

        for well in od_values:
            if well in drop_wells:
                od_values[well] = np.nan

        if drop_neg:
            for well in od_values:
                # od_values[ od_values[well] < 0 ] = np.nan
                od_values[od_values[well] < 0] = 0

        for well in wells:
            if well in blanks:
                od_values[well] = None
            else:
                od_values[well] -= blanks_means

        od_values = od_values.astype('float64').clip(lower=0).values.flatten().tolist()
        res[tri_name] = np.nan
        res[tri_name][:len(od_values)] = od_values
        # res[tri_name] = od_values
    return res


def gen_pair_graphs(df: pd.DataFrame, cols: List[str], title: str,
                    title_postfix: str = None, suptitle: str = None,
                    legend_labels: List[str] = None, xticks: Iterable = None,
                    figsize_h: Tuple[float, float] = ((25, 9.5)), figsize_v: Tuple[float, float] = (12, 15),
                    xlabel: str = 'Time (hours)', ylabel: str = 'OD 600nm', alignment: float = 1,
                    line_kwargs: dict = {}, sns_theme_kwargs: dict = {}, sns_palette_kwargs: dict = {},
                    legend_kwargs: dict = {}, title_kwargs: dict = {}) -> Tuple[plt.Figure, plt.Axes]:
    def _update_dict(old: dict, new: dict):
        res = old.copy()
        res.update(new)
        return res

    if xticks is None:
        # lo = int(df['Time'].min())
        lo = 0
        hi = int(df['Time'].max() + 1)
        xticks = range(lo, hi, 1 if hi - lo < 20 else 2)

    ####################################
    ########### kwargs setup ###########
    sns_theme_kwargs = _update_dict(
        {
            'style': 'white',
            # 'style': 'dark',
            'font_scale': 1.5,
        },
        sns_theme_kwargs
    )
    sns_palette_kwargs = _update_dict(
        {
            'n_colors': 12,
            # 'palette': 'bone',
            'palette': 'gray',
            # 'palette': 'binary',
        },
        sns_palette_kwargs
    )
    line_kwargs = _update_dict(
        {
            'ci': 'sd',
            'dashes': False,
            'markersize': 20,
            # 'markevery': (0.1,0.1),
        },
        line_kwargs
    )
    legend_kwargs = _update_dict(
        {
            'fontsize': 18,
            # 'loc': (1.02, 0),
            # 'loc': (-0.0675, 1.02),
            # 'loc': (0, -0.32),

            'ncol': 2,
            # 'loc': 'upper center',
            'loc': 'upper left',
            'bbox_to_anchor': (0, -0.11),
            # 'loc': 'lower left',
            # 'bbox_to_anchor': (0, -0.3),
            'fancybox': True,
            'shadow': True,
        },
        legend_kwargs
    )
    title_kwargs = _update_dict(
        {'fontsize': 21},
        title_kwargs

    )
    ########### kwargs setup ###########
    ####################################

    sns.set_theme(**sns_theme_kwargs)
    sns.set_palette(**sns_palette_kwargs)

    markers = CircularList(['o', 'd', 'v', 's', 'p', '*', '^', 'X'])
    colors = CircularList(sns.color_palette())
    markevery_cases = [(0.1, 0.1), (0.15, 0.1), (0.125, 0.15), (0.1, 0.125)]
    # markevery_cases = [(0.1,0.1)]
    mpl.rcParams['axes.prop_cycle'] = cycler(markevery=markevery_cases)
    # mpl.rcParams["text.usetex"] = True
    # mpl.rcParams["font.family"] = 'fantasy'
    mpl.rcParams["font.family"] = 'TeX Gyre Heros'

    if alignment == 1:
        # horizontal
        (fig, axs) = plt.subplots(1, 2, figsize=figsize_h)
        d = title_kwargs.copy()
        d['fontsize'] += 5
        plt.suptitle(title, **d)  # , weight='bold')
        title = ''
        # if suptitle is None and '\n' in title:
        #     suptitle,title = title.split('\n')
    else:
        # vertical
        (fig, axs) = plt.subplots(2, 1, figsize=figsize_v)
    axs = axs.flatten().tolist()

    # if suptitle is not None:
    #     plt.suptitle(suptitle, **title_kwargs)

    cols_mc_plus = []
    cols_mc_minus = []
    for col in cols:
        if '+MC' in col:
            cols_mc_plus += [col]
        elif '-MC' in col:
            cols_mc_minus += [col]

    for (ax, c) in zip(axs, [cols_mc_plus, cols_mc_minus]):
        y_vals = df[c].values
        y_max = y_vals[~np.isnan(y_vals)].max() + 0.05
        ax.set(ylabel=ylabel, xlabel=xlabel, xticks=xticks, xlim=(xticks[0], xticks[-1]), ylim=(0, y_max))
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

    # +MC #
    ax = axs.pop(0)
    labels = []
    for i, col in enumerate(df[cols_mc_plus]):
        labels += [col.replace(' +MC', '').replace('d_', 'Δ')]
        sns.lineplot('Time', col, data=df, ax=ax, color=colors[i], marker=markers[i], **line_kwargs)

    if title_postfix is not None:
        ax.set_title(f'{title} {{+MC {title_postfix}}}'.strip(), **title_kwargs)
        labels = [l.replace(f' {title_postfix}', '') for l in labels]
    else:
        ax.set_title(f'{title} {{+MC}}'.strip(), **title_kwargs)

    if legend_labels is not None:
        labels = [col.replace(' +MC', '').replace('\\\\', '\\').replace('d_', 'Δ')
                  for col in legend_labels if '+MC' in col]
    ax.legend(labels, **legend_kwargs)

    # -MC #
    ax = axs.pop(0)
    labels = []
    for i, col in enumerate(df[cols_mc_minus]):
        labels += [col.replace(' -MC', '').replace('d_', 'Δ')]
        sns.lineplot('Time', col, data=df, ax=ax, color=colors[i], marker=markers[i], **line_kwargs)

    if title_postfix is not None:
        ax.set_title(f'{title} {{-MC {title_postfix}}}'.strip(), **title_kwargs)
        labels = [l.replace(f' {title_postfix}', '') for l in labels]
    else:
        ax.set_title(f'{title} {{-MC}}'.strip(), **title_kwargs)

    if legend_labels is not None:
        labels = [col.replace(' -MC', '').replace('\\\\', '\\').replace('d_', 'Δ')
                  for col in legend_labels if '-MC' in col]
    ax.legend(labels, **legend_kwargs)

    plt.tight_layout()
    return (fig, axs)
