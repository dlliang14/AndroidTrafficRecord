from concurrent .futures import ThreadPoolExecutor ,wait ,ALL_COMPLETED #line:1
import subprocess #line:2
import threading #line:3
import pandas as pd #line:4
import numpy as np #line:5
import warnings #line:6
import dpkt #line:7
import time #line:8
import math #line:9
import os #line:10
import re #line:11
import traceback #line:12
import wget #line:13
import keyboard #line:14
class Tester :#line:17
    def __init__ (O0O0OO0OO0OO00O00 ,OO00000O000OO0OOO ,OO0OO000O0OO0O00O ,OO0OO0OO000OO0OOO ,OOO0OO00OO00000O0 ,OO00O0OOOOO000O0O ,O0OOOO0O000OOO0OO ,O0OOO00O0O0O00000 ,OO00000O0O0OOO0OO ,O0O00O00O000OOO00 ,OOO0OOOO0OOO000OO ,O000OO00OOO0O0O0O ,OOO0OO0O0OO00O00O ,OOOOO00O00OOOOO00 ):#line:18
        warnings .filterwarnings ("ignore")#line:19
        O0O0OO0OO0OO00O00 .__O0O00OO0OO000O00O =OO00000O000OO0OOO #line:20
        O0O0OO0OO0OO00O00 .__O00OOO0OOOO0OOO0O =OO0OO000O0OO0O00O #line:21
        O0O0OO0OO0OO00O00 .__OOOOO00O000O0OOOO =OO0OO0OO000OO0OOO #line:22
        O0O0OO0OO0OO00O00 .__O0000O0OO0OO00OO0 =OOO0OO00OO00000O0 #line:23
        O0O0OO0OO0OO00O00 .__OO00O0O0000OOOO0O =OO00O0OOOOO000O0O #line:24
        O0O0OO0OO0OO00O00 .__O000O0000000O000O =O0OOOO0O000OOO0OO #line:25
        O0O0OO0OO0OO00O00 .__OOO00OOOO0OOOOOOO =OO00000O0O0OOO0OO #line:26
        O0O0OO0OO0OO00O00 .__O0O00OO00O0OOOO00 =0 #line:27
        O0O0OO0OO0OO00O00 .__O00O0O0O0OO000OOO =O0O00O00O000OOO00 #line:28
        O0O0OO0OO0OO00O00 .__OO0OO0O00O000OO00 =OOO0OOOO0OOO000OO #line:29
        O0O0OO0OO0OO00O00 .__O0O00OO00OO0OOOO0 =O0OOO00O0O0O00000 #line:30
        O0O0OO0OO0OO00O00 .__O00O000OO0O0O00OO =O000OO00OOO0O0O0O #line:31
        O0O0OO0OO0OO00O00 .__O0OOO0OO00OOOOO0O =OOO0OO0O0OO00O00O #line:32
        O0O0OO0OO0OO00O00 .__O0OO000OO000OO000 =OOOOO00O00OOOOO00 #line:33
        O0O0OO0OO0OO00O00 .__OO0OO0000O0OO00OO =os .path .dirname (__file__ )#line:34
        O0O0OO0OO0OO00O00 .__OOO00OO00OO0OO0O0 =False #line:35
        if O0O0OO0OO0OO00O00 .__OOO00OOOO0OOOOOOO :#line:36
            keyboard .hook (O0O0OO0OO0OO00O00 .__OO0OOO000O0O0OOOO )#line:37
        O0O0OO0OO0OO00O00 .__OO00O00O00000OO00 =threading .Lock ()#line:40
        if not O0O0OO0OO0OO00O00 .__OO0OO0O00O000OO00 :#line:41
            if not os .path .exists (O0O0OO0OO0OO00O00 .__O00OOO0OOOO0OOO0O ):#line:42
                os .makedirs (O0O0OO0OO0OO00O00 .__O00OOO0OOOO0OOO0O )#line:43
            O0O000OOO000O0O0O =O0O0OO0OO0OO00O00 .__OO0OOOO0O00O000OO ()#line:44
            if not os .path .exists ("./ATR_result.csv"):#line:45
                OO00OO000OO000OOO =pd .DataFrame (columns =O0O000OOO000O0O0O )#line:46
                OO00OO000OO000OOO .to_csv ("./ATR_result.csv",index =False ,encoding ="gb2312")#line:47
            O0O0OO0OO0OO00O00 .__O0O00OO000OO00O0O =pd .read_csv ("./ATR_result.csv",encoding ="gb2312")#line:48
            O0OO0O0OOOOO0OOOO =set (O0O0OO0OO0OO00O00 .__O0O00OO000OO00O0O .columns .tolist ())#line:50
            for OO00O00OOO0OOOOOO in O0O000OOO000O0O0O :#line:51
                if OO00O00OOO0OOOOOO not in O0OO0O0OOOOO0OOOO :#line:52
                    os .rename ("./ATR_result.csv","./ATR_result.csv.bak")#line:54
                    OO00OO000OO000OOO =pd .DataFrame (columns =O0O000OOO000O0O0O )#line:55
                    OO00OO000OO000OOO .to_csv ("./ATR_result.csv",index =False ,encoding ="gb2312")#line:57
                    O0O0OO0OO0OO00O00 .__O0O00OO000OO00O0O =pd .read_csv ("./ATR_result.csv",encoding ="gb2312")#line:58
                    break #line:59
    def __OO0OOO000O0O0OOOO (O00000O0OO00OO0O0 ,O0OOOO0O000O00O0O ):#line:61
        if O0OOOO0O000O00O0O .event_type =='up'and O0OOOO0O000O00O0O .name =='enter':#line:62
            O00000O0OO00OO0O0 .__OOO00OO00OO0OO0O0 =True #line:63
    def __OO0OOOO0O00O000OO (OO00O0OOO0O00OOO0 ):#line:65
        ""#line:69
        O0OO0000O0OOO0O00 =["PackageName"]#line:70
        for O0OO0O0OOOOOO0OOO in ["ChinaTelecom","ChinaUnicom","ChinaMobile"]:#line:71
            for OOOOO000OOOO000OO in ["IPv4","IPv6"]:#line:72
                for OOOO00O0000OOOO00 in ["rx_packets","rx_bytes","tx_bytes","tx_packets","rx_tcp_bytes","rx_tcp_packets","rx_udp_bytes","rx_udp_packets","tx_tcp_bytes","tx_tcp_packets","tx_udp_bytes","tx_udp_packets"]:#line:75
                    O0OO0000O0OOO0O00 .append ("-".join ([O0OO0O0OOOOOO0OOO ,OOOOO000OOOO000OO ,OOOO00O0000OOOO00 ]))#line:76
            O0OO0000O0OOO0O00 .append ("-".join ([O0OO0O0OOOOOO0OOO ,"IPv6Rate","bytes"]))#line:77
            O0OO0000O0OOO0O00 .append ("-".join ([O0OO0O0OOOOOO0OOO ,"IPv6Rate","packets"]))#line:78
        return O0OO0000O0OOO0O00 #line:79
    def __OOO00O0OOO00O0OO0 (OOOO00O000O0O00O0 ):#line:81
        ""#line:86
        O0O0OO000OO00O00O =OOOO00O000O0O00O0 .__O0OOO0000OOOO0O00 ("su -h",True )#line:87
        O0O00OO0OOO00O00O =O0O0OO000OO00O00O [1 ]#line:88
        if "su: not found"in O0O00OO0OOO00O00O or "su: inaccessible"in O0O00OO0OOO00O00O :#line:89
            return False #line:90
        if "pass COMMAND to the invoked shell"in O0O00OO0OOO00O00O :#line:91
            OOOO00O000O0O00O0 .__O0O00OO00O0OOOO00 =0 #line:92
        else :#line:93
            OOOO00O000O0O00O0 .__O0O00OO00O0OOOO00 =1 #line:94
        OO00OO0OO000O0OO0 =OOOO00O000O0O00O0 .__O0OOO0000OOOO0O00 ("su root -c ping",True )#line:95
        O00O00OOO00OO0OOO =OO00OO0OO000O0OO0 [1 ]#line:96
        if "sage: ping ["in O00O00OOO00OO0OOO :#line:97
            OOOO00O000O0O00O0 .__O0O00OO00O0OOOO00 =0 #line:98
        else :#line:99
            OOOO00O000O0O00O0 .__O0O00OO00O0OOOO00 =1 #line:100
        if "ermission denied"in O00O00OOO00OO0OOO :#line:101
            return False #line:102
        return True #line:103
    def __OO00O0O000OO00OOO (O0OOOOO0O00O0O0O0 ):#line:105
        ""#line:110
        OOO000OO0O0OO00OO =O0OOOOO0O00O0O0O0 .__O0OOO0000OOOO0O00 ("ping -w 1 ipv4.vm3.test-ipv6.com",True )#line:111
        OO0OOOOOO00O0OO00 =OOO000OO0O0OO00OO [1 ]#line:112
        OO00O0O0OOO000OO0 =O0OOOOO0O00O0O0O0 .__O0OOO0000OOOO0O00 ("ping6 -w 1 ipv6.vm3.test-ipv6.com",True )#line:113
        O000O0O0OOOO0OOOO =OO00O0O0OOO000OO0 [1 ]#line:114
        return "icmp_seq=1"in OO0OOOOOO00O0OO00 and "icmp_seq=1"in O000O0O0OOOO0OOOO #line:115
    def __OOOOO00OOOO0O00O0 (O000O00OO00O000O0 ):#line:117
        ""#line:122
        OOO00O000O000OO0O =O000O00OO00O000O0 .__O0OOO0000OOOO0O00 ("version")#line:123
        O0OOO000O0O00O0O0 =OOO00O000O000OO0O [1 ]#line:124
        OO0O0000O00000OOO =None #line:125
        O00O0O0OO0OO0OOO0 =False #line:126
        if O0OOO000O0O00O0O0 .find ("Android Debug Bridge version")!=-1 :#line:128
            OOO00O000O000OO0O =O000O00OO00O000O0 .__O0OOO0000OOOO0O00 ("devices")#line:129
            OOOO00OO0000O0O0O =OOO00O000O000OO0O [1 ]#line:130
            if "\tdevice"in OOOO00OO0000O0O0O .replace (' ','').replace ('\n','').replace ('\r',''):#line:132
                if O000O00OO00O000O0 .__OOO00O0OOO00O0OO0 ():#line:133
                    O00O0O0OO0OO0OOO0 =True #line:134
                else :#line:135
                    OO0O0000O00000OOO ="Not a rooted device"#line:136
            else :#line:137
                OO0O0000O00000OOO ="No connected devices"#line:138
        else :#line:139
            OO0O0000O00000OOO ="ADB lost"#line:140
        return [OO0O0000O00000OOO ,O00O0O0OO0OO0OOO0 ]#line:141
    # 强制终止所有正在运行的 adb.exe 进程
    def __O0O0O0O000000O0O0 (OOOO0OOO0O0O00O00 ):#line:143
        ""#line:145
        subprocess .getstatusoutput ("TASKKILL /F /IM adb.exe")#line:146
    def __O0OO00OOOO0O00OOO (OO0OOO0OOO0OO0000 ,O000OO0O0O00OOO00 ,O0O000O00O000OOOO ,O00OO000O00O00O00 ):#line:148
        ""#line:155
        O000O0OO0000OO0O0 ="\"%s/adb\" "%OO0OOO0OOO0OO0000 .__OO0OO0000O0OO00OO #line:156
        if O0O000O00O000OOOO :#line:157
            O000O0OO0000OO0O0 +="shell "#line:158
            if O00OO000O00O00O00 :#line:159
                O000O0OO0000OO0O0 +="su root "#line:160
                if OO0OOO0OOO0OO0000 .__O0O00OO00O0OOOO00 ==0 :#line:161
                    O000O0OO0000OO0O0 +="-c "#line:162
                elif OO0OOO0OOO0OO0000 .__O0O00OO00O0OOOO00 ==1 :#line:163
                    pass #line:164
        O000O0OO0000OO0O0 +=O000OO0O0O00OOO00 #line:165
        return O000O0OO0000OO0O0 #line:166
    def __O0OOO0000OOOO0O00 (O00O0O0OOOO0OOOO0 ,OO000OO0OOOOO0OOO ,O00OO0OO00OO00000 =False ,OO000O0O0OOOOO0OO =False ):#line:168
        ""#line:175
        O0O0O0OO00O00OO00 =O00O0O0OOOO0OOOO0 .__O0OO00OOOO0O00OOO (OO000OO0OOOOO0OOO ,O00OO0OO00OO00000 ,OO000O0O0OOOOO0OO )#line:176
        if O00O0O0OOOO0OOOO0 .__O00O0O0O0OO000OOO :#line:177
            print ("Execute ADB command: %s"%O0O0O0OO00O00OO00 )#line:178
        O0OOOO00000000O0O =subprocess .getstatusoutput ("%s"%(O0O0O0OO00O00OO00 ))#line:179
        if O00O0O0OOOO0OOOO0 .__O00O0O0O0OO000OOO :#line:180
            print ("ADB result: \n%s"%str (O0OOOO00000000O0O ))#line:181
        return O0OOOO00000000O0O #line:182
    def __OO0O000OOO0000OO0 (O0OO000O000000OOO ,O0O00O0000O0O000O ):#line:184
        ""#line:190
        try :#line:191
            O0O000O0OOOO0OOO0 =subprocess .check_output ("%s/aapt dump badging %s"%(O0OO000O000000OOO .__OO0OO0000O0OO00OO ,O0O00O0000O0O000O ))#line:192
            O00OO0O0OO0O0O000 =O0O000O0OOOO0OOO0 [:O0O000O0OOOO0OOO0 .index (b"sdkVersion")].decode ("gbk")#line:193
            OOOO00OOO00OO00OO =re .compile ("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match (O00OO0O0OO0O0O000 )#line:194
        except :#line:195
            return None #line:196
        if not OOOO00OOO00OO00OO :#line:197
            return None #line:198
        return OOOO00OOO00OO00OO .group (1 )#line:199
    def __OOO00OO000OOO0O00 (OO00O00OOO00O0O00 ,O0O00OO0O00OOOOOO ):#line:201
        ""#line:204
        OOO0000OO0O0O0O0O =OO00O00OOO00O0O00 .__O0OO00OOOO0O00OOO ("install -f -r -d -g %s"%(O0O00OO0O00OOOOOO ),False ,False )#line:205
        OOO0OO0OO00O00OO0 =False #line:206
        def O0000O00000O00O0O (OO0O0O00O00O0OOO0 ):#line:207
            nonlocal OOO0OO0OO00O00OO0 #line:208
            OOO0OO0OO00O00OO0 =False #line:209
            OO0O0O00O00O0OOO0 .terminate ()#line:210
            print ("Warning: ADB installation stuck, RETRY\n",end ="",flush =True )#line:211
        while not OOO0OO0OO00O00OO0 :#line:212
            OO00OOOO0OOOO0OO0 =subprocess .Popen (OOO0000OO0O0O0O0O ,stdout =subprocess .PIPE ,stderr =subprocess .STDOUT ,shell =False )#line:213
            OOO000OO00OOO0O00 =threading .Timer (OO00O00OOO00O0O00 .__O0OO000OO000OO000 ,O0000O00000O00O0O ,[OO00OOOO0OOOO0OO0 ])#line:214
            OOO0OO0OO00O00OO0 =True #line:215
            try :#line:216
                OOO000OO00OOO0O00 .start ()#line:217
                OO0O000O0OOO00O0O =OO00OOOO0OOOO0OO0 .stdout .read ().decode ('gbk')#line:218
            finally :#line:219
                OOO000OO00OOO0O00 .cancel ()#line:220
        if "DOWNGRADE"in OO0O000O0OOO00O0O :#line:221
            print ("Warning: A newer version of the app has been installed on Android device, SKIPPED\n",end ="",flush =True )#line:222
        return "Success"in OO0O000O0OOO00O0O or "DOWNGRADE"in OO0O000O0OOO00O0O #line:223
    def __O0O0O00OO0OO0O000 (OOOOO0O0O00OO00O0 ,OO0O00OOO000O00O0 ,OOOOO0000OOO0O000 ):#line:225
        ""#line:229
        O0O0OOO0000OOO0O0 =OOOOO0O0O00OO00O0 .__O0OOO0000OOOO0O00 ("\"pm dump %s | grep versionName=%s\""%(OO0O00OOO000O00O0 ,OOOOO0000OOO0O000 ),True )#line:230
        OOOO00OO000O00O0O =O0O0OOO0000OOO0O0 [1 ]#line:231
        if "versionName="in OOOO00OO000O00O0O :#line:233
            return True #line:234
        return False #line:235
    def __OO000O0O000OO0O0O (OO0O0OO0OO0O000O0 ,OOO0O0O00000O00OO ):#line:237
        ""#line:240
        OO0O0OO0OO0O000O0 .__O0OOO0000OOOO0O00 ("monkey -p %s -c android.intent.category.LAUNCHER 1"%OOO0O0O00000O00OO ,True )#line:241
    def __OO00OO0O000O00000 (O0OOO0000OO00000O ,O0OO0OO0O00OO000O ,O0000000O0O00O000 ):#line:243
        ""#line:247
        OO00O0O00000OOOOO =O0OOO0000OO00000O .__O0OO00OOOO0O00OOO ("\"monkey --ignore-crashes --ignore-native-crashes --ignore-timeouts --throttle 1000 --pct-pinchzoom 0 --pct-trackball 0 --pct-rotation 0 --pct-nav 0 --pct-majornav 0 --pct-syskeys 0 --pct-appswitch 0 --pct-flip 0 --pct-anyevent 0 -p %s %d 1>/dev/null 2>&1\""%(O0OO0OO0O00OO000O ,O0000000O0O00O000 ),True ,False )#line:248
        subprocess .Popen (OO00O0O00000OOOOO ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,shell =False )#line:249
    def __OO0000OO00OO00OOO (OOOO0O00O0OO00000 ):#line:252
        ""#line:257
        OO00OO00OO0OOO000 ="com.android.commands.monkey"#line:258
        OO00000000000O000 =OOOO0O00O0OO00000 .__O0OOO0000OOOO0O00 ("\"ps -A | grep com.android.commands.monkey\"",True )#line:259
        O0OO0OOO0O0000OO0 =OO00000000000O000 [1 ]#line:260
        if OO00OO00OO0OOO000 in O0OO0OOO0O0000OO0 :#line:261
            return True #line:262
        O00O0O0O0OOO00O00 =OOOO0O00O0OO00000 .__O0OOO0000OOOO0O00 ("\"ps | grep com.android.commands.monkey\"",True )#line:263
        OOOOO0OO00O0OO0OO =O00O0O0O0OOO00O00 [1 ]#line:264
        return OO00OO00OO0OOO000 in OOOOO0OO00O0OO0OO #line:265
    def __OOOO0O0000O0OOO0O (O0O0OO000O00O0O0O ):#line:267
        ""#line:269
        OOO0O00O000000OO0 ="com.android.commands.monkey"#line:270
        O0O0O00000O000000 =O0O0OO000O00O0O0O .__O0OOO0000OOOO0O00 ("\"ps -A | grep com.android.commands.monkey\"",True )#line:271
        if OOO0O00O000000OO0 in O0O0O00000O000000 [1 ]:#line:272
            OOOO0000O0OOOO0OO =O0O0O00000O000000 [1 ]#line:273
        else :#line:274
            OO0000O0000O0000O =O0O0OO000O00O0O0O .__O0OOO0000OOOO0O00 ("\"ps | grep com.android.commands.monkey\"",True )#line:275
            OOOO0000O0OOOO0OO =OO0000O0000O0000O [1 ]#line:276
        OOOO00OO0000O0OO0 =OOOO0000O0OOOO0OO .split ("\n")#line:277
        for O00O00OO000000OO0 in OOOO00OO0000O0OO0 :#line:278
            O00O000O0000O0OOO =O00O00OO000000OO0 .split (" ")#line:279
            OO000O0O00OOO000O =[]#line:280
            for O000OO00O00O00OO0 in O00O000O0000O0OOO :#line:281
                if len (O000OO00O00O00OO0 )>0 :#line:282
                    OO000O0O00OOO000O .append (O000OO00O00O00OO0 )#line:283
            if len (OO000O0O00OOO000O )>1 :#line:284
                O000000O0OOOO0OOO =OO000O0O00OOO000O [1 ]#line:285
                O0O0OO000O00O0O0O .__O0OOO0000OOOO0O00 ("\"kill %s\""%(O000000O0OOOO0OOO ),True )#line:286
    def __O0000O0OOOOOOOOOO (OO0O0OOO0OOOO0O00 ,O0O0OOOOOOOO0000O ):#line:288
        ""#line:291
        OO0O0OOO0OOOO0O00 .__O0OOO0000OOOO0O00 ("uninstall %s"%O0O0OOOOOOOO0000O )#line:292
    def __OOOO0000O0O0OOOOO (O0O00000OOOO00O00 ,O000OOO000O0000OO ):#line:294
        ""#line:297
        O00OO0OOO00OO00O0 ="pm disable-user %s"%O000OOO000O0000OO #line:298
        O0OOO00OOO0O0OO0O =O0O00000OOOO00O00 .__O0OOO0000OOOO0O00 (O00OO0OOO00OO00O0 ,True )#line:299
        O000O000000OO0OOO =O0OOO00OOO0O0OO0O [1 ]#line:300
        if "java.lang.SecurityException"in O000O000000OO0OOO :#line:301
            O0O00000OOOO00O00 .__O0OOO0000OOOO0O00 (O00OO0OOO00OO00O0 ,True ,True )#line:302
    def __OOO0OO0000O00OO0O (O0OO000O0000O0000 ,OO0O0O00OO00O0000 ):#line:304
        ""#line:307
        O0O0OO0O0O00O0OO0 ="pm enable %s"%OO0O0O00OO00O0000 #line:308
        O00OO0000OO0O0000 =O0OO000O0000O0000 .__O0OOO0000OOOO0O00 (O0O0OO0O0O00O0OO0 ,True )#line:309
        OO00O0OO0O0O00O00 =O00OO0000OO0O0000 [1 ]#line:310
        if "java.lang.SecurityException"in OO00O0OO0O0O00O00 :#line:311
            O0OO000O0000O0000 .__O0OOO0000OOOO0O00 (O0O0OO0O0O00O0OO0 ,True ,True )#line:312
    def __OOOOOOO0OO000O0OO (OO0OOOO00O000O0O0 ,O0000OO0OOO0OOOO0 ):#line:314
        ""#line:317
        OO0OOOO00O000O0O0 .__O0OOO0000OOOO0O00 ("am force-stop %s"%O0000OO0OOO0OOOO0 ,True )#line:318
    def __O0OOO000000000OOO (OOO0OO0O0OOOOO00O ,O00O0O00O0O00000O ,OOO000OOOOO00O000 ):#line:320
        ""#line:327
        O0O0OO00OO00000O0 =OOO0OO0O0OOOOO00O .__O0OOO0000OOOO0O00 ("wc -c /data/local/tmp/uid-%s.pcap"%(O00O0O00O0O00000O ),True ,True )#line:328
        # print(O0O0OO00OO00000O0)
        OO000OOO0O0OOO000 =O0O0OO00OO00000O0 [1 ]#line:329
        OO0O0O0O0O0O0O0OO =OO000OOO0O0OOO000 .split (" ")#line:330
        O00OOOOOO0OOO00OO =[]#line:331
        for OO0O00000O0O0OOO0 in OO0O0O0O0O0O0O0OO :#line:332
            if len (OO0O00000O0O0OOO0 )>0 :#line:333
                O00OOOOOO0OOO00OO .append (OO0O00000O0O0OOO0 )#line:334
        if len (O00OOOOOO0OOO00OO )>=2 :#line:335
            O000OOOOOOO00O000 =int (O00OOOOOO0OOO00OO [0 ])#line:336
            O000OOOOOOO00O000 /=1024 *1024 #line:337
            print(O000OOOOOOO00O000)
            return O000OOOOOOO00O000 >=OOO000OOOOO00O000 #line:338
        return False #line:339
    def __O0OO0O0OO0OO00O00 (O0OOOOOO000OOO0O0 ,OOOO00O0O00O0O0OO ):#line:341
        ""#line:347
        OOO00OOOOO0O000OO =O0OOOOOO000OOO0O0 .__O0OOO0000OOOO0O00 ("\"dumpsys package %s | grep appId=\""%(OOOO00O0O00O0O0OO ),True )#line:348
        OOO0O0O000OOOOOO0 =OOO00OOOOO0O000OO [1 ]#line:349
        OO0OO000OOOO00O0O ="appId="#line:350
        if OOO0O0O000OOOOOO0 .find (OO0OO000OOOO00O0O )!=-1 :#line:351
            O00OOOO0O00000O0O =OOO0O0O000OOOOOO0 [OOO0O0O000OOOOOO0 .index (OO0OO000OOOO00O0O )+len (OO0OO000OOOO00O0O ):]#line:352
            if O00OOOO0O00000O0O .find (" ")!=-1 :#line:353
                O00OOOO0O00000O0O =O00OOOO0O00000O0O [:O00OOOO0O00000O0O .index (" ")]#line:354
            if O00OOOO0O00000O0O .find ("\n")!=-1 :#line:355
                O00OOOO0O00000O0O =O00OOOO0O00000O0O [:O00OOOO0O00000O0O .index ("\n")]#line:356
            if O00OOOO0O00000O0O .find ("\r")!=-1 :#line:357
                O00OOOO0O00000O0O =O00OOOO0O00000O0O [:O00OOOO0O00000O0O .index ("\r")]#line:358
            return O00OOOO0O00000O0O #line:359
        else :#line:360
            return None #line:361
    def __O00000OOO000OO00O (OO00OO00O000OOO00 ,O00OOOO0OOO0O00OO ):#line:363
        ""#line:367
        O0O0OO00O0O00O0O0 ={"rx_bytes":0 ,"rx_packets":0 ,"tx_bytes":0 ,"tx_packets":0 ,"rx_tcp_bytes":0 ,"rx_tcp_packets":0 ,"rx_udp_bytes":0 ,"rx_udp_packets":0 ,"tx_tcp_bytes":0 ,"tx_tcp_packets":0 ,"tx_udp_bytes":0 ,"tx_udp_packets":0 ,}#line:381
        OOOOOO0O0000O0O00 =OO00OO00O000OOO00 .__O0OOO0000OOOO0O00 ("cat /proc/net/xt_qtaguid/stats",True )#line:382
        OOO0O0O0OOOO00O00 =OOOOOO0O0000O0O00 [1 ]#line:383
        OOOO0O0O00O00000O =OOO0O0O0OOOO00O00 .split ("\n")#line:384
        for OO0000000OOO0O00O in OOOO0O0O00O00000O :#line:385
            if OO0000000OOO0O00O .find (" %s "%(O00OOOO0OOO0O00OO ))!=-1 :#line:386
                OO00O0000O0OOO0OO =OO0000000OOO0O00O .split (" ")#line:387
                if len (OO00O0000O0OOO0OO )==21 and OO00O0000O0OOO0OO [3 ]==O00OOOO0OOO0O00OO :#line:388
                    O0O0OO00O0O00O0O0 ["rx_bytes"]+=int (OO00O0000O0OOO0OO [5 ])#line:389
                    O0O0OO00O0O00O0O0 ["rx_packets"]+=int (OO00O0000O0OOO0OO [6 ])#line:390
                    O0O0OO00O0O00O0O0 ["tx_bytes"]+=int (OO00O0000O0OOO0OO [7 ])#line:391
                    O0O0OO00O0O00O0O0 ["tx_packets"]+=int (OO00O0000O0OOO0OO [8 ])#line:392
                    O0O0OO00O0O00O0O0 ["rx_tcp_bytes"]+=int (OO00O0000O0OOO0OO [9 ])#line:393
                    O0O0OO00O0O00O0O0 ["rx_tcp_packets"]+=int (OO00O0000O0OOO0OO [10 ])#line:394
                    O0O0OO00O0O00O0O0 ["rx_udp_bytes"]+=int (OO00O0000O0OOO0OO [11 ])#line:395
                    O0O0OO00O0O00O0O0 ["rx_udp_packets"]+=int (OO00O0000O0OOO0OO [12 ])#line:396
                    O0O0OO00O0O00O0O0 ["tx_tcp_bytes"]+=int (OO00O0000O0OOO0OO [15 ])#line:397
                    O0O0OO00O0O00O0O0 ["tx_tcp_packets"]+=int (OO00O0000O0OOO0OO [16 ])#line:398
                    O0O0OO00O0O00O0O0 ["tx_udp_bytes"]+=int (OO00O0000O0OOO0OO [17 ])#line:399
                    O0O0OO00O0O00O0O0 ["tx_udp_packets"]+=int (OO00O0000O0OOO0OO [18 ])#line:400
        return O0O0OO00O0O00O0O0 #line:401
    def __O0OO0O000O000000O (OO0000OO00O0OOOOO ):#line:403
        ""#line:405
        OO0000O0OOOO0O000 =OO0000OO00O0OOOOO .__O0OOO0000OOOO0O00 ("/data/local/tmp/tcpdump -h",True ,True )#line:406
        O0OO0O000OOOO00OO =OO0000O0OOOO0O000 [1 ]#line:407
        if "Usage: tcpdump"in O0OO0O000OOOO00OO :#line:408
            return True #line:409
        return False #line:410
    def __O000O0O00OOO0OO00 (O0OO00OOOO0OO000O ):#line:412
        ""#line:414
        O0OO00OOOO0OO000O .__O0OOO0000OOOO0O00 ("mkdir /data/local/tmp",True ,True )#line:415
        O0OO00OOOO0OO000O .__O0OOO0000OOOO0O00 ("chmod -R 777 /data/local/tmp",True ,True )#line:416
        O0OO00OOOO0OO000O .__O0OOO0000OOOO0O00 ("push \"%s/tcpdump\" /data/local/tmp"%(O0OO00OOOO0OO000O .__OO0OO0000O0OO00OO ))#line:417
        O0OO00OOOO0OO000O .__O0OOO0000OOOO0O00 ("chmod 777 /data/local/tmp/tcpdump",True ,True )#line:418
    def __OO00OO00O000OOOOO (OOOO000O0O0O00000 ):#line:420
        ""#line:422
        OOOO000O0O0O00000 .__O0OOO0000OOOO0O00 ("reboot")#line:423
    def __OOO0OO0OO00O00O00 (OO00OOOOOOO00O000 ,O0O0000OOOOO0OO0O ,O000O0OO00OOOO000 =False ):#line:425
        ""#line:431
        if not OO00OOOOOOO00O000 .__O0OO0O000O000000O ():#line:432
            OO00OOOOOOO00O000 .__O000O0O00OOO0OO00 ()#line:433
        if not O000O0OO00OOOO000 :#line:434
            OO00OOOOOOO00O000 .__O0OOO0000OOOO0O00 ("iptables -A OUTPUT -m owner --uid-owner %s -j CONNMARK --set-mark %s"%(O0O0000OOOOO0OO0O ,O0O0000OOOOO0OO0O ),True ,True )#line:435
            OO00OOOOOOO00O000 .__O0OOO0000OOOO0O00 ("iptables -A INPUT -m connmark --mark %s ! -s 127.0.0.1 ! -d 127.0.0.1 -j NFLOG --nflog-group %s"%(O0O0000OOOOO0OO0O ,O0O0000OOOOO0OO0O ),True ,True )#line:436
            OO00OOOOOOO00O000 .__O0OOO0000OOOO0O00 ("iptables -A OUTPUT -m connmark --mark %s ! -s 127.0.0.1 ! -d 127.0.0.1 -j NFLOG --nflog-group %s"%(O0O0000OOOOO0OO0O ,O0O0000OOOOO0OO0O ),True ,True )#line:437
            OO00OOOOOOO00O000 .__O0OOO0000OOOO0O00 ("ip6tables -A OUTPUT -m owner --uid-owner %s -j CONNMARK --set-mark %s"%(O0O0000OOOOO0OO0O ,O0O0000OOOOO0OO0O ),True ,True )#line:438
            OO00OOOOOOO00O000 .__O0OOO0000OOOO0O00 ("ip6tables -A INPUT -m connmark --mark %s ! -s ::1 ! -d ::1 -j NFLOG --nflog-group %s"%(O0O0000OOOOO0OO0O ,O0O0000OOOOO0OO0O ),True ,True )#line:439
            OO00OOOOOOO00O000 .__O0OOO0000OOOO0O00 ("ip6tables -A OUTPUT -m connmark --mark %s ! -s ::1 ! -d ::1 -j NFLOG --nflog-group %s"%(O0O0000OOOOO0OO0O ,O0O0000OOOOO0OO0O ),True ,True )#line:440
        return subprocess .Popen (OO00OOOOOOO00O000 .__O0OO00OOOO0O00OOO ("/data/local/tmp/tcpdump -i nflog:%s -w /data/local/tmp/uid-%s.pcap"%(O0O0000OOOOO0OO0O ,O0O0000OOOOO0OO0O ),True ,True ),stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,shell =False )#line:442
    def __OOOO0OOOOO000O0OO (O00OOO0000O00O000 ,O000O0000O0OO0O00 ,OO00O0O0O0O00OO0O ):#line:444
        ""#line:450
        O00OO0O0O00OOOOOO =O00OOO0000O00O000 .__O0OOO0000OOOO0O00 ("pkill -2 tcpdump",True ,True )#line:451
        O000000O000OO00O0 =O00OO0O0O00OOOOOO [1 ]#line:452
        if "Unknown option 2"in O000000O000OO00O0 :#line:453
            O00OOO0000O00O000 .__O0OOO0000OOOO0O00 ("pkill tcpdump",True ,True )#line:454
        O000O0000O0OO0O00 .wait ()#line:455
        return "/data/local/tmp/uid-%s.pcap"%(OO00O0O0O0O00OO0O )#line:456
    def __O0O000OO00O0OOO00 (O000O00000O0O00O0 ,OO0OOO00O0O000000 ,OO00OOO0000000OOO ):#line:458
        ""#line:464
        OOOO0OOO000000000 ="%s/%s-%s.pcap"%(O000O00000O0O00O0 .__O00OOO0OOOO0OOO0O ,OO00OOO0000000OOO ,O000O00000O0O00O0 .__O000O0000000O000O )#line:465
        O000O00000O0O00O0 .__O0OOO0000OOOO0O00 ("chmod 777 %s"%(OO0OOO00O0O000000 ),True ,True )#line:467
        O000O00000O0O00O0 .__O0OOO0000OOOO0O00 ("pull %s %s"%(OO0OOO00O0O000000 ,OOOO0OOO000000000 ))#line:468
        O000O00000O0O00O0 .__O0OOO0000OOOO0O00 ("rm %s"%(OO0OOO00O0O000000 ),True ,True )#line:469
        return OOOO0OOO000000000 #line:470
    def __OOOOO00OO00OOOOOO (OO00OOO00OO000O0O ,O0O0OOOO0000O00OO ):#line:472
        ""#line:475
        OOOO0O00OOOO00OOO =subprocess .getstatusoutput ("\"%s/pcapfix\" \"%s\" -o \"%s_\""%(OO00OOO00OO000O0O .__OO0OO0000O0OO00OO ,O0O0OOOO0000O00OO ,O0O0OOOO0000O00OO ))#line:476
        OOOO0O0O00O0O0O0O =OOOO0O00OOOO00OOO [1 ]#line:477
        if OOOO0O0O00O0O0O0O .find ("fixed!")!=-1 :#line:478
            os .remove (O0O0OOOO0000O00OO )#line:479
            os .rename ("%s_"%O0O0OOOO0000O00OO ,O0O0OOOO0000O00OO )#line:480
    def __O00OO0OO00OO00O0O (O0000OO0OOO0OOO0O ,OOO000000O0OO000O ,OOOO0O0O00O00O0OO ,OO00O0OOOOO000OOO ,O0O000O00O00O0OO0 ):#line:482
        ""#line:490
        OO00O0O0O000O0OOO ={}#line:491
        OO00O0O0O000O0OOO ["PackageName"]=OOOO0O0O00O00O0OO #line:492
        for O0O0000OOOO0OO0OO in ["IPv4","IPv6"]:#line:493
            for OOOO0O0000O0OO0OO in ["rx_packets","rx_bytes","tx_bytes","tx_packets","rx_tcp_bytes","rx_tcp_packets","rx_udp_bytes","rx_udp_packets","tx_tcp_bytes","tx_tcp_packets","tx_udp_bytes","tx_udp_packets"]:#line:496
                OO00O0O0O000O0OOO ["%s-%s-%s"%(O0000OO0OOO0OOO0O .__O000O0000000O000O ,O0O0000OOOO0OO0OO ,OOOO0O0000O0OO0OO )]=0 #line:497
        try :#line:498
            O0O0O00O000OOO0O0 =os .path .getsize (OOO000000O0OO000O )#line:499
            O0O0O00O000OOO0O0 /=1024 *1024 #line:500
            if O0O0O00O000OOO0O0 <OO00O0OOOOO000OOO :#line:501
                raise Exception ("Size of pcap (%.2f) is smaller than threshold (%.2f)"%(O0O0O00O000OOO0O0 ,OO00O0OOOOO000OOO ))#line:502
            with open (OOO000000O0OO000O ,"rb")as OOOO0O0000O0OO0OO :#line:503
                O0000O00O0O0OO0O0 =dpkt .pcap .Reader (OOOO0O0000O0OO0OO )#line:504
                for OOOOOOO0OO00OO00O ,OOO0O0O000OO00OO0 in O0000O00O0O0OO0O0 :#line:505
                    try :#line:506
                        if OOO0O0O000OO00OO0 [0 ]!=2 and OOO0O0O000OO00OO0 [0 ]!=10 :#line:507
                            continue #line:508
                        OOO00000OOO00O00O =len (OOO0O0O000OO00OO0 )#line:509
                        O000O00000O00OOOO =4 #line:510
                        while True :#line:511
                            O000000OO000O000O =OOO0O0O000OO00OO0 [O000O00000O00OOOO ]+(OOO0O0O000OO00OO0 [O000O00000O00OOOO +1 ]<<8 )#line:512
                            O000000OO000O000O =math .ceil (O000000OO000O000O /4 )*4 #line:513
                            if O000O00000O00OOOO +O000000OO000O000O >=OOO00000OOO00O00O or O000000OO000O000O ==0 :#line:514
                                break #line:515
                            O000O00000O00OOOO +=O000000OO000O000O #line:516
                        OO00OO0O0O00000O0 =O000O00000O00OOOO +4 #line:517
                        OOOOOO0OOOOOOOO00 =OOO0O0O000OO00OO0 [10 ]#line:518
                        if OOOOOO0OOOOOOOO00 ==3 :#line:519
                            O00OOO00O00000000 ="tx"#line:520
                        elif OOOOOO0OOOOOOOO00 ==1 :#line:521
                            O00OOO00O00000000 ="rx"#line:522
                        else :#line:523
                            continue #line:524
                        OOO000OO0OOO00O00 =OOO0O0O000OO00OO0 [0 ]#line:525
                        if OOO000OO0OOO00O00 ==2 :#line:526
                            O0O0000OOOO0OO0OO ="IPv4"#line:527
                            OO0O000O00O00O0OO =OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +9 ]#line:528
                            if (OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +12 ]==127 and OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +13 ]==0 and OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +14 ]==0 and OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +15 ]==1 )or (OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +16 ]==127 and OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +17 ]==0 and OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +18 ]==0 and OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +19 ]==1 ):#line:529
                                continue #line:530
                            OOO00000OOO00O00O =(OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +2 ]<<8 )+OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +3 ]#line:531
                        elif OOO000OO0OOO00O00 ==10 :#line:532
                            O0O0000OOOO0OO0OO ="IPv6"#line:533
                            OO0O000O00O00O0OO =OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +6 ]#line:534
                            OOOO00O0OO0000O00 =OO00OO0O0O00000O0 +8 #line:535
                            O0000O0O00O000O00 =True #line:536
                            for O00000O00O0O0O0OO in range (16 ):#line:537
                                if (O00000O00O0O0O0OO <15 and OOO0O0O000OO00OO0 [OOOO00O0OO0000O00 +O00000O00O0O0O0OO ]!=0 )or (OOO0O0O000OO00OO0 [OOOO00O0OO0000O00 +O00000O00O0O0O0OO ]!=1 ):#line:538
                                    O0000O0O00O000O00 =False #line:539
                                    break #line:540
                            if O0000O0O00O000O00 :#line:541
                                continue #line:542
                            OO0O00O0O000OO00O =OO00OO0O0O00000O0 +24 #line:543
                            OO000O0OOO0O0O00O =True #line:544
                            for O00000O00O0O0O0OO in range (16 ):#line:545
                                if (O00000O00O0O0O0OO <15 and OOO0O0O000OO00OO0 [OO0O00O0O000OO00O +O00000O00O0O0O0OO ]!=0 )or (OOO0O0O000OO00OO0 [OO0O00O0O000OO00O +O00000O00O0O0O0OO ]!=1 ):#line:546
                                    OO000O0OOO0O0O00O =False #line:547
                                    break #line:548
                            if OO000O0OOO0O0O00O :#line:549
                                continue #line:550
                            OOO00000OOO00O00O =(OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +4 ]<<8 )+OOO0O0O000OO00OO0 [OO00OO0O0O00000O0 +5 ]#line:551
                        else :#line:552
                            continue #line:553
                        if OO0O000O00O00O0OO ==6 :#line:554
                            O000OO00OOO000OO0 ="tcp"#line:555
                        elif OO0O000O00O00O0OO ==17 :#line:556
                            O000OO00OOO000OO0 ="udp"#line:557
                        else :#line:558
                            continue #line:559
                    except :#line:560
                        continue #line:561
                    OO00O0O0O000O0OOO ["%s-%s-%s_packets"%(O0000OO0OOO0OOO0O .__O000O0000000O000O ,O0O0000OOOO0OO0OO ,O00OOO00O00000000 )]+=1 #line:562
                    OO00O0O0O000O0OOO ["%s-%s-%s_bytes"%(O0000OO0OOO0OOO0O .__O000O0000000O000O ,O0O0000OOOO0OO0OO ,O00OOO00O00000000 )]+=OOO00000OOO00O00O #line:563
                    OO00O0O0O000O0OOO ["%s-%s-%s_%s_packets"%(O0000OO0OOO0OOO0O .__O000O0000000O000O ,O0O0000OOOO0OO0OO ,O00OOO00O00000000 ,O000OO00OOO000OO0 )]+=1 #line:564
                    OO00O0O0O000O0OOO ["%s-%s-%s_%s_bytes"%(O0000OO0OOO0OOO0O .__O000O0000000O000O ,O0O0000OOOO0OO0OO ,O00OOO00O00000000 ,O000OO00OOO000OO0 )]+=OOO00000OOO00O00O #line:565
            OO000O00OOOO000O0 =OO00O0O0O000O0OOO ["%s-IPv4-rx_bytes"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]+OO00O0O0O000O0OOO ["%s-IPv4-tx_bytes"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]#line:566
            O0OO00OOOO00000O0 =OO00O0O0O000O0OOO ["%s-IPv6-rx_bytes"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]+OO00O0O0O000O0OOO ["%s-IPv6-tx_bytes"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]#line:567
            O00O000O0O00OO0OO =OO00O0O0O000O0OOO ["%s-IPv4-rx_packets"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]+OO00O0O0O000O0OOO ["%s-IPv4-rx_packets"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]#line:568
            O00O000000O0O00OO =OO00O0O0O000O0OOO ["%s-IPv6-rx_packets"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]+OO00O0O0O000O0OOO ["%s-IPv6-rx_packets"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]#line:569
            if O0O000O00O00O0OO0 >1 and O0OO00OOOO00000O0 ==0 :#line:570
                raise Exception ("Bytes of IPv6 is zero")#line:571
            OO00O0O0O000O0OOO ["%s-IPv6Rate-bytes"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]="%.2f%%"%(O0OO00OOOO00000O0 *100.0 /(O0OO00OOOO00000O0 +OO000O00OOOO000O0 ))#line:572
            OO00O0O0O000O0OOO ["%s-IPv6Rate-packets"%(O0000OO0OOO0OOO0O .__O000O0000000O000O )]="%.2f%%"%(O00O000000O0O00OO *100.0 /(O00O000000O0O00OO +O00O000O0O00OO0OO ))#line:573
            with O0000OO0OOO0OOO0O .__OO00O00O00000OO00 :#line:574
                if OOOO0O0O00O00O0OO in O0000OO0OOO0OOO0O .__O0O00OO000OO00O0O ["PackageName"].tolist ():#line:575
                    O0O0OO0000OOOO000 =O0000OO0OOO0OOO0O .__O0O00OO000OO00O0O [O0000OO0OOO0OOO0O .__O0O00OO000OO00O0O ["PackageName"]==OOOO0O0O00O00O0OO ].index .tolist ()[0 ]#line:576
                    for OOO0OOOOOOOOO00O0 in OO00O0O0O000O0OOO :#line:577
                        O0000OO0OOO0OOO0O .__O0O00OO000OO00O0O [OOO0OOOOOOOOO00O0 ][O0O0OO0000OOOO000 ]=OO00O0O0O000O0OOO [OOO0OOOOOOOOO00O0 ]#line:578
                else :#line:579
                    O0000OO0OOO0OOO0O .__O0O00OO000OO00O0O =O0000OO0OOO0OOO0O .__O0O00OO000OO00O0O .append (OO00O0O0O000O0OOO ,ignore_index =True )#line:580
                O0000OO0OOO0OOO0O .__O0O00OO000OO00O0O .to_csv ("./ATR_result.csv",index =False ,encoding ="gb2312")#line:581
                print ("Info: Pcap of [%s] calculated successfully\n"%OOOO0O0O00O00O0OO ,end ='',flush =True )#line:582
        except Exception as O0O0O0OOO00OO0000 :#line:584
            if O0000OO0OOO0OOO0O .__O00O0O0O0OO000OOO :#line:585
                print (traceback .format_exc ())#line:586
            print ("Warning: Pcap of [%s] calculated faild for [%s]\n"%(OOOO0O0O00O00O0OO ,str (O0O0O0OOO00OO0000 )),end ="",flush =True )#line:587
            return False #line:588
        return True #line:589
    def __O000OOO0O0000OOO0 (O00OO0OOOOO0O0O00 ,OOO0000OO0OO0OOOO ,O0O00OOO0O0O0O000 ):#line:591
        ""#line:592
        OOO0000OO0OO0OOOO =ctypes .c_long (OOO0000OO0OO0OOOO )#line:593
        if not inspect .isclass (O0O00OOO0O0O0O000 ):#line:594
            O0O00OOO0O0O0O000 =type (O0O00OOO0O0O0O000 )#line:595
        O000OOO00O0OOOOO0 =ctypes .pythonapi .PyThreadState_SetAsyncExc (OOO0000OO0OO0OOOO ,ctypes .py_object (O0O00OOO0O0O0O000 ))#line:596
        if O000OOO00O0OOOOO0 ==0 :#line:597
            raise ValueError ("invalid thread id")#line:598
        elif O000OOO00O0OOOOO0 !=1 :#line:599
            ctypes .pythonapi .PyThreadState_SetAsyncExc (OOO0000OO0OO0OOOO ,None )#line:600
            raise SystemError ("PyThreadState_SetAsyncExc failed")#line:601
    def __OO0OOOO0OO0000O0O (OO000OOO0000O000O ,OO0O0000O00OO00OO ):#line:603
        OO000OOO0000O000O .__O000OOO0O0000OOO0 (OO0O0000O00OO00OO .ident ,SystemExit )#line:604
    def __OO00OOO00OO0O00OO (OOOOO0O00O00O0OOO ,OOO0O0OO0OO0O0000 ,OO000000OO0O0OOOO ,O0O0O0OOO000O000O ,O0OO0O0000OOOOO0O ):#line:606
        ""#line:614
        return OOOOO0O00O00O0OOO .__O00OO0OO00OO00O0O (OOO0O0OO0OO0O0000 ,OO000000OO0O0OOOO ,O0O0O0OOO000O000O ,O0OO0O0000OOOOO0O )#line:616
    def just_uninstall (OO0O0OO00OO0O0O00 ,O0OOO0O00O000O00O ):#line:618
        ""#line:620
        OO0O0OO00OO0O0O00 .__O0O0O0O000000O0O0 ()#line:621
        print ("Uninstall applications only!")#line:622
        O0O0000O000OOO000 =OO0O0OO00OO0O0O00 .__OOOOO00OOOO0O00O0 ()#line:623
        if O0O0000O000OOO000 [1 ]:#line:624
            O0OO00OO0000OO000 =len (O0OOO0O00O000O00O )#line:625
            for OOOO00OO0OO00OOOO ,OOO0OOOOO000OOO00 in enumerate (O0OOO0O00O000O00O ):#line:626
                print ("[%d / %d] %s ..."%(OOOO00OO0OO00OOOO +1 ,O0OO00OO0000OO000 ,OOO0OOOOO000OOO00 ),end ='',flush =True )#line:627
                if OO0O0OO00OO0O0O00 .__O0O0O00OO0OO0O000 (OOO0OOOOO000OOO00 ,""):#line:628
                    OO0O0OO00OO0O0O00 .__O0000O0OOOOOOOOOO (OOO0OOOOO000OOO00 )#line:629
                    print ("Successfully",flush =True )#line:630
                else :#line:631
                    print ("Failed",flush =True )#line:632
            OO0O0OO00OO0O0O00 .__O0O0O0O000000O0O0 ()#line:633
        else :#line:634
            print ("Error: %s"%(O0O0000O000OOO000 [0 ]))#line:635
    def go (O0OO00000OOO0O0OO ):#line:637
        print("是自带的module")
        ""#line:640
        # 强制终止所有正在运行的 adb.exe 进程
        O0OO00000OOO0O0OO .__O0O0O0O000000O0O0 ()#line:641
        OO0O0O0OO0OO00OO0 =O0OO00000OOO0O0OO .__OOOOO00OOOO0O00O0 ()#line:642
        if OO0O0O0OO0OO00OO0 [1 ]:#line:643
            if not O0OO00000OOO0O0OO .__OO0OO0O00O000OO00 :#line:644
                pass
                # # 重启
                # print ("You MUST reboot Android device first!\nPress Enter to reboot.")#line:645
                # input ()#line:646
                # O0OO00000OOO0O0OO .__OO00OO00O000OOOOO ()#line:647
                # while True :#line:648
                #     print ("Make Sure the Android device is booted, and ADB connection is OK. Press Enter and go on.")#line:649
                #     input ()#line:650
                #     if O0OO00000OOO0O0OO .__OOOOO00OOOO0O00O0 ()[1 ]:#line:651
                #         break #line:652
            else :#line:656
                print ("Install applications only!")#line:657
            O0OO0O000O0OOOO0O =len (O0OO00000OOO0O0OO .__OO00O0O0000OOOO0O )#line:658
            for O0OO000OO0O00O00O ,OOO00000OOO00OOO0 in enumerate (O0OO00000OOO0O0OO .__OO00O0O0000OOOO0O ):#line:659
                OO0OO00000O0000OO =OOO00000OOO00OOO0 [0 ]#line:660
                OOO0O0OO00OOOO0OO =O0OO00000OOO0O0OO .__O0O00OO00OO0OOOO0 if OOO00000OOO00OOO0 [1 ]==0 else OOO00000OOO00OOO0 [1 ]#line:661
                O00OOOOOOOO000O00 =O0OO00000OOO0O0OO .__O00O000OO0O0O00OO if OOO00000OOO00OOO0 [2 ]==0 else OOO00000OOO00OOO0 [2 ]#line:662
                O0O000O00O0OOOO00 =O0OO00000OOO0O0OO .__O0000O0OO0OO00OO0 if OOO00000OOO00OOO0 [3 ]==0 else OOO00000OOO00OOO0 [3 ]#line:663
                OOO0O0O00O0O00O00 =OOO00000OOO00OOO0 [4 ]#line:664
                print ("[%d / %d] %s"%(O0OO000OO0O00O00O +1 ,O0OO0O000O0OOOO0O ,OO0OO00000O0000OO ),flush =True )#line:665
                OO0000OO00OOO0OO0 ="%s/%s"%(O0OO00000OOO0O0OO .__O0O00OO0OO000O00O ,OO0OO00000O0000OO )#line:666
                O00000O0O0O00O00O =O0OO00000OOO0O0OO .__OO0O000OOO0000OO0 (OO0000OO00OOO0OO0 )#line:667
                if not O00000O0O0O00O00O :#line:668
                    print ("Warning: cannot get info of APK [%s], SKIPPED"%(OO0OO00000O0000OO ),flush =True )#line:669
                else :#line:670
                    if not O0OO00000OOO0O0OO .__OO0OO0O00O000OO00 and O00000O0O0O00O00O in O0OO00000OOO0O0OO .__O0O00OO000OO00O0O ["PackageName"].tolist ()and not np .isnan (O0OO00000OOO0O0OO .__O0O00OO000OO00O0O [O0OO00000OOO0O0OO .__O0O00OO000OO00O0O ["PackageName"]==O00000O0O0O00O00O ]["%s-IPv4-rx_packets"%(O0OO00000OOO0O0OO .__O000O0000000O000O )].tolist ()[0 ]):#line:672
                        print ("Warning: [%s] has been tested, SKIPPED"%(O00000O0O0O00O00O ),flush =True )#line:673
                    else :#line:674
                        OOOO0OOOO000O00OO =O0OO00000OOO0O0OO .__O0O0O00OO0OO0O000 (O00000O0O0O00O00O ,OOO0O0O00O0O00O00 )#line:675
                        if OOOO0OOOO000O00OO :#line:676
                            print ("Info: Already installed, skip installation\n",end ='',flush =True )#line:677
                        else :#line:678
                            print ("Installing...",end ='',flush =True )#line:679
                            O00OOO000O0OO0000 =O0OO00000OOO0O0OO .__OOO00OO000OOO0O00 (OO0000OO00OOO0OO0 )#line:680
                            if not O00OOO000O0OO0000 :#line:681
                                print ("Failed\n",end ='',flush =True )#line:682
                                continue #line:683
                            print ("OK\n",end ='',flush =True )#line:684
                        if not O0OO00000OOO0O0OO .__OO0OO0O00O000OO00 :#line:685
                            print ("Enabling app...",end ='',flush =True )#line:686
                            O0OO00000OOO0O0OO .__OOO0OO0000O00OO0O (O00000O0O0O00O00O )#line:687
                            print ("OK\n",end ='',flush =True )#line:688
                            OO0OO000O0O0O00OO =2 #line:689
                            while OO0OO000O0O0O00OO >0 :#line:690
                                # 获取uid
                                O000O000OOOOO000O =O0OO00000OOO0O0OO .__O0OO0O0OO0OO00O00 (O00000O0O0O00O00O )#line:691
                                # 启动程序
                                print ("Start app...",end ='',flush =True )#line:693
                                O0OO00000OOO0O0OO .__OO000O0O000OO0O0O (O00000O0O0O00O00O )#line:694
                                print ("sleep30",end ='',flush =True )#line:693
                                time .sleep (30 )#line:700
                                # 设置 iptables 规则并启动 tcpdump
                                OOOO000000000000O =O0OO00000OOO0O0OO .__OOO0OO0OO00O00O00 (O000O000OOOOO000O ,OO0OO000O0O0O00OO <2 )#line:692
                                print ("OK\n",end ='',flush =True )#line:695
                                # 人工模式
                                if O0OO00000OOO0O0OO .__OOO00OOOO0OOOOOOO :#line:696
                                    print ("You can operate on the application for now!\nPress Enter to end test of this app!\n",end ='',flush =True )#line:697
                                    O0OO00000OOO0O0OO .__OOO00OO00OO0OO0O0 =False #line:698
                                    while not O0OO00000OOO0O0OO .__OOO00OO00OO0OO0O0 :#line:699
                                        time .sleep (1 )#line:700
                                        if O0OO00000OOO0O0OO .__O0OOO000000000OOO (O000O000OOOOO000O ,O00OOOOOOOO000O00 ):#line:701
                                            print ("Filesize of pcap exceeds the threshold (%.2f)!\n"%(O00OOOOOOOO000O00 ),end ='',flush =True )#line:702
                                            break #line:703
                                # monkey模式
                                else :#line:704
                                    print ("You can operate on the application for %d seconds now!\n"%(O0OO00000OOO0O0OO .__OOOOO00O000O0OOOO ),end ='',flush =True )#line:705
                                    time .sleep (O0OO00000OOO0O0OO .__OOOOO00O000O0OOOO )#line:706
                                    print ("Monkey...\n",end ='',flush =True )#line:707
                                    O0OO00000OOO0O0OO .__OO00OO0O000O00000 (O00000O0O0O00O00O ,O0O000O00O0OOOO00 )#line:708
                                    while True :#line:709
                                        time .sleep (1 )#line:710
                                        if O0OO00000OOO0O0OO .__O0OOO000000000OOO (O000O000OOOOO000O ,O00OOOOOOOO000O00 ):#line:711
                                            O0OO00000OOO0O0OO .__OOOO0O0000O0OOO0O ()#line:712
                                            print ("Filesize of pcap exceeds the threshold (%.2f)!\n"%(O00OOOOOOOO000O00 ),end ='',flush =True )#line:713
                                            break #line:714
                                        else :#line:715
                                            if not O0OO00000OOO0O0OO .__OO0000OO00OO00OOO ():#line:716
                                                break #line:717
                                # 停止 tcpdump
                                OOO00OO0OOO0OOOO0 =O0OO00000OOO0O0OO .__OOOO0OOOOO000O0OO (OOOO000000000000O ,O000O000OOOOO000O )#line:718
                                # # 停止应用
                                # print ("Force stopping app...",end ='',flush =True )#line:722
                                # O0OO00000OOO0O0OO .__OOOOOOO0OO000O0OO (O00000O0O0O00O00O )#line:723
                                # print ("OK\n",end ='',flush =True )#line:724
                                # 获取 pcap到本地
                                print ("Pulling PCAP...",end ='',flush =True )#line:725
                                O0O0OO0000O0000O0 =O0OO00000OOO0O0OO .__O0O000OO00O0OOO00 (OOO00OO0OOO0OOOO0 ,O00000O0O0O00O00O )#line:726
                                print ("OK\n",end ='',flush =True )#line:727
                                # 计算 pcap
                                print ("Calculating PCAP...\n",end ='',flush =True )#line:731
                                if O0OO00000OOO0O0OO .__OO00OOO00OO0O00OO (O0O0OO0000O0000O0 ,O00000O0O0O00O00O ,OOO0O0OO00OOOO0OO ,OO0OO000O0O0O00OO ):#line:732
                                    break #line:733
                                OO0OO000O0O0O00OO -=1 #line:734
                                if OO0OO000O0O0O00OO >0 :#line:735
                                    print ("Retry\n",end ='',flush =True )#line:736
                        if O0OO00000OOO0O0OO .__O0OOO0OO00OOOOO0O :#line:737
                            print ("Disabling app...",end ='',flush =True )#line:738
                            O0OO00000OOO0O0OO .__OOOO0000O0O0OOOOO (O00000O0O0O00O00O )#line:739
                        else:
                            print ("dont Disabling app...",end ='',flush =True )
                        print ("OK\n",end ='',flush =True )#line:740
            O0OO00000OOO0O0OO .__O0O0O0O000000O0O0 ()#line:741
        else :#line:742
            print ("Error: %s"%(OO0O0O0OO0OO00OO0 [0 ]))#line:743
