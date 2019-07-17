#!env python

import sys
import shlex
import subprocess


def convert(curl: str) -> str:
    wrk = ["/usr/local/bin/wrk", "-t2", "-c100", "-d30s", "--latency"]
    parts = shlex.split(curl)
    eat = False
    for p in parts[2:]:
        if eat:
            wrk.append(shlex.quote(p))
            eat = False
        elif p == "-H":
            wrk.append(p)
            eat = True
        else:
            print(f"Skipping {p}")
    wrk.append(parts[1])  # url
    return wrk


def main():
    cmd = convert(sys.argv[1])
    # print(cmd)
    res = subprocess.run(cmd, universal_newlines=True)
    # print(res)


if __name__ == "__main__":
    main()
