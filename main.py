#!env python

import sys
import shutil
import shlex
import subprocess
import multiprocessing


def get_env():
    cmd = shutil.which("wrk")
    if cmd is None:
        print("wrk command not found.")
        sys.exit(1)
    cpu = multiprocessing.cpu_count()
    return [cmd, f"-t{cpu}"]

def convert(curl: str) -> list:
    wrk = get_env()
    wrk.extend(sys.argv[2:])  # anything else on the command line will be copied
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
    # print("-------")
    # print(" ".join(cmd))
    # print("-------")
    subprocess.run(cmd, universal_newlines=True)
    # print(res)


if __name__ == "__main__":
    main()
