-- SQLite

-- Customer（販売先マスタ）
CREATE TABLE Customer (
    ID CHAR(5) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Addr VARCHAR(200) NOT NULL,
    Tel VARCHAR(11) NOT NULL
);

-- Supplier（仕入先マスタ）
CREATE TABLE Supplier (
    ID CHAR(5) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Addr VARCHAR(200) NOT NULL,
    Tel VARCHAR(11) NOT NULL
);

-- Product（商品マスタ）
CREATE TABLE Product (
    ID CHAR(5) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    SupID CHAR(5) NOT NULL,
    PPrc INT NOT NULL,
    SPrc INT NOT NULL,
    FOREIGN KEY (SupID) REFERENCES Supplier(ID)
);

-- Stock（在庫表）
CREATE TABLE Stock (
    PrdID CHAR(5) PRIMARY KEY,
    Stk INT NOT NULL,
    FOREIGN KEY (PrdID) REFERENCES Product(ID)
);

-- SalesSlip（販売伝票表）
CREATE TABLE SalesSlip (
    ID CHAR(5) PRIMARY KEY,
    SDate DATE NOT NULL,
    CustID CHAR(5) NOT NULL,
    FOREIGN KEY (CustID) REFERENCES Customer(ID)
);

-- SalesInfo（商品販売表）
CREATE TABLE SalesInfo (
    ID CHAR(5) PRIMARY KEY,
    SSlpID CHAR(5) NOT NULL,
    PrdID CHAR(5) NOT NULL,
    Sqnty INT NOT NULL,
    FOREIGN KEY (SSlpID) REFERENCES SalesSlip(ID),
    FOREIGN KEY (PrdID) REFERENCES Product(ID)
);

-- PurchaseSlip（仕入伝票表）
CREATE TABLE PurchaseSlip (
    ID CHAR(5) PRIMARY KEY,
    PDate DATE NOT NULL,
    PrdID CHAR(5) NOT NULL,
    Pqnty INT NOT NULL,
    FOREIGN KEY (PrdID) REFERENCES Product(ID)
);
----------------------------------------------------------
INSERT INTO Supplier (ID, Name, Addr, Tel) VALUES
('S0001', '四四電気', '北海道札幌市', '111-222-3333'),
('S0002', '東東電機', '宮城県仙台市', '222-333-4444'),
('S0003', '日日製造', '三重県津市', '333-444-5555'),
('S0004', '三三電子', '香川県高松市', '444-555-6666');

INSERT INTO Customer (ID, Name, Addr, Tel) VALUES
('H0001', '岸田商店', '栃木県宇都宮市', '123-234-3456'),
('H0002', '勝又電気', '千葉県千葉市', '234-345-4567'),
('H0003', '佐野電気', '長崎県長崎市', '345-456-5678'),
('H0004', '堀商店', '大阪府大阪市', '456-678-6789'),
('H0005', '池谷商店', '東京都新宿区', '567-789-8901'),
('H0006', '岩佐電気店', '神奈川県横浜市', '789-890-9012'),
('H0007', '向井電気', '福島県福島市', '987-876-7654'),
('H0008', '松下商会', '富山県富山市', '765-654-5432');

INSERT INTO Product (ID, Name, SupID, PPrc, SPrc) VALUES
('A0001', '液晶テレビ', 'S0001', 50160, 62700),
('A0002', 'プラズマテレビ', 'S0002', 81440, 101800),
('A0003', 'プロジェクタ', 'S0003', 50160, 62700),
('A0011', 'DVDプレーヤ', 'S0001', 3150, 4500),
('A0012', 'ブルーレイプレーヤ', 'S0004', 9090, 12980),
('A0021', 'MP3 プレーヤ', 'S0003', 17040, 21300),
('A0022', 'スピーカ', 'S0001', 20290, 25360),
('A0023', 'CDプレーヤ', 'S0002', 21020, 26720),
('A0024', 'IC レコーダ', 'S0004', 5490, 6860),
('A0031', 'FAX', 'S0003', 14670, 16300),
('A0032', '電話機', 'S0001', 11520, 12800);

