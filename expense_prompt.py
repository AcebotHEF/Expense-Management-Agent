from langchain_core.prompts import PromptTemplate

expense_prompt = PromptTemplate.from_template("""
You are an AI expense compliance auditor.

Below is a list of expenses submitted by an employee:

{expense_table}

Tasks:
1. Check if any items exceed reasonable expense policy limits:
   - Travel: Limit $500
   - Meals: Limit $100
   - Training: Limit $1000
2. Suggest which specific items should be reviewed or flagged.
3. Provide a concise summary for the finance team recommending approval or rejection.
""")