#### misc operations on lists 

import math 


def batch_list(A, n=None, nbatches=None):
    """
    Splits the list A into batches of size n. 
    If nbatches is specified, splits A evenly into nbatches batches. 
    """
    if nbatches is not None:
        n = len(A) // nbatches
    else:
        nbatches = math.ceil(A / n)

    out = [None for _ in range(nbatches)]
    for i, j in enumerate(range(0, len(A), n)):
        out[i] = A[j:j+n]

    return out
