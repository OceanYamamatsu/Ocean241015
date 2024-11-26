-- SQLite

-- create view [namae]
-- select from where

-- CREATE TABLE `Club` (`ID` int(11) NOT NULL primary key,`Name` varchar(50) NOT NULL,`Captain` varchar(50) NOT NULL,`Class` varchar(10) NOT NULL,`Adviser` varchar(50) NOT NULL,`Members` int(11) NOT NULL,`Type` char(1) NOT NULL,`Room` char(3) NOT NULL,`Budget` int(11) NOT NULL);
-- -- table作成

-- INSERT INTO `Club` (`ID`, `Name`, `Captain`, `Class`, `Adviser`, `Members`, `Type`, `Room`, `Budget`) 
-- VALUES (1, '演劇部', '矢野みかこ', '3-4', '大森', 21, '1', '501', 150000),
-- (2, '剣道部', '佐々木浩美', '2-4', '岡村', 8, '2', '502', 50000),
-- (3, 'サッカー部', '望月健太', '3-3', '斉藤', 38, '2', '401', 200000),
-- (4, '茶道部', '堀井ゆかり', '3-1', '杉浦', 14, '1', '304', 50000),
-- (5, '新聞部', '遠藤光二', '2-4', '大野', 9, '1', '123', 50000),
-- (6, '水泳部', '片桐洋平', '3-2', '吉川', 16, '2', '503', 100000),
-- (7, '吹奏楽部', '今野春香', '3-5', '山田', 22, '1', '303', 250000),
-- (8, 'テニス部', '川上さとし', '3-5', '山口', 19, '2', '403', 100000),
-- (9, '野球部', '阿部拓也', '3-1', '高田', 37, '2', '401', 200000),
-- (10, '陸上部', '岩本さなえ', '3-2', '田中', 22, '2', '401', 100000);
-- SELECT * from club;

-- -- 問１
-- create view Club2(name, captain, adviser, members)
-- as
-- select name, captain, adviser, members from club;

-- drop view club2;
-- select * from Club2;

-- -- 問２
-- create view TotalBudget(Type, TotalBaget)
-- as
-- select type, sum(budget) from club GROUP by type;
-- drop view club2;

-- SELECT * from TotalBaget;

-- 問３
-- SELECT type, TotalBaget from TotalBudget where type=1;