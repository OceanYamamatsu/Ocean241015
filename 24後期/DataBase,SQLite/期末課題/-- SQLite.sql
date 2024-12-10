-- -- SQLite3
-- -- 販売先マスタ (Customer)
-- CREATE TABLE Customer (
--     ID CHAR(5) PRIMARY KEY,              -- 販売先コード
--     Name VARCHAR(100) NOT NULL,         -- 販売先名
--     Addr VARCHAR(200) NOT NULL,         -- 販売先住所
--     Tel VARCHAR(11) NOT NULL            -- 販売先電話番号
-- );

-- -- 仕入先マスタ (Supplier)
-- CREATE TABLE Supplier (
--     ID CHAR(5) PRIMARY KEY,              -- 仕入先コード
--     Name VARCHAR(100) NOT NULL,         -- 仕入先名
--     Addr VARCHAR(200) NOT NULL,         -- 仕入先住所
--     Tel VARCHAR(11) NOT NULL            -- 仕入先電話番号
-- );

-- -- 在庫表 (Stock)
-- CREATE TABLE Stock (
--     PrdID CHAR(5) PRIMARY KEY,          -- 商品コード (ProductのIDと同様の値)
--     Stk INT NOT NULL                    -- 在庫数
-- );

-- -- 商品マスタ (Product)
-- CREATE TABLE Product (
--     ID CHAR(5) PRIMARY KEY,              -- 商品コード
--     Name VARCHAR(50) NOT NULL,          -- 商品名
--     SupID CHAR(5) NOT NULL,             -- 仕入先コード (SupplierのIDと同様の値)
--     PPrc INT NOT NULL,                  -- 仕入単価
--     SPrc INT NOT NULL,                  -- 販売単価
--     FOREIGN KEY (SupID) REFERENCES Supplier(ID)
-- );

-- -- 販売伝票表 (Sales Slip)
-- CREATE TABLE SalesSlip (
--     ID CHAR(5) PRIMARY KEY,              -- 販売伝票番号
--     SDate DATE NOT NULL,                -- 販売日
--     CustID CHAR(5) NOT NULL,            -- 販売先コード (CustomerのIDと同様の値)
--     FOREIGN KEY (CustID) REFERENCES Customer(ID)
-- );

-- -- 仕入伝票表 (Purchase Slip)
-- CREATE TABLE PurchaseSlip (
--     ID CHAR(5) PRIMARY KEY,              -- 仕入伝票番号
--     PDate DATE NOT NULL,                -- 仕入日
--     PrdID CHAR(5) NOT NULL,             -- 商品コード (ProductのIDと同様の値)
--     Panty INT NOT NULL,                 -- 仕入数量
--     FOREIGN KEY (PrdID) REFERENCES Product(ID)
-- );

-- -- 商品販売表
-- CREATE TABLE Sales (
--     ID CHAR(5) PRIMARY KEY,              -- 販売No
--     SSIPID CHAR(5) NOT NULL,            -- 販売伝票番号 (SalesSlipのIDと同様の値)
--     PrdID CHAR(5) NOT NULL,             -- 商品コード (ProductのIDと同様の値)
--     Santy INT NOT NULL,                 -- 販売数量
--     FOREIGN KEY (SSIPID) REFERENCES SalesSlip(ID),
--     FOREIGN KEY (PrdID) REFERENCES Product(ID)
-- );

-- 1) 商品販売表 (Sales)
-- INSERT INTO Sales (ID, SSIPID, PrdID, Santy) VALUES
-- (0, 'D0001', 'A0001', 1),
-- (1, 'D0001', 'A0024', 4),
-- (2, 'D0001', 'A0031', 4),
-- (3, 'D0002', 'A0002', 2),
-- (4, 'D0002', 'A0031', 1),
-- (5, 'D0003', 'A0002', 3),
-- (6, 'D0003', 'A0022', 4),
-- (7, 'D0004', 'A0022', 2),
-- (8, 'D0005', 'A0012', 2),
-- (9, 'D0006', 'A0003', 2),
-- (10, 'D0007', 'A0023', 3),
-- (11, 'D0008', 'A0001', 2),
-- (12, 'D0008', 'A0002', 1),
-- (13, 'D0008', 'A0011', 1),
-- (14, 'D0008', 'A0031', 3);

