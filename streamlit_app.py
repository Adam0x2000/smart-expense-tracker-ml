
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Expense Tracker", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}

.main-title {
    background: linear-gradient(90deg, #0f5132, #198754);
    padding: 30px;
    border-radius: 12px;
    color: white;
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 20px;
}

.section-card {
    background-color: white;
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 6px 14px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.metric-card {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

# ---------------- LOGIN SIMULATION ----------------
st.sidebar.title("🔐 Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username != "admin" or password != "admin123":
    st.sidebar.warning("Please login to continue")
    st.stop()
else:
    st.sidebar.success("Login successful")

# ---------------- TITLE ----------------
st.markdown('<div class="main-title">💰 Smart Expense Tracker</div>', unsafe_allow_html=True)

# ---------------- DEMO DATA ----------------
if st.button("🔁 Fill Demo Data"):
    st.session_state.monthly_income = 35000.0
    st.session_state.monthly_expense_total = 14658.0
    st.session_state.savings_rate = 0.58
    st.session_state.budget_goal = 18000.0
    st.session_state.credit_score = 720
    st.session_state.debt_to_income_ratio = 0.15
    st.session_state.loan_payment = 2000.0
    st.session_state.transaction_count = 45
    st.session_state.discretionary_spending = 5000.0
    st.session_state.essential_spending = 9658.0
    st.session_state.rent_or_mortgage = 7000.0
    st.session_state.actual_savings = 20342.0
    st.session_state.savings_goal_met = 1
    st.session_state.financial_advice_score = 78
    st.session_state.fraud_flag = 0
    st.session_state.investment_amount = 3000.0
    st.session_state.emergency_fund = 10000.0
    st.session_state.subscription_services = 599.0
    st.session_state.income_type = "Salary"
    st.session_state.category = "Food"
    st.session_state.financial_scenario = "normal"
    st.session_state.financial_stress_level = "low"

# ---------------- INPUT SECTION ----------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("📌 Financial Inputs")

col1, col2, col3 = st.columns(3)

with col1:
    monthly_income = st.number_input("Monthly Income (₹)", min_value=0.0, key="monthly_income")
    credit_score = st.slider("Credit Score", 300, 850, 650, key="credit_score")
    transaction_count = st.number_input("Transaction Count", min_value=0, key="transaction_count")
    investment_amount = st.number_input("Investment Amount (₹)", min_value=0.0, key="investment_amount")

with col2:
    monthly_expense_total = st.number_input("Monthly Expense Total (₹)", min_value=0.0, key="monthly_expense_total")
    debt_to_income_ratio = st.slider("Debt to Income Ratio", 0.0, 1.0, 0.3, key="debt_to_income_ratio")
    discretionary_spending = st.number_input("Discretionary Spending (₹)", min_value=0.0, key="discretionary_spending")
    emergency_fund = st.number_input("Emergency Fund (₹)", min_value=0.0, key="emergency_fund")

with col3:
    savings_rate = st.slider("Savings Rate", 0.0, 1.0, 0.2, key="savings_rate")
    loan_payment = st.number_input("Loan Payment (₹)", min_value=0.0, key="loan_payment")
    essential_spending = st.number_input("Essential Spending (₹)", min_value=0.0, key="essential_spending")
    subscription_services = st.number_input("Subscription Services (₹)", min_value=0.0, key="subscription_services")

rent_or_mortgage = st.number_input("Rent / Mortgage (₹)", min_value=0.0, key="rent_or_mortgage")
actual_savings = st.number_input("Actual Savings (₹)", min_value=0.0, key="actual_savings")
budget_goal = st.number_input("Budget Goal (₹)", min_value=0.0, key="budget_goal")

income_type = st.selectbox("Income Type", ["Salary", "Freelance", "Business"], key="income_type")
category = st.selectbox("Expense Category", ["Food", "Travel", "Rent", "Shopping"], key="category")
financial_scenario = st.selectbox("Financial Scenario", ["normal", "inflation", "recession"], key="financial_scenario")
financial_stress_level = st.selectbox("Financial Stress Level", ["low", "medium", "high"], key="financial_stress_level")

savings_goal_met = st.selectbox("Savings Goal Met", [0, 1], key="savings_goal_met")
financial_advice_score = st.slider("Financial Advice Score", 0, 100, 70, key="financial_advice_score")
fraud_flag = st.selectbox("Fraud Flag", [0, 1], key="fraud_flag")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- WARNING ----------------
if monthly_expense_total > monthly_income:
    st.error("🚨 Your expenses exceed your income!")

# ---------------- PREDICTION ----------------
if st.button("🔮 Predict Cash Flow Status"):
    input_df = pd.DataFrame([{
        "monthly_income": monthly_income,
        "monthly_expense_total": monthly_expense_total,
        "savings_rate": savings_rate,
        "budget_goal": budget_goal,
        "credit_score": credit_score,
        "debt_to_income_ratio": debt_to_income_ratio,
        "loan_payment": loan_payment,
        "transaction_count": transaction_count,
        "discretionary_spending": discretionary_spending,
        "essential_spending": essential_spending,
        "rent_or_mortgage": rent_or_mortgage,
        "actual_savings": actual_savings,
        "savings_goal_met": savings_goal_met,
        "financial_advice_score": financial_advice_score,
        "fraud_flag": fraud_flag,
        "investment_amount": investment_amount,
        "emergency_fund": emergency_fund,
        "subscription_services": subscription_services,
        "income_type": income_type,
        "category": category,
        "financial_scenario": financial_scenario,
        "financial_stress_level": financial_stress_level
    }])

    transformed = encoder.transform(input_df)
    prediction = model.predict(transformed)[0]
    confidence = model.predict_proba(transformed).max() * 100

    st.success(f"📊 Cash Flow Status: **{prediction}**")
    st.info(f"🔍 Prediction Confidence: **{confidence:.2f}%**")

    # ---------------- KPI CARDS ----------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f'<div class="metric-card">💰<br><b>Income</b><br>₹ {monthly_income:,.0f}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card">💸<br><b>Expenses</b><br>₹ {monthly_expense_total:,.0f}</div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card">💾<br><b>Savings</b><br>₹ {monthly_income - monthly_expense_total:,.0f}</div>', unsafe_allow_html=True)

    # ---------------- INSIGHT ----------------
    if prediction.lower() in ["good", "positive", "stable"]:
        st.success("✅ You are managing your finances well.")
    elif prediction.lower() == "average":
        st.warning("⚠️ Your finances are stable but could improve.")
    else:
        st.error("❌ Financial stress detected. Review expenses.")

    # ---------------- PIE CHART ----------------
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("📊 Expense Distribution")

    expense_data = {
        "Essential": essential_spending,
        "Discretionary": discretionary_spending,
        "Rent": rent_or_mortgage,
        "Subscriptions": subscription_services
    }

    fig, ax = plt.subplots()
    ax.pie(expense_data.values(),
           labels=expense_data.keys(),
           autopct="%1.1f%%",
           startangle=90)
    ax.axis("equal")

    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)
