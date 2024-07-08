def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the leading '$' and convert the remaining string to a float
    d_without_dollar_sign=d.replace("$"," ")
    return float(d_without_dollar_sign)


def percent_to_float(p):
    #Remove the trailing '%' and convert the remaining string to a float, then divide by 100 to get the percentage
    p_without_parcent=p.replace("%"," ")
    p_converted=float(p_without_percent)/ 100
    return p_converted


main()
