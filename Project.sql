DROP DATABASE IF EXISTS Project;
CREATE DATABASE Project;



USE Project;

DROP TABLE IF EXISTS DONORS;
CREATE TABLE DONORS (
  donorID       varchar(5) not null,
  firstName     varchar(15),
  lastName      varchar(15), 
  address		varchar(30),
  phone			char(10),
  constraint pk_donors primary key (donorID)
);


DROP TABLE IF EXISTS RECEIVERS;
CREATE TABLE RECEIVERS (
  receiverID    varchar(5) not null,
  firstName     varchar(15),
  lastName      varchar(15), 
  address		varchar(30),
  phone			char(10),
  constraint pk_recievers primary key (receiverID)
);


DROP TABLE IF EXISTS FOOD;
CREATE TABLE FOOD (
	foodID		varchar(5) not null,
    foodName	varchar(15),
    foodType	varchar(15),
    expDate		date,
    constraint pk_food primary key (foodID)
);


DROP TABLE IF EXISTS DONATES;
CREATE TABLE DONATES (
	dtID		varchar(5) not null,
	donorID		varchar(5) not null,
    foodID		varchar(5) not null,
    quantity	int,
    constraint pk_donates primary key (dtID, donorID, foodID),
    constraint fk_donates_donor foreign key (donorID) references DONORS(donorID),
    constraint fk_donates_food foreign key (foodID) references FOOD(foodID)
);


DROP TABLE IF EXISTS RECEIVES;
CREATE TABLE RECEIVES (
	rtID			varchar(5) not null,
	receiverID		varchar(5) not null,
    foodID			varchar(5) not null,
    quantity		int,
    constraint pk_donates primary key (rtID, receiverID, foodID),
    constraint fk_receives_receiver foreign key (receiverID) references RECEIVERS(receiverID),
    constraint fk_receives_food foreign key (foodID) references FOOD(foodID)
);


DROP TABLE IF EXISTS ADM;
CREATE TABLE ADM (
	ssn				varchar(9) not null,
    firstName		varchar(15),
    lastName		varchar(15),
    address			varchar(15),
    salary			decimal(10,2),
    constraint pk_adm primary key (ssn)
);

DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE (
	ssn				varchar(9) not null,
    firstName		varchar(15),
    lastName		varchar(15),
    address			varchar(15),
    salary			decimal(10,2),
    constraint pk_employee primary key (ssn)
);

DROP TABLE IF EXISTS VOLUNTEER;
CREATE TABLE VOLUNTEER (
	ssn				varchar(9) not null,
    firstName		varchar(15),
    lastName		varchar(15),
    address			varchar(15),
    constraint pk_volunteer primary key (ssn)
);
DROP TABLE IF EXISTS SUPERVISES;
CREATE TABLE SUPERVISES (
	assn		varchar(9) not null,
	essn		varchar(9) not null,
    constraint pk_supervises primary key (assn, essn),
    constraint fk_supervises_adm foreign key (assn) references ADM(ssn),
    constraint fk_supervises_employee foreign key (essn) references EMPLOYEE(ssn)
);

DROP TABLE IF EXISTS MANAGES;
CREATE TABLE MANAGES (
	essn		varchar(9) not null,
	vssn		varchar(9) not null,
    constraint pk_manages primary key (essn, vssn),
    constraint fk_manages_employee foreign key (essn) references EMPLOYEE(ssn),
    constraint fk_manages_volunteer foreign key (vssn) references VOLUNTEER(ssn)
);


DROP TABLE IF EXISTS LOGS_DOONATIONS;
CREATE TABLE LOGS_DONATIONS (
	vssn		varchar(9) not null,
    foodID		varchar(5) not null,
    dtID		varchar(5) not null,
    constraint pk_logs_donations primary key (vssn, dtID),
    constraint fk_logsdonations_volunteer foreign key (vssn) references VOLUNTEER(ssn),
    constraint fk_logsdonations_food foreign key (foodID) references FOOD(foodID),
    constraint fk_logskdonations_donates foreign key (dtID) references DONATES(dtID)
);

DROP TABLE IF EXISTS LOGS_TRANSACTIONS;
CREATE TABLE LOGS_TRANSACTIONS (
	vssn		varchar(9) not null,
    foodID		varchar(9) not null,
    rtID		varchar(5) not null,
    constraint pk_logs_transactions primary key (vssn, rtID),
    constraint fk_logstransactions_volunteer foreign key (vssn) references VOLUNTEER(ssn),
    constraint fk_logstransactions_food foreign key (foodID) references FOOD(foodID),
    constraint fk_logstransactions_receives foreign key (rtID) references RECEIVES(rtID)
);





INSERT INTO DONORS(donorID, firstName, lastName, address, phone) VALUES ("99999", "Leslie", "Knope", "111 11th st", "1112223333");

INSERT INTO RECEIVERS(receiverID, firstName, lastName, address, phone) VALUES ("11111", "Tammy", "Swanson", "111 11th st", "1112223333");

INSERT INTO FOOD(foodID, foodName, foodType, expDate) VALUES ("34978", "Soup", "Vegan", "2022-12-31");

INSERT INTO DONATES(dtID, donorID, foodID, quantity) VALUES ("14398", "99999", "34978", 19);
INSERT INTO DONATES(dtID, donorID, foodID, quantity) VALUES ("14397", "99999", "34978", 4);

INSERT INTO RECEIVES(rtID, receiverID, foodID, quantity) VALUES ("95876", "11111", "34978", 4);
INSERT INTO RECEIVES(rtID, receiverID, foodID, quantity) VALUES ("95875", "11111", "34978", 10);


INSERT INTO ADM(ssn, firstName, lastName, address, salary) VALUES ("111111111", "Thomas", "Williams", "11 100th st", "50000.00" );

INSERT INTO EMPLOYEE(ssn, firstName, lastName, address, salary) VALUES ("222222222", "Jack", "White", "12 10th st", "45000.00" );

INSERT INTO VOLUNTEER(ssn, firstName, lastName, address) VALUES ("333333333", "Pheobe", "Tonkin", "19 19th st" );

INSERT INTO SUPERVISES(assn, essn) VALUES ("111111111", "222222222");

INSERT INTO MANAGES(essn, vssn) VALUES ("222222222", "333333333");

INSERT INTO LOGS_DONATIONS(vssn, foodID, dtID) VALUES ("333333333", "34978", "14398");
INSERT INTO LOGS_TRANSACTIONS(vssn, foodID, rtID) VALUES ("333333333","34978" ,"95876");




SELECT * FROM DONORS;
SELECT * FROM RECEIVERS;
SELECT * FROM FOOD;
SELECT * FROM DONATES;
SELECT * FROM RECEIVES;
SELECT * FROM ADM;
SELECT * FROM EMPLOYEE;
SELECT * FROM VOLUNTEER;
SELECT * FROM SUPERVISES;
SELECT * FROM MANAGES;
SELECT * FROM LOGS_DONATIONS;
SELECT * FROM LOGS_TRANSACTIONS;