INSERT INTO Stock (PrdID, Stk) VALUES
('A0001', 10), ('A0002', 10), ('A0003', 10), ('A0011', 10),
('A0012', 10), ('A0021', 10), ('A0022', 10), ('A0023', 10),
('A0024', 10), ('A0031', 10), ('A0032', 10);

INSERT INTO SalesSlip (ID, SDate, CustID) VALUES
('D0001', '2015-01-10', 'H0001'),
('D0002', '2015-01-10', 'H0002'),
('D0003', '2015-01-10', 'H0003'),
('D0004', '2015-01-10', 'H0005'),
('D0005', '2015-01-10', 'H0006'),
('D0006', '2015-01-10', 'H0007'),
('D0007', '2015-01-10', 'H0008'),
('D0008', '2015-01-15', 'H0004');

INSERT INTO SalesInfo (ID, SSlpID, PrdID, Sqnty) VALUES
('B0001', 'D0001', 'A0001', 1),
('B0002', 'D0001', 'A0024', 4),
('B0003', 'D0001', 'A0031', 4),
('B0004', 'D0002', 'A0002', 2),
('B0005', 'D0002', 'A0031', 1),
('B0006', 'D0003', 'A0002', 3),
('B0007', 'D0003', 'A0022', 4),
('B0008', 'D0004', 'A0022', 2),
('B0009', 'D0005', 'A0012', 2),
('B0010', 'D0006', 'A0003', 2),
('B0011', 'D0007', 'A0023', 3),
('B0012', 'D0008', 'A0001', 2),
('B0013', 'D0008', 'A0002', 1),
('B0014', 'D0008', 'A0011', 1),
('B0015', 'D0008', 'A0031', 3);

INSERT INTO PurchaseSlip (ID, PDate, PrdID, Pqnty) VALUES
('P0001', '2015-01-05', 'A0001', 2),
('P0002', '2015-01-05', 'A0011', 3),
('P0003', '2015-01-06', 'A0002', 15),
('P0004', '2015-01-06', 'A0003', 5),
('P0005', '2015-01-06', 'A0011', 5),
('P0006', '2015-01-07', 'A0012', 7),
('P0007', '2015-01-07', 'A0021', 20),
('P0008', '2015-01-07', 'A0022', 7),
('P0009', '2015-01-08', 'A0023', 5),
('P0010', '2015-01-08', 'A0024', 5),
('P0011', '2015-01-09', 'A0031', 7),
('P0012', '2015-01-09', 'A0032', 4);
----------------------------------------------------------
問１
CREATE VIEW View01 AS
SELECT ID AS 商品コード, Name AS 商品名, PPrc AS 仕入単価
FROM Product;

SELECT * FROM View01;

--問２
CREATE VIEW View02 AS
SELECT ID, Name, SupID, PPrc, SPrc
FROM Product
WHERE SupID = 'S0002';

SELECT * FROM View02;

--問３
CREATE VIEW View03 AS
SELECT PurchaseSlip.ID AS 仕入伝票番号, PDate AS 仕入日, Product.Name AS 商品名, 
       Product.PPrc AS 仕入単価, PurchaseSlip.Pqnty AS 仕入数量
FROM PurchaseSlip
JOIN Product ON PurchaseSlip.PrdID = Product.ID;

SELECT * FROM View03;

--問４
CREATE VIEW View04 AS
SELECT SalesInfo.PrdID AS 商品コード, SUM(SalesInfo.Sqnty) AS 販売数量合計
FROM SalesInfo
GROUP BY SalesInfo.PrdID;

SELECT * FROM View04;

--問５
CREATE VIEW View05 AS
SELECT SalesInfo.PrdID AS 商品コード, 
       SUM(SalesInfo.Sqnty * Product.SPrc) AS 販売金額
