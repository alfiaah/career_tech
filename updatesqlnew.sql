/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.6.16 : Database - career_techs_new
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`career_techs_new` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `career_techs_new`;

/*Table structure for table `answer` */

DROP TABLE IF EXISTS `answer`;

CREATE TABLE `answer` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `test_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `mark_awarded` varchar(50) DEFAULT NULL,
  `grand_total` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `exam_attend` varchar(50) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`answer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `answer` */

insert  into `answer`(`answer_id`,`test_type_id`,`user_id`,`mark_awarded`,`grand_total`,`date`,`exam_attend`,`company_id`) values 
(1,1,14,'2','3','2023-04-27','attend',1),
(2,2,14,'0','2','2023-04-27','attend',1),
(3,7,14,'1','2','2023-04-27','attend',4),
(4,6,14,'1','2','2023-04-27','attend',4),
(5,1,14,'0','3','2023-04-27','attend',4),
(6,2,14,'0','1','2023-04-27','attend',4),
(7,3,14,'2','2','2023-04-27','attend',4),
(8,5,14,'2','3','2023-04-27','attend',4),
(9,8,14,'1','1','2023-04-27','attend',4),
(10,9,14,'1','1','2023-04-27','attend',4),
(11,1,14,'1','1','2023-04-27','attend',8);

/*Table structure for table `answers` */

DROP TABLE IF EXISTS `answers`;

