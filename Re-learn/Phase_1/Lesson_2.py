def get_annual_salary() -> float:
    salary = float(input("What is your monthly salary? $"))
    return salary * 12

def get_bonus_percentage() -> float:
    percent = float(input("What is your bonus percentage? "))
    return percent/100

def get_bonus_amount(annual_salary, percent) -> float:
    return annual_salary * percent

def get_gross_total(annual_salary , bonus_amount)-> float:
    return annual_salary + bonus_amount

def get_tax_percentage() -> float:
    tax = float(input("How much is your tax percentage? "))
    return tax/100

def get_net_total(gross, tax)-> float:
    return gross - (gross * tax)

def formatter(annual_salary, bonus_amount, gross_total, net_total):
    result = (f"Annual Salary: ${annual_salary:,.2f}.\n"
        f"Bonus Amount: ${bonus_amount:,.2f}\n"
        f"Gross Total: ${gross_total:,.2f}\n"
        f"Net Total: ${net_total:,.2f}\n"
        )
    
    return result
    

def main():
    annual_salary = get_annual_salary()

    bonus_percent = get_bonus_percentage()

    if bonus_percent >= 0.5:
        print("Bonus unusually high")

    bonus_amount = get_bonus_amount(annual_salary, bonus_percent)
    gross_total = get_gross_total(annual_salary, bonus_amount)
    tax = get_tax_percentage()

    if tax <= 0:
        print("Invalid tax rate")
        return
    

    net_total = get_net_total(gross_total, tax)


    result = formatter(annual_salary, bonus_amount, gross_total, net_total)
    print(result)


main()


# 1. I learned how to make functions for each problem and assign return values to another functions
# 2. I learned that understanding the problem and the outcome of it is important
# 3. I learned that I must give some comments to know what that thing do.