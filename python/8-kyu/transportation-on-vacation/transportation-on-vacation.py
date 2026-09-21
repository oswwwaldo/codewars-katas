def rental_car_cost(d):
    total = d * 40
    if (d >= 7):
        total = total - 50
    elif (d >= 3):
        total = total - 20
    return total