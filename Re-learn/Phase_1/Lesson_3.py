# region raw data
def get_age() -> int:
    age: int = int(input("What is your age? "))
    return age

def get_monthly_income() -> float:
    income: float = float(input("What is your monthly income? "))
    return income

def get_credit_score() -> int:
    credit_score = int(input("What is your credit score (0-850)? "))
    return credit_score


# endregion

# region validate raw data
def validate_age(age) -> bool:
    return 21 <= age <=65

    

def validate_monthly_income(income) -> bool:
    return income >= 20_000


def validate_credit_score(credit_score) -> bool:
    return credit_score >= 650


# endregion

# region final check
def check_special_scenario(income, credit) -> bool:
    return income > 100_000 or credit > 800


def check_validity(is_age_valid, is_income_valid, is_credit_score_valid) -> bool:
    return is_age_valid and is_income_valid and  is_credit_score_valid


def reason_for_invalidity(is_age_valid, is_income_valid, is_credit_score_valid):
    reasons = []
    if not is_age_valid:
        reasons.append("Age must be between 21-65")
    if not is_income_valid:
        reasons.append("Income is below 20,000")
    if not  is_credit_score_valid:
        reasons.append("credit is below 650")

    return ", ".join(reasons)


def normal_result(is_valid, reason):
    if is_valid:
        return "Loan Approved"
    return f"Loan Denied - reasons: {reason} "
    

# endregion

def main():
    age = get_age()
    income = get_monthly_income()
    credit_score = get_credit_score()

    is_special = check_special_scenario(income, credit_score)
    if is_special:
        result = normal_result(is_special, reason='')
        print(result)
        return



    is_age_valid = validate_age(age)
    is_income_valid = validate_monthly_income(income)
    is_credit_score_valid = validate_credit_score(credit_score)

    is_valid_for_loan = check_validity(is_age_valid, is_income_valid, is_credit_score_valid)
    reason = reason_for_invalidity(is_age_valid, is_income_valid, is_credit_score_valid)
    result = normal_result(is_valid_for_loan, reason)
    print(result)

main()



# I learned that regioning is important for easy access
# I learned that the result or the output must be user friendly. Answer the question "Will I get confused if I am the user?"