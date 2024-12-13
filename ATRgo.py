import os

from AndroidTrafficRecord import Tester
from AndroidTrafficRecord import Downloader
import argparse

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", help = "path of sample URL file or a single APK", required = True)
    argParser.add_argument("-b", "--brand", help = "0: ChinaTelecom, 1: ChinaUnicom, 2: ChinaMobile", type = int, required = True)
    argParser.add_argument("-t", "--humantest", help = "no monkey", dest = 'onlyhuman', nargs='?', const = 1)
    argParser.add_argument("-d", "--downloadfolder", help = "downloaded APK folder, default: ./downloadAPK", nargs='?', const = 1, type = str, default = "./downloadAPK")
    argParser.add_argument("-p", "--pcapfolder", help = "temporary pcap folder, default: ./tempPCAP", nargs='?', const = 1, type = str, default = "./tempPCAP")
    argParser.add_argument("-w", "--waittime", help = "wait time before monkey(seconds), default: 30s", nargs='?', const = 1, type = int, default = 30)
    argParser.add_argument("-m", "--monkeycount", help = "fake operation count by monkey, default: 800", nargs='?', const = 1, type = int, default = 800)
    argParser.add_argument("-ps", "--pcapsizethreshold", help = "filesize threshold (MiB) of pcap file, default: 20.00", nargs='?', const = 1, type = float, default = 20.00)
    argParser.add_argument("-psm", "--maxpcapsizethreshold", help = "max filesize threshold (MiB) of pcap file, default: 50.00", nargs='?', const = 1, type = float, default = 50.00)
    argParser.add_argument("-da", "--dapp", help = "disable applications after test", dest = 'disableapp', nargs='?', const = 0) # 修改默认值为0
    argParser.add_argument("-itl", "--installtimelimit", help = "install application time limit(seconds), default: 300s", nargs='?', const = 1, type = int, default = 300)
    argParser.add_argument("-l", "--logs", help="show detail logs while testing", dest = 'showlogs', nargs='?', const = 1)

    args = argParser.parse_args()


    downloadfolder = args.downloadfolder
    pcapfolder = args.pcapfolder
    waittime = int(args.waittime)
    monkeycount = int(args.monkeycount)
    pcapsizethreshold = float(args.pcapsizethreshold)
    maxpcapsizethreshold = float(args.maxpcapsizethreshold)
    installtimelimit = int(args.installtimelimit)

    brand = ""
    if args.brand == 0:
        brand = "ChinaTelecom"
    elif args.brand == 1:
        brand = "ChinaUnicom"
    elif args.brand == 2:
        brand = "ChinaMobile"
    else:
        print("invalid brand")
        return
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
                    info.append([parts[1], parts[3], float(parts[4]), float(parts[5]), int(parts[6]), parts[2]])
        downloader = Downloader(info, downloadfolder)
        fileinfo = downloader.go()
    tester = Tester(
        downloadfolder, 
        pcapfolder, 
        waittime, 
        monkeycount, 
        fileinfo, 
        brand, 
        pcapsizethreshold, 
        True if args.onlyhuman else False, 
        True if args.showlogs else False, 
        False, # False为重启手机，还会初始化csv等
        maxpcapsizethreshold, 
        True if args.disableapp else False, 
        installtimelimit)
    tester.go()

if __name__ == "__main__":
    main()
