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
	donorID		varchar(5) not null,
    foodID		varchar(5) not null,
    quantity	int,
    constraint pk_donates primary key (donorID, foodID),
    constraint fk_donates_donor foreign key (donorID) references DONORS(donorID),
    constraint fk_donates_food foreign key (foodID) references FOOD(foodID)
);


DROP TABLE IF EXISTS RECEIVES;
CREATE TABLE RECEIVES (
	receiverID		varchar(5) not null,
    foodID			varchar(5) not null,
    quantity		int,
    constraint pk_donates primary key (receiverID, foodID),
    constraint fk_receives_receiver foreign key (receiverID) references RECEIVERS(receiverID),
    constraint fk_receives_food foreign key (foodID) references FOOD(foodID)
);


DROP TABLE IF EXISTS DONOR_FOOD;
CREATE TABLE DONOR_FOOD (
	donorID		varchar(5) not null,
    foodID		varchar(5) not null,
    constraint pk_DF primary key (donorID),
    constraint fk_DF_food foreign key (foodID) references FOOD(foodID)
);


DROP TABLE IF EXISTS RECEIVER_FOOD;
CREATE TABLE RECEIVER_FOOD (
	receiverID		varchar(5) not null,
    foodID		varchar(5) not null,
    constraint pk_RF primary key (receiverID),
    constraint fk_RF_food foreign key (foodID) references FOOD(foodID)
);


INSERT INTO DONORS VALUES ('12345', 'Max', 'Smith', '123 50th st', '2341238765');
INSERT INTO DONORS VALUES ('12344', 'Matt', 'Smith', '123 50th st', '2341238765');

INSERT INTO RECEIVERS VALUES ('11111', 'Todd', 'Williams', '124 25th st', '1230987856');

INSERT INTO FOOD VALUES ('00000', 'Soup', 'Vegan', '2025-01-31');
INSERT INTO FOOD VALUES ('00001', 'Soup', 'Vegan', '2025-01-31');

INSERT INTO DONATES VALUES ('12345', '00000', 5);
INSERT INTO DONATES VALUES ('12344', '00000', 5);
INSERT INTO DONATES VALUES ('12344', '00001', 5);

INSERT INTO RECEIVES VALUES ('11111', '00000', 2);

INSERT INTO DONOR_FOOD VALUES ('12345', '00000');

INSERT INTO RECEIVER_FOOD VALUES ('11111', '00000');


SELECT * FROM DONORS;
SELECT * FROM RECEIVERS;
SELECT * FROM FOOD;
SELECT * FROM DONATES;
SELECT * FROM RECEIVES;
SELECT * FROM DONOR_FOOD;
SELECT * FROM RECEIVER_FOOD;