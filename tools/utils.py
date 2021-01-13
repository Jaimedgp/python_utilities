"""
Script con algunas funciones utiles para el estudio y procesamiento de los
datos de los diferentes dataFrames

@author Jaimedgp
@date Jun, 2020
"""

from multiprocessing import Pool
import os


def to_all(dataFrame, labels, function, *arg):
    """ Apply the function to all labels in dataFrame """

    processes = (os.cpu_count()-1 if os.cpu_count()-1 > len(labels)
                                  else len(labels))

    df = [dataFrame[lab].copy().dropna() for lab in labels]
    iteration = zip(df, *arg)

    with Pool(processes) as p:
        p.starmap(function, iteration)
