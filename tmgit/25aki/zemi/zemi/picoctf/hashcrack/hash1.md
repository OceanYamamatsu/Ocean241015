                                       
┌──(kali㉿kali)-[~]
└─$ nc verbal-sleep.picoctf.net 51204~  
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash:                                                                                                                                                          
┌──(kali㉿kali)-[~]
└─$ hash="482c811da5d5b4bc6d497ffa98491e38"
echo -n "$hash" | wc -c   # 32 と出れば32文字（hex32）
32
                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ hash="482c811da5d5b4bc6d497ffa98491e38"
echo -n "$hash" | wc -c   # 32 と出れば32文字（hex32）
pip install hashid
hashid 482c811da5d5b4bc6d497ffa98491e38
32
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: hashid in /usr/lib/python3/dist-packages (3.1.4)
Analyzing '482c811da5d5b4bc6d497ffa98491e38'
[+] MD2 
[+] MD5 
[+] MD4 
[+] Double MD5 
[+] LM 
[+] RIPEMD-128 
[+] Haval-128 
[+] Tiger-128 
[+] Skein-256(128) 
[+] Skein-512(128) 
[+] Lotus Notes/Domino 5 
[+] Skype 
[+] Snefru-128 
[+] NTLM 
[+] Domain Cached Credentials 
[+] Domain Cached Credentials 2 
[+] DNSSEC(NSEC3) 
[+] RAdmin v2.x 
                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ ┌──(root㉿kali)-[~]                  
└─# timedatectl set-timezone Asia/Tokyo

┌──(root㉿kali)-[~]: コマンドが見つかりません
└─#: コマンドが見つかりません
                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ timedatectl set-timezone Asia/Tokyo
                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ timedatectl  
               Local time: 水 2025-10-01 11:24:44 JST
           Universal time: 水 2025-10-01 02:24:44 UTC
                 RTC time: 火 2025-09-30 17:21:36
                Time zone: Asia/Tokyo (JST, +0900)
System clock synchronized: no
              NTP service: inactive
          RTC in local TZ: no
                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ nc verbal-sleep.picoctf.net 57897
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: abs
Incorrect. Goodbye.






hashcat -m 0 -a 3 482c811da5d5b4bc6d497ffa98491e38 '?a?a?a?a?a?a?a?a'
nc verbal-sleep.picoctf.net 51214
482c811da5d5b4bc6d497ffa98491e38
