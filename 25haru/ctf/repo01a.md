## PHPファイルアップロードにおける脆弱性の検証とその対策

### 〜 picoCTF「n0s4n1ty 1」 を題材に 〜

---

### ■ 背景・目的

Webアプリケーションにおけるファイルアップロード機能は、利便性の一方で重大なセキュリティリスクを伴う。中でも、PHPスクリプトをアップロードすることで任意のコードが実行される脆弱性（PHPインジェクション）は、攻撃者によるサーバ乗っ取りにつながる。本研究では、CTF問題「n0s4n1ty 1」を題材に、実際に脆弱性の再現・検証を行い、その仕組みと対策について考察する。

---

### ■ スライド1：PHPファイルアップロードの脆弱性検証（picoCTF編）

* picoCTF「n0s4n1ty 1」に含まれる脆弱なWebアプリケーションを対象に調査を実施。
* 主な検証項目：

  * アップロード可能な拡張子の確認
  * PHPコードの実行可否の検証
  * system()等の関数によるコマンド実行
  * サーバユーザーの権限確認（sudo）
  * リバースシェルの実行可否

---

### ■ スライド2：検証結果とその意味

* 拡張子制限が不十分で `.jpg`, `.phtml` などが許可されていた。
* `<?php echo "hello"; ?>` を含む静的PHPコードは実行可能。
* `system("ls /")` などのコマンドも実行可能だった。
* `sudo -l` 実行の結果、www-dataがパスワードなしで全コマンド実行可能な設定であると判明。
* `sudo cat /root/flag.txt` により、フラグファイルを取得可能だった。
* `system($_GET['cmd'])` のような外部入力を伴うコードや、リバースシェルはWAFによりブロックされた。

---

### ■ スライド3：歴史的攻撃例「phpBB LFI脆弱性」

* phpBBは2005年、Local File Inclusion（LFI）の脆弱性（CVE-2005-3415）により大規模な攻撃を受けた。
* 問題のコード例：

  ```php
  include($phpbb_root_path . 'language/lang_' . $board_config['default_lang'] . '/lang_main.' . $phpEx);
  ```
* 攻撃者は `default_lang=../../../../etc/passwd%00` などを渡すことで、OSファイルを読み込ませることができた。
* ヌルバイト（%00）を含むことで、`.php` 等の拡張子チェックを回避。
* この攻撃はログファイル等と組み合わせることで、リモートコード実行（RCE）にも発展。

---

### ■ スライド4：対策と教訓

| リスク     | 例                         | 推奨される対策                    |
| ------- | ------------------------- | -------------------------- |
| 任意コード実行 | `system()`, `eval()`      | 拡張子・MIMEタイプの厳密なチェック、WAFの導入 |
| 権限昇格    | `sudo cat /root/flag.txt` | Webユーザーのsudo権限を制限、最小権限の原則  |
| サーバ制御   | リバースシェル                   | 外部通信の制限、コマンド構文のフィルタリング     |
| 情報漏洩    | `/etc/passwd`の閲覧          | 実行ディレクトリに制限を設ける、ログ監視       |

* PHPの`include()`等は、外部入力を直接使わない設計が重要。
* 入力値のホワイトリスト化、PHPバージョンの最新化、ヌルバイトの無効化（PHP5.3以降）
* 歴史的攻撃例から学び、単一の防御策ではなく多層防御の考え方が必要。

---

### ■ 参考文献

* picoCTF「n0s4n1ty 1」 [https://play.picoctf.org/practice/challenge/482](https://play.picoctf.org/practice/challenge/482)
* OWASP File Upload Cheat Sheet [https://cheatsheetseries.owasp.org/cheatsheets/File\_Upload\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
* Linux sudo manページ [https://linux.die.net/man/8/sudo](https://linux.die.net/man/8/sudo)
* phpBB脆弱性 CVE-2005-3415 [https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-3415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-3415)

---

### ■ 結論と今後の課題

* PHPファイルアップロードによるインジェクションや、includeの不適切な利用によるLFIは、古典的だが依然として有効な攻撃ベクタ。
* Webサーバの設定・権限管理・WAF設定・ユーザー入力バリデーションなど、複数の対策を組み合わせることが求められる。
* 今後は、PHP以外の言語やフレームワークにおけるアップロード・インクルージョンの脆弱性にも着目したい。
