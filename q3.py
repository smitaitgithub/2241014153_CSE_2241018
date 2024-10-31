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
hourly_rate=20
hours_worked_per_week=45
basic_salary_value=basic_salary(hourly_rate,hours_worked_per_week)
gross_salary_value=gross_salary(basic_salary_value)
print(f"Basic salary:{basic_salary_value}")
print(f"Gross salary :{gross_salary_value}")