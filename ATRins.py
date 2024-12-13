import os

from AndroidTrafficRecord import Tester
from AndroidTrafficRecord import Downloader
import argparse

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", help = "path of sample URL file or a single APK", required = True)
    argParser.add_argument("-d", "--downloadfolder", help = "downloaded APK folder, default: ./downloadAPK", nargs='?', const = 1, type = str, default = "./downloadAPK")
    argParser.add_argument("-da", "--dapp", help = "disable applications after test", dest = 'disableapp', nargs='?', const = 1)
    argParser.add_argument("-itl", "--installtimelimit", help = "install application time limit(seconds), default: 300s", nargs='?', const = 1, type = int, default = 300)

    args = argParser.parse_args()


    downloadfolder = args.downloadfolder
    pcapfolder = ""
    waittime = 0
    monkeycount = 0
    installtimelimit = int(args.installtimelimit)

    brand = "Invalid"
    if args.input.endswith(".apk"):
        filename = args.input
        downloadfolder, filename = os.path.split(filename)
        fileinfo = [[filename, 0, 0, 0, "InvalidVersion"]]
        if len(downloadfolder) == 0:
            downloadfolder = "."
    else:
        try:
            with open(args.input, "r") as f:
                content = f.read()
        except:
            print("read URL list from input file failed")
            return
        lines = content.split("\n")
        info = []
        for line in lines:
            if len(line) > 0:
                parts = line.split(",")
                if len(parts) >= 7 and len(parts[3]) > 0:
                    info.append([parts[1], parts[3], parts[4], parts[5], parts[6], parts[2]])
        downloader = Downloader(info, downloadfolder)
        fileinfo = downloader.go()
    tester = Tester(downloadfolder, pcapfolder, waittime, monkeycount, fileinfo, brand, 0, False, False, True, 0, True if args.disableapp else False, installtimelimit)
    tester.go()

if __name__ == "__main__":
    main()
