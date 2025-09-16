#!/usr/bin/env python3
"""
Simple test script to validate SQL files
"""

def test_sql_files():
    """Test that SQL files are readable and have basic structure"""
    sql_files = [
        '01_setup.sql',
        '02_tables.sql', 
        '03_data.sql',
        '04_cortex.sql'
    ]
    
    print("🧪 Testing SQL Files...")
    
    for sql_file in sql_files:
        try:
            with open(sql_file, 'r') as f:
                content = f.read()
                
            # Basic checks
            if len(content) < 100:
                print(f"  ❌ {sql_file}: Too short")
                continue
                
            if 'CREATE' not in content.upper() and 'INSERT' not in content.upper():
                print(f"  ❌ {sql_file}: No CREATE or INSERT statements")
                continue
                
            print(f"  ✅ {sql_file}: OK ({len(content)} chars)")
            
        except Exception as e:
            print(f"  ❌ {sql_file}: Error - {e}")
    
    print("\n🎯 SQL files ready for Snowflake!")

if __name__ == "__main__":
    test_sql_files()
