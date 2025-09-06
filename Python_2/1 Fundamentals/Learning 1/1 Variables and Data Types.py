bullets = 13_140_000_000
death = 20_000_000
days_in_year = 365
years_lasted = 6

bullet_daily = bullets / (days_in_year * years_lasted)
deaths_daily = death / (days_in_year * years_lasted)
bullet_per_death = bullet_daily / deaths_daily



print(bullet_daily.__round__())
print(deaths_daily.__round__())
print(bullet_per_death.__round__())



boolean = 4 == 4
print(boolean)

