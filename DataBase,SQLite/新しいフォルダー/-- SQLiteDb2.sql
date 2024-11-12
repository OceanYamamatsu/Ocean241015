-- SQLite
---- テーブルの構造 `Lending`　下記のSQL文をコピーして実行してください。
-- CREATE TABLE `Lending` (`ID` int(3) NOT NULL,`BookID` varchar(5) NOT NULL,`StudentID` varchar(3) NOT NULL,`CheckoutDate` date NOT NULL,`DueDate` date NOT NULL,`ReturnDate` date NOT NULL) ;
---- テーブルのデータ `Lending`
-- INSERT INTO `Lending` (`ID`, `BookID`, `StudentID`, `CheckoutDate`, `DueDate`, `ReturnDate`) VALUES (1, 'K-37', '2', '2015-04-08', '2015-04-15', '2015-04-10'),(2, 'U-91', '2', '2015-04-08', '2015-04-15', '2015-04-10'),(3, 'T-35', '23', '2015-04-08', '2015-04-15', '0000-00-00'),(4, 'A-69', '7', '2015-04-08', '2015-04-15', '2015-04-15'),(5, 'F-45', '36', '2015-04-09', '2015-04-16', '2015-04-10'),(6, 'N-58', '15', '2015-04-09', '2015-04-16', '2015-04-14'),(7, 'J-11', '17', '2015-04-09', '2015-04-16', '0000-00-00'),(8, 'F-45', '17', '2015-04-10', '2015-04-17', '0000-00-00'),(9, 'K-37', '19', '2015-04-10', '2015-04-17', '2015-04-16'),(10, 'U-91', '28', '2015-04-10', '2015-04-17', '2015-04-15');
-- select * from Lending;
---- テーブルの構造 `Book` 下記のSQL文をコピーして実行してください。
-- CREATE TABLE `Book` (`ID` varchar(5) NOT NULL,`Name` varchar(50) NOT NULL,`Type` int(1) NOT NULL) ;
---- テーブルのデータ `Book`
-- INSERT INTO `Book` (`ID`, `Name`, `Type`) VALUES ('A-69', 'IT産業の興亡', 6),('F-45', '富士山の岩と石', 4),('J-11', '17歳のための哲学入門', 1),('K-37', 'ケータイと学校文化', 3),('N-58', '日本の町工場', 5),('P-23', 'パリ歴史散歩', 2),('T-35', '統計でみる日本と世界の高校生', 3),('U-91', '海辺のフェリーチェ', 9);

select * from Lending;
select * from book;
-- select * from Lending, book;
----24/11/12
----Q1
select lending.id, bookid, name, Duedate, ReturnDate 
from Lending, book 
where bookid = book.id;
----Q2
select lending.id, bookid, name, StudentID, CheckoutDate, DueDate, ReturnDate 
from Lending, Book where Lending.BookID = Book.id and DueDate = '2015-04-17';
----Q3
select lending.id, Bookid, name, StudentID, CheckoutDate, DueDate
from lending, book 
where lending.bookid = book.id 
and DueDate >= '2015-04-16' and ReturnDate = '0000-00-00';

