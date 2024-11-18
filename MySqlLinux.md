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