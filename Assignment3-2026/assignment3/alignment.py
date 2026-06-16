#!/usr/bin/env python3
"""
alignment.py - Compute edit distances and CIGAR strings for DNA sequence alignment.

Parts 2 and 3: Dynamic Programming Edit Distance and CIGAR Generation
Usage: python3 alignment.py <fasta_file>
Output: distances.tsv, alignments.tsv
"""

import re
import sys


# ---------------------------------------------------------------------------
# FASTA parsing (shared helper, same logic as parse_fasta.py)
# ---------------------------------------------------------------------------

def parse_fasta(filepath):
    """
    Read a FASTA file and return a list of (accession, sequence) tuples.
    Accession is extracted via regex; multi-line sequences are concatenated.
    """
    sequences = []
    current_accession = None
    current_seq_parts = []

    header_re = re.compile(r'^>(\S+)')

    with open(filepath, 'r') as fh:
        for line in fh:
            line = line.rstrip('\n')
            if not line:
                continue

            header_match = header_re.match(line)
            if header_match:
                if current_accession is not None:
                    sequences.append((current_accession, ''.join(current_seq_parts)))
                current_accession = header_match.group(1)
                current_seq_parts = []
            else:
                current_seq_parts.append(line.strip())

    if current_accession is not None:
        sequences.append((current_accession, ''.join(current_seq_parts)))

    return sequences


# ---------------------------------------------------------------------------
# Part 2: Dynamic Programming Edit Distance
# ---------------------------------------------------------------------------

def edit_distance_dp(pattern, text):
    """
    Compute the edit distance between pattern and text using bottom-up Dynamic
    Programming (tabulation).

    The DP matrix M has dimensions (len(pattern)+1) x (len(text)+1).
    Cell M[i][j] stores the edit distance between pattern[0:i] and text[0:j],
    i.e., the minimum number of single-character edits (insertion, deletion,
    substitution) needed to transform the first i characters of pattern into
    the first j characters of text.

    Initialization:
      M[i][0] = i   (delete all i characters from pattern to reach empty string)
      M[0][j] = j   (insert j characters to reach text[0:j] from empty string)

    Recurrence for i>=1, j>=1:
      cost = 0 if pattern[i-1] == text[j-1] else 1
      M[i][j] = min(
          M[i-1][j-1] + cost,   # diagonal: match (cost=0) or substitution (cost=1)
          M[i-1][j]   + 1,      # up:       deletion  (remove pattern[i-1])
          M[i][j-1]   + 1,      # left:     insertion (insert text[j-1])
      )

    The final edit distance is stored in M[n][m].

    Time complexity: O(n * m), where n = len(pattern) and m = len(text).
    This avoids repeated sub-problem computation by storing results in the
    matrix rather than recomputing them recursively.

    Returns the complete DP matrix for inspection and traceback.
    """
    n = len(pattern)
    m = len(text)

    # Allocate (n+1) x (m+1) matrix filled with zeros
    M = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: aligning against the empty string requires gap operations
    for i in range(n + 1):
        M[i][0] = i  # i deletions to empty pattern[0:i]
    for j in range(m + 1):
        M[0][j] = j  # j insertions to build text[0:j] from empty string

    # Fill the matrix row by row (bottom-up tabulation)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if pattern[i - 1] == text[j - 1] else 1

            M[i][j] = min(
                M[i - 1][j - 1] + cost,  # diagonal: match or substitution
                M[i - 1][j] + 1,          # up:       deletion
                M[i][j - 1] + 1,          # left:     insertion
            )

    return M


# ---------------------------------------------------------------------------
# Part 3: CIGAR Traceback
# ---------------------------------------------------------------------------

