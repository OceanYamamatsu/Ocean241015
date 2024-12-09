-- SQLite
-- --から始まっている行は「コメント行」である。
--
-- テーブルの作成（下記のCREATE文をコピーして実行しなさい）
--
-- CREATE TABLE `Seminar` (`ID` int(11) NOT NULL primary key,`Teacher` varchar(50) NOT NULL,`Leader` varchar(50) NOT NULL,`Members` int(11) NOT NULL,`Type` int(1) NOT NULL,`Feature` varchar(30) NOT NULL,`Recruit` int(1) NOT NULL,`Budget` int(11) NOT NULL,`DOW` char(1) NOT NULL);
-- --
-- -- テーブルのデータの作成（下記のINSERT文をコピーして実行しなさい）
-- --
-- INSERT INTO `Seminar` (`ID`, `Teacher`, `Leader`, `Members`, `Type`, `Feature`, `Recruit`, `Budget`, `DOW`) VALUES(1,'石田','中村',36,1,'世界・英語',1,100000,1),(2,'出田','野原',16,3,'情報技術',1,300000,3),(3,'和泉','波津',10,3,'情報・モデル化',1,300000,2),(4,'梅川','浜岡',24,2,'地域',1,200000,4),(5,'加瀬','増山',32,3,'情報・心理学',2,100000,5),(6,'木田','浮合',15,3,'会計',1,100000,2),(7,'金山','水森',10,1,'世界とアジア',1,500000,3),(8,'久保','良岡',18,3,'情報・統計',1,300000,5),(9,'小東','田村',22,3,'マーケティング',1,200000,4),(10,'松澤','横島',26,1,'地域ビジネス',1,200000,3),(11,'彩川','清竹',20,3,'情報・マルチメディア',1,300000,5),(12,'齋田','五島',18,3,'情報倫理',1,100000,2),(13,'杉下','唐山',34,1,'スポーツ',2,200000,1),(14,'日笠','菅沢',12,1,'法律',2,100000,1),(15,'山坂','竹本',26,1,'地域・イノベーション',2,100000,3),(16,'下山','上庭',26,1,'社会制度',1,100000,5),(17,'杉山','峰岸',38,1,'レジャー',1,300000,4),(18,'高田','大林',22,1,'世界の哲学',1,100000,2),(19,'中川','佐藤',28,2,'メディア',1,200000,3),(20,'中田','関田',16,2,'地域政策',1,200000,4);
select * from seminar;
SELECT DISTINCT Teacher FROM Seminar;
SELECT DISTINCT Teacher, Feature FROM Seminar;
SELECT Teacher, Leader, Members FROM Seminar;
SELECT DISTINCT Teacher FROM Seminar WHERE Members < 10;
SELECT Teacher, Leader FROM Seminar WHERE Leader = '彩川';
SELECT Teacher, Members, Feature FROM Seminar WHERE Members >= 20;
SELECT Teacher, Type, Members, Budget FROM Seminar WHERE Type = 2 AND Members <= 20;
SELECT Teacher, Type, Members FROM Seminar WHERE Type = 2 OR Members <= 20;
SELECT Teacher, Type, Budget FROM Seminar WHERE Type != 2;
SELECT Teacher, Type, Members FROM Seminar WHERE Members < 20;
SELECT SUM(Members) AS Total, AVG(Members) AS Average, MIN(Members) AS Min, MAX(Members) AS Max, COUNT(*) AS Count FROM Seminar;
SELECT MAX(Budget) - MIN(Budget) AS Difference FROM Seminar;
SELECT COUNT(*) AS 募集停止ゼミ数 FROM Seminar WHERE Recruit = 2;
SELECT Teacher, Type, Members FROM Seminar ORDER BY Type ASC, Members DESC;
SELECT Teacher, Members FROM Seminar WHERE Recruit = 2 ORDER BY Members DESC;
SELECT DISTINCT DOW FROM Seminar;
SELECT * FROM Seminar WHERE Budget BETWEEN 150000 AND 299999;
SELECT Teacher, Leader, Feature FROM Seminar WHERE Teacher IN ('加瀬', '野原', '横島', '下山');
SELECT Teacher, Feature FROM Seminar WHERE Feature LIKE '%情報%';
SELECT Type, Budget FROM Seminar GROUP BY Type, Budget;
SELECT Type, AVG(Members) AS 平均 FROM Seminar GROUP BY Type;
SELECT Type, AVG(Members) AS 平均 FROM Seminar GROUP BY Type HAVING AVG(Members) >= 20;
