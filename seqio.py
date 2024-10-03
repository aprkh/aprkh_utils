
from . import stringops

from Bio import SeqIO
from Bio.Seq import Seq 
from Bio.SeqRecord import SeqRecord 


def main():
    seqs = {'seq1': 'aaccggtt',
            'seq2': 'aaccggt',
            'seq3': 'aaccggttt'}
    n = 4
    outfile = 'test.fasta'

    write_fasta(seqs, outfile, n)

    seqs = [('seq1', 'aaccggtt'),
            ('seq2', 'aaccggt'),
            ('seq3', 'aaccggttt')]
    n = 4
    outfile = 'test2.fasta'

    write_fasta(seqs, outfile, n)


def write_fasta(seqs, outfile, n=80):
    """
    Write sequences to fasta file. Note that we assume the order of the sequences
    is unimportant if the input passed in is a dictionary. 

    Input: 
        seqs (dict[str] -> str) OR (list[(str, str)]): a dictionary or a list of tuples (fasta header, sequence)
        outfile (str): path for output file
    """
    if isinstance(seqs, dict):
        seqs = seqs.items()
    with open(outfile, 'wt') as fout:
        for header, seq in seqs:
            print(f'>{header}', file=fout)
            print('\n'.join(stringops.chop(seq, n)), file=fout)


if __name__ == '__main__': 
    main()
