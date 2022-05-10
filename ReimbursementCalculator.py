import datetime

ONE_DAY = datetime.timedelta(days=1)

RATE_CODE_VALUES = {
    'h': 'HIGH COST',
    'l': 'LOW COST',
    't': 'TRAVEL DAY',
    'f': 'FULL DAY'
}

REIMBURSEMENT_CODES = {
    'lt': 45,
    'ht': 55,
    'lf': 75,
    'hf': 85
}


def validate_date(date_str):
    converted_date = None
    try:
        converted_date = datetime.datetime.strptime(date_str, '%m/%d/%y').date()
    except:
        try:
            converted_date = datetime.datetime.strptime(date_str, '%m/%d/%Y').date()
        except:
            print('Oops!  Please enter dates in the format mm/dd/yy or mm/dd/yyyy.')
            print('')
    return converted_date


def validate_cost(cost_str):
    cost_value = None
    if cost_str.lower() in ('h', 'l'):
        cost_value = cost_str.lower()
    else:
        print('Oops!  Please enter project location costs in the format "H", "h", "L", or "l".')
        print('')
    return cost_value


input_done = False
high_cost_dates = []
low_cost_dates = []
print('')
print('Welcome to the project reimbursement calculator.')
print('Please enter all of the required information for at least one project.')
print('')

while not input_done:
    # Retrieve and validate start date from the user
    start_date_valid = False
    while not start_date_valid:
        start_date_input = input("Enter the project start date. (Format: mm/dd/yyyy or mm/dd/yy): ")
        start_date = validate_date(start_date_input)
        if start_date is not None:
            start_date_valid = True

    # Retrieve and validate end date from the user
    end_date_valid = False
    while not end_date_valid:
        end_date_input = input("Enter the project end date. (Format: mm/dd/yyyy or mm/dd/yy): ")
        end_date = validate_date(end_date_input)
        if end_date is not None:
            end_date_valid = True

    # Retrieve and validate location cost from the user
    cost_valid = False
    while not cost_valid:
        cost_input = input("Enter the project location cost. (H/h for High Cost or L/l for Low Cost): ")
        cost = validate_cost(cost_input)
        if cost is not None:
            cost_valid = True

    # Uncomment to show validated info for each record entered.
    # print('')
    # print('Project record entered -> (Start: ' + start_date.strftime('%m/%d/%Y') + ' End: ' + end_date.strftime('%m/%d/%Y') + ' Location cost: ' + RATE_CODE_VALUES[cost] + ')')
    # print('')

    # Parse project records into separate lists by their location cost value
    work_date = start_date
    while work_date <= end_date:
        if cost == 'h':
            high_cost_dates.append(work_date)
        else:
            low_cost_dates.append(work_date)
        work_date = work_date + ONE_DAY

    # Check if the user still has project records to enter
    input_done_valid = False
    while not input_done_valid:
        user_done_input = input("Would you like to enter another project? (Y/y for Yes or N/n for No): ")
        if user_done_input.lower() == 'y':
            input_done_valid = True
            input_done = False
            print('')
        elif user_done_input.lower() == 'n':
            input_done_valid = True
            input_done = True
        else:
            print('Oops!  Please enter your response in the format "Y", "y", "N", or "n".')
            print('')

# Remove duplicate dates and keep HIGH COST dates when there is an overlap
all_dates_and_rates = []
for date in high_cost_dates:
    record = (date, 'h')
    if record not in all_dates_and_rates:
        all_dates_and_rates.append(record)
for date in low_cost_dates:
    record = (date, 'l')
    if date not in high_cost_dates and record not in all_dates_and_rates:
        all_dates_and_rates.append(record)

# Sort the de-duped list
sorted_dates = sorted(all_dates_and_rates, key=lambda x: x[0])

# Search for gaps to determine extra travel days
for i in range(len(sorted_dates)):
    if i == 0 or i == len(sorted_dates) - 1:
        sorted_dates[i] = sorted_dates[i] + ('t',)
    else:
        current_work_day = sorted_dates[i][0]
        previous_day = current_work_day - ONE_DAY
        next_day = current_work_day + ONE_DAY
        previous_work_day = sorted_dates[i-1][0]
        next_work_day = sorted_dates[i+1][0]
        if next_work_day != next_day or previous_work_day != previous_day:
            sorted_dates[i] = sorted_dates[i] + ('t',)
        else:
            sorted_dates[i] = sorted_dates[i] + ('f',)

print('')
total_reimbursement = 0

# Calculate the daily and total reimbursement amounts and display them to the user
for date in sorted_dates:
    reimbursement_code = date[1] + date[2]
    daily_reimbursement = REIMBURSEMENT_CODES[reimbursement_code]
    print(date[0].strftime('%m/%d/%Y') + ' was a ' + RATE_CODE_VALUES[date[2]] + ' in a ' + RATE_CODE_VALUES[date[1]] + ' city and is reimbursed at $' + str(daily_reimbursement) + '/day.')
    total_reimbursement += daily_reimbursement

print('')
print('The total reimbursement for this set of projects is $' + str(total_reimbursement) + '.')
