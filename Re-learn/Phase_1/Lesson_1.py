full_name: str = input('What is your fullname? ')
age: int = int(input('What is your age? '))
city: str = input('What is your city of residence? ')
income: float = float(input('What is your monthly income? $ '))
annual_income = income * 12


sentence = f"Hi there {full_name}. Your age is {age}. You live in {city}.\n Your annual income is ${annual_income:,.2f} "

print(sentence)

# I learned how to typehint and format income.
