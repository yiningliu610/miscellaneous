Login postgres:
psql postgres

Logout postgres:
\q

Create database:
CREATE DATABASE testdb;

Select database:
\c testdb;

Create table:
CREATE TABLE test_zipcodes(
   PO_NAME CHAR(30) NOT NULL,
   ZIP           CHAR(5) PRIMARY KEY NOT NULL,
   STATE         CHAR(2)      NOT NULL
);

Import data:
- Find the location of psql in computer
	SHOW data_directory;
- Move the data from local directory to psql server directory:
	cp ~/Desktop/db_tables/bayarea_zipcodes.csv /usr/local/var/postgres/data4table
- Copy the data from csv into the tables
        COPY test_zipcodes(po_name, zip, state) 
        FROM '/usr/local/var/postgres/data4table/bayarea_zipcodes.csv' DELIMITER ',' CSV HEADER;

- Export data into csv files:
	\COPY (select * from test_zipcodes where po_name = 'SAN FRANCISCO') TO '/usr/local/var/postgres/data4table/HAHA.csv' WITH CSV;
	cp /usr/local/var/postgres/data4table/HAAH.csv ~/Desktop/db_tables/
