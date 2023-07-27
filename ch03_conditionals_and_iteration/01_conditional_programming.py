#########################
# Conditional programming
#########################
# conditional.1.py
late = True
if late:
    print('I need to call my manager!')

# conditional.2.py
late = False
if late:
    print('I need to call my manager!')
else:
    print('no need to call my manager...')

#############################
# ## A specialized else: elif
#############################
# taxes.py
income = 15000
if income < 10000:
    tax_coefficient = 0.0
elif income < 30000:
    tax_coefficient = 0.2
elif income < 100000:
    tax_coefficient = 0.35
else:
    tax_coefficient = 0.45

print(f'You will pay: ${income * tax_coefficient} in taxes')


def send_email(email, error_message):
    print(f'Send message "{error_message}" to "{email}"')


# errorsalert.py
alert_system = 'console'  # other value can be 'email'
error_severity = 'critical'  # other values: 'medium' or 'low'
error_message = 'OMG! Something terrible happened!'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        send_email('admin@example.com', error_message)
    elif error_severity == 'medium':
        send_email('support.1@example.com', error_message)
    else:
        send_email('support.2@example.com', error_message)

#############################
# ## The ternary operator
#############################
# ternary.py
order_total = 247  # GBP

# classic if/else form
if order_total > 100:
    discount = 25  # GBP
else:
    discount = 0  # GBP
print(order_total, discount)

# ternary operator
discount = 25 if order_total > 100 else 0
print(order_total, discount)
