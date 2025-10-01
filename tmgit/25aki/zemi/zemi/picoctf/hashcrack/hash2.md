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
                                                            


                                                            