import os

from AndroidTrafficRecord import Tester
import argparse

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", help = "path of package name list file (ready to be uninstalled) or a single package name", required = True)
    argParser.add_argument("-l", "--list", help = "the input is a file path", dest = 'islist', nargs='?', const = 1)

    args = argParser.parse_args()

    pkgname_list = []
    if not args.islist:
        pkgname_list.append(args.input)
    else:
        try:
            with open(args.input, "r") as f:
                content = f.read()
        except:
            print("read package name list from input file failed")
            return
        lines = content.split("\n")
        for line in lines:
            pkgname = line.replace("\r", "").strip()
            if len(pkgname) > 0:
                pkgname_list.append(pkgname)
    uninstaller = Tester(None, None, 0, 0, None, 0, 0, False, False, True, 0, False, 100)
    uninstaller.just_uninstall(pkgname_list)

if __name__ == "__main__":
    main()
