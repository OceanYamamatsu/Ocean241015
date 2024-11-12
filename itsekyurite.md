#itセキュリティ用

itセキュリティ
kali
msfadmin


sudo shutdown now


https://editor.note.com/notes/nc0ef0d7438d0/edit/

192.168.56.101
msfconsole

nmap -sV <teaget ip>

search vsftpd 2.3.4
              ↑vol.

use <kougekimozyuname>

set RHOST 192.168.56.101

exploit


exploit



11/05

sudo apt update && upgrade -y
//sudo(すーdu-)
//updateする
//&&を使用すると連続で実行できる

sudo apt install -y snort
//installする



snort --version
//instoll確認


snortのルール作成

cd /etc/dnort/rules
//ruleが書いてある
//Tere is an exprotion 

help version9
alert tcp [ip] any -> [ipホストオンリ] 22 (msg: "SSH conection from kall", sid:1000002; rev:1;)


alert tcp 192.168.56.105 any -> 192.168.56.255/24 22 (msg: "SSH conection from kall", sid:1000002; rev:1;)

ssh user@ip
//kaliでうぶんとに投げる

24/11/12


Docker Desktop
arm for windousをdl

docker desktopのインストール
docker hub からubuntu/nginx内の
https://hub.docker.com/r/ubuntu/nginx
Launch this image locally:の下
''docker run -d --name nginx-container -e TZ=UTC -p 8080:80 ubuntu/nginx:1.18-22.04_beta''
をcopyしてWindowsCmdにてペーストしてdockerの起動


　　　　　　　　　　　　　　　　　　↓時間指定　　　　　↓バージョン指定
docker run -d --name nginx-container -e TZ=UTC -p 8080:80 ubuntu/nginx:1.18-22.04_beta
↑起動　　　　↑コンテナの名前を付ける　　　　↑-pポート開放

本授業のコンテナid''3a0b771daba1''

docker ps -a
すべてのコンテナを表示

docker start コンテナid
コンテナ起動

docker stop コンテナid
コンテナ終了
