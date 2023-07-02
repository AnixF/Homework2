num_tickets = int(input("Введите количество билетов: "))
total_cost = 0  # общая стоимость заказа
discount = 0  # скидка

for _ in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))

    if age < 18:
        cost = 0
    elif age >= 18 and age < 25:
        cost = 990
    else:
        cost = 1390
    
    total_cost += cost

# применяем скидку, если количество билетов больше 3
if num_tickets > 3:
    discount = total_cost * 0.1

total_cost -= discount

print("Общая стоимость билетов:", total_cost, "руб.")
input()