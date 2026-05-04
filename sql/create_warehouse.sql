CREATE DATABASE WineWarehouse;
GO

USE WineWarehouse;
GO


CREATE TABLE dbo.WineData (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    FixedAcidity FLOAT,
    VolatileAcidity FLOAT,
    CitricAcid FLOAT,
    ResidualSugar FLOAT,
    Chlorides FLOAT,
    FreeSulfurDioxide FLOAT,
    TotalSulfurDioxide FLOAT,
    Density FLOAT,
    PH FLOAT,
    Sulphates FLOAT,
    Alcohol FLOAT,
    Quality INT,
    ColorBin INT, 
    LoadDate DATETIME DEFAULT GETDATE() 
);
GO