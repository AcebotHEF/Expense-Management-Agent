import streamlit as st
from expense_agent import analyze_expenses

# Optional: Set tab title
st.set_page_config(page_title="Expense Auditor", page_icon="💳")

st.title("💳 Expense Management Agent")

if st.button("Audit My Expenses"):
    with st.spinner("Analyzing receipts against policy..."):
        df, result = analyze_expenses()

        st.subheader("📂 Expense Report")
        st.dataframe(df)

        st.divider()

        st.subheader("🔍 AI Compliance Review")
        # Use markdown so bold text and lists render correctly
        st.markdown(result)