FROM SalesInfo
JOIN Product ON SalesInfo.PrdID = Product.ID
GROUP BY SalesInfo.PrdID;

SELECT * FROM View05;

--問６
CREATE VIEW View06 AS
SELECT PurchaseSlip.PrdID AS 商品コード, SUM(PurchaseSlip.Pqnty) AS 仕入数量合計
FROM PurchaseSlip
GROUP BY PurchaseSlip.PrdID;

SELECT * FROM View06;

--問７
CREATE VIEW View07 AS
SELECT PurchaseSlip.ID AS 仕入伝票番号, PurchaseSlip.PDate AS 仕入日, Supplier.ID AS 仕入先コード, 
       Supplier.Name AS 仕入先名, Product.Name AS 商品名, Product.PPrc AS 仕入単価, 
       PurchaseSlip.Pqnty AS 仕入数量, (Product.PPrc * PurchaseSlip.Pqnty) AS 仕入金額
FROM PurchaseSlip
JOIN Product ON PurchaseSlip.PrdID = Product.ID
JOIN Supplier ON Product.SupID = Supplier.ID;

SELECT * FROM View07;

--問８
CREATE VIEW View08 AS
SELECT 仕入先コード, 仕入先名, SUM(仕入金額) AS 仕入金額合計
FROM View07
GROUP BY 仕入先コード, 仕入先名;

SELECT * FROM View08;

--問９
CREATE VIEW View09 AS
SELECT SalesSlip.ID AS 販売伝票番号, SalesSlip.SDate AS 販売日, Customer.Name AS 販売先名, 
       SalesInfo.PrdID AS 商品コード, Product.Name AS 商品名, Product.SPrc AS 販売単価, 
       SalesInfo.Sqnty AS 販売数量, (Product.SPrc * SalesInfo.Sqnty) AS 販売金額
FROM SalesSlip
JOIN SalesInfo ON SalesSlip.ID = SalesInfo.SSlpID
JOIN Product ON SalesInfo.PrdID = Product.ID
JOIN Customer ON SalesSlip.CustID = Customer.ID;

SELECT * FROM View09;

--問１０
CREATE VIEW View10 AS
SELECT 商品コード, 商品名, SUM(販売金額) AS 販売金額合計
FROM View09
GROUP BY 商品コード, 商品名;

SELECT * FROM View10;
-- ----------------------------------------------------------
--5．クエリとビューの作成Ⅱ 
-- 商品ごとの在庫数と販売数の確認のビュー
CREATE VIEW View11 AS
SELECT Product.ID AS 商品コード, Product.Name AS 商品名, 
       Stock.Stk AS 在庫数, 
       IFNULL(SUM(SalesInfo.Sqnty), 0) AS 販売数量
FROM Product
LEFT JOIN Stock ON Product.ID = Stock.PrdID
LEFT JOIN SalesInfo ON Product.ID = SalesInfo.PrdID
GROUP BY Product.ID, Product.Name, Stock.Stk;

SELECT * FROM View11;

-- 在庫がゼロの商品のリストのビュー
CREATE VIEW View12 AS
SELECT Product.ID AS 商品コード, Product.Name AS 商品名, Stock.Stk AS 在庫数
FROM Product
JOIN Stock ON Product.ID = Stock.PrdID
WHERE Stock.Stk = 0;

SELECT * FROM View12;
--↑このビューは何も表示されてなくてよい（在庫がゼロの商品がないから）


-- DROP TABLE IF EXISTS Supplier;
-- DROP TABLE IF EXISTS Customer;
-- DROP TABLE IF EXISTS Product;
-- DROP TABLE IF EXISTS Stock;
-- DROP TABLE IF EXISTS SalesSlip;
-- DROP TABLE IF EXISTS SalesInfo;
-- DROP TABLE IF EXISTS PurchaseSlip;