## PHPファイルアップロードにおける脆弱性の検証とその対策

### 〜 picoCTF「n0s4n1ty 1」 を題材に 〜

---

### ■ 背景・目的

Webアプリケーションにおけるファイルアップロード機能は、利便性の一方で重大なセキュリティリスクを伴う。中でも、PHPスクリプトをアップロードすることで任意のコードが実行される脆弱性（PHPインジェクション）は、攻撃者によるサーバ乗っ取りにつながる。本研究では、CTF問題「n0s4n1ty 1」を題材に、実際に脆弱性の再現・検証を行い、その仕組みと対策について考察する。

---

### ■ 手法

* picoCTF「n0s4n1ty 1」に含まれる脆弱なWebアプリケーションを対象に調査を実施。
* 主な検証項目：

  * アップロード可能な拡張子の確認
  * PHPコードの実行可否の検証
  * system()等の関数によるコマンド実行
  * サーバユーザーの権限確認（sudo）
  * リバースシェルの実行可否

---

### ■ 検証結果

* 拡張子制限が不十分で `.jpg`, `.phtml` などが許可されていた。
* `<?php echo "hello"; ?>` を含む静的PHPコードは実行可能。
* `system("ls /")` などのコマンドも実行可能だった。
* `sudo -l` 実行の結果、www-dataがパスワードなしで全コマンド実行可能な設定であると判明。
* `sudo cat /root/flag.txt` により、フラグファイルを取得可能だった。
* `system($_GET['cmd'])` のような外部入力を伴うコードや、リバースシェルはWAFによりブロックされた。

---

### ■ PHPインジェクションの流れ

1. ファイルアップロード機能に対して `.phtml` 等でPHPスクリプトをアップロード
2. PHPファイルに任意コード（system等）を記述
3. Web上からアクセスし、コードが実行される
4. `sudo` などを利用し権限昇格
5. 機密ファイルの閲覧やサーバの制御が可能となる

---

### ■ 危険性と対策

| リスク     | 例                         | 推奨される対策                    |
| ------- | ------------------------- | -------------------------- |
| 任意コード実行 | `system()`, `eval()`      | 拡張子・MIMEタイプの厳密なチェック、WAFの導入 |
| 権限昇格    | `sudo cat /root/flag.txt` | Webユーザーのsudo権限を制限、最小権限の原則  |
| サーバ制御   | リバースシェル                   | 外部通信の制限、コマンド構文のフィルタリング     |
| 情報漏洩    | `/etc/passwd`の閲覧          | 実行ディレクトリに制限を設ける、ログ監視       |

---

### ■ 結論と今後の課題

* PHPファイルアップロードによるインジェクションは、設定ミスや不十分なバリデーションにより簡単に成立しうる。
* 特にWebサーバのユーザー権限やWAFの設定ミスは、致命的な侵害につながる。
* 今後は、さらなるCTF課題への挑戦や、PHP以外の言語（Python, Node.jsなど）における同様の脆弱性パターンの分析も行いたい。

---

### ■ 参考文献

* picoCTF「n0s4n1ty 1」 [https://play.picoctf.org/practice/challenge/482](https://play.picoctf.org/practice/challenge/482)
* OWASP File Upload Cheat Sheet [https://cheatsheetseries.owasp.org/cheatsheets/File\_Upload\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
* Linux sudo manページ [https://linux.die.net/man/8/sudo](https://linux.die.net/man/8/sudo)
