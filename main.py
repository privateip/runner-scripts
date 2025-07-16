import sys

import ansible_runner

def main():
    module_name = sys.argv[1]
    host_pattern = sys.argv[2]
    res = ansible_runner.run(module=module_name, host_pattern=host_pattern, quiet=True)

    s = [r for r in res.stdout]
    print("".join(s))



if __name__ == "__main__":
    main()
