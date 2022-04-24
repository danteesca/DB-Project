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




INSERT INTO DONORS(donorID, firstName, lastName, address, phone) VALUES ("99999", "Leslie", "Knope", "111 11th st", "1112223333");

INSERT INTO RECEIVERS(receiverID, firstName, lastName, address, phone) VALUES ("11111", "Tammy", "Swanson", "111 11th st", "1112223333");

INSERT INTO FOOD(foodID, foodName, foodType, expDate) VALUES ("34978", "Soup", "Vegan", "2022-12-31");

INSERT INTO DONATES(dtID, donorID, foodID, quantity) VALUES ("14398", "99999", "34978", 19);
INSERT INTO DONATES(dtID, donorID, foodID, quantity) VALUES ("14397", "99999", "34978", 4);

INSERT INTO RECEIVES(rtID, receiverID, foodID, quantity) VALUES ("95876", "11111", "34978", 4);
INSERT INTO RECEIVES(rtID, receiverID, foodID, quantity) VALUES ("95875", "11111", "34978", 10);



SELECT * FROM DONORS;
SELECT * FROM RECEIVERS;
SELECT * FROM FOOD;
SELECT * FROM DONATES;
SELECT * FROM RECEIVES;
SELECT * FROM DONOR_FOOD;
SELECT * FROM RECEIVER_FOOD;