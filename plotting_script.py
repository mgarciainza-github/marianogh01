import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_meas(df : pd.DataFrame, axis_x, axis_y, sweep, info : dict):

    '''
    df      -> DataFrame
    axis_x  -> 
    axis_y  -> 
    sweep   -> ''
    info    -> Datos para el plot
    |-> info.title
    |-> info.label
    |-> info.xlabel
    |-> info.ylabel
    |-> info.leyend
    '''
    
    # Cuando este todo terminado esto se hace afuera
    # para capturar los plots en figures o subplots
    # plt.figure()

    if sweep != '':
        grouped_df = df.groupby(sweep)
        for key, item in grouped_df:
            x = grouped_df.get_group(key)[axis_x]
            y = grouped_df.get_group(key)[axis_y]
            plt.plot(x, y, marker='o')
    else:
        x = df[axis_x]
        y = df[axis_y]
        plt.plot(x, y, marker='o')

    plt.title(info['title'])
    plt.xlabel(info['xlabel'])
    plt.ylabel(info['ylabel'])
    plt.legend(info['leyend'])

    plt.grid(True)
    plt.tight_layout()
    # plt.show()