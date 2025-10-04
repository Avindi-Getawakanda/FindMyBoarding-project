def rent_calculator(income, other_expenses):
    """Calculate available budget for rent"""
    try:
        income = float(income)
        other_expenses = float(other_expenses)
        available_budget = income - other_expenses
        print(f"You can afford rent up to: Rs. {available_budget:,.2f}")
        return available_budget
    except (ValueError, TypeError):
        print("Invalid input. Please enter valid numbers.")
        return 0