CREATE TABLE `answers` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `mark` int(11) DEFAULT NULL,
  PRIMARY KEY (`answer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=149 DEFAULT CHARSET=latin1;

/*Data for the table `answers` */

insert  into `answers`(`answer_id`,`user_id`,`mark`) values 
(88,8,4),
(79,2,4),
(78,2,4),
(77,2,3),
(76,2,2),
(40,4,4),
(39,4,4),
(38,4,1),
(37,4,4),
(36,4,3),
(41,5,3),
(42,5,4),
(43,5,2),
(44,5,1),
(45,5,3),
(46,6,2),
(47,6,3),
(48,6,4),
(49,6,5),
(50,6,1),
(90,9,3),
(89,8,3),
(87,8,1),
(86,8,5),
(85,8,4),
(84,8,3),
(91,9,4),
(92,9,3),
(93,9,4),
(94,9,1),
(95,9,4),
(131,10,3),
(130,10,3),
(129,10,1),
(128,10,2),
(127,10,3),
(126,10,4),
(148,11,5),
(147,11,2),
(146,11,3),
(145,11,4),
(144,11,3);

/*Table structure for table `application` */

DROP TABLE IF EXISTS `application`;

CREATE TABLE `application` (
  `application_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `resume_path` varchar(500) DEFAULT NULL,
  `personality` varchar(100) DEFAULT NULL,
  `skill` varchar(50) DEFAULT NULL,
  `mark` int(50) DEFAULT NULL,
  `job_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `application_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`application_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `application` */

insert  into `application`(`application_id`,`user_id`,`date`,`resume_path`,`personality`,`skill`,`mark`,`job_id`,`company_id`,`application_status`) values 
(1,14,'2023-04-20','static/uploads/8b6b9c66-6b5d-4fe1-ac8e-6179b92f0603cv.docx','0','Python',0,7,4,'You Are Selected'),
(2,14,'2023-04-20','static/uploads/5f3fc8f9-d193-4057-83b5-2cf61b1c8dc8cv.docx','0','Python',0,8,4,'You Are Rejected'),
(3,14,'2023-04-20','static/uploads/7d1acdd7-84b0-41d4-ac4b-1d3fe1c5f878cv.docx','0','Php',0,9,5,'pending'),
(4,14,'2023-04-20','static/uploads/37cc4754-b605-4c03-9f3f-dbbba235c654cv.docx','0','Python',0,10,6,'pending'),
(5,14,'2023-04-25','static/uploads/8d22943b-e17e-4b29-820c-3afd8f509085cv.docx','0','Python',0,12,7,'pending'),
(6,14,'2023-04-27','static/uploads/a7d62c7b-ee1b-4e32-999a-32acf6de2040Cover Letter - ALFIA A H.pdf','0','C',0,4,2,'pending'),
(7,15,'2023-04-27','static/uploads/5bdff8fb-2625-4080-85d5-3eed97fa7280Cover Letter - ALFIA A H.pdf','0','C',0,8,4,'pending');

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `company` */

insert  into `company`(`company_id`,`login_id`,`company`,`place`,`phone`,`email`) values 
(1,9,'company1','alp','9874563211','c1@mail'),
(2,10,'company2','tvm','9876541233','c2@mail'),
(4,19,'Simplex','Aluva','9387015546','simplexplaza@gmail.com'),
(5,21,'ijij','kjkj','1234567891','ahdd@gmail.com'),
(6,22,'plaza','asokapuram','8547007763','plaza@gmail.com'),
(7,23,'techarts','Perumbavoor','2616979562','techart@gmail.com'),
(8,24,'techassist','aluva','9856742315','techassist@gmail.com');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`user_type`,`complaint`,`reply`,`date`) values 
(1,14,'user','hi','pending','2023-04-20'),
(2,14,'user','ddfef','pending','2023-04-20'),
(3,4,'company','sfwe','hi','2023-04-20'),
(4,14,'user','ghgjhj','bh','2023-04-20');

/*Table structure for table `job` */

DROP TABLE IF EXISTS `job`;

CREATE TABLE `job` (
  `job_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `job` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `last_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `job` */

insert  into `job`(`job_id`,`company_id`,`job`,`details`,`last_date`) values 
(13,8,'PHP Developer','Python,Sql,Java','2023-04-08'),
(4,2,'c2job2c','deeeeeeeetailsccc','2023-05-17'),
(12,7,'PHP Developer','Python,Sql,Java','2023-04-02'),
(7,4,'PHP Developer','Sql,php','2023-04-30'),
(8,4,'Python Developer','Python Full Stack','2023-05-06'),
(9,5,'PHP Developer','Sql,php','2023-04-30'),
(10,6,'Software Engineer','Python,Sql,Java','2023-05-31');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'user1','user1','user'),
(2,'user2','user2','user'),
(3,'user3','user3','user'),
(4,'user4','user4','user'),
(5,'user5','user5','user'),
(6,'user6','user6','user'),
(7,'user7','user7','user'),
(8,'admin','admin','admin'),
(9,'company1','company1','company'),
(10,'company2','company2','company'),
(11,'user10','user10','user'),
(12,'user20','user20','user'),
(13,'user25','user25','user'),
(14,'user24','user24','user'),
(15,'user100','user100','user'),
(16,'user50','user50','user'),
(18,'alfia','alfia','user'),
(19,'simplex','simplex','company'),
(20,'akshay','akshay','user'),
(21,'ijo','1234','company'),
(22,'plaza','plaza','company'),
(23,'techart','techart','company'),
(24,'techassist','techassist','company');

/*Table structure for table `online_test` */

DROP TABLE IF EXISTS `online_test`;

CREATE TABLE `online_test` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `test_type_id` int(11) DEFAULT NULL,
  `question` varchar(200) DEFAULT NULL,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `correct_option` varchar(50) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;

/*Data for the table `online_test` */

insert  into `online_test`(`exam_id`,`test_type_id`,`question`,`option1`,`option2`,`option3`,`correct_option`,`company_id`) values 
(1,1,'sdfghjk','qwe','asd','zxc','asd',1),
(2,1,'dhcbdfgdhgv','poi','lkj','mnb','lkj',1),
(3,1,'hdvegdv','yui','hjk','bnm','yui',1),
(4,2,'dvbjhe','qaz','wsx','edc','edc',1),
(5,2,'jbdjd','edc','rfv','tgb','rfv',2),
(6,2,'ehrgesbv','yhn','ujm','ikl','ikl',2),
(7,3,'asasfsfs','qwerty','asdfg','zxcvb','qwerty',2),
(8,3,'rgreha','ergaer','ergae','asd','asd',1),
(9,2,'fhbvjrhebvrkh','mnb','yhr','etbnte','yhr',1),
(10,5,'A man is swimming in a stream which flows at the r','7.5','9.5','4.5','4.5',4),
(12,5,'Odd one out (3, 5, 11, 14, 17, 21)','21','17','14','14',4),
(13,6,'Which is the correct hierarchy of arithmetic opera',' / + * -',' / * + -',' * - / +',' / * + -',4),
(14,6,'Which is the correct usage of conditional operator','a>b ? c=30 : c=40;','a>b ? c=30;','max = a>b ? a>c?a:c:b>c?b:c','max = a>b ? a>c?a:c:b>c?b:c',4),
(15,1,'What is the probability of getting a sum 9 from tw',' 1/6','1/9',' 1/12','1/9',4),
(16,1,'probability of getting at most two heads in 3 unbi',' 7/8','3/8','3/4',' 7/8',4),
(17,7,'SCD, TEF, UGH, ____, WKL','UJI','VIJ','IJT','VIJ',4),
(18,7,' B2CD, _____, BCD4, B5CD, BC6D','B2C2D','BC3D','B2C3D','BC3D',4),
(19,1,'Odd one out (3, 5, 11, 14, 17, 21)','3','14','11','14',4),
(20,2,'asdadfwe','a','b','c','d',4),
(21,3,'njjokkk','abc','123','efg','123',4),
(22,5,'A train running at the speed of 60km/hr crosses a pole in 9 seconds. What is the length of the train','7.5','9.5','4.5','4.5',4),
(23,3,'dsf','7.5','ef','d','ef',4),
(24,8,'12345','1','2','3','2',4),
(25,1,'216594625','2','65','36','65',5),
(26,2,'asfcafuHW','as','asd','agrr','as',5),
(27,3,'A train 125m long passes a man, running at 5km/h in the same direction in which the train is going, in 10 seconds. The speed of the train is','7.5','9.5','4.5','4.5',5),
(28,5,'A train 125m long passes a man, running at 5km/h in the same direction in which the train is going, in 10 seconds. The speed of the train is','21','17','14','14',5),
(29,6,'abcde','ab','cd','e','e',5),
(30,8,'Odd one out (3, 5, 11, 14, 17, 21)','21','17','14','14',5),
(31,7,'SCD, TEF, UGH, ____, WKL','asd','ads','wrqf','ads',5),
(32,1,'abcde','ab','bc','','',6),
(33,1,'abcde','ab','cd','e','e',6),
(34,2,'123456','12','34','56','56',6),
(35,3,'dsf','g','j','d','d',6),
(36,5,'A train running at the speed of 60km/hr crosses a pole in 9 seconds. What is the length of the train','7.5','9.5','4.5','4.5',6),
(37,6,'gwe4fdgf','gwe','4fd','235','235',6),
(38,7,'SCD, TEF, UGH, ____, WKL','wfq','sfs','sff','sff',6),
(39,8,'Odd one out (3, 5, 11, 14, 17, 21)','3','5','14','14',6),
(40,9,'test1','1234','5678','abcd','abcd',4),
(41,1,'12356458','1','2','3','3',8);

/*Table structure for table `questionanswer` */

DROP TABLE IF EXISTS `questionanswer`;

CREATE TABLE `questionanswer` (
  `qstansr_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `answer` varchar(500) DEFAULT NULL,
  `mark` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`qstansr_id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

/*Data for the table `questionanswer` */

insert  into `questionanswer`(`qstansr_id`,`question_id`,`answer`,`mark`) values 
(1,1,'option1','1'),
(2,1,'option2','2'),
(3,1,'option3','3'),
(4,1,'option4','4'),
(5,1,'option5','5'),
(6,2,'option1','1'),
(7,2,'option2','2'),
(8,2,'option3','3'),
(9,2,'option4','4'),
(10,2,'option5','5'),
(11,3,'option1','1'),
(12,3,'option2','2'),
(13,3,'option3','3'),
(14,3,'option4','4'),
(15,3,'option5','5'),
(16,4,'option1','1'),
(17,4,'option2','2'),
(18,4,'option3','3'),
(19,4,'option4','4'),
(20,4,'option5','5'),
(30,6,'option 5','5'),
(29,6,'option 4','4'),
(28,6,'option 3','3'),
(27,6,'option 2','2'),
(26,6,'option1','1');

/*Table structure for table `questions` */

DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `question_id` int(50) NOT NULL AUTO_INCREMENT,
  `question` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `questions` */

insert  into `questions`(`question_id`,`question`) values 
(1,'Question1'),
(2,'Question2'),
(3,'Question3'),
(4,'Question4'),
(6,'Question5');

/*Table structure for table `team` */

DROP TABLE IF EXISTS `team`;

CREATE TABLE `team` (
  `team_id` int(11) NOT NULL AUTO_INCREMENT,
  `team` varchar(100) DEFAULT NULL,
  `no_of_members` varchar(100) DEFAULT NULL,
  `skill` varchar(50) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `team` */

insert  into `team`(`team_id`,`team`,`no_of_members`,`skill`,`company_id`) values 
(1,'team1p','15','Python',1),
(2,'team2a','5','android',1),
(3,'team1c2','5','Python',2),
(4,'team2c2','5','C',2);

/*Table structure for table `teammember` */

DROP TABLE IF EXISTS `teammember`;

CREATE TABLE `teammember` (
  `taemmember_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `team_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`taemmember_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `teammember` */

insert  into `teammember`(`taemmember_id`,`user_id`,`team_id`) values 
(1,1,1),
(2,2,4),
(3,4,3),
(4,3,2),
(5,6,1),
(6,8,3),
(7,9,1);

/*Table structure for table `test_type` */

DROP TABLE IF EXISTS `test_type`;

CREATE TABLE `test_type` (
  `test_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`test_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `test_type` */

insert  into `test_type`(`test_type_id`,`type`) values 
(1,'arithemetic'),
(2,'technical'),
(3,'level1'),
(5,'Aptitude'),
(6,'Programming'),
(7,'Reasoning'),
(8,'logical'),
(9,'test1'),
(10,'test2');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,1,'usera','fvbn','aaaaaaaaaaaaaaaaaaaaa','741236985','user1@mail'),
(2,2,'userb','ds','fdargfav','123654789','uds@majd'),
(3,3,'userc','sdf','sdfsfs','741258963','dsj@dmf'),
(4,4,'userd','djbshguh','dsfniudfhdn','874569321','dvbkhfej@mdd'),
(5,5,'usere','fdkj','dfgfkhbhfv','487946532','dmnfdh@dfe'),
(6,6,'userf','fdgre','fbgfgbebg','9876544322','fgrge@qwe'),
(7,7,'userg','fgew','fgrbevsfgr','1234567889','fngre@djd'),
(8,11,'aaaaaa','fdkfmsk','fknskdfn','741852963','dfksdfk@mail'),
(9,12,'raha','a','somewhere','5486741','anu@mail'),
(10,13,'raheal','a','a','4525789','anu@mail'),
(11,14,'achu','w','sdfsd','215484515','jasna@mail'),
(12,15,'qwsdxfc','rdcyhg','rkfnker','111','asdf@mail'),
(13,16,'fysd','dfsjfh','dfsbdd','9874563210','dfgsd@mail'),
(14,18,'ALFIA','A H','Aluva','8590922936','alfia@gmail.com'),
(15,20,'AKSHAY','SAMJI','CHOONDY','9778232157','akshaysamji023@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
