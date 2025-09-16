-- Manufacturing Intelligence Demo - Sample Data
-- Clean, simple test data

USE DATABASE MANUFACTURING_DEMO;
USE SCHEMA DEMO_DATA;
USE WAREHOUSE DEMO_WH;

-- Insert Plants
INSERT INTO PLANTS VALUES
('PLANT_001', 'North America Hub', 'North America', 'USA'),
('PLANT_002', 'Europe Center', 'Europe', 'Germany'),
('PLANT_003', 'Asia Pacific', 'Asia', 'Singapore'),
('PLANT_004', 'Latin America', 'LATAM', 'Mexico');

-- Insert Inventory
INSERT INTO INVENTORY VALUES
('INV_001', 'Steel Components', 'PLANT_001', 'Raw Materials', 2500, 500, 12.50),
('INV_002', 'Electronic Parts', 'PLANT_001', 'Components', 1200, 300, 45.00),
('INV_003', 'Motor Assembly', 'PLANT_001', 'Finished Goods', 150, 50, 245.00),
('INV_004', 'Steel Components', 'PLANT_002', 'Raw Materials', 3200, 600, 11.80),
('INV_005', 'Precision Bearings', 'PLANT_002', 'Components', 800, 200, 89.50),
('INV_006', 'Control Systems', 'PLANT_003', 'Electronics', 450, 100, 156.00),
('INV_007', 'Sensor Arrays', 'PLANT_003', 'Electronics', 600, 150, 78.90),
('INV_008', 'Packaging Materials', 'PLANT_004', 'Materials', 5000, 1000, 2.30);

-- Insert Suppliers
INSERT INTO SUPPLIERS VALUES
('SUP_001', 'Global Steel Solutions', 'USA', 94.5, 2.1),
('SUP_002', 'European Precision Mfg', 'Germany', 97.8, 1.5),
('SUP_003', 'Asia Components Ltd', 'Singapore', 89.2, 4.2),
('SUP_004', 'Reliable Electronics', 'Taiwan', 91.7, 3.1),
('SUP_005', 'Premium Bearings Intl', 'Sweden', 96.3, 1.8);

-- Insert Production Data
INSERT INTO PRODUCTION VALUES
('PROD_001', 'PLANT_001', 'Motor Assembly', '2024-09-01', 150, 89.2),
('PROD_002', 'PLANT_001', 'Control Unit', '2024-09-02', 200, 92.1),
('PROD_003', 'PLANT_002', 'Precision Parts', '2024-09-01', 300, 94.5),
('PROD_004', 'PLANT_002', 'Bearing Sets', '2024-09-02', 250, 93.2),
('PROD_005', 'PLANT_003', 'Sensor Modules', '2024-09-01', 400, 88.7),
('PROD_006', 'PLANT_003', 'Electronic Boards', '2024-09-02', 180, 91.5);

-- Insert Financial KPIs
INSERT INTO FINANCIAL_KPIS VALUES
('2024-09-01', 'PLANT_001', 15750000, 45200000, 850000),
('2024-09-01', 'PLANT_002', 18920000, 38900000, 1200000),
('2024-09-01', 'PLANT_003', 12680000, 29800000, 650000),
('2024-09-01', 'PLANT_004', 8950000, 18500000, 420000);

-- Verify data loaded
SELECT 'Data loaded successfully' AS STATUS,
       (SELECT COUNT(*) FROM PLANTS) AS PLANTS_COUNT,
       (SELECT COUNT(*) FROM INVENTORY) AS INVENTORY_COUNT,
       (SELECT COUNT(*) FROM SUPPLIERS) AS SUPPLIERS_COUNT,
       (SELECT COUNT(*) FROM PRODUCTION) AS PRODUCTION_COUNT,
       (SELECT COUNT(*) FROM FINANCIAL_KPIS) AS FINANCIAL_COUNT;
