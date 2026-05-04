#!/soft/Miniconda3/bin/python
"""
merge_primes.py – merge all partial prime result files into ALL_PRIMES.txt.

Reads every *.txt file in results_dir (except ALL_PRIMES.txt itself),
extracts integer prime values, deduplicates, sorts, and writes:

    results/ALL_PRIMES.txt
        <prime_1>
        <prime_2>
        ...
        TOTAL:  <count>

Usage
-----
    python merge_primes.py /path/to/results/
"""

import sys
import os
import glob


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: merge_primes.py <results_dir>", file=sys.stderr)
        sys.exit(1)

    results_dir = sys.argv[1]

    if not os.path.isdir(results_dir):
        print(f"ERROR: results directory not found: {results_dir}", file=sys.stderr)
        sys.exit(1)

    # Gather all partial result files, skipping the final output file
    result_files = sorted(
        f for f in glob.glob(os.path.join(results_dir, "*.txt"))
        if os.path.basename(f) != "ALL_PRIMES.txt"
    )

    if not result_files:
        print(f"ERROR: no result files found in {results_dir}", file=sys.stderr)
        sys.exit(1)

    primes: set[int] = set()

    for filepath in result_files:
        print(f"  Reading: {os.path.basename(filepath)}")
        with open(filepath, "r") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("TOTAL:"):
                    continue
                try:
                    primes.add(int(line))
                except ValueError:
                    pass  # ignore unexpected non-integer lines

    sorted_primes = sorted(primes)
    out_file = os.path.join(results_dir, "ALL_PRIMES.txt")

    with open(out_file, "w") as fh:
        for p in sorted_primes:
            fh.write(f"{p}\n")
        fh.write(f"TOTAL:  {len(sorted_primes)}\n")

    print(f"ALL_PRIMES.txt written: {len(sorted_primes)} unique primes.")


if __name__ == "__main__":
    main()
