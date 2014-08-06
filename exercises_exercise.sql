-- MySQL dump 10.13  Distrib 5.5.38, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: profproject
-- ------------------------------------------------------
-- Server version	5.5.38-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exercises_exercise`
--

DROP TABLE IF EXISTS `exercises_exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercises_exercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `discipline_id` int(11) DEFAULT NULL,
  `exo_number` int(11) NOT NULL,
  `question` varchar(300) NOT NULL,
  `question_type` varchar(30) NOT NULL,
  `answer` varchar(30) NOT NULL,
  `question_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `exercises_exercise_subject_id_36e3763664005b8d_uniq` (`discipline_id`),
  CONSTRAINT `exercises_exercise_discipline_id_35a359f4d4c676a4_fk` FOREIGN KEY (`discipline_id`) REFERENCES `exercises_discipline` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises_exercise`
--

LOCK TABLES `exercises_exercise` WRITE;
/*!40000 ALTER TABLE `exercises_exercise` DISABLE KEYS */;
INSERT INTO `exercises_exercise` VALUES (1,1,1,'rouge?','text','rouge','2014-07-30'),(2,1,1,'blanc?','text','blanc','2014-07-30'),(3,2,1,'10?','text','10','2014-07-30'),(4,1,2,'noir?','text','noir','2014-07-30'),(5,4,1,'France?','text','France','2014-07-30');
/*!40000 ALTER TABLE `exercises_exercise` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-07-30 21:50:19
