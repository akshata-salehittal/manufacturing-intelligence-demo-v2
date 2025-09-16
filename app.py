"""
Manufacturing Intelligence Demo - Clean Version
Simple, reliable Streamlit app with Snowflake + Cortex AI
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import snowflake.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Manufacturing Intelligence Demo",
    page_icon="🏭",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f77b4 0%, #2ca02c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_snowflake_connection():
    """Create Snowflake connection"""
    try:
        conn = snowflake.connector.connect(
            account=os.getenv('SNOWFLAKE_ACCOUNT'),
            user=os.getenv('SNOWFLAKE_USER'),
            password=os.getenv('SNOWFLAKE_PASSWORD'),
            warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
            database=os.getenv('SNOWFLAKE_DATABASE'),
            schema=os.getenv('SNOWFLAKE_SCHEMA'),
            role=os.getenv('SNOWFLAKE_ROLE')
        )
        return conn
    except Exception as e:
        st.error(f"Connection failed: {e}")
        return None

@st.cache_data(ttl=300)
def run_query(query):
    """Execute Snowflake query"""
    conn = get_snowflake_connection()
    if conn is None:
        return pd.DataFrame()
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(results, columns=columns)
        cursor.close()
        return df
    except Exception as e:
        st.error(f"Query failed: {e}")
        return pd.DataFrame()

def test_cortex_ai(question):
    """Test Cortex AI with a question"""
    query = f"""
    SELECT SNOWFLAKE.CORTEX.COMPLETE(
        'mixtral-8x7b',
        'You are a manufacturing analyst. Answer this question based on the context: {question}',
        {{'max_tokens': 300, 'temperature': 0.1}}
    ) as response
    """
    result = run_query(query)
    if not result.empty:
        return result.iloc[0]['RESPONSE']
    return "AI service unavailable"

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏭 Manufacturing Intelligence Platform</h1>
        <p>Powered by Snowflake + Cortex AI | Unified Manufacturing Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🎯 Demo Controls")
        
        # Connection test
        conn = get_snowflake_connection()
        if conn:
            st.success("✅ Connected to Snowflake")
        else:
            st.error("❌ Connection failed")
            st.info("💡 Check your .env configuration")
        
        # Demo sections
        demo_section = st.selectbox(
            "Choose Demo Section:",
            ["Executive Dashboard", "AI Assistant", "Data Explorer"]
        )
    
    # Main content based on selection
    if demo_section == "Executive Dashboard":
        render_executive_dashboard()
    elif demo_section == "AI Assistant":
        render_ai_assistant()
    else:
        render_data_explorer()

def render_executive_dashboard():
    """Executive dashboard with key metrics"""
    st.header("📊 Executive Dashboard")
    
    # Get financial KPIs
    financial_query = """
    SELECT 
        SUM(INVENTORY_VALUE) as TOTAL_INVENTORY,
        SUM(WORKING_CAPITAL) as TOTAL_WORKING_CAPITAL,
        SUM(COST_SAVINGS) as TOTAL_SAVINGS,
        COUNT(DISTINCT PLANT_ID) as TOTAL_PLANTS
    FROM FINANCIAL_KPIS
    """
    
    financial_data = run_query(financial_query)
    
    if not financial_data.empty:
        # KPI Cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Plants", 
                f"{int(financial_data.iloc[0]['TOTAL_PLANTS'])}"
            )
        
        with col2:
            inventory_val = financial_data.iloc[0]['TOTAL_INVENTORY'] / 1000000
            st.metric(
                "Inventory Value", 
                f"${inventory_val:.1f}M"
            )
        
        with col3:
            wc_val = financial_data.iloc[0]['TOTAL_WORKING_CAPITAL'] / 1000000
            st.metric(
                "Working Capital", 
                f"${wc_val:.1f}M"
            )
        
        with col4:
            savings_val = financial_data.iloc[0]['TOTAL_SAVINGS'] / 1000000
            st.metric(
                "Cost Savings", 
                f"${savings_val:.1f}M"
            )
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Inventory by plant
        inventory_query = """
        SELECT 
            PLANT_ID,
            SUM(CURRENT_STOCK * UNIT_COST) as INVENTORY_VALUE
        FROM INVENTORY
        GROUP BY PLANT_ID
        ORDER BY INVENTORY_VALUE DESC
        """
        
        inventory_data = run_query(inventory_query)
        if not inventory_data.empty:
            fig = px.bar(
                inventory_data, 
                x='PLANT_ID', 
                y='INVENTORY_VALUE',
                title="Inventory Value by Plant",
                color='INVENTORY_VALUE',
                color_continuous_scale='Blues'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Production efficiency
        production_query = """
        SELECT 
            PLANT_ID,
            AVG(EFFICIENCY_PERCENT) as AVG_EFFICIENCY
        FROM PRODUCTION
        GROUP BY PLANT_ID
        ORDER BY AVG_EFFICIENCY DESC
        """
        
        production_data = run_query(production_query)
        if not production_data.empty:
            fig = px.bar(
                production_data,
                x='PLANT_ID',
                y='AVG_EFFICIENCY',
                title="Average Production Efficiency",
                color='AVG_EFFICIENCY',
                color_continuous_scale='Greens'
            )
            fig.add_hline(y=90, line_dash="dash", line_color="red", 
                         annotation_text="Target: 90%")
            st.plotly_chart(fig, use_container_width=True)

def render_ai_assistant():
    """AI Assistant powered by Cortex"""
    st.header("🤖 AI Assistant")
    st.write("Ask questions about your manufacturing data using natural language.")
    
    # Sample questions
    with st.expander("💡 Sample Questions"):
        sample_questions = [
            "What's our total inventory value across all plants?",
            "Which plant has the highest production efficiency?",
            "What suppliers pose the highest risk?",
            "How can we optimize our inventory levels?"
        ]
        
        for question in sample_questions:
            if st.button(question, key=f"sample_{hash(question)}"):
                with st.spinner("Analyzing..."):
                    response = test_cortex_ai(question)
                    st.write("**AI Response:**")
                    st.write(response)
    
    # Chat interface
    user_question = st.text_input("Ask your question:")
    
    if user_question:
        with st.spinner("Getting AI insights..."):
            response = test_cortex_ai(user_question)
            st.write("**AI Response:**")
            st.write(response)

def render_data_explorer():
    """Data explorer with raw data views"""
    st.header("🔍 Data Explorer")
    
    # Data tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Inventory", "Production", "Suppliers", "Financial"])
    
    with tab1:
        st.subheader("Inventory Data")
        inventory_data = run_query("SELECT * FROM INVENTORY ORDER BY PLANT_ID, CATEGORY")
        if not inventory_data.empty:
            st.dataframe(inventory_data, use_container_width=True)
            
            # Quick stats
            total_value = (inventory_data['CURRENT_STOCK'] * inventory_data['UNIT_COST']).sum()
            st.metric("Total Inventory Value", f"${total_value:,.2f}")
    
    with tab2:
        st.subheader("Production Data")
        production_data = run_query("SELECT * FROM PRODUCTION ORDER BY PRODUCTION_DATE DESC")
        if not production_data.empty:
            st.dataframe(production_data, use_container_width=True)
            
            avg_efficiency = production_data['EFFICIENCY_PERCENT'].mean()
            st.metric("Average Efficiency", f"{avg_efficiency:.1f}%")
    
    with tab3:
        st.subheader("Supplier Data")
        supplier_data = run_query("SELECT * FROM SUPPLIERS ORDER BY RISK_SCORE DESC")
        if not supplier_data.empty:
            st.dataframe(supplier_data, use_container_width=True)
            
            high_risk = len(supplier_data[supplier_data['RISK_SCORE'] >= 4])
            st.metric("High Risk Suppliers", high_risk)
    
    with tab4:
        st.subheader("Financial KPIs")
        financial_data = run_query("SELECT * FROM FINANCIAL_KPIS ORDER BY KPI_DATE DESC")
        if not financial_data.empty:
            st.dataframe(financial_data, use_container_width=True)

if __name__ == "__main__":
    main()
