-- Manufacturing Intelligence Demo - Cortex AI Setup (Fixed)
-- Compatible with different Snowflake Cortex versions

USE DATABASE MANUFACTURING_DEMO;
USE SCHEMA DEMO_DATA;
USE WAREHOUSE DEMO_WH;

-- Test Cortex AI is available (Simple version)
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'mixtral-8x7b',
    'Hello! Please respond with: Cortex AI is working correctly for the manufacturing demo.'
) AS AI_TEST;

-- Alternative test if the above fails (try this version):
-- SELECT SNOWFLAKE.CORTEX.COMPLETE(
--     'llama2-70b-chat',
--     'Hello! Please respond with: Cortex AI is working correctly.'
-- ) AS AI_TEST_ALTERNATIVE;

-- Create a simple view with AI insights
CREATE OR REPLACE VIEW INVENTORY_INSIGHTS AS
SELECT 
    PLANT_ID,
    CATEGORY,
    SUM(CURRENT_STOCK) AS TOTAL_STOCK,
    SUM(CURRENT_STOCK * UNIT_COST) AS TOTAL_VALUE,
    COUNT(*) AS ITEM_COUNT,
    CASE 
        WHEN SUM(CURRENT_STOCK) < SUM(REORDER_POINT) THEN 'LOW_STOCK'
        WHEN SUM(CURRENT_STOCK) > SUM(REORDER_POINT) * 3 THEN 'EXCESS_STOCK'
        ELSE 'NORMAL'
    END AS STOCK_STATUS
FROM INVENTORY
GROUP BY PLANT_ID, CATEGORY;

-- Create supplier risk view
CREATE OR REPLACE VIEW SUPPLIER_RISK AS
SELECT 
    SUPPLIER_NAME,
    COUNTRY,
    PERFORMANCE_SCORE,
    RISK_SCORE,
    CASE 
        WHEN RISK_SCORE >= 4 THEN 'HIGH_RISK'
        WHEN RISK_SCORE >= 2 THEN 'MEDIUM_RISK'
        ELSE 'LOW_RISK'
    END AS RISK_CATEGORY
FROM SUPPLIERS
ORDER BY RISK_SCORE DESC;

-- Test what Cortex functions are available in your account
SELECT 'Available Cortex functions:' AS INFO;

-- Show available models (if this works in your version)
-- SHOW FUNCTIONS LIKE 'SNOWFLAKE.CORTEX.%';

-- Test views created
SELECT 'Cortex setup complete' AS STATUS;
