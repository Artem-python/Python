money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

while True:
    delta = spend - salary
    if delta > money_capital:
        break
    month += 1
    money_capital -= delta
    spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", month)
