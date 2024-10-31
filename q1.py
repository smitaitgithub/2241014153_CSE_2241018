
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
hourly_rate=20
hours_worked_per_week=45
total=total_salary(hourly_rate,hours_worked_per_week)
print(f"total salary:{total}")
