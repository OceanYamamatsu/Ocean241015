

Data Dictionary

仕入販売管理 Database

Customer(販売先マスタ)

KEY

FIELD NAME

DATA TYPE/FIELD SIZE

REQUIRED?

NOTES

PK ID

CHAR(5)

Y

販売先コード

Name

VARCHAR(100)

Y

販売先名

Addr

VARCHAR(200)

Y

販売先住所

Tel

VARCHAR(11)

Y

販売先電話番号

Data Dictionary

仕入販売管理 Database

Supplier (仕入先マスタ)

KEY FIELD NAME

DATA TYPE / FIELD SIZE

REQUIRED?

NOTES

PK ID

CHAR(5)

Y

仕入先コード

Name

VARCHAR(100)

Y

仕入先名

Addr

VARCHAR(200)

Y

仕入先住所

Tel

VARCHAR(11)

Y

「仕入先電話番号

Data Dictionary

仕入販売管理 Database

Stock(在庫表)

KEY

FIELD NAME

DATA TYPE/FIELD SIZE

REQUIRED?

PK PrdID

Stk

CHAR(5)

INT

Y

Y

NOTES

商品コード ProductのIDと同様の値

在庫数

Data Dictionary

仕入販売管理 Database

Product (商品マスタ)

KEY

FIELD NAME

DATA TYPE/FIELD SIZE

REQUIRED?

NOTES

PK ID

CHAR(5)

Y

商品コード

Name

VARCHAR(50)

Y

商品名

FK SupID

CHAR(5)

Y

「仕入先コード

SupplierのIDと同様の値

PPrc

INT

Y

仕入単価

SPrc

INT

Y

販売単価

Data Dictionary

仕入販売管理 Database

Sales Slip(販売伝票表)

KEY FIELD NAME

DATA TYPE/FIELD SIZE

REQUIRED?

NOTES

PK ID

SDate

CHAR(5)

DATE

Y

販売伝票番号

Y

販売日

FK CustID

CHAR(5)

Y

販売先コード CustomerのIDと同様の値

Data Dictionary

仕入販売管理 Database

PurchaseSlip (仕入伝票表)

KEY

FIELD NAME

DATA TYPE / FIELD SIZE

REQUIRED?

NOTES

PK ID

CHAR(5)

Y

仕入伝票番号

PDate

FK PrdID

Panty

DATE

CHAR(5)

INT

Y

仕入日

Y

商品コード

ProductのIDと同様の値

Y

仕入数量

Data Dictionary

仕入販売管理 Database

KEY FIELD NAME

DATA TYPE / FIELD SIZE

REQUIRED?

PK ID

CHAR(5)

FK SSIPID

CHAR(5)

FK PrdID

CHAR(5)

Santy

INT

NOTES

Y

販売No

Y

販売伝票番号

Sales SlipのIDと同様の値

Y

商品コード

ProductのIDと同様の値

Y

販売数量

テーブルの定義

SQLiteを使用しData Dictionary (上記)に従って、商品販売表,販売伝票表,販売先マス 夕,仕入伝票表、仕入先マスタ、商品マスタ、在庫表の各テーブルを定義しなさい。