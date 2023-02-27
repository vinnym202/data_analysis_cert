import numpy as np


def calculate(list):
    calculations = {}
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        nparry = np.asarray(list)
        nparry = np.reshape(nparry, (3, 3))
        calculations['mean'] = [
            np.mean(nparry, axis=0).tolist(),
            np.mean(nparry, axis=1).tolist(),
            np.mean(nparry).tolist(),
        ]
        calculations['variance'] = [
            np.var(nparry, axis=0).tolist(),
            np.var(nparry, axis=1).tolist(),
            np.var(nparry).tolist(),
        ]
        calculations['standard deviation'] = [
            np.std(nparry, axis=0).tolist(),
            np.std(nparry, axis=1).tolist(),
            np.std(nparry).tolist(),
        ]
        calculations['max'] = [
            np.max(nparry, axis=0).tolist(),
            np.max(nparry, axis=1).tolist(),
            np.max(nparry).tolist(),
        ]
        calculations['min'] = [
            np.min(nparry, axis=0).tolist(),
            np.min(nparry, axis=1).tolist(),
            np.min(nparry).tolist(),
        ]
        calculations['sum'] = [
            np.sum(nparry, axis=0).tolist(),
            np.sum(nparry, axis=1).tolist(),
            np.sum(nparry).tolist(),
        ]
    return calculations
