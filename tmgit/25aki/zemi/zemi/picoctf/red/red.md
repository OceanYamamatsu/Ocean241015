┌──(kali㉿kali)-[~]
└─$ cd picoctf/RED              
                                                                                                                                                         
┌──(kali㉿kali)-[~/picoctf/RED]
└─$ file red.png                
red.png: PNG image data, 128 x 128, 8-bit/color RGBA, non-interlaced
                                                                                                                                                         
┌──(kali㉿kali)-[~/picoctf/RED]
└─$ xxd red.png | head          
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0080 0000 0080 0806 0000 00c3 3e61  ..............>a
00000020: cb00 0000 e774 4558 7450 6f65 6d00 4372  .....tEXtPoem.Cr
00000030: 696d 736f 6e20 6865 6172 742c 2076 6962  imson heart, vib
00000040: 7261 6e74 2061 6e64 2062 6f6c 642c 0a48  rant and bold,.H
00000050: 6561 7274 7320 666c 7574 7465 7220 6174  earts flutter at
00000060: 2079 6f75 7220 7369 6768 742e 0a45 7665   your sight..Eve
00000070: 6e69 6e67 7320 676c 6f77 2073 6f66 746c  nings glow softl
00000080: 7920 7265 642c 0a43 6865 7272 6965 7320  y red,.Cherries 
00000090: 6275 7273 7420 7769 7468 2073 7765 6574  burst with sweet
                                 


┌──(kali㉿kali)-[~/picoctf/RED]
└─$ sudo apt update
sudo apt install python3-pip -y
pip3 install pillow

取得:1 http://mirror.tefexia.net/kali kali-rolling InRelease [34.0 kB]
取得:2 http://mirror.tefexia.net/kali kali-rolling/main amd64 Packages [20.9 MB]
取得:3 http://mirror.tefexia.net/kali kali-rolling/main amd64 Contents (deb) [52.2 MB]
取得:4 http://mirror.tefexia.net/kali kali-rolling/contrib amd64 Packages [116 kB]                                                                      
取得:5 http://mirror.tefexia.net/kali kali-rolling/contrib amd64 Contents (deb) [319 kB]                                                                
取得:6 http://mirror.tefexia.net/kali kali-rolling/non-free amd64 Packages [186 kB]                                                                     
取得:7 http://mirror.tefexia.net/kali kali-rolling/non-free amd64 Contents (deb) [893 kB]                                                               
取得:8 http://mirror.tefexia.net/kali kali-rolling/non-free-firmware amd64 Packages [11.3 kB]                                                           
取得:9 http://mirror.tefexia.net/kali kali-rolling/non-free-firmware amd64 Contents (deb) [28.4 kB]                                                     
74.7 MB を 18秒 で取得しました (4,170 kB/s)                                                                                                             
WARNING:root:cannot read /var/lib/command-not-found/commands.db.metadata: Expecting value: line 1 column 1 (char 0)
アップグレードできるパッケージが 2237 個あります。表示するには 'apt list --upgradable' を実行してください。
Warning: http://http.kali.org/kali/dists/kali-rolling/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Upgrading:                                                  
  libjs-sphinxdoc  python3-pip  python3-pip-whl
                                                                                                                                                         
Summary:
  Upgrading: 3, Installing: 0, Removing: 0, Not Upgrading: 2234
  Download size: 2,842 kB
  Freed space: 317 kB

取得:1 http://mirror.tefexia.net/kali kali-rolling/main amd64 libjs-sphinxdoc all 8.2.3-8 [27.6 kB]
取得:2 http://http.kali.org/kali kali-rolling/main amd64 python3-pip all 25.2+dfsg-1 [1,386 kB]
取得:3 http://http.kali.org/kali kali-rolling/main amd64 python3-pip-whl all 25.2+dfsg-1 [1,428 kB]
2,842 kB を 5秒 で取得しました (605 kB/s)
(データベースを読み込んでいます ... 現在 395765 個のファイルとディレクトリがインストールされています。)
.../libjs-sphinxdoc_8.2.3-8_all.deb を展開する準備をしています ...
libjs-sphinxdoc (8.2.3-8) で (7.3.7-3 に) 上書き展開しています ...
.../python3-pip_25.2+dfsg-1_all.deb を展開する準備をしています ...
python3-pip (25.2+dfsg-1) で (24.1.1+dfsg-1 に) 上書き展開しています ...
.../python3-pip-whl_25.2+dfsg-1_all.deb を展開する準備をしています ...
python3-pip-whl (25.2+dfsg-1) で (24.1.1+dfsg-1 に) 上書き展開しています ...
python3-pip-whl (25.2+dfsg-1) を設定しています ...
python3-pip (25.2+dfsg-1) を設定しています ...
libjs-sphinxdoc (8.2.3-8) を設定しています ...
man-db (2.12.1-2) のトリガを処理しています ...
kali-menu (2024.3.1) のトリガを処理しています ...
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pillow in /usr/lib/python3/dist-packages (10.3.0)
     




echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d


https://speakerdeck.com/kuroiwasi/cpawctf-steganography?slide=19

┌──(kali㉿kali)-[~/picoctf/RED]
└─$ zsteg red.png
meta Poem           .. text: "Crimson heart, vibrant and bold,\nHearts flutter at your sight.\nEvenings glow softly red,\nCherries burst with sweet life.\nKisses linger with your warmth.\nLove deep as merlot.\nScarlet leaves falling softly,\nBold in every stroke."                                            
b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=="                     
b1,rgba,msb,xy      .. file: OpenPGP Public Key
b2,g,lsb,xy         .. text: "ET@UETPETUUT@TUUTD@PDUDDDPE"
b2,rgb,lsb,xy       .. file: OpenPGP Secret Key
b2,bgr,msb,xy       .. file: OpenPGP Public Key
b2,rgba,lsb,xy      .. file: OpenPGP Secret Key
b2,rgba,msb,xy      .. text: "CIkiiiII"
b2,abgr,lsb,xy      .. file: OpenPGP Secret Key
b2,abgr,msb,xy      .. text: "iiiaakikk"
b3,rgba,msb,xy      .. text: "#wb#wp#7p"
b3,abgr,msb,xy      .. text: "7r'wb#7p"
b4,b,lsb,xy         .. file: 0421 Alliant compact executable not stripped
                                   