-- -- 2) 販売伝票表 (SalesSlip)
-- INSERT INTO SalesSlip (ID, SDate, CustID) VALUES
-- ('D0001', '2015-01-10', 'H0001'),
-- ('D0002', '2015-01-10', 'H0002'),
-- ('D0003', '2015-01-10', 'H0003'),
-- ('D0004', '2015-01-10', 'H0005'),
-- ('D0005', '2015-01-10', 'H0006'),
-- ('D0006', '2015-01-10', 'H0007'),
-- ('D0007', '2015-01-10', 'H0008'),
-- ('D0008', '2015-01-15', 'H0004');

-- -- 3) 販売先マスタ (Customer)
-- INSERT INTO Customer (ID, Name, Addr, Tel) VALUES
-- ('H0001', '岸田商店', '栃木県宇都宮市', '123-234-3456'),
-- ('H0002', '勝又電気', '千葉県千葉市', '234-345-4567'),
-- ('H0003', '佐野電気', '長崎県長崎市', '345-456-5678'),
-- ('H0004', '堀商店', '大阪府大阪市', '456-678-6789'),
-- ('H0005', '池谷商店', '東京都新宿区', '567-789-8901'),
-- ('H0006', '岩佐電気店', '神奈川県横浜市', '789-890-9012'),
-- ('H0007', '向井電気', '福島県福島市', '987-876-7654'),
-- ('H0008', '松下商会', '富山県富山市', '765-654-5432');

-- -- 4) 仕入伝票表 (PurchaseSlip)
-- INSERT INTO PurchaseSlip (ID, PDate, PrdID, Panty) VALUES
-- (0, '2015-01-05', 'A0001', 2),
-- (1, '2015-01-05', 'A0011', 3),
-- (2, '2015-01-06', 'A0002', 15),
-- (3, '2015-01-06', 'A0003', 5),
-- (4, '2015-01-06', 'A0011', 5),
-- (5, '2015-01-07', 'A0012', 7),
-- (6, '2015-01-07', 'A0021', 20),
-- (7, '2015-01-07', 'A0022', 7),
-- (8, '2015-01-08', 'A0023', 5),
-- (9, '2015-01-08', 'A0024', 5),
-- (10, '2015-01-09', 'A0031', 7),
-- (11, '2015-01-09', 'A0032', 4);

-- -- 5) 商品マスタ (Product)
-- INSERT INTO Product (ID, Name, SupID, PPrc, SPrc) VALUES
-- ('A0001', '液晶テレビ', 'S0001', 50160, 62700),
-- ('A0002', 'プラズマテレビ', 'S0002', 81440, 101800),
-- ('A0003', 'プロジェクタ', 'S0003', 50160, 62700),
-- ('A0011', 'DVDプレーヤ', 'S0001', 3150, 4500),
-- ('A0012', 'ブルーレイプレーヤ', 'S0004', 9090, 12980),
-- ('A0021', 'MP3プレーヤ', 'S0003', 17040, 21300),
-- ('A0022', 'スピーカ', 'S0001', 20290, 25360),
-- ('A0023', 'CDプレーヤ', 'S0002', 21020, 26720),
-- ('A0024', 'ICレコーダ', 'S0004', 5490, 6860),
-- ('A0031', 'FAX', 'S0003', 14670, 16300),
-- ('A0032', '電話機', 'S0001', 11520, 12800);

-- -- 6) 在庫表 (Stock)
-- INSERT INTO Stock (PrdID, Stk) VALUES
-- ('A0001', 10),
-- ('A0002', 10),
-- ('A0003', 10),
-- ('A0011', 10),
-- ('A0012', 10),
-- ('A0021', 10),
-- ('A0022', 10),
-- ('A0023', 10),
-- ('A0024', 10),
-- ('A0031', 10),
-- ('A0032', 10);
SELECT * from Customer;
SELECT * from Supplier;
SELECT * from Stock;
SELECT * from Product;
SELECT * from SalesSlip;
SELECT * from PurchaseSlip;
SELECT * from SalesInfo;