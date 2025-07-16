import sys
import argparse

import ansible_runner

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--module")
    parser.add_argument("--host")

    args = parser.parse_args()

    res = ansible_runner.run(
        module=args.module,
        host_pattern=args.host,
        quiet=True,
    )

    s = [r for r in res.stdout]
    print("".join(s))



if __name__ == "__main__":
    main()
