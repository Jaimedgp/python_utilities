"""
Script con diferentes metodos para la representacion de los datos de los
DataFrames en funcion de los que se quiera observar

@author Jaimedgp
@date Jun, 2020
"""

import matplotlib.pyplot as plt


def grid_dataFrame(dataFrame, title="Todas las Columnas", toSave=False):
    """ Comparar todas las columnas del dataFrame """

    columns = dataFrame.columns
    numcols = len(columns)

    fig, axs = plt.subplots(numcols, numcols,
                          sharex='col', sharey='row',
                          figsize=(17, 10),
                         )

    for i in range(0, numcols**2):
        x = i // numcols
        y = i % numcols

        dataFrame.plot(kind='scatter',
                       x=columns[x], y=columns[y],
                       ax=axs[y][x]
                      )

        if x == 0:
            axs[y][x].set_ylabel(columns[y])
        if y == 0:
            axs[y][x].set_xlabel(columns[x])

    fig.suptitle(title)
    fig.subplots_adjust(top=0.905,
                        bottom=0.075,
                        left=0.07,
                        right=0.96,
                        hspace=0,
                        wspace=0
                       )

    if toSave:
        file = title.replace(" ", "_")
        fig.savefig("../Figures/"+file+".png")
    else:
        plt.show()


def compare_cols(col1, col2, dataFrame,
                 title="Cols1 frente a Cols2", toSave=False):
    """ Comparar un conjunto de columnas con otro conjunto """

    numcols = len(col1)
    numrows = len(col2)

    fig, axs = plt.subplots(numcols, numrows,
                          sharex='col', sharey='row',
                          figsize=(17, 8),
                         )

    for i in range(0, numcols*numrows):
        x = i // numcols
        y = i % numcols

        dataFrame.plot(kind='scatter',
                       x=col2[x], y=col1[y],
                       ax=axs[y][x]
                      )

        if x == 0:
            axs[y][x].set_ylabel(col1[y])
        if y == 0:
            axs[y][x].set_xlabel(col2[x])

    fig.suptitle(title)
    fig.subplots_adjust(top=0.905,
                        bottom=0.075,
                        left=0.07,
                        right=0.96,
                        hspace=0,
                        wspace=0
                       )

    if toSave:
        file = title.replace(" ", "_")
        fig.savefig("../Figures/"+file+".png")
    else:
        plt.show()
