from conn import create_connection


def rent_calculator(income, other_expenses):
    available_budget = income - other_expenses
    print("You can afford rent up to: ", available_budget, " Rs.")
    return available_budget

connection=create_connection()