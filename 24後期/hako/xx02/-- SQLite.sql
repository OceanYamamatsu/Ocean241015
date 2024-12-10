-- SQLite

-- SQLite
-- 販売先マスタ (Customer)
CREATE TABLE Customer (
    ID CHAR(5) PRIMARY KEY,              -- 販売先コード
    Name VARCHAR(100) NOT NULL,         -- 販売先名
    Addr VARCHAR(200) NOT NULL,         -- 販売先住所
    Tel VARCHAR(11) NOT NULL            -- 販売先電話番号
);

-- 仕入先マスタ (Supplier)
CREATE TABLE Supplier (
    ID CHAR(5) PRIMARY KEY,              -- 仕入先コード
    Name VARCHAR(100) NOT NULL,         -- 仕入先名
    Addr VARCHAR(200) NOT NULL,         -- 仕入先住所
    Tel VARCHAR(11) NOT NULL            -- 仕入先電話番号
);

-- 在庫表 (Stock)
CREATE TABLE Stock (
    PrdID CHAR(5) PRIMARY KEY,          -- 商品コード (ProductのIDと同様の値)
    Stk INT NOT NULL                    -- 在庫数
);

-- 商品マスタ (Product)
CREATE TABLE Product (
    ID CHAR(5) PRIMARY KEY,              -- 商品コード
    Name VARCHAR(50) NOT NULL,          -- 商品名
    SupID CHAR(5) NOT NULL,             -- 仕入先コード (SupplierのIDと同様の値)
    PPrc INT NOT NULL,                  -- 仕入単価
    SPrc INT NOT NULL,                  -- 販売単価
    FOREIGN KEY (SupID) REFERENCES Supplier(ID)
);

-- 販売伝票表 (Sales Slip)
CREATE TABLE SalesSlip (
    ID CHAR(5) PRIMARY KEY,              -- 販売伝票番号
    SDate DATE NOT NULL,                -- 販売日
    CustID CHAR(5) NOT NULL,            -- 販売先コード (CustomerのIDと同様の値)
    FOREIGN KEY (CustID) REFERENCES Customer(ID)
);

-- 仕入伝票表 (Purchase Slip)
CREATE TABLE PurchaseSlip (
    ID CHAR(5) PRIMARY KEY,              -- 仕入伝票番号
    PDate DATE NOT NULL,                -- 仕入日
    PrdID CHAR(5) NOT NULL,             -- 商品コード (ProductのIDと同様の値)
    Pqnty INT NOT NULL,                 -- 仕入数量
    FOREIGN KEY (PrdID) REFERENCES Product(ID)
);

-- 商品販売表
CREATE TABLE SalesInfo (
    ID CHAR(5) PRIMARY KEY,              -- 販売No
    SSIPID CHAR(5) NOT NULL,            -- 販売伝票番号 (SalesSlipのIDと同様の値)
    PrdID CHAR(5) NOT NULL,             -- 商品コード (ProductのIDと同様の値)
    Sqnty INT NOT NULL,                 -- 販売数量
    FOREIGN KEY (SSIPID) REFERENCES SalesSlip(ID),
    FOREIGN KEY (PrdID) REFERENCES Product(ID)
);


-- 1) 商品販売表 (SalesInfo)
INSERT INTO SalesInfo (ID, SSIPID, PrdID, Sqnty) VALUES
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

-- 2) 販売伝票表 (SalesSlip)
INSERT INTO SalesSlip (ID, SDate, CustID) VALUES
('D0001', '2015-01-10', 'H0001'),
('D0002', '2015-01-10', 'H0002'),
('D0003', '2015-01-10', 'H0003'),
('D0004', '2015-01-10', 'H0005'),
('D0005', '2015-01-10', 'H0006'),
('D0006', '2015-01-10', 'H0007'),
('D0007', '2015-01-10', 'H0008'),
('D0008', '2015-01-15', 'H0004');

-- 3) 販売先マスタ (Customer)
INSERT INTO Customer (ID, Name, Addr, Tel) VALUES
('H0001', '岸田商店', '栃木県宇都宮市', '123-234-3456'),
('H0002', '勝又電気', '千葉県千葉市', '234-345-4567'),
('H0003', '佐野電気', '長崎県長崎市', '345-456-5678'),
('H0004', '堀商店', '大阪府大阪市', '456-678-6789'),
('H0005', '池谷商店', '東京都新宿区', '567-789-8901'),
('H0006', '岩佐電気店', '神奈川県横浜市', '789-890-9012'),
('H0007', '向井電気', '福島県福島市', '987-876-7654'),
('H0008', '松下商会', '富山県富山市', '765-654-5432');

-- 4) 仕入伝票表 (PurchaseSlip)
INSERT INTO PurchaseSlip (ID, PDate, PrdID, Pqnty) VALUES
('C0001', '2015-01-05', 'A0001', 2),
('C0002', '2015-01-05', 'A0011', 3),
('C0003', '2015-01-06', 'A0002', 15),
('C0004', '2015-01-06', 'A0003', 5),
('C0005', '2015-01-06', 'A0011', 5),
('C0006', '2015-01-07', 'A0012', 7),
('C0007', '2015-01-07', 'A0021', 20),
('C0008', '2015-01-07', 'A0022', 7),
('C0009', '2015-01-08', 'A0023', 5),
('C0010', '2015-01-08', 'A0024', 5),
('C0011', '2015-01-09', 'A0031', 7),
('C0012', '2015-01-09', 'A0032', 4);

