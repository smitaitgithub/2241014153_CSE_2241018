def basic_salary(hourly_rate,hours_worked_per_week):
    return hourly_rate*hours_worked_per_week*4
def tax_amount(basic_salary):
    if basic_salary<60000:
        tax=basic_salary*0.1
    elif 60000<=basic_salary<=85000:
        tax=basic_salary*0.15
    else:
        tax=basic_salary*0.2
    return tax
def gross_salary(basic_salary):
    allowances=0.2*basic_salary
    tax=tax_amount(basic_salary)
    return basic_salary+allowances-tax
def salary_bracket(gross_salary):
    if gross_salary<50000:
         return"low income"
    elif 50000<=gross_salary<=80000:
        return "Middle income"
    else:
        return "High income"
hourly_rate=20
hours_worked_per_week=45
basic_salary_value=basic_salary(hourly_rate,hours_worked_per_week)
gross_salary_value=gross_salary(basic_salary_value)
bracket=salary_bracket(gross_salary_value)
print(f"basic salary:{basic_salary_value}")
print(f"gross salary:{gross_salary_value}")
print(f"salary bracket is:{bracket}")