class Downloader :#line:745
    def __init__ (O00O0OO00OOOOO000 ,O0O000O0OOOOOO000 ,O00OO00OO0OO0OO00 ):#line:746
        warnings .filterwarnings ("ignore")#line:747
        O00O0OO00OOOOO000 .__O000OO00OO0O0OOO0 =O0O000O0OOOOOO000 #line:748
        O00O0OO00OOOOO000 .__O00O000000000000O =O00OO00OO0OO0OO00 #line:749
        O00O0OO00OOOOO000 .__OO0000OOOOO00O0O0 =threading .Lock ()#line:750
        O00O0OO00OOOOO000 .__OOOO0O0O0O0O00OOO =len (O0O000O0OOOOOO000 )#line:751
        O00O0OO00OOOOO000 .__O0OOOOOOO0OOOO00O =1 #line:752
        O00O0OO00OOOOO000 .__OOOOOO0O0000000OO =[]#line:753
    def __O0OOOOOOOO000OOO0 (O0O00OO0O000OOO0O ,O0OO00OO0OOOOO00O ):#line:755
        ""#line:757
        OO0OOO0OO00O0O0OO ="%s.apk"%(O0OO00OO0OOOOO00O [0 ])#line:758
        OOOOO00OOO0OO00OO =O0OO00OO0OOOOO00O [1 ]#line:759
        O0OOO00O0O0O0O000 =O0OO00OO0OOOOO00O [2 ]#line:760
        OO00O0000O000OOOO =O0OO00OO0OOOOO00O [3 ]#line:761
        O00O00OOO0OOO00OO =O0OO00OO0OOOOO00O [4 ]#line:762
        O0OO0O000O00OO00O =O0OO00OO0OOOOO00O [5 ]#line:763
        O00O000O0O00O0000 ="%s/%s"%(O0O00OO0O000OOO0O .__O00O000000000000O ,OO0OOO0OO00O0O0OO )#line:764
        if not os .path .exists (O00O000O0O00O0000 ):#line:765
            OOOO0OO0OO00OO000 =3 #line:766
            while OOOO0OO0OO00OO000 >0 :#line:767
                try :#line:768
                    wget .download (OOOOO00OOO0OO00OO ,out =O00O000O0O00O0000 ,bar =None )#line:769
                    O0O00OO0O000OOO0O .__OOOOOO0O0000000OO .append ([OO0OOO0OO00O0O0OO ,O0OOO00O0O0O0O000 ,OO00O0000O000OOOO ,O00O00OOO0OOO00OO ,O0OO0O000O00OO00O ])#line:770
                    break #line:771
                except Exception as OOOO000OOO0000000 :#line:772
                    OOOO0OO0OO00OO000 -=1 #line:773
            if OOOO0OO0OO00OO000 >0 :#line:774
                with O0O00OO0O000OOO0O .__OO0000OOOOO00O0O0 :#line:775
                    print ("[%5d] Succeeded - %s"%(O0O00OO0O000OOO0O .__O0OOOOOOO0OOOO00O ,O0OO00OO0OOOOO00O [0 ]),flush =True )#line:776
                    O0O00OO0O000OOO0O .__O0OOOOOOO0OOOO00O +=1 #line:777
            else :#line:778
                with O0O00OO0O000OOO0O .__OO0000OOOOO00O0O0 :#line:779
                    print ("[%5d]   Failed  - %s"%(O0O00OO0O000OOO0O .__O0OOOOOOO0OOOO00O ,O0OO00OO0OOOOO00O [0 ]),flush =True )#line:780
                    O0O00OO0O000OOO0O .__O0OOOOOOO0OOOO00O +=1 #line:781
        else :#line:782
            with O0O00OO0O000OOO0O .__OO0000OOOOO00O0O0 :#line:783
                print ("[%5d]  Skipped  - %s"%(O0O00OO0O000OOO0O .__O0OOOOOOO0OOOO00O ,O0OO00OO0OOOOO00O [0 ]),flush =True )#line:784
                O0O00OO0O000OOO0O .__O0OOOOOOO0OOOO00O +=1 #line:785
                O0O00OO0O000OOO0O .__OOOOOO0O0000000OO .append ([OO0OOO0OO00O0O0OO ,O0OOO00O0O0O0O000 ,OO00O0000O000OOOO ,O00O00OOO0OOO00OO ,O0OO0O000O00OO00O ])#line:786
    def go (OOO0O0O00O00000OO ):#line:788
        if not os .path .exists (OOO0O0O00O00000OO .__O00O000000000000O ):#line:789
            os .makedirs (OOO0O0O00O00000OO .__O00O000000000000O )#line:790
        OOO00OOO0OOO0OO00 =ThreadPoolExecutor (max_workers =4 )#line:791
        OOOOO0000000OOOO0 =[]#line:792
        print ("Downloader is working, total %5d tasks"%(OOO0O0O00O00000OO .__OOOO0O0O0O0O00OOO ),flush =True )#line:793
        for O00O0O00000OOO00O ,O00OOOO0OO00OOO00 in enumerate (OOO0O0O00O00000OO .__O000OO00OO0O0OOO0 ):#line:794
            if len (O00OOOO0OO00OOO00 )>0 :#line:795
                OOOOO0000000OOOO0 .append (OOO00OOO0OOO0OO00 .submit (OOO0O0O00O00000OO .__O0OOOOOOOO000OOO0 ,O00OOOO0OO00OOO00 ))#line:796
        wait (OOOOO0000000OOOO0 ,return_when =ALL_COMPLETED )#line:797
        print ("\nALL Downloaded!\n",end ="",flush =True )#line:798
        return OOO0O0O00O00000OO .__OOOOOO0O0000000OO #line:799
