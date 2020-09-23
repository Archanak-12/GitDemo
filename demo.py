import csv

column = []

with open('hotels.csv', 'rt') as f:
    reader = csv.DictReader(f)
    for row in reader:
        column.append(row)

# print(column)

print('What is the state:')
state = input()

print('Cost or Rating:')
column_for_operation = input()

print('Operation:')
operation = input()

data_having_state = []
for sub in column:
    if sub['State'].lower() == state.lower():
        data_having_state.append(sub)
        # print(sub)

# print(data_having_state)
if column_for_operation.lower() == 'cost':
    # print(column_for_operation)
    sorted_cost_data_having_state = sorted(data_having_state, key=lambda k: int(k['Cost']))
    # for sub in sorted_cost_data_having_state:
    #     print(sub)

    len = len(sorted_cost_data_having_state)
    if operation.lower() == 'cheapest':
        print('Hotel with cheapest price in {} is {} with price {}'.format(state, sorted_cost_data_having_state[0]["Hotel Code"], sorted_cost_data_having_state[0]["Cost"]))
    elif operation.lower() == 'highest':
        print("Hotel with highest price in {} is {} with price {}".format(state, sorted_cost_data_having_state[len - 1]["Hotel Code"], sorted_cost_data_having_state[len - 1]["Cost"]))
    elif operation.lower() == 'average':
        sum = 0.0
        for sub in sorted_cost_data_having_state:
            sum += float(sub["Cost"])
        average_cost = sum / len
        print('Average cost of Hotel in {} is {}'.format(state, average_cost))
elif column_for_operation.lower() == 'rating':
    print(column_for_operation)
    sorted_rating_data_having_state = sorted(data_having_state, key=lambda k: float(k['Ratings']))
    len = len(sorted_rating_data_having_state)
    # for sub in sorted_rating_data_having_state:
    #     print(sub)

    if operation.lower() == 'cheapest':

        print('Hotel with cheapest rating in {} is {} with rating {}'.format(state, sorted_rating_data_having_state[0]["Hotel Code"], sorted_rating_data_having_state[0]["Ratings"]))
    elif operation.lower() == 'highest':
        print('Hotel with highest rating in {} is {} with rating {}'.format(state, sorted_rating_data_having_state[len - 1]["Hotel Code"], sorted_rating_data_having_state[len - 1]["Ratings"]))
    elif operation.lower() == 'average':
        sum = 0.0
        for sub in sorted_rating_data_having_state:
            sum += float(sub["Ratings"])
        average_rating = sum / len
        # print(sum)
        # print(average_rating)
        print('Average rating of Hotel in {} is {}'.format(state, average_rating))

