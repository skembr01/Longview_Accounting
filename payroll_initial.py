#Embry's Longview Payroll Calculator

#Function which calculates federal taxes to be withheld

def federal_withhold(gross):
    if 75 <= gross < 265:
        cycles = int((gross - 75) / 15)
        value = 0
        for i in range(0, cycles + 1):
            value += 1
    elif 265 <= gross < 340:
        cycles = int((gross - 265) / 15)
        value = 19
        for i in range(0, cycles + 1):
            if i % 4 == 0:
                value += 1
            elif i % 4 != 0:
                value += 2
    elif 340 <= gross < 850:
        cycles = int(((gross - 265) / 15) - 4)
        value = 27
        for i in range(1, cycles + 1):
            if i % 5 == 0:
                value += 1
            elif i % 5 != 0:
                value += 2
    return value

#Function which calculates the pay for hourly employees with different \
#wages and different withholdings

def hourly_calc(name, hours):
    count = 0
    if name == 'josh' or name == 'JOSH' or name == 'Josh' \
        or name == 'lucas' or name == 'LUCAS' or name == 'Lucas':
        count += 1
    elif name == 'amanda' or name == 'AMANDA' or name == 'Amanda':
        count += 2
    elif name == 'mike' or name == 'MIKE' or name == 'Mike':
        count += 3
    if count == 1:
        wage = 10
        gross = round((hours * wage), 2)
        ss = round((gross * 0.062), 2)
        medicare = round((gross * 0.0145), 2)
        ky_withhold = round((((int(gross / 10) - 5) * 0.5) + 0.20), 2)
        fed_withhold = round(federal_withhold(gross), 2)
        net = round((gross - (ss + medicare + ky_withhold + fed_withhold)), 2)
        return ('gross pay: ' + str(gross) + '\n' + ('ss: ' + str(ss)) + '\n' + ('medicare: ' + str(round(medicare, 5)) + '\n' + ('ky withhold: ' + str(ky_withhold)) + '\n' + ('fed withhold: ' + str(fed_withhold)) + '\n' + ('net pay: ' + str(net))))
    elif count == 2:
        wage = 9
        gross = round((hours * wage), 2)
        ss = round((gross * 0.062), 2)
        medicare = round((gross * 0.0145), 2)
        ky_withhold = round((((int(gross / 10) - 5) * 0.5) + 0.20), 2)
        fed_withhold = round(federal_withhold(gross), 2)
        net = round((gross - (ss + medicare + ky_withhold + fed_withhold)), 2)
        return ('gross pay: ' + str(gross) + '\n' + ('ss: '  + str(ss)) + '\n' + ('medicare: ' + str(round(medicare, 5)) + '\n' + ('ky withhold: ' + str(ky_withhold)) + '\n' + ('fed withhold: ' + str(fed_withhold)) + '\n' + ('net pay: ' + str(net))))
    elif count == 3:
        wage = 10
        gross = round((hours * wage), 2)
        ss = round((gross * 0.062), 2)
        medicare = round((gross * 0.0145), 2)
        ky_withhold = round((((int(gross / 10) - 5) * 0.5) + 0.20), 2)
        fed_withhold = round(federal_withhold(gross), 2)
        child_support = 58.20
        net = round(gross - (ss + medicare + ky_withhold + fed_withhold + child_support), 2)
        return ('gross pay: ' + str(gross) + '\n' + ('ss: ' + str(ss)) + '\n' + ('medicare: ' + str(round(medicare, 5)) + '\n' + ('ky withhold: ' + str(ky_withhold)) + '\n' + ('fed withhold: ' + str(fed_withhold)) + '\n' + ('child support: ' + str(child_support)) + '\n' + ('net pay: ' + str(net))))

#Function for salaried employees so their taxes and pay can be easily \
#visualized for each payment cycle

def salary_calc(gross):
    ss = round((gross * 0.062), 2)
    medicare = round((gross * 0.0145), 2)
    ky_withhold = round((((int(gross / 10) - 5) * 0.5) + 0.20), 2)
    fed_withhold = round(federal_withhold(gross), 2)
    net = round((gross - (ss + medicare + ky_withhold + fed_withhold)), 2)
    return ('gross pay: ' + str(gross) + '\n' + ('ss: ' + str(ss)) + '\n' + ('medicare: ' + str(round(medicare, 5)) + '\n' + ('ky withhold: ' + str(ky_withhold)) + '\n' + ('fed withhold: ' + str(fed_withhold)) + '\n' + ('net pay: ' + str(net))))



name = input('name: ')
if name == 'ross' or name == 'ROSS' or name == 'Ross':
    gross = int(input('weekly wage: '))
    print(salary_calc(gross))
elif name == 'matt' or name == 'MATT' or name == 'Matt':
    gross = int(input('weekly wage: '))
    print(salary_calc(gross))
else:
    hours = float(input('hours: '))
    print(hourly_calc(name, hours))
