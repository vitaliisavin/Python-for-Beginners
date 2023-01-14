import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", choices=["annuity", "diff"])
parser.add_argument('-pc', '--principal', type=float)
parser.add_argument('-pr', '--periods', type=float)
parser.add_argument('-i', '--interest', type=float)
parser.add_argument('-pay', '--payment', type=float)
args = parser.parse_args()

if args.type is None or args.interest is None or args.type == 'diff' and args.payment is not None:
    print('Incorrect parameters')
    exit()

parameters = [args.type, args.principal, args.periods, args.interest, args.payment]
count = 5
for param in parameters:
    if param is None:
        count += 1
    elif type(param) is float and param < 0:
        count = 0
if count < 4:
    print('Incorrect parameters')
    exit()


def for_annuity_payment(rate, payments):
    return ((rate * math.pow(1 + rate, payments)) /
            (math.pow(1 + rate, payments) - 1))


loan_principal = parameters[1]  # It's 'P'
interest_rate = parameters[3] / (12 * 100)  # It's 'i'
number_of_payments = parameters[2]  # It's 'n'
annuity_payment = parameters[4]

if args.type == 'diff':
    i = 1
    all_payments = 0
    while i <= number_of_payments:
        diff_payment = (loan_principal / number_of_payments) + interest_rate * \
                       (loan_principal - (loan_principal * (i - 1) / number_of_payments))
        diff_payment = round(math.ceil(diff_payment))
        print(f'Month {i}: payment is {diff_payment}')
        all_payments += diff_payment
        i += 1
    print(f'Overpayment = {round(all_payments - loan_principal)}')

elif args.type == 'annuity':
    if loan_principal is None:
        loan_principal = annuity_payment / for_annuity_payment(interest_rate, number_of_payments)
        loan_principal = round(loan_principal)
        print(f'Your loan principal = {loan_principal}!')
    elif number_of_payments is None:
        numbs_of_months = math.log(annuity_payment / (annuity_payment - (interest_rate * loan_principal)), 1 + interest_rate)
        numbs_of_months = math.ceil(numbs_of_months)
        overpayment = numbs_of_months * annuity_payment - loan_principal
        print(numbs_of_months // 12, round(overpayment))
    elif annuity_payment is None:
        annuity_payment = loan_principal * for_annuity_payment(interest_rate, number_of_payments)
        print(f'Your annuity payment = {round(math.ceil(annuity_payment))}!')
        overpayment = round(math.ceil(annuity_payment)) * number_of_payments - loan_principal
        print(f'Overpayment = {round(overpayment)}')