-- 5) 商品マスタ (Product)
INSERT INTO Product (ID, Name, SupID, PPrc, SPrc) VALUES
('A0001', '液晶テレビ', 'S0001', 50160, 62700),
('A0002', 'プラズマテレビ', 'S0002', 81440, 101800),
('A0003', 'プロジェクタ', 'S0003', 50160, 62700),
('A0011', 'DVDプレーヤ', 'S0001', 3150, 4500),
('A0012', 'ブルーレイプレーヤ', 'S0004', 9090, 12980),
('A0021', 'MP3プレーヤ', 'S0003', 17040, 21300),
('A0022', 'スピーカ', 'S0001', 20290, 25360),
('A0023', 'CDプレーヤ', 'S0002', 21020, 26720),
('A0024', 'ICレコーダ', 'S0004', 5490, 6860),
('A0031', 'FAX', 'S0003', 14670, 16300),
('A0032', '電話機', 'S0001', 11520, 12800);

-- 6) 在庫表 (Stock)
INSERT INTO Stock (PrdID, Stk) VALUES
('A0001', 10),
('A0002', 10),
('A0003', 10),
('A0011', 10),
('A0012', 10),
('A0021', 10),
('A0022', 10),
('A0023', 10),
('A0024', 10),
('A0031', 10),
('A0032', 10);


select * from SalesInfo;
select * from SalesSlip;
select * from Customer;
select * from PurchaseSlip;
select * from Product;
select * from Stock;

--1
SELECT ID AS 商品コード, Name AS 商品名, PPrc AS 仕入単価
FROM Product;

--2

SELECT ID AS 商品コード, Name AS 商品名, PPrc AS 仕入単価, SPrc AS 販売単価
FROM Product
WHERE SupID = 'S0002';

--3
SELECT 
    PurchaseSlip.ID AS 仕入伝票番号,
    PurchaseSlip.PDate AS 仕入日,
    Product.Name AS 商品名,
    Product.PPrc AS 仕入単価,
    PurchaseSlip.Pqnty AS 仕入数量
FROM 
    PurchaseSlip
JOIN 
    Product ON PurchaseSlip.PrdID = Product.ID;

--4
SELECT 
    Product.ID AS 商品コード,
    Product.Name AS 商品名,
    SUM(SalesInfo.Sqnty) AS 販売数量合計
FROM 
    SalesInfo
JOIN 
    Product ON SalesInfo.PrdID = Product.ID
GROUP BY 
    Product.ID, Product.Name;

--5
SELECT 
    SalesInfo.ID AS 販売No,
    Product.ID AS 商品コード,
    Product.Name AS 商品名,
    Product.SPrc AS 販売単価,
    SalesInfo.Sqnty AS 販売数量,
    Product.SPrc * SalesInfo.Sqnty AS 販売金額
FROM 
    SalesInfo
JOIN 
    Product ON SalesInfo.PrdID = Product.ID;

--6
SELECT 
    Product.ID AS 商品コード,
    Product.Name AS 商品名,
    SUM(PurchaseSlip.Pqnty) AS 仕入数量合計
FROM 
    PurchaseSlip
JOIN 
    Product ON PurchaseSlip.PrdID = Product.ID
GROUP BY 
    Product.ID, Product.Name;

--7
CREATE VIEW PurchaseSummary AS
SELECT 
    PurchaseSlip.ID AS 仕入伝票番号,
    PurchaseSlip.PDate AS 仕入日,
    Supplier.ID AS 仕入先コード,
    Supplier.Name AS 仕入先名,
    Product.Name AS 商品名,
    Product.PPrc AS 仕入単価,
    PurchaseSlip.Pqnty AS 仕入数量,
    Product.PPrc * PurchaseSlip.Pqnty AS 仕入金額
FROM 
    PurchaseSlip
JOIN 
    Product ON PurchaseSlip.PrdID = Product.ID
JOIN 
    Supplier ON Product.SupID = Supplier.ID;

SELECT * FROM PurchaseSummary; -- ビューを表示

-- --8
-- SELECT 
--     仕入先コード,
--     仕入先名,
--     SUM(仕入金額) AS 仕入金額合計
-- FROM 
--     PurchaseSummary
-- GROUP BY 
--     仕入先コード, 仕入先名;

--8
SELECT 
    Supplier AS 仕入先コード,
    SupplierName AS 仕入先名,
    SUM(PurchaseAmount) AS 合計仕入金額
FROM 
    PurchaseSummary
GROUP BY 
    Supplier, SupplierName
ORDER BY 
    Supplier;


--9
CREATE VIEW SalesSummary AS
SELECT 
    SalesSlip.ID AS 販売伝票番号,
    SalesSlip.SDate AS 販売日,
    Customer.Name AS 販売先名,
    Product.ID AS 商品コード,
    Product.Name AS 商品名,
    Product.SPrc AS 販売単価,
    SalesInfo.Sqnty AS 販売数量,
    Product.SPrc * SalesInfo.Sqnty AS 販売金額
FROM 
    SalesSlip
JOIN 
    SalesInfo ON SalesInfo.SSIPID = SalesSlip.ID
JOIN 
    Product ON SalesInfo.PrdID = Product.ID
JOIN 
    Customer ON SalesSlip.CustID = Customer.ID;

SELECT * FROM SalesSummary; -- ビューを表示

--10
SELECT 
    商品コード,
    商品名,
    SUM(販売金額) AS 販売金額合計
FROM 
    SalesSummary
GROUP BY 
    商品コード, 商品名;