def traceback_cigar(M, pattern, text):
    """
    Recover the expanded CIGAR string by tracing back through the DP matrix
    from the bottom-right cell M[n][m] to the top-left cell M[0][0].

    Each traceback step corresponds to one alignment operation:
      - Diagonal (pattern[i-1] == text[j-1]): 'M' (Match)
      - Diagonal (pattern[i-1] != text[j-1]): 'X' (Substitution)
      - Up   (i decreases):                    'D' (Deletion in query)
      - Left (j decreases):                    'I' (Insertion in query)

    Operations are collected in reverse order and then reversed to produce the
    forward CIGAR string.

    If multiple traceback paths are equally optimal, this implementation
    prefers the diagonal, then up, then left (consistent tie-breaking).
    """
    i = len(pattern)
    j = len(text)
    ops = []

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            cost = 0 if pattern[i - 1] == text[j - 1] else 1

            # Check diagonal first (prefer matches/substitutions)
            if M[i][j] == M[i - 1][j - 1] + cost:
                ops.append('M' if cost == 0 else 'X')
                i -= 1
                j -= 1
            elif M[i][j] == M[i - 1][j] + 1:
                # Came from above: deletion
                ops.append('D')
                i -= 1
            else:
                # Came from left: insertion
                ops.append('I')
                j -= 1
        elif i > 0:
            # Only pattern characters remaining: deletions
            ops.append('D')
            i -= 1
        else:
            # Only text characters remaining: insertions
            ops.append('I')
            j -= 1

    # Reverse to restore forward (left-to-right) order
    ops.reverse()
    return ''.join(ops)


# ---------------------------------------------------------------------------
# Pretty-print the DP matrix (used for the first sequence, required by Part 2)
# ---------------------------------------------------------------------------

def print_dp_matrix(M, pattern, text):
    """Print the DP matrix with row/column labels for inspection."""
    col_labels = [' '] + list(text)
    header = '      ' + '   '.join(col_labels)
    print(header)
    print('      ' + '---' * len(col_labels))

    for i, row in enumerate(M):
        row_label = ' ' if i == 0 else pattern[i - 1]
        cells = '   '.join(f'{v:2d}' for v in row)
        print(f'  {row_label} | {cells}')

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <fasta_file>", file=sys.stderr)
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequences = parse_fasta(fasta_file)

    if not sequences:
        print("Error: No sequences found in FASTA file.", file=sys.stderr)
        sys.exit(1)

    # Reference sequence: first 18 nucleotides of the first record, uppercased.
    # This is extracted automatically from the FASTA file (not hard-coded).
    FRAGMENT_LEN = 18
    reference = sequences[0][1][:FRAGMENT_LEN].upper()
    print(f"Reference ({sequences[0][0]}, first {FRAGMENT_LEN} nt): {reference}")

    # Print the full DP matrix for the first sequence (self-comparison).
    # By definition this distance is 0; the matrix is required for answers.pdf.
    first_fragment = sequences[0][1][:FRAGMENT_LEN].upper()
    M_first = edit_distance_dp(reference, first_fragment)
    print(f"\nDP matrix for the first sequence (self-alignment, distance = 0):")
    print_dp_matrix(M_first, reference, first_fragment)

    # Compute distances and CIGAR strings for every sequence in the file
    dist_rows = []      # (accession, distance)
    align_rows = []     # (accession, distance, cigar)

    for accession, seq in sequences:
        fragment = seq[:FRAGMENT_LEN].upper()
        M = edit_distance_dp(reference, fragment)
        distance = M[len(reference)][len(fragment)]
        cigar = traceback_cigar(M, reference, fragment)
        dist_rows.append((accession, distance))
        align_rows.append((accession, distance, cigar))

    # Write distances.tsv
    with open('distances.tsv', 'w') as f:
        f.write('Accession\tDistance\n')
        for accession, distance in dist_rows:
            f.write(f'{accession}\t{distance}\n')

    # Write alignments.tsv
    with open('alignments.tsv', 'w') as f:
        f.write('Accession\tDistance\tCIGAR\n')
        for accession, distance, cigar in align_rows:
            f.write(f'{accession}\t{distance}\t{cigar}\n')

    print(f"Processed {len(sequences)} sequences.")
    print("Output written to distances.tsv and alignments.tsv")


if __name__ == '__main__':
    main()
