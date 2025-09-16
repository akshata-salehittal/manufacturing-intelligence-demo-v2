# Cortex AI Troubleshooting Guide

## 🚨 **Common Cortex AI Issues & Solutions**

### **Issue 1: Invalid argument types for function 'COMPLETE$V6'**

**Problem:** The Cortex function syntax varies between Snowflake versions.

**Solutions to try (in order):**

#### **Option A: Simple Syntax (Try First)**
```sql
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'mixtral-8x7b',
    'Hello! Please respond with: Cortex AI is working correctly.'
) AS AI_TEST;
```

#### **Option B: Different Model**
```sql
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'llama2-70b-chat',
    'Hello! Please respond with: Cortex AI is working correctly.'
) AS AI_TEST;
```

#### **Option C: Check Available Models**
```sql
-- See what models are available in your account
SHOW FUNCTIONS LIKE 'SNOWFLAKE.CORTEX.%';
```

### **Issue 2: Cortex AI Not Enabled**

**Error:** `Function SNOWFLAKE.CORTEX.COMPLETE does not exist`

**Solution:**
1. Contact your Snowflake admin to enable Cortex AI
2. Or use the demo without AI features (dashboards still work)

### **Issue 3: Insufficient Privileges**

**Error:** `Insufficient privileges to operate on function`

**Solution:**
```sql
-- Grant Cortex permissions (run as ACCOUNTADMIN)
GRANT USAGE ON FUNCTION SNOWFLAKE.CORTEX.COMPLETE TO ROLE YOUR_ROLE;
```

### **Issue 4: Model Not Available**

**Error:** `Model 'mixtral-8x7b' is not available`

**Try these models instead:**
- `llama2-70b-chat`
- `mistral-7b`
- `reka-flash`

## 🔧 **Demo Without Cortex AI**

If Cortex AI isn't working, you can still run a great demo:

### **What Still Works:**
- ✅ Executive Dashboard with all KPIs
- ✅ Interactive charts and visualizations  
- ✅ Data Explorer with all tables
- ✅ Professional Streamlit UI

### **What to Say:**
> *"The AI assistant requires Cortex AI to be enabled in your account. But as you can see, we've unified all your manufacturing data into these executive dashboards. The AI would let you ask questions like 'What's our inventory value?' and get instant business insights."*

### **Modified Demo Flow:**
1. **Focus on data unification** - show the dashboards
2. **Emphasize business value** - point to the KPIs
3. **Show technical capability** - use Data Explorer
4. **Promise AI demo** - "Let's set up Cortex for your pilot"

## 🎯 **Quick Fixes for Demo Day**

### **If Cortex Fails During Demo:**

#### **Stay Calm:**
- "Let me show you the data foundation first"
- Navigate to Executive Dashboard
- Show the unified KPIs and charts

#### **Pivot to Value:**
- "This is the real power - unified data from all your systems"
- Point to specific metrics: "$56M inventory value across 4 plants"
- "Imagine asking this data questions in natural language"

#### **Promise Follow-up:**
- "I'll set up the AI features for our next session"
- "The important thing is you can see the unified data foundation"

## 🚀 **Testing Cortex Before Demo**

### **Pre-Demo Checklist:**
```sql
-- 1. Test basic connection
SELECT CURRENT_USER(), CURRENT_ROLE();

-- 2. Test simple Cortex call
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'mixtral-8x7b',
    'Say hello'
);

-- 3. Test with manufacturing context
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'mixtral-8x7b',
    'You are a manufacturing analyst. What are key inventory metrics?'
);
```

### **If Tests Fail:**
- Use `04_cortex_fixed.sql` instead of `04_cortex.sql`
- Focus demo on dashboards and data unification
- Schedule follow-up for AI features

---

**Remember: The data unification and dashboards are the core value. Cortex AI is the cherry on top!** 🍒
