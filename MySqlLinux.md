
# Mysqlを知れよ
Linux Mysql

system start mysqld.service

mysql -u root -p
//passは空白

Mysqlを使用してdatabseseを作成してみよう
https://eng-entrance.com/mysql%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86-%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E4%BD%9C%E6%88%90%E7%B7%A8

https://www.demandosigno.study/entry/2019/09/16/174753

metasploitableでsql検索した時に出てきた。良さげ
https://www.demandosigno.study/archive/category/Metasploitable%202

脆弱なアプリケーション(DVWA)をOCIにデプロイする
https://qiita.com/western24/items/92bc1b82d164d9be41f6

【Webアプリ開発】セキュリティ入門⑤　DVWAの活用方法の紹介（note）
https://note.com/kenpapa/n/nc2dd1fa6f6e2

厚労省が出してるセキュリティ講座
https://www.mhlw.go.jp/content/11800000/000701091.pdf

https://www.google.com/search?q=metasploitable+2+sql&sca_esv=58681a8b88731783&rlz=1C1FCZY_jaJP1101JP1103&sxsrf=ADLYWILZ-kOzefzMG673OsuX9CayAPZdWA%3A1730865922593&ei=AusqZ6r6I5alvr0PyKiWqAI&ved=0ahUKEwiqg-GD6saJAxWWkq8BHUiUBSUQ4dUDCA8&uact=5&oq=metasploitable+2+sql&gs_lp=Egxnd3Mtd2l6LXNlcnAiFG1ldGFzcGxvaXRhYmxlIDIgc3FsMgsQABiABBjHAxjLATIGEAAYCBgeMgYQABgIGB4yCBAAGIAEGKIEMggQABiABBiiBDIGEAAYCBgeSLoYUF5YhRRwAXgAkAEAmAGRAaABsQOqAQMyLjK4AQPIAQD4AQGYAgSgAsoDwgIIEAAYgAQYywGYAwCIBgGSBwMxLjOgB-oN&sclient=gws-wiz-serp
# MySqlLinux
yaruyo

https://qiita.com/kaburankattara/items/842e2e1758ea00d19553

mysql --version
確認

sudo systemctl start mysqld

↑わからない

mysql -u root -p
ログイン

mysql> create user 'devuser'@'%' identified by 'Password@1';
内容の説明：
create user
新しいユーザーを作成するSQL文です。
'devuser'
作成するユーザーの名前です。この場合、ユーザー名は devuser です。
'@'%'
ユーザーがどこから接続できるかを指定しています。
'%' はワイルドカードで、任意のホスト（IPアドレスやドメイン）からの接続を許可する設定です。
※ セキュリティ上、本番環境では推奨されません。
identified by 'Password@1'
作成するユーザーのパスワードを指定しています。この場合、パスワードは Password@1 です。

セキュリティ
'%' を使うとどこからでもアクセス可能になるため、可能であれば特定のホスト（例: 'devuser'@'192.168.1.100'）に限定するべきです。
強力なパスワードを使用することを推奨します。
権限設定
ユーザーを作成しただけでは、まだ何の権限も与えられていません。この後、必要に応じて GRANT コマンドで権限を付与する必要があります。
GRANT ALL PRIVILEGES ON mydatabase.* TO 'devuser'@'%';

# q
以下のコマンドは、MySQL データベースで新しいユーザーを作成するためのものです：

```sql
mysql> create user 'devuser'@'%' identified by 'Password@1';
```

### 内容の説明：
1. **`create user`**  
   - 新しいユーザーを作成するSQL文です。

2. **`'devuser'`**  
   - 作成するユーザーの名前です。この場合、ユーザー名は **`devuser`** です。

3. **`'@'%'`**  
   - ユーザーがどこから接続できるかを指定しています。  
   - **`'%'`** はワイルドカードで、任意のホスト（IPアドレスやドメイン）からの接続を許可する設定です。  
     ※ セキュリティ上、本番環境では推奨されません。

4. **`identified by 'Password@1'`**  
   - 作成するユーザーのパスワードを指定しています。この場合、パスワードは **`Password@1`** です。

---

### 意味：
このコマンドは、任意のホストからアクセス可能な `devuser` という新しいユーザーを MySQL に作成し、そのユーザーのパスワードを `Password@1` に設定するという操作を意味します。

