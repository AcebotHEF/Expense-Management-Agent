# Expense Management Agent

An AI-powered compliance auditor that automates the review of employee expense reports. This agent checks financial data against company policies and flags violations instantly.

## 📝 Overview

Manual expense auditing is tedious and error-prone. This agent solves that by acting as a **Digital Forensic Auditor**. It:
1.  **Ingests** structured expense data (simulated via Pandas).
2.  **Analyzes** every transaction against a defined set of "Company Policies" (e.g., *Meals must be under $100*).
3.  **Reports** findings using **Google Gemini**, providing a clear summary of what to approve and what to flag.

---

## 🚀 Key Features

* **Automated Policy Checks:** Instantly detects transactions that exceed budget limits.
* **🧠 AI Reasoning:** Uses **Google Gemini (Flash 2.0)** to understand context (e.g., differentiating between a "Team Dinner" and a personal snack).
* **📊 Clear Reporting:** Displays the raw data alongside the AI's forensic analysis in a clean **Streamlit** dashboard.
* **Extensible Logic:** Policies are defined in natural language, making them easy to update without rewriting code.

---

## 🧰 Tech Stack

* **Language:** Python 3.11+
* **Interface:** Streamlit
* **AI Engine:** Google Gemini (via `langchain-google-genai`)
* **Data Processing:** Pandas
* **Orchestration:** LangChain

---

run the command below in the terminal after cloning the repository.
pip install -r requirements.txt



📂 Project Structure
expense_management_agent/
│
├── app.py                  # Main Streamlit dashboard
├── expense_agent.py        # Logic connecting Data + AI
├── expense_data.py         # Mock database of employee receipts
├── expense_prompt.py       # The "Persona" and "Rules" for the AI
└── requirements.txt        # Project dependencies

🧠 How It Works
Data Loading: expense_data.py creates a DataFrame with transactions like "Flight to NYC ($450)" and "Team Dinner ($180)".

Policy Definition: expense_prompt.py contains the instructions: "Check if Meals > $100".

AI Analysis: The agent sends the data + rules to Google Gemini. The AI reasoning engine compares the numbers and generates a text summary.

Visualization: Streamlit renders the table and the markdown response for the user.