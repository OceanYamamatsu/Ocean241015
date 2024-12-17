Data Dictionary
仕⼊販売管理 Database
 Customer（販売先マスタ）
KEY FIELD NAME DATA TYPE / FIELD SIZE REQUIRED? NOTES
 PK ID
 CHAR(5)
 Y
 Name
 Addr
 Tel
 VARCHAR(100)
 VARCHAR(200)
 VARCHAR(11)
 Y
 Y
 Y
販売先コード
販売先名
販売先住所
販売先電話番号

Data Dictionary
仕⼊販売管理 Database
 Supplier(仕⼊先マスタ）
KEY FIELD NAME DATA TYPE / FIELD SIZE REQUIRED? NOTES
 PK ID
 CHAR(5)
 Y
 Name
 Addr
 Tel
 VARCHAR(100)
 VARCHAR(200)
 VARCHAR(11)
 Y
 Y
 Y
仕⼊先コード
仕⼊先名
仕⼊先住所
仕⼊先電話番号

Data Dictionary
仕⼊販売管理 Database
 Stock（在庫表）
KEY FIELD NAME DATA TYPE / FIELD SIZE REQUIRED?
 PK PrdID
 CHAR(5)
 NOTES
 Y
 Stk
 INT
 Y
商品コード ProductのIDと同様の値
在庫数

Data Dictionary
仕⼊販売管理 Database
 Product（商品マスタ）
KEY FIELD NAME DATA TYPE / FIELD SIZE REQUIRED?
 NOTES
 PK ID
 CHAR(5)
 Y
 Name
 VARCHAR(50)
 Y
 FK SupID
 CHAR(5)
 Y
 PPrc
 INT
 Y
 SPrc
 INT
 Y
商品コード
商品名
仕⼊先コード SupplierのIDと同様の値
仕⼊単価
販売単価


Data Dictionary
仕⼊販売管理 Database
 SalesSlip（販売伝票表）
KEY FIELD NAME DATA TYPE / FIELD SIZE REQUIRED?
 PK ID
 CHAR(5)
 NOTES
 Y
 SDate
 FK CustID
 DATE
 CHAR(5)
 Y
 Y
販売伝票番号
販売⽇
販売先コード CustomerのIDと同様の値


Data Dictionary
仕⼊販売管理 Database
 PurchaseSlip（仕⼊伝票表）
KEY FIELD NAME DATA TYPE / FIELD SIZE REQUIRED?
 PK ID
 PDate
 CHAR(5)
 DATE
 Y
 NOTES
 Y
 FK PrdID
 Pqnty
 CHAR(5)
 INT
 Y
 Y
仕⼊伝票番号
仕⼊⽇
商品コード ProductのIDと同様の値
仕⼊数量


Data Dictionary
仕⼊販売管理 Database
 SalesInfo（商品販売表）
KEY FIELD NAME DATA TYPE / FIELD SIZE REQUIRED?
 PK ID
 FK SSlpID
 CHAR(5)
 CHAR(5)
 Y
 NOTES
 Y
 FK PrdID
 Sqnty
 CHAR(5)
 INT
 Y
 Y
販売No
販売伝票番号 SalesSlipのIDと同様の値
商品コード ProductのIDと同様の値
販売数量

SQLiteを使用してテーブル定義を作成して