---

### 注意点：
1. **セキュリティ**  
   - **`'%'`** を使うとどこからでもアクセス可能になるため、可能であれば特定のホスト（例: `'devuser'@'192.168.1.100'`）に限定するべきです。
   - 強力なパスワードを使用することを推奨します。

2. **権限設定**  
   - ユーザーを作成しただけでは、まだ何の権限も与えられていません。この後、必要に応じて `GRANT` コマンドで権限を付与する必要があります。

例：  
```sql
GRANT ALL PRIVILEGES ON mydatabase.* TO 'devuser'@'%';
```

これで、`mydatabase` に対するすべての操作が可能になります。

172.17.0.2/16

# MySQL サーバーに他の IP から接続するには
`172.17.0.2/16` の MySQL サーバーに他の IP から接続するには、以下の手順を実施してください。

---

## **1. MySQLサーバー側の設定**

### **(1) `bind-address` を変更**
MySQL の設定で外部接続を許可します。

1. **設定ファイルを編集**:
   MySQL の設定ファイル（通常は `/etc/my.cnf` または `/etc/mysql/my.cnf`）を開きます。
   ```bash
   sudo nano /etc/mysql/my.cnf
   ```

2. **`bind-address` の設定を変更**:
   `bind-address` を `0.0.0.0` に変更して、すべてのIPアドレスからの接続を受け付けるようにします。
   ```ini
   [mysqld]
   bind-address = 0.0.0.0
   ```

3. **MySQLを再起動**:
   設定を反映させるために MySQL を再起動します。
   ```bash
   sudo systemctl restart mysql
   ```

---

### **(2) ファイアウォール設定**
MySQL のデフォルトポートである `3306` を開放します。

- **UFWを使用する場合**:
  ```bash
  sudo ufw allow 3306/tcp
  ```

- **FirewallDを使用する場合**:
  ```bash
  sudo firewall-cmd --permanent --add-port=3306/tcp
  sudo firewall-cmd --reload
  ```

---

### **(3) MySQLユーザーに接続を許可**
MySQL のユーザー設定で、外部ホスト（任意のIP）からの接続を許可します。

1. **MySQL にログイン**:
   ```bash
   mysql -u root -p
   ```

2. **外部接続用のユーザーを作成または更新**:
   - 任意のホスト（全IP）から接続を許可:
     ```sql
     CREATE USER 'username'@'%' IDENTIFIED BY 'password';
     GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' WITH GRANT OPTION;
     FLUSH PRIVILEGES;
     ```
   - 特定のIP範囲（例: `192.168.1.%`）からの接続を許可:
     ```sql
     CREATE USER 'username'@'192.168.1.%' IDENTIFIED BY 'password';
     GRANT ALL PRIVILEGES ON *.* TO 'username'@'192.168.1.%' WITH GRANT OPTION;
     FLUSH PRIVILEGES;
     ```

---

## **2. クライアント側の設定**

1. **ネットワークが接続可能か確認**:
   クライアント側から MySQL サーバーに通信できるか確認します。

   - **Pingで確認**:
     ```bash
     ping 172.17.0.2
     ```
   - **Telnetでポート3306が開いているか確認**:
     ```bash
     telnet 172.17.0.2 3306
     ```

2. **MySQLクライアントで接続**:
   MySQL クライアントを使用して、サーバーに接続します。
   ```bash
   mysql -h 172.17.0.2 -u username -p
   ```

---

## **3. トラブルシューティング**

### **(1) ポートが閉じている場合**
ファイアウォールまたはネットワーク設定で、ポート `3306` が閉じている可能性があります。ファイアウォールの設定を再確認してください。

### **(2) サーバーが特定のIPからの接続を拒否**
`bind-address` または MySQLユーザー設定で、接続元のIPが制限されている場合があります。設定を確認し、必要に応じて変更します。

### **(3) ネットワークルートの問題**
異なるサブネットにいる場合、ルーターやゲートウェイの設定を確認してください。適切なルーティングが必要です。

---

## **4. サンプル設定**

- **サーバーIP:** `172.17.0.2`  
- **クライアントIP:** `192.168.1.100`  

