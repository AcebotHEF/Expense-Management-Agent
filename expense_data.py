import pandas as pd

def load_expenses():
    data = {
        "Date": [
            "2025-07-01", "2025-07-01", "2025-07-02", 
            "2025-07-03", "2025-07-03", "2025-07-04"
        ],
        "Description": [
            "Flight to NYC", "Uber to Hotel", "Hotel Stay", 
            "Team Dinner", "Uber to Airport", "Conference Fee"
        ],
        "Category": [
            "Travel", "Transport", "Lodging", 
            "Meals", "Transport", "Training"
        ],
        "Amount": [450.00, 45.50, 600.00, 180.00, 42.00, 1200.00]
    }
    df = pd.DataFrame(data)
    return df