#### misc operations on lists 

import math 


def batch_list(A, n):
    """
    Splits the list A into batches of size n. 
    """
    nbatches = math.ceil(len(A) / n)
    out = [None for _ in range(nbatches)]
    for i, j in enumerate(range(0, len(A), n)):
        out[i] = A[j:j+n]
    return out
