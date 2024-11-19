-- SQLite

-- テーブルの構造 `Student`

-- CREATE TABLE `Student` (`ID` varchar(3) NOT NULL,`Name` varchar(50) NOT NULL);

-- テーブルのデータのダンプ `Student`

-- INSERT INTO `Student` (`ID`, `Name`) VALUES('1', '井上孝'),('2', '上田亜希'),('3', '宇野さとし'),('4', '大久保啓子'),('5', '河村宏'),('6', '杉谷好美'),('7', '竹内雄一');

-- -- テーブルの構造 `Certification`

-- CREATE TABLE `Certification` (`ID` int(3) NOT NULL,`StudentID` varchar(3) NOT NULL,`CertificationID` varchar(4) NOT NULL,`CertificationName` varchar(100) NOT NULL,`PassingDate` date NOT NULL);
-- --
-- -- テーブルのデータのダンプ `Certification`

-- INSERT INTO `Certification` (`ID`, `StudentID`, `CertificationID`, `CertificationName`, `PassingDate`) VALUES(1, '2', 'D-3', '文書処理検定3級', '2015-06-12'),(2, '5', 'D-3', '文書処理検定3級', '2015-06-12'),(3, '6', 'D-3', '文書処理検定3級', '2015-06-12');
-- INSERT INTO `Certification` (`ID`, `StudentID`, `CertificationID`, `CertificationName`, `PassingDate`) VALUES(4, '2', 'S-3', '表計算検定3級', '2015-10-16'),(5, '3', 'S-3', '表計算検定3級', '2015-10-16');
-- INSERT INTO `Certification` (`ID`, `StudentID`, `CertificationID`, `CertificationName`, `PassingDate`) VALUES(6, '4', 'S-3', '表計算検定3級', '2015-10-16'),(7, '5', 'S-2', '表計算検定2級', '2015-10-16');
-- drop TABLE Student;
select * from Student;
select * from Certification;

-- --問１
-- select certificationname from Certification 
-- where studentid = ( SELECT id from student where name = '河村宏' );

-- --問２
-- select name from student 
-- where id in (select studentid 
-- from Certification where PassingDate = '2015-10-16');

-- --問３
-- select name from student 
-- where id in (select studentid 
-- from certification where certificationid = 'S-3');

--問４
select count(name) as '2015/10/16合格者数' from student 
where id in (select studentid 
from Certification where PassingDate = '2015-10-16');

--問５
select name from student where id in (select studentid 
from Certification where PassingDate >= '2015-01-01');

--問６
select CertificationID, CertificationName from Certification 
where StudentID in (select studentid from Student 
where id = '2' and '2015-10-01' >= PassingDate >= '2016-3-31');

--問７
select name from student where id 
not in (select studentid from Certification);