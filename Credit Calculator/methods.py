import math


def args_checker(_list):
    numbers = {}
    if len(_list) < 4:
        return 'error'
    for i in _list:
        temp_list = i.split('=')
        formatted_key = temp_list[0][2:]
        try:
            float(temp_list[1])
        except:
            formatted_value = temp_list[1]
        else:
            formatted_value = float(temp_list[1])
            if formatted_value < 0:
                return 'error'
        numbers[formatted_key] = temp_list[1]
    if ('annuity' not in numbers['type']) and ('diff' not in numbers['type']):
        return 'error'
    elif numbers['type'] == 'diff' and 'payment' in numbers:
        return 'error'
    elif 'interest' not in numbers:
        return 'error'
    return numbers


def annuity(_dict):
    if 'principal' not in _dict:
        payment = float(_dict['payment'])
        periods = int(_dict['periods'])
        interest = float(_dict['interest']) / 1200
        principal = int(
            payment/((interest*((1+interest)**periods))/(((1+interest)**periods)-1)))
        print(f"Your credit principal = {principal}!")
        print(f'Overpayment = {int(payment * periods - principal)}')
    elif 'payment' not in _dict:
        principal = int(_dict['principal'])
        periods = int(_dict['periods'])
        interest = float(_dict['interest'])/1200
        annuity = principal * \
            ((interest*((1+interest)**periods))/(((1+interest)**periods)-1))
        print(f"Your annuity payment = {math.ceil(annuity)}!")
        print(f'Overpayment = {math.ceil(annuity) * periods - principal}')
    else:
        principal = int(_dict['principal'])
        payment = float(_dict['payment'])
        interest = float(_dict['interest'])/1200
        periods = math.ceil(
            math.log(payment/(payment-(interest*principal)))/math.log(1+interest))
        if periods < 12:
            print(f"You need {int(periods/12)} months to repay this credit!")
        elif periods % 12 == 0:
            print(f"You need {int(periods/12)} years to repay this credit!")
        else:
            print(
                f"You need {math.floor(periods/12)} years and {math.ceil(periods-(math.floor(periods/12)*12))} months to repay this credit!")
        print(f'Overpayment = {math.ceil(payment) * periods - principal}')


def diff(_dict):
    principal = int(_dict['principal'])
    periods = int(_dict['periods'])
    interest = float(_dict['interest']) / 1200
    total_payments = 0
    for month in range(1, periods + 1):
        payment = math.ceil(principal / periods + interest *
                            (principal - ((principal * (month - 1)) / periods)))
        total_payments += payment
        print(f'Month {month}: paid out {payment}')
    print(f'Overpayment = {total_payments - principal}')
