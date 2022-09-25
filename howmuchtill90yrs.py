age = input("What is your current age?")
total_days_90_yrs=90*365
total_weeks_90yrs=90*52
total_months_90yrs=90*12
days=total_days_90_yrs-(int(age)*365)
months=total_months_90yrs-(int(age)*12)
weeks=total_weeks_90yrs-(int(age)*52)
print(f"you have {days} days, {weeks} weeks and {months} months left")
