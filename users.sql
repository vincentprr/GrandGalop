/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 80030
Source Host           : 127.0.0.1:3306
Source Database       : ecole

Target Server Type    : MYSQL
Target Server Version : 80030
File Encoding         : 65001

Date: 2023-01-17 17:08:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admins
-- ----------------------------
DROP TABLE IF EXISTS `admins`;
CREATE TABLE `admins` (
  `IdP` int unsigned NOT NULL AUTO_INCREMENT,
  `Image` longblob,
  PRIMARY KEY (`IdP`),
  CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`IdP`) REFERENCES `personnes` (`IdP`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of admins
-- ----------------------------
INSERT INTO `admins` VALUES ('3', null);

-- ----------------------------
-- Table structure for moniteurs
-- ----------------------------
DROP TABLE IF EXISTS `moniteurs`;
CREATE TABLE `moniteurs` (
  `IdP` int unsigned NOT NULL AUTO_INCREMENT,
  `Image` longblob,
  PRIMARY KEY (`IdP`),
  CONSTRAINT `moniteurs_ibfk_1` FOREIGN KEY (`IdP`) REFERENCES `personnes` (`IdP`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of moniteurs
-- ----------------------------
INSERT INTO `moniteurs` VALUES ('2', null);

-- ----------------------------
-- Table structure for personnes
-- ----------------------------
DROP TABLE IF EXISTS `personnes`;
CREATE TABLE `personnes` (
  `IdP` int unsigned NOT NULL AUTO_INCREMENT,
  `EmailC` varchar(255) NOT NULL,
  `MotDePasseC` text NOT NULL,
  `PrenomC` text NOT NULL,
  `NomC` text NOT NULL,
  `TelephoneC` varchar(13) NOT NULL,
  `AdresseC` text NOT NULL,
  PRIMARY KEY (`IdP`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of personnes
-- ----------------------------
INSERT INTO `personnes` VALUES ('1', 'test@test.fr', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'Vincent', 'Poirier', '0620457899', '23 rue de zouzouin, Orléans');
INSERT INTO `personnes` VALUES ('2', 'test@moniteur.fr', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'Vincent', 'Moniteur', '0620147852', '45 Mzoungou street, Vagiland');
INSERT INTO `personnes` VALUES ('3', 'test@admin.fr', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'Vincent', 'Admin', '0620145878', '25 rue de test, Paris');
