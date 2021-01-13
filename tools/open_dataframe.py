"""
Script con funciones para la lectura de los datos de dataframe desde archivos
binarios pickle

@author Jaimedgp
@date Jun, 2020
"""

import pandas as pd
import numpy as np


def from_pkl(file):
    """ Importar el dataFrame desde un archivo pickle y obtener los labels
        unicos que identifican las caracteristicas de los datos

        return: DataFrame, labels
    """

    dataFrame = pd.read_pickle(file)
    labels = np.unique([col[:-1] for col in dataFrame.columns], axis=0)

    # transform unique listo to tuple
    labels = [tuple(lab) for lab in labels]

    return dataFrame, labels
