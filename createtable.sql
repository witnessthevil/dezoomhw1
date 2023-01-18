create table green(
  VendorID int, 
 lpep_pickup_datetime timestamp, 
 lpep_dropoff_datetime timestamp,
 store_and_fwd_flag varchar(3),
 RatecodeID int,
 PULocationID int,
 DOLocationID int,
 passenger_count int,
 trip_distance float,
 fare_amount float,
 extra float,
 mta_tax float,
 tip_amount float,
 tolls_amount float,
 ehail_fee varchar(100),
 improvement_surcharge float,
 total_amount float,
 payment_type int,
 trip_type int,
 congestion_surcharge float
)

create table zone(
LocationID int, 
 Borough varchar(50),
 Zone varchar(100),
 service_zone varchar(50)
)