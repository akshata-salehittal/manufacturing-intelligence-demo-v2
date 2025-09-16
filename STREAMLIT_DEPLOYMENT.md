# Streamlit in Snowflake Deployment Guide
## Import Manufacturing Intelligence Demo from GitHub

### 🚀 **Direct Import from GitHub**

Your Streamlit app is now ready for direct import into Snowflake!

**📍 GitHub Repository:** https://github.com/akshata-salehittal/manufacturing-intelligence-demo-v2

---

## 📋 **Step-by-Step Deployment**

### **Step 1: Create Streamlit App in Snowflake**

1. **Login to Snowflake Web UI**
2. **Navigate to Streamlit Apps:**
   - Go to **Projects** → **Streamlit** (left sidebar)
   - Or **Data** → **Apps** → **Streamlit Apps**

3. **Create New App:**
   - Click **"+ Streamlit App"**
   - **App Name:** `Manufacturing Intelligence Demo`
   - **Database:** `MANUFACTURING_DEMO`
   - **Schema:** `DEMO_DATA`
   - **Warehouse:** `DEMO_WH`

### **Step 2: Import from GitHub**

**Option A: Direct GitHub Import (Recommended)**
1. **Select "Import from GitHub"**
2. **Repository URL:** `https://github.com/akshata-salehittal/manufacturing-intelligence-demo-v2`
3. **Main File:** `streamlit_snowflake_app.py`
4. **Branch:** `main`

**Option B: Manual Copy-Paste**
1. **Go to GitHub:** https://github.com/akshata-salehittal/manufacturing-intelligence-demo-v2/blob/main/streamlit_snowflake_app.py
2. **Copy the raw file content**
3. **Paste into Snowflake Streamlit editor**
4. **Save as:** `streamlit_app.py`

### **Step 3: Configure App Settings**

```sql
-- App Configuration
Database: MANUFACTURING_DEMO
Schema: DEMO_DATA
Warehouse: DEMO_WH
Main File: streamlit_snowflake_app.py (or streamlit_app.py if copied)
```

### **Step 4: Deploy and Test**

1. **Click "Run"** to deploy the app
2. **Wait for deployment** (usually 30-60 seconds)
3. **Test the app** - it should show:
   - ✅ Executive Dashboard with KPIs
   - ✅ AI Assistant with sample questions
   - ✅ Data Explorer with all tables

---

## 🎯 **What You'll Get**

### **📊 Executive Dashboard**
- **4 Key Metrics:** Plants, Inventory Value, Working Capital, Cost Savings
- **Interactive Charts:** Inventory by plant, Production efficiency
- **Business Insights:** Key recommendations and alerts

### **🤖 AI Assistant**
- **Sample Questions:** Pre-built manufacturing scenarios
- **Natural Language:** Ask anything about your data
- **Cortex AI Powered:** Real business insights, not just data

### **🔍 Data Explorer**
- **4 Data Tabs:** Inventory, Production, Suppliers, Financial
- **Interactive Tables:** Full data exploration
- **Quick Stats:** Summary metrics for each dataset

---

## 🔧 **Troubleshooting**

### **If Import Fails:**
1. **Check Repository Access:** Ensure the GitHub repo is public
2. **Verify File Path:** Use `streamlit_snowflake_app.py` as main file
3. **Manual Copy:** Use Option B (copy-paste) as backup

### **If App Won't Start:**
1. **Check Database Context:**
   ```sql
   USE DATABASE MANUFACTURING_DEMO;
   USE SCHEMA DEMO_DATA;
   USE WAREHOUSE DEMO_WH;
   ```

2. **Verify Data Exists:**
   ```sql
   SELECT COUNT(*) FROM INVENTORY; -- Should return 8
   SELECT COUNT(*) FROM SUPPLIERS; -- Should return 5
   ```

### **If Cortex AI Fails:**
- **App still works** - shows data dashboards
- **Focus on data unification** story
- **Promise AI features** in pilot phase

---

## 🎪 **Demo Ready Features**

### **Professional Presentation:**
- ✅ **Gradient header** with manufacturing branding
- ✅ **Clean metrics cards** with business KPIs
- ✅ **Interactive charts** with Plotly visualizations
- ✅ **Business insights** with actionable recommendations

### **Native Snowflake Integration:**
- ✅ **No external connections** - uses `get_active_session()`
- ✅ **Real-time data** - directly from your Snowflake tables
- ✅ **Secure sharing** - built-in Snowflake security
- ✅ **Enterprise ready** - scalable and reliable

---

## 📱 **Sharing Your Demo**

### **With Internal Team:**
1. **Click "Share" button** in the app
2. **Grant access** to specific users/roles
3. **Send direct link** to the app

### **With Customers:**
1. **Create demo user** in your Snowflake account
2. **Grant limited permissions** to demo database
3. **Share app link** for live demo sessions

---

## 🚀 **Demo Script**

### **Opening (30 seconds):**
> *"This is running natively in Snowflake - no external tools, no data movement. Everything you see is live manufacturing data unified in real-time."*

### **Executive Dashboard (2 minutes):**
- Point to **$56M inventory value** across 4 plants
- Show **90.8% average efficiency** with plant comparisons
- Highlight **business insights** with quantified impact

### **AI Assistant (2 minutes):**
- Click sample question: *"What's our total inventory value?"*
- Let audience ask: *"Which plant needs attention?"*
- Show **natural language** to **business insights**

### **Data Explorer (1 minute):**
- Show **unified data** from multiple sources
- Emphasize **real-time access** to operational data
- **Technical validation** for IT stakeholders

### **Close (30 seconds):**
> *"This is your future state - unified manufacturing intelligence with AI-powered insights, all native in Snowflake. Let's discuss your pilot program."*

---

## ✅ **Deployment Checklist**

- [ ] All 4 SQL scripts executed successfully
- [ ] Data verification queries return expected results
- [ ] Streamlit app imported from GitHub
- [ ] App deployed and running in Snowflake
- [ ] Executive Dashboard displays correctly
- [ ] AI Assistant responds to sample questions
- [ ] Data Explorer shows all tables
- [ ] Demo script practiced and ready

---

**🎉 Your Manufacturing Intelligence Demo is now live in Snowflake!**

**Repository:** https://github.com/akshata-salehittal/manufacturing-intelligence-demo-v2

**Ready to wow customers with native Snowflake + Cortex AI manufacturing intelligence!** 🚀
