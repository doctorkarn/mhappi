
CREATE TABLE `medical_prescritpion` (`id` integer NOT NULL PRIMARY KEY, `drug_list` text NOT NULL, `officer_id` integer NOT NULL REFERENCES `authenication_officer` (`id`), `patient_id` integer NOT NULL REFERENCES `authenication_patient` (`id`));
INSERT INTO `medical_prescritpion` VALUES (1,'sdfufduo
aspofdohiadf
adsphidfohid',8,1);
CREATE TABLE `medical_patientinfo` (`id` integer NOT NULL PRIMARY KEY, `information` text NOT NULL, `officer_id` integer NOT NULL REFERENCES `authenication_officer` (`id`), `patient_id` integer NOT NULL REFERENCES `authenication_patient` (`id`));
INSERT INTO `medical_patientinfo` VALUES (1,'hsdlfhlja
dsasfjhldsah
asjdk;fhjadkl',10,1);
INSERT INTO `medical_patientinfo` VALUES (2,'fhodsfohfohfpji
''pohfohiasfhidfpij
''fadphhfdsohifhkpf
fds;khfspihdf
fdsfdsphidfphi@#$%^&*(',10,1);
CREATE TABLE `medical_medicalrecord` (`id` integer NOT NULL PRIMARY KEY, `symptom` text NOT NULL, `diagnosis` text NOT NULL, `drg_code` varchar(20) NOT NULL, `officer_id` integer NOT NULL REFERENCES `authenication_officer` (`id`), `patient_id` integer NOT NULL REFERENCES `authenication_patient` (`id`));
INSERT INTO `medical_medicalrecord` VALUES (1,'fadsugfadhdsfhfd
asfpfdhiodsfhipf
fdsoifaohidhiodsfih','ohiohidhio
skdsfihdsfhk
sldsfhkldsfhk','AB123',8,1);
CREATE TABLE `django_session` (`session_key` varchar(40) NOT NULL PRIMARY KEY, `session_data` text NOT NULL, `expire_date` datetime NOT NULL);
INSERT INTO `django_session` VALUES ('jfwu4fiapxcr8blyrgyzorkgg5dp6jlh','MTdlOGEyZWFkYzFjYzZhZGYxMzc5MjQyOGU5MzRiZjg3YmU0MTUyODp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzNmM0M2M1ZTc0YjA1ZWNkNTU4YTMxZWY1Njc0ZWY2ZjliYjE4ZjciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-10-07 08:14:46.730300');
CREATE TABLE `django_migrations` (`id` integer NOT NULL PRIMARY KEY, `app` varchar(255) NOT NULL, `name` varchar(255) NOT NULL, `applied` datetime NOT NULL);
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-09-23 08:13:51.326164');
INSERT INTO `django_migrations` VALUES (2,'auth','0001_initial','2015-09-23 08:13:51.598244');
INSERT INTO `django_migrations` VALUES (3,'admin','0001_initial','2015-09-23 08:13:51.840197');
INSERT INTO `django_migrations` VALUES (4,'contenttypes','0002_remove_content_type_name','2015-09-23 08:13:52.186678');
INSERT INTO `django_migrations` VALUES (5,'auth','0002_alter_permission_name_max_length','2015-09-23 08:13:52.434600');
INSERT INTO `django_migrations` VALUES (6,'auth','0003_alter_user_email_max_length','2015-09-23 08:13:52.686771');
INSERT INTO `django_migrations` VALUES (7,'auth','0004_alter_user_username_opts','2015-09-23 08:13:52.972730');
INSERT INTO `django_migrations` VALUES (8,'auth','0005_alter_user_last_login_null','2015-09-23 08:13:53.249853');
INSERT INTO `django_migrations` VALUES (9,'auth','0006_require_contenttypes_0002','2015-09-23 08:13:53.334955');
INSERT INTO `django_migrations` VALUES (10,'sessions','0001_initial','2015-09-23 08:13:53.540334');
INSERT INTO `django_migrations` VALUES (13,'authenication','0001_initial','2015-10-26 05:44:13.153376');
INSERT INTO `django_migrations` VALUES (15,'authenication','0002_officer_position','2015-10-26 05:53:20.333848');
INSERT INTO `django_migrations` VALUES (18,'appointment','0001_initial','2015-10-29 03:06:12.768730');
INSERT INTO `django_migrations` VALUES (19,'medical','0001_initial','2015-10-29 03:44:23.963226');
INSERT INTO `django_migrations` VALUES (20,'authenication','0003_auto_20151029_1211','2015-10-29 05:12:16.350726');
CREATE TABLE `django_content_type` (`id` integer NOT NULL PRIMARY KEY, `app_label` varchar(100) NOT NULL, `model` varchar(100) NOT NULL, UNIQUE (`app_label`, `model`));
INSERT INTO `django_content_type` VALUES (1,'admin','logentry');
INSERT INTO `django_content_type` VALUES (2,'auth','permission');
INSERT INTO `django_content_type` VALUES (3,'auth','group');
INSERT INTO `django_content_type` VALUES (4,'auth','user');
INSERT INTO `django_content_type` VALUES (5,'contenttypes','contenttype');
INSERT INTO `django_content_type` VALUES (6,'sessions','session');
INSERT INTO `django_content_type` VALUES (7,'authenication','patient');
INSERT INTO `django_content_type` VALUES (8,'authenication','officer');
INSERT INTO `django_content_type` VALUES (9,'appointment','appointment');
INSERT INTO `django_content_type` VALUES (10,'appointment','clinictime');
INSERT INTO `django_content_type` VALUES (11,'medical','medicalrecord');
INSERT INTO `django_content_type` VALUES (12,'medical','patientinfo');
INSERT INTO `django_content_type` VALUES (13,'medical','prescritpion');
CREATE TABLE `django_admin_log` (`id` integer NOT NULL PRIMARY KEY, `action_time` datetime NOT NULL, `object_id` text NULL, `object_repr` varchar(200) NOT NULL, `action_flag` smallint unsigned NOT NULL, `change_message` text NOT NULL, `content_type_id` integer NULL REFERENCES `django_content_type` (`id`), `user_id` integer NOT NULL REFERENCES `auth_user` (`id`));
CREATE TABLE `authenication_patient` (`id` integer NOT NULL PRIMARY KEY, `hospital_id` varchar(20) NOT NULL, `national_id` varchar(20) NOT NULL, `prefix_name` varchar(200) NOT NULL, `first_name` varchar(200) NOT NULL, `last_name` varchar(200) NOT NULL, `gender` integer NOT NULL, `birthdate` datetime NOT NULL, `address` varchar(500) NOT NULL, `phone` varchar(200) NOT NULL, `email` varchar(200) NOT NULL, `user_id` integer NOT NULL REFERENCES `auth_user` (`id`));
INSERT INTO `authenication_patient` VALUES (1,'58xxxxx1','1234567890','','banana','banana',1,'1999-12-31 17:00:00','banana','banana','banana@example.com',1);
INSERT INTO `authenication_patient` VALUES (3,'58xxxxx0','1234567890','','user02','user02',2,'1999-12-31 17:00:00','','1234567890','user02@example.com',3);
INSERT INTO `authenication_patient` VALUES (4,'58xxxxx7','1234567890','','user03','user03',1,'1999-12-31 17:00:00','@@@@@@@@@@@@@@','0000000000','user03@example.com',4);
CREATE TABLE `authenication_officer` (`id` integer NOT NULL PRIMARY KEY, `hospital_id` varchar(20) NOT NULL, `national_id` varchar(20) NOT NULL, `prefix_name` varchar(200) NOT NULL, `first_name` varchar(200) NOT NULL, `last_name` varchar(200) NOT NULL, `gender` integer NOT NULL, `birthdate` date NOT NULL, `address` varchar(500) NOT NULL, `phone` varchar(200) NOT NULL, `email` varchar(200) NOT NULL, `specialist` varchar(200) NOT NULL, `user_id` integer NOT NULL REFERENCES `auth_user` (`id`), `position` integer NOT NULL);
INSERT INTO `authenication_officer` VALUES (8,'MDxxxxx9','1234567890','','karn','the doctor',1,'2000-01-01','@@@@@@@@@@','0987654321','doctor@example.com','',8,2);
INSERT INTO `authenication_officer` VALUES (9,'MDxxxxx6','0987654321','','kam','the doctor',2,'2000-01-01','##########','0000000000','doctorA@example.com','',9,2);
INSERT INTO `authenication_officer` VALUES (10,'MDxxxxx3','1234567890','','nurse01','nurse01',1,'2000-01-01','','','','',10,3);
CREATE TABLE `auth_user_user_permissions` (`id` integer NOT NULL PRIMARY KEY, `user_id` integer NOT NULL REFERENCES `auth_user` (`id`), `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`), UNIQUE (`user_id`, `permission_id`));
CREATE TABLE `auth_user_groups` (`id` integer NOT NULL PRIMARY KEY, `user_id` integer NOT NULL REFERENCES `auth_user` (`id`), `group_id` integer NOT NULL REFERENCES `auth_group` (`id`), UNIQUE (`user_id`, `group_id`));
CREATE TABLE `auth_user` (`id` integer NOT NULL PRIMARY KEY, `password` varchar(128) NOT NULL, `is_superuser` bool NOT NULL, `username` varchar(30) NOT NULL UNIQUE, `first_name` varchar(30) NOT NULL, `last_name` varchar(30) NOT NULL, `email` varchar(254) NOT NULL, `is_staff` bool NOT NULL, `is_active` bool NOT NULL, `date_joined` datetime NOT NULL, `last_login` datetime NULL);
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$YIKaBOmcaJk2$3iSbmucC48sn1gB/Bi8E4PCDY0Fg80Y0x1LeEUHtGgo=',1,'admin','','','admin@example.com',1,1,'2015-09-23 08:14:37.229925','2015-11-02 03:39:39.600112');
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$20000$7QvGM0dTeYuz$QQNmbsRp/sQ8Ti21MGhjPadposdTqyGyv3KMDJA3pYA=',0,'user','','','user@example.com',0,1,'2015-10-25 14:35:23.839017','2015-10-25 17:35:46.507278');
INSERT INTO `auth_user` VALUES (3,'pbkdf2_sha256$20000$3gb08Al3SxtZ$+gc4/2VTbgPkKrclpJaW5jTdCK4Kt/oljruETxaxKtM=',0,'user01','','','user02@example.com',0,1,'2015-10-29 04:40:06.573636',NULL);
INSERT INTO `auth_user` VALUES (4,'pbkdf2_sha256$20000$3DzQZJeLNZ1K$Cm45x0mhEcG4Buz0MaNpLjjhqLsM4W/IOSMQy2Psyik=',0,'user03','','','user03@example.com',0,1,'2015-10-29 04:54:29.085918',NULL);
INSERT INTO `auth_user` VALUES (8,'pbkdf2_sha256$20000$DAIcJwzNuaXA$Y34K+Jpmb/8ENG+kWFTBH3ConxublhndoJRYnhSryr8=',0,'doctor','','','doctor@example.com',1,1,'2015-10-29 05:17:53.313272',NULL);
INSERT INTO `auth_user` VALUES (9,'pbkdf2_sha256$20000$BJCF56OWwSS4$owWlzqVCuLSRNbEv00EC+PFbATuaN3wHycgHOxQpB/s=',0,'doctor_A','','','doctorA@example.com',1,1,'2015-10-29 06:42:13.449074',NULL);
INSERT INTO `auth_user` VALUES (10,'pbkdf2_sha256$20000$PbJ66RNX1ihB$vEIaZ5jjwhSgHiPypcvLg6GWshxyxaByuBdsYuGbO1g=',0,'nurse01','','','',1,1,'2015-10-29 11:12:46.899498',NULL);
CREATE TABLE `auth_permission` (`id` integer NOT NULL PRIMARY KEY, `content_type_id` integer NOT NULL REFERENCES `django_content_type` (`id`), `codename` varchar(100) NOT NULL, `name` varchar(255) NOT NULL, UNIQUE (`content_type_id`, `codename`));
INSERT INTO `auth_permission` VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO `auth_permission` VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO `auth_permission` VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO `auth_permission` VALUES (4,2,'add_permission','Can add permission');
INSERT INTO `auth_permission` VALUES (5,2,'change_permission','Can change permission');
INSERT INTO `auth_permission` VALUES (6,2,'delete_permission','Can delete permission');
INSERT INTO `auth_permission` VALUES (7,3,'add_group','Can add group');
INSERT INTO `auth_permission` VALUES (8,3,'change_group','Can change group');
INSERT INTO `auth_permission` VALUES (9,3,'delete_group','Can delete group');
INSERT INTO `auth_permission` VALUES (10,4,'add_user','Can add user');
INSERT INTO `auth_permission` VALUES (11,4,'change_user','Can change user');
INSERT INTO `auth_permission` VALUES (12,4,'delete_user','Can delete user');
INSERT INTO `auth_permission` VALUES (13,5,'add_contenttype','Can add content type');
INSERT INTO `auth_permission` VALUES (14,5,'change_contenttype','Can change content type');
INSERT INTO `auth_permission` VALUES (15,5,'delete_contenttype','Can delete content type');
INSERT INTO `auth_permission` VALUES (16,6,'add_session','Can add session');
INSERT INTO `auth_permission` VALUES (17,6,'change_session','Can change session');
INSERT INTO `auth_permission` VALUES (18,6,'delete_session','Can delete session');
INSERT INTO `auth_permission` VALUES (19,7,'add_patient','Can add patient');
INSERT INTO `auth_permission` VALUES (20,7,'change_patient','Can change patient');
INSERT INTO `auth_permission` VALUES (21,7,'delete_patient','Can delete patient');
INSERT INTO `auth_permission` VALUES (22,8,'add_officer','Can add officer');
INSERT INTO `auth_permission` VALUES (23,8,'change_officer','Can change officer');
INSERT INTO `auth_permission` VALUES (24,8,'delete_officer','Can delete officer');
INSERT INTO `auth_permission` VALUES (25,9,'add_appointment','Can add appointment');
INSERT INTO `auth_permission` VALUES (26,9,'change_appointment','Can change appointment');
INSERT INTO `auth_permission` VALUES (27,9,'delete_appointment','Can delete appointment');
INSERT INTO `auth_permission` VALUES (28,10,'add_clinictime','Can add clinic time');
INSERT INTO `auth_permission` VALUES (29,10,'change_clinictime','Can change clinic time');
INSERT INTO `auth_permission` VALUES (30,10,'delete_clinictime','Can delete clinic time');
INSERT INTO `auth_permission` VALUES (31,11,'add_medicalrecord','Can add medical record');
INSERT INTO `auth_permission` VALUES (32,11,'change_medicalrecord','Can change medical record');
INSERT INTO `auth_permission` VALUES (33,11,'delete_medicalrecord','Can delete medical record');
INSERT INTO `auth_permission` VALUES (34,12,'add_patientinfo','Can add patient info');
INSERT INTO `auth_permission` VALUES (35,12,'change_patientinfo','Can change patient info');
INSERT INTO `auth_permission` VALUES (36,12,'delete_patientinfo','Can delete patient info');
INSERT INTO `auth_permission` VALUES (37,13,'add_prescritpion','Can add prescritpion');
INSERT INTO `auth_permission` VALUES (38,13,'change_prescritpion','Can change prescritpion');
INSERT INTO `auth_permission` VALUES (39,13,'delete_prescritpion','Can delete prescritpion');
CREATE TABLE `auth_group_permissions` (`id` integer NOT NULL PRIMARY KEY, `group_id` integer NOT NULL REFERENCES `auth_group` (`id`), `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`), UNIQUE (`group_id`, `permission_id`));
CREATE TABLE `auth_group` (`id` integer NOT NULL PRIMARY KEY, `name` varchar(80) NOT NULL UNIQUE);
CREATE TABLE `appointment_clinictime` (`id` integer NOT NULL PRIMARY KEY, `clinic_datetime` datetime NOT NULL, `clinic_status` smallint NOT NULL, `officer_id` integer NOT NULL REFERENCES `authenication_officer` (`id`));
INSERT INTO `appointment_clinictime` VALUES (1,'2015-08-11 17:00:00',1,8);
INSERT INTO `appointment_clinictime` VALUES (2,'2015-09-08 17:00:00',1,8);
INSERT INTO `appointment_clinictime` VALUES (3,'2015-09-10 17:00:00',1,9);
CREATE TABLE `appointment_appointment` (`id` integer NOT NULL PRIMARY KEY, `appointment_status` smallint NOT NULL, `clinic_time_id` integer NOT NULL REFERENCES `appointment_clinictime` (`id`), `patient_id` integer NOT NULL REFERENCES `authenication_patient` (`id`));
INSERT INTO `appointment_appointment` VALUES (1,1,3,3);
INSERT INTO `appointment_appointment` VALUES (2,1,2,3);
INSERT INTO `appointment_appointment` VALUES (3,1,3,3);
CREATE INDEX `medical_prescritpion_e1d6855c` ON `medical_prescritpion` (`officer_id`);
CREATE INDEX `medical_prescritpion_9f065c57` ON `medical_prescritpion` (`patient_id`);
CREATE INDEX `medical_patientinfo_e1d6855c` ON `medical_patientinfo` (`officer_id`);
CREATE INDEX `medical_patientinfo_9f065c57` ON `medical_patientinfo` (`patient_id`);
CREATE INDEX `medical_medicalrecord_e1d6855c` ON `medical_medicalrecord` (`officer_id`);
CREATE INDEX `medical_medicalrecord_9f065c57` ON `medical_medicalrecord` (`patient_id`);
CREATE INDEX `django_session_de54fa62` ON `django_session` (`expire_date`);
CREATE INDEX `django_admin_log_e8701ad4` ON `django_admin_log` (`user_id`);
CREATE INDEX `django_admin_log_417f1b1c` ON `django_admin_log` (`content_type_id`);
CREATE INDEX `authenication_patient_e8701ad4` ON `authenication_patient` (`user_id`);
CREATE INDEX `authenication_officer_e8701ad4` ON `authenication_officer` (`user_id`);
CREATE INDEX `auth_user_user_permissions_e8701ad4` ON `auth_user_user_permissions` (`user_id`);
CREATE INDEX `auth_user_user_permissions_8373b171` ON `auth_user_user_permissions` (`permission_id`);
CREATE INDEX `auth_user_groups_e8701ad4` ON `auth_user_groups` (`user_id`);
CREATE INDEX `auth_user_groups_0e939a4f` ON `auth_user_groups` (`group_id`);
CREATE INDEX `auth_permission_417f1b1c` ON `auth_permission` (`content_type_id`);
CREATE INDEX `auth_group_permissions_8373b171` ON `auth_group_permissions` (`permission_id`);
CREATE INDEX `auth_group_permissions_0e939a4f` ON `auth_group_permissions` (`group_id`);
CREATE INDEX `appointment_clinictime_e1d6855c` ON `appointment_clinictime` (`officer_id`);
CREATE INDEX `appointment_appointment_9f065c57` ON `appointment_appointment` (`patient_id`);
CREATE INDEX `appointment_appointment_605aeafd` ON `appointment_appointment` (`clinic_time_id`);

