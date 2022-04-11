DROP TABLE IF EXISTS BTC_addresses ; -- Create Database with Address and Id for BTC

CREATE TABLE BTC_addresses 
(
    BTC_address TEXT NOT NULL,
    BTC_id TEXT NOT NULL
)
;


DROP TABLE IF EXISTS ETH_addresses ; -- Create Database with Address and Id for ETH

CREATE TABLE ETH_addresses 
(
    ETH_address TEXT PRIMARY KEY AUTOINCREMENT,
    ETH_id TEXT NOT NULL
)
;








