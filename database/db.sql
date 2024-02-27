/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.25-MariaDB : Database - career_techs_new
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
  PRIMARY KEY (`answer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `answer` */

insert  into `answer`(`answer_id`,`test_type_id`,`user_id`,`mark_awarded`,`grand_total`,`date`) values 
(1,1,1,'2','3','2023-02-08'),
(2,1,1,'1','3','2023-02-08'),
(3,2,1,'1','3','2023-02-08'),
(4,2,1,'1','3','2023-02-08'),
(5,1,8,'2','3','2023-02-08'),
(6,2,8,'1','2','2023-02-08'),
(7,2,8,'1','2','2023-02-08'),
(8,2,8,'1','2','2023-02-08'),
(9,2,8,'0','2','2023-02-08'),
(10,2,8,'1','2','2023-02-08'),
(11,2,8,'0','2','2023-02-08'),
(12,1,1,'0','3','2023-03-16'),
(13,2,1,'0','2','2023-03-16');

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
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `application` */

insert  into `application`(`application_id`,`user_id`,`date`,`resume_path`,`personality`,`skill`,`mark`,`job_id`,`company_id`,`application_status`) values 
(1,1,'2023-01-05','static/uploads/a0552b9b-b831-41e4-af02-f1354ad25422Rosu_CV.docx','lively','Python',15,1,1,'pending'),
(2,1,'2023-01-05','static/uploads/4bc7f972-7503-4c39-b33f-0d8e54d4d726CVpj_tweet.pdf','lively','Android',15,2,1,'pending'),
(3,1,'2023-01-05','static/uploads/4513c445-2116-4b66-8ace-bcd9b3a05de2veena_cv.pdf','lively','Python',15,3,2,'pending'),
(4,2,'2023-01-05','static/uploads/a1a2fe77-685d-42a2-90ba-fe90c9849d65cvdoc.docx','lively','Python',15,1,1,'pending'),
(5,2,'2023-01-05','static/uploads/fd8d6eec-26aa-4d1e-b63a-8176b6edc077CVpj_tweet.pdf','responsible','C',14,4,2,'pending'),
(6,3,'2023-01-05','static/uploads/561cb1b0-7a04-4a98-99bb-59f8e80d9020veena_cv.pdf','lively','Android',15,2,1,'pending'),
(7,4,'2023-01-05','static/uploads/944d393f-5bab-4348-8202-0423d4c1530bCVpj_tweet.pdf','responsible','Python',14,1,1,'pending'),
(8,4,'2023-01-05','static/uploads/1e3eb60d-2530-4b25-8a49-0235d15b88b2cvdoc.docx','lively','Android',16,2,1,'pending'),
(9,5,'2023-01-05','static/uploads/53323461-acaf-4fa2-a7b0-c5bed1ce913cRosu_CV.pdf','lively','Python',13,1,1,'pending'),
(10,6,'2023-01-05','static/uploads/e611d57a-0449-4d55-95ac-7c4c060d6505Rosu_CV.pdf','responsible','Python',15,1,1,'pending'),
(11,8,'2023-01-21','static/uploads/1e5a302c-aa92-4d16-a9d9-2aafb9bceee8jasnaresume (1).docx','responsible','Python',9,2,1,'pending'),
(12,8,'2023-01-21','static/uploads/1e50e3e4-189c-490c-b047-c7f014b59819jasnaresume.pdf','lively','Java',10,1,1,NULL),
(13,2,'2023-01-21','static/uploads/456bcfa5-d828-4317-8302-563e3228f2cbjasnaresume.pdf','lively','C',13,3,2,'pending'),
(14,8,'2023-01-21','static/uploads/18a460d5-2f80-4529-8bc7-f00ac823c65fjasnaresume.pdf','lively','C',17,4,2,'pending'),
(15,8,'2023-01-23','static/uploads/49bc1244-bf8b-44c0-b665-d3f77e80369bElectric Recharge Bunk using  Mobile Application.txt 1.docx','lively','Python',20,3,2,'You Are Rejected'),
(16,9,'2023-01-27','static/uploads/3f3ffc91-eb0b-485f-a9fd-acd9fbcbb285Blood Donation - Modules and Tables.docx','responsible','Python',19,1,1,'pending'),
(17,10,'2023-01-27','static/uploads/e0c47e63-ad9b-4ca2-aa16-fa64f914a098Blood Donation - Modules and Tables.docx','responsible','Python',16,1,1,'You Are Selected'),
(18,11,'2023-01-27','static/uploads/ea405aac-5e07-4f02-a6bd-7acc5396c2faStudents’ performance prediction - Modules (1).docx','responsible','Python',17,3,2,'You Are Selected'),
(19,1,'2023-02-08','static/uploads/a08dc3c6-d281-4b8b-932b-b6f3170406f3BZONE - Modules and Tables.docx','extraverted','Python',0,5,1,'pending'),
(20,1,'2023-02-08','static/uploads/90bb70c6-4a89-4770-ac13-6ba4383e24dccrimefile.docx','responsible','C',0,4,2,'pending'),
(21,1,'2023-02-08','static/uploads/c407f947-30fb-4f1a-91fd-16ff14ccb2f2crimefile.docx','responsible','C',0,4,2,'pending'),
(22,8,'2023-02-08','static/uploads/936f1dff-d111-4a4c-8594-7ef06ef697c2Baby cradle.docx','lively','Python',20,5,1,'pending');

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
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `company` */

insert  into `company`(`company_id`,`login_id`,`company`,`place`,`phone`,`email`) values 
(1,9,'company1','alp','9874563211','c1@mail'),
(2,10,'company2','tvm','9876541233','c2@mail');

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
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`user_type`,`complaint`,`reply`,`date`) values 
(1,1,'user','dfgfhdb','pending','2023-01-19'),
(2,1,'company','jhjjioj;ijiuohuu','lkoo','2023-01-19'),
(3,8,'user','somethinggg','pending','2023-01-21'),
(4,10,'user','aaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzxxxxxxxxxxxxxxxxxxxxcccc','mdbfjdbfs','2023-01-27'),
(5,10,'user',',mkjkjnknnjhnmnbn','ndbgfdjbgdmvmdn','2023-01-27'),
(6,1,'company','yhnre','pending','2023-02-08'),
(7,8,'user','ffev','pending','2023-02-08');

/*Table structure for table `job` */

DROP TABLE IF EXISTS `job`;

CREATE TABLE `job` (
  `job_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `job` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `last_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `job` */

insert  into `job`(`job_id`,`company_id`,`job`,`details`,`last_date`) values 
(1,1,'c1job1','deeeeeeeeeeeeeeeeetailspython','2023-02-28'),
(2,1,'c1job2android','deeeeeeeeeeeeeetailsaaaaaandroid','2023-04-05'),
(3,2,'c2job1p','deeeetailspython','2023-02-10'),
(4,2,'c2job2c','deeeeeeeetailsccc','2023-05-17'),
(5,1,'jobqweerty','kdsjndjbvjdbvmdnfbvwmfv','2023-01-27');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

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
(16,'user50','user50','user');

/*Table structure for table `online_test` */

DROP TABLE IF EXISTS `online_test`;

CREATE TABLE `online_test` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `test_type_id` int(11) DEFAULT NULL,
  `question` varchar(50) DEFAULT NULL,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `correct_option` varchar(50) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

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
(9,2,'fhbvjrhebvrkh','mnb','yhr','etbnte','yhr',1);

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
  `question` varchar(500) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `test_type` */

insert  into `test_type`(`test_type_id`,`type`) values 
(1,'arithemetic'),
(2,'technical'),
(3,'level1'),
(4,'leve2');

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
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

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
(13,16,'fysd','dfsjfh','dfsbdd','9874563210','dfgsd@mail');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
