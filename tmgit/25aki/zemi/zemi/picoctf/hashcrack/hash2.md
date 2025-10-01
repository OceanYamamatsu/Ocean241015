command 'hash-identifier' from deb hash-identifier


ls -l -h -s


┌──(kali㉿kali)-[~/picoctf/hashcrack]
└─$ git clone https://github.com/danielmiessler/SecLists.git
Cloning into 'SecLists'...
remote: Enumerating objects: 48580, done.
remote: Total 48580 (delta 0), reused 0 (delta 0), pack-reused 48580 (from 1)
Receiving objects: 100% (48580/48580), 2.46 GiB | 5.00 MiB/s, done.
Resolving deltas: 100% (34668/34668), done.
Updating files: 100% (6239/6239), done.


┌──(kali㉿kali)-[~/picoctf/hashcrack]
└─$ nc verbal-sleep.picoctf.net 65348
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: password123
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: letmein
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: 



password123
letmein

tryhack me

qwerty098


┌──(kali㉿kali)-[~]
└─$ nc verbal-sleep.picoctf.net 62191
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: password123
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: letmein
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: qwerty098
Correct! You've cracked the SHA-256 hash with a secret found. 
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4c95d69f}
                                                            



┌──(kali㉿kali)-[~/picoctf/hashcrack]
└─$ hashcat -m 1400 -a 0 hash2.txt ./SecLists/Passwords/Leaked-Databases -w 3               
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, LLVM 17.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #1: cpu-haswell-13th Gen Intel(R) Core(TM) i7-1355U, 1403/2870 MB (512 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache built:
* Filename..: ./SecLists/Passwords/Leaked-Databases/000webhost.txt
* Passwords.: 720302
* Bytes.....: 7708819
* Keyspace..: 720302
* Runtime...: 0 secs

916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745:qwerty098
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1400 (SHA2-256)
Hash.Target......: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad...697745
Time.Started.....: Wed Oct  1 18:16:25 2025 (0 secs)
Time.Estimated...: Wed Oct  1 18:16:25 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (./SecLists/Passwords/Leaked-Databases/000webhost.txt)
Guess.Queue......: 1/56 (1.79%)
Speed.#1.........:  1051.2 kH/s (0.19ms) @ Accel:256 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 158208/720302 (21.96%)
Rejected.........: 0/158208 (0.00%)
Restore.Point....: 157696/720302 (21.89%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: CBFa354AW456 -> putriforever1
Hardware.Mon.#1..: Util: 45%

Started: Wed Oct  1 18:16:24 2025
Stopped: Wed Oct  1 18:16:27 2025
