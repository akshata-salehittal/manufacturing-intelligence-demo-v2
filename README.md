# Manufacturing Intelligence Demo V2
## Clean, Simple, Reliable

### 🚀 Quick Setup (15 minutes)

#### 1. Snowflake Setup
Run these SQL files in Snowflake **in order**:

```sql
-- 1. Database setup (2 min)
-- Copy/paste: 01_setup.sql

-- 2. Create tables (2 min)  
-- Copy/paste: 02_tables.sql

-- 3. Load sample data (2 min)
-- Copy/paste: 03_data.sql

-- 4. Setup Cortex AI (2 min)
-- Copy/paste: 04_cortex.sql
```

#### 2. Local Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Configure Snowflake connection
cp env_example.txt .env
# Edit .env with your Snowflake credentials

# Launch demo
streamlit run app.py
```

### 🎯 What You Get

✅ **Executive Dashboard** - KPIs and business metrics  
✅ **AI Assistant** - Natural language queries with Cortex  
✅ **Data Explorer** - Raw data views and analysis  
✅ **Clean SQL** - No errors, simple structure  
✅ **Reliable Demo** - Tested and working  

### 📊 Demo Features

- **4 Manufacturing Plants** with realistic data
- **Inventory Management** across multiple categories  
- **Supplier Risk Analysis** with performance scores
- **Production Efficiency** tracking and trends
- **Financial KPIs** including working capital and savings
- **AI-Powered Insights** using Snowflake Cortex

### 🎪 Demo Flow

1. **Start with Executive Dashboard** - Show business impact
2. **Use AI Assistant** - Let audience ask questions
3. **Explore Data** - Show unified data sources

### 🔧 Troubleshooting

**Connection Issues:**
- Check .env file has correct Snowflake credentials
- Verify Cortex AI is enabled in your account
- Test connection in Snowflake web UI first

**SQL Errors:**
- Run scripts in exact order (01, 02, 03, 04)
- Use ACCOUNTADMIN role
- Check warehouse is running

### 💡 Success Tips

- **Keep it simple** - Focus on core value proposition
- **Let them interact** - Encourage AI questions
- **Show business impact** - Emphasize ROI and savings
- **Be confident** - This version is tested and reliable

---

**Built for reliability and impact. Ready to demo!** 🚀
