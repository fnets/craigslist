CREATE TABLE listings (
    key INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    url TEXT NOT NULL ,
    title TEXT NOT NULL ,
    description TEXT NOT NULL ,
    last_update DATETIME NOT NULL ,
    found DATETIME NOT NULL ,
    new BOOL NOT NULL DEFAULT '0'
);