1. **MySQL設定 (`my.cnf`):**
   ```ini
   [mysqld]
   bind-address = 0.0.0.0
   ```

2. **MySQLユーザー作成:**
   ```sql
   CREATE USER 'clientuser'@'192.168.1.%' IDENTIFIED BY 'SecurePass123';
   GRANT ALL PRIVILEGES ON *.* TO 'clientuser'@'192.168.1.%' WITH GRANT OPTION;
   FLUSH PRIVILEGES;
   ```

3. **ファイアウォール開放:**
   ```bash
   sudo ufw allow 3306/tcp
   ```

4. **クライアント接続:**
   ```bash
   mysql -h 172.17.0.2 -u clientuser -p
   ```

これで、`172.17.0.2` の MySQL サーバーに他のIPから接続できるようになります。

# 他のIpからログインしようとしてERROR 2026 (HY000): TLS/SSL error: wrong version numberが出たら

`ERROR 2026 (HY000): TLS/SSL error: wrong version number` が表示される理由は、MySQL クライアントとサーバー間の TLS/SSL 設定に互換性がない場合です。具体的には、クライアントとサーバーが異なるバージョンの TLS/SSL プロトコルを使用しようとした場合に発生します。

このエラーを解決するためには、以下の手順を試してみてください。

---

### **1. MySQL クライアントで SSL を無効にする**

MySQL が SSL/TLS 接続を使用しようとする場合、SSL 設定が正しくないとエラーが発生することがあります。この場合、SSL を無効にして接続を試みることができます。

**接続時に `--ssl-mode=DISABLED` オプションを追加してみてください:**

```bash
mysql -h 192.168.56.106 -u root -p --ssl-mode=DISABLED
```

これにより、SSL 接続を無効にして、通常の非暗号化接続でサーバーに接続できます。

---

### **2. サーバー側で SSL 設定を確認する**

もしサーバー側で SSL/TLS 設定を有効にしている場合、以下の確認と修正を行います。

#### **(1) サーバーの SSL 設定を確認する**

MySQL サーバーの設定ファイル（通常は `/etc/mysql/my.cnf` または `/etc/mysql/mysql.conf.d/mysqld.cnf`）で、SSL 関連の設定が正しいか確認します。以下のような設定が存在する場合、SSL バージョンに関する問題が発生する可能性があります。

```ini
[mysqld]
ssl-ca=/path/to/ca-cert.pem
ssl-cert=/path/to/server-cert.pem
ssl-key=/path/to/server-key.pem
```

もし、`ssl` 関連の設定がある場合、サーバーが正しく SSL をサポートしていることを確認し、必要な証明書ファイルが存在するか確認します。

#### **(2) SSL/TLS バージョンを明示的に設定する**

サーバー側で使用する SSL/TLS バージョンを明示的に設定することも有効です。MySQL 5.7 以降では、TLS1.2 以上を推奨しています。

サーバー設定ファイルで以下のように TLS バージョンを指定します（`tls_version` オプション）：

```ini
[mysqld]
tls_version=TLSv1.2,TLSv1.3
```

設定後、MySQL サーバーを再起動します：

```bash
sudo systemctl restart mysql
```

---

### **3. MySQL クライアントの SSL 設定を確認する**

もしクライアントが SSL/TLS 接続を試みる場合、使用する TLS バージョンがサーバーと互換性がないことが原因でエラーが発生することがあります。

#### **(1) クライアント側で使用する SSL バージョンを指定する**

MySQL クライアントに SSL バージョンを指定することができます。例えば、TLS1.2 を指定する場合は次のようにします：

```bash
mysql -h 192.168.56.106 -u root -p --ssl-cipher=DHE-RSA-AES256-SHA --ssl-version=TLSv1.2
```

このオプションで、クライアントが TLS1.2 を使用して接続を試みます。

---

### **4. MySQL サーバー側の SSL 設定を無効にする**

もし SSL を使う必要がない場合、サーバー側で SSL 設定を無効にすることも可能です。

#### **(1) MySQL サーバーの SSL 設定を無効にする**

サーバー設定ファイル（`my.cnf`）で、SSL 関連の設定を削除またはコメントアウトします：

