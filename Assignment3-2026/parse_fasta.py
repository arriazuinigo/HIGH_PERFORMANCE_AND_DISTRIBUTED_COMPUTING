#!/usr/bin/env python3
"""
parse_fasta.py - Parse a FASTA file and extract accession IDs and sequence lengths.

Part 1: FASTA Parsing and Regular Expressions
Usage: python3 parse_fasta.py <fasta_file>
Output: sequences.tsv
"""

import re
import sys


def parse_fasta(filepath):
    """
    Read a FASTA file and return a list of (accession, sequence) tuples.

    The accession identifier is extracted from the header line using a regular
    expression that matches the first whitespace-delimited token after '>'.
    Sequences that span multiple lines are concatenated into a single string.
    """
    sequences = []
    current_accession = None
    current_seq_parts = []

    # Regular expression to extract the accession identifier from a FASTA header.
    # The header line starts with '>' followed by the accession (no whitespace)
    # and then optional description text.
    header_re = re.compile(r'^>(\S+)')

    with open(filepath, 'r') as fh:
        for line in fh:
            line = line.rstrip('\n')

            if not line:
                continue  # skip blank lines

            header_match = header_re.match(line)
            if header_match:
                # Save the previous sequence before starting a new one
                if current_accession is not None:
                    sequences.append((current_accession, ''.join(current_seq_parts)))
                # Start a new record
                current_accession = header_match.group(1)
                current_seq_parts = []
            else:
                # Sequence line: accumulate (strip trailing whitespace)
                current_seq_parts.append(line.strip())

    # Save the last sequence in the file
    if current_accession is not None:
        sequences.append((current_accession, ''.join(current_seq_parts)))

    return sequences


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <fasta_file>", file=sys.stderr)
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequences = parse_fasta(fasta_file)

    # Write sequences.tsv with one row per sequence
    output_file = 'sequences.tsv'
    with open(output_file, 'w') as out:
        out.write('Accession\tLength\n')
        for accession, seq in sequences:
            out.write(f'{accession}\t{len(seq)}\n')

    print(f"Parsed {len(sequences)} sequences. Output written to {output_file}")


if __name__ == '__main__':
    main()
