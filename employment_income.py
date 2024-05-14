def tax(income):
    if income >= 40000000:
        return round(income * 0.45, 2) - 4796000
    elif income < 39999000 and income >= 18000000:
        return round(income * 0.4, 2) - 2796000
    elif income < 17999000 and income >= 9000000:
        return round(income * 0.33, 2) - 1536000
    elif income < 8999000 and income >= 6950000:
        return round(income * 0.23, 2) - 636000
    elif income < 6949000 and income >= 3300000:
        return round(income * 0.20, 2) - 427500
    elif income < 3299000 and income >= 1950000:
        return round(income * 0.10, 2) - 97500
    elif income < 1949000 and income >= 1000:
        return round(income * 0.05, 2)
    else:
        return 0


def actual_burden_ratio(income):
    return str(round(tax(income) / income * 100, 2)) + "%"


income = int(input()) * 10000
print(tax(income), actual_burden_ratio(income))