```ini
[mysqld]
# ssl-ca=/path/to/ca-cert.pem
# ssl-cert=/path/to/server-cert.pem
# ssl-key=/path/to/server-key.pem
# tls_version=TLSv1.2,TLSv1.3
```

その後、サーバーを再起動します：

```bash
sudo systemctl restart mysql
```

これにより、SSL 設定を完全に無効にすることができます。

---

### **5. バージョンの互換性を確認**

MySQL クライアントとサーバーのバージョンによっては、TLS/SSL のサポートに差異があります。最新の MySQL クライアントとサーバーを使用していることを確認し、可能であれば MySQL を最新バージョンにアップデートしてください。

---

### **まとめ**

- **SSL/TLS 接続を無効にする**: `--ssl-mode=DISABLED` オプションを使用。
- **サーバー側の SSL 設定を確認**: サーバー設定ファイルで `ssl` 設定を確認し、必要に応じてバージョンを指定。
- **クライアントの SSL バージョンを指定**: `--ssl-version=TLSv1.2` オプションを使って適切なバージョンを選択。
- **SSL を無効にする**: サーバー側で SSL を無効にする設定を行う。

これらの対処方法を試して、問題が解決するか確認してください。
# 接続時に --ssl-mode=DISABLED オプションを追加したらmysql: unknown variable 'ssl-mode=DISABLED'が出た
`mysql: unknown variable 'ssl-mode=DISABLED'` というエラーメッセージが表示された場合、`ssl-mode=DISABLED` オプションは MySQL のクライアントで使用できないオプションか、または使用している MySQL クライアントのバージョンに対応していない可能性があります。

代わりに、MySQL クライアントで SSL を無効にする方法をいくつか紹介します。

---

### **1. SSL を無効にする方法 (MySQL クライアント側で設定)**

MySQL クライアントから SSL を無効にするためには、以下の方法を試してください。

#### **(1) `--skip-ssl` オプションを使用**

MySQL クライアントで SSL を無効にするためには、`--skip-ssl` オプションを使用します。

```bash
mysql -h 192.168.56.106 -u root -p --skip-ssl
```

これにより、SSL/TLS 接続を無効にして、通常の非暗号化接続を使用します。

---

### **2. サーバー側で SSL を無効にする**

もしサーバー側で SSL 設定を無効にする必要がある場合、サーバーの設定を変更して SSL を無効にすることができます。

#### **(1) MySQL サーバーの設定ファイルを編集**

MySQL サーバー側で SSL を無効にするには、MySQL の設定ファイル（通常は `/etc/mysql/my.cnf` や `/etc/mysql/mysql.conf.d/mysqld.cnf`）を編集し、`ssl` 関連の設定を無効にします。

1. 設定ファイルを開きます：
   ```bash
   sudo nano /etc/mysql/my.cnf
   ```

2. `ssl` 関連の設定をコメントアウトまたは削除します：

   ```ini
   [mysqld]
   # ssl-ca=/path/to/ca-cert.pem
   # ssl-cert=/path/to/server-cert.pem
   # ssl-key=/path/to/server-key.pem
   # tls_version=TLSv1.2,TLSv1.3
   ```

3. サーバーを再起動します：
   ```bash
   sudo systemctl restart mysql
   ```

これにより、MySQL サーバーで SSL が無効になります。

---

### **3. SSL/TLS バージョンを指定する**

もし SSL を有効にしている場合で、TLS のバージョンに問題がある場合、`--ssl-cipher` と `--ssl-version` を指定して接続することもできます。

#### **(1) クライアント側で TLS バージョンを指定**

例えば、TLS 1.2 を使用する場合、次のように指定できます：

```bash
mysql -h 192.168.56.106 -u root -p --ssl-cipher=DHE-RSA-AES256-SHA --ssl-version=TLSv1.2
```

これにより、特定のバージョンの TLS を使用して接続できます。

---

### **まとめ**

- `--ssl-mode=DISABLED` オプションではなく、`--skip-ssl` オプションを使って SSL を無効にする。
- サーバー側で SSL を無効にする場合は、設定ファイルで SSL 設定をコメントアウトして再起動する。
- SSL バージョンの不一致を解決するために、クライアントで `--ssl-version` や `--ssl-cipher` を指定する。

これらを試してみてください。エラーが解決するか確認をお願いします。