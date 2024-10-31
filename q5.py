def basic_salary(hourly_rate,hours_worked_per_week):
    return hourly_rate*hours_worked_per_week*4
def overtime_salary(hourly_rate,hours_worked_per_week):
    if hours_worked_per_week>40:
        overtime=hours_worked_per_week-40
        return overtime*hourly_rate*1.5
    return 0
def total_salary(hourly_rate,hours_worked_per_week):
    basic=basic_salary(hourly_rate,hours_worked_per_week)
    overtime=overtime_salary(hourly_rate,hours_worked_per_week)
    return basic+overtime
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
def employee_report():
    num_sets=3
    employees=[]
    for i in range(num_sets):
        print(f"\n Entering details for employee set{i+1}:")
        name=input("Enter employee name:")
        hourly_rate=float(input("Enter hourly rate:"))
        hours_worked_per_week=float(input("Enter hours worked per week:"))
        basic_sal=basic_salary(hourly_rate,hours_worked_per_week)
        total_sal=total_salary(hourly_rate,hours_worked_per_week)
        gross_sal=gross_salary(basic_sal)
        tax=tax_amount(basic_sal)
        salary_cat=salary_bracket(gross_sal)
        employee_details={
            "name":name,
            "basic_salary":basic_sal,
            "gross_salary":gross_sal,
            "tax_amount":tax,
            "salary_bracket":salary_cat,
        }
        employees.append(employee_details)
        print("\nEmployee Salary Report:")
        print("{:<20} {:<15} {:<15} {:<15} {:<15}".format("Name","Basic Salary","Gross salary","Tax Amount","Salary Bracket"))
        print("-" * 80)
        for emp in employees:
            print("{:<20} ${:<14.2f} ${:<14.2f} ${:<14.2f} {}".format(
                emp["name"],
                emp["basic_salary"],
                emp["gross_salary"],
                emp["tax_amount"],
                emp["salary_bracket"]
            ))
employee_report()



        