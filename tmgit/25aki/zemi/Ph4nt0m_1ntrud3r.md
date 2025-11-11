┌──(kali㉿kali)-[~]
└─$ sudo apt update
sudo apt install wireshark tshark tcpdump zeek suricata python3-pip networkminer binwalk foremost bulk-extractor exiftool
pip3 install pyshark scapy dpkt
# zsteg (Ruby gem) が必要なら: sudo gem install zsteg

[sudo] kali のパスワード:
取得:1 http://mirror.tefexia.net/kali kali-rolling InRelease [34.0 kB]
取得:2 http://mirror.tefexia.net/kali kali-rolling/main amd64 Packages [21.0 MB]                              
取得:3 http://mirror.tefexia.net/kali kali-rolling/main amd64 Contents (deb) [52.3 MB]                        
取得:4 http://mirror.tefexia.net/kali kali-rolling/contrib amd64 Packages [114 kB]                            
取得:5 http://mirror.tefexia.net/kali kali-rolling/contrib amd64 Contents (deb) [259 kB]                      
取得:6 http://mirror.tefexia.net/kali kali-rolling/non-free amd64 Packages [186 kB]                           
取得:7 http://mirror.tefexia.net/kali kali-rolling/non-free amd64 Contents (deb) [893 kB]                     
取得:8 http://mirror.tefexia.net/kali kali-rolling/non-free-firmware amd64 Packages [11.3 kB]                 
取得:9 http://mirror.tefexia.net/kali kali-rolling/non-free-firmware amd64 Contents (deb) [28.4 kB]           
74.8 MB を 51秒 で取得しました (1,473 kB/s)                                                                   
WARNING:root:cannot read /var/lib/command-not-found/commands.db.metadata: Expecting value: line 1 column 1 (char 0)
アップグレードできるパッケージが 2241 個あります。表示するには 'apt list --upgradable' を実行してください。
Warning: http://http.kali.org/kali/dists/kali-rolling/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
注意、'exiftool' の代わりに 'libimage-exiftool-perl' を選択します
Error: パッケージ networkminer が見つかりません
Defaulting to user installation because normal site-packages is not writeable
Collecting pyshark
  Downloading pyshark-0.6-py3-none-any.whl.metadata (806 bytes)
Requirement already satisfied: scapy in /usr/lib/python3/dist-packages (2.5.0+git20240324.2b58b51)
Collecting dpkt
  Downloading dpkt-1.9.8-py3-none-any.whl.metadata (1.7 kB)
Requirement already satisfied: lxml in /usr/lib/python3/dist-packages (from pyshark) (5.1.0)
Requirement already satisfied: termcolor in /usr/lib/python3/dist-packages (from pyshark) (2.4.0)
Requirement already satisfied: packaging in /usr/lib/python3/dist-packages (from pyshark) (24.1)
Requirement already satisfied: appdirs in /usr/lib/python3/dist-packages (from pyshark) (1.4.4)
Downloading pyshark-0.6-py3-none-any.whl (41 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.4/41.4 kB 1.6 MB/s eta 0:00:00
Downloading dpkt-1.9.8-py3-none-any.whl (194 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 195.0/195.0 kB 1.8 MB/s eta 0:00:00
Installing collected packages: dpkt, pyshark
Successfully installed dpkt-1.9.8 pyshark-0.6

=============================================================================================================
=============================================================================================================
=============================================================================================================

                                                                                                     
┌──(kali㉿kali)-[~/picoctf/Ph4nt0m_1ntrud3r]
└─$ capinfos myNetworkTraffic.pcap 
File name:           myNetworkTraffic.pcap
File type:           Wireshark/tcpdump/... - pcap
File encapsulation:  Raw IPv4
File timestamp precision:  microseconds (6)
Packet size limit:   file hdr: 65535 bytes
Number of packets:   22
File size:           1,452 bytes
Data size:           1,076 bytes
Capture duration:    0.005471 seconds
First packet time:   2025-03-06 12:31:35.791921
Last packet time:    2025-03-06 12:31:35.797392
Data byte rate:      196 kBps
Data bit rate:       1,573 kbps
Average packet size: 48.91 bytes
Average packet rate: 4,021 packets/s
SHA256:              3fdced1b943e568fd2d351d3b6e76a4379c863021f9424c5f57fe4c67de7a622
SHA1:                ea2b4083a5ac17bd5a7dde60593dd8de3f4c860e
Strict time order:   False
Number of interfaces in file: 1
Interface #0 info:
                     Encapsulation = Raw IPv4 (129 - rawip4)
                     Capture length = 65535
                     Time precision = microseconds (6)
                     Time ticks per second = 1000000
                     Number of stat entries = 0
                     Number of packets = 22
=============================================================================================================
=============================================================================================================
=============================================================================================================
