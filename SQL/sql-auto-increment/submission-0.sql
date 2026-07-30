CREATE SEQUENCE GOV_ID START WITH 1000 INCREMENT BY 3;

CREATE TABLE GOV_EMPLOYEE(
  ID INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  GOV_ID INTEGER DEFAULT nextval('GOV_ID'),
  NAME TEXT
);









-- Do not modify below this line --
INSERT INTO gov_employee (name) 
  VALUES
      ('John Doe'),
      ('Jane Doe'),
      ('Jim Beam');

SELECT * FROM gov_employee;
