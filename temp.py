def check_temperature(temp):
    if temp >= 28:
        return "Hot"
    elif 18 <= temp <= 28: 
        return "Warm"
    else:
        return "Cold"
print(check_temperature(18)) 
