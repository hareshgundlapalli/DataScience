#!/usr/bin/python -tt

import sys

###
##excercise1: https://app.dataquest.io/m/312/lists-and-for-loops/6/list-of-lists
##Assign the resulting list of lists to a variable named app_data_set.
##Compute the average rating of the apps by retrieving the right data points from the app_data_set list of lists.
##The rating is the last element of each row. You'll need to sum up the ratings and then divide by the number of ratings.
##Assign the result to a variable named avg_rating.
###

def exercise_1():
    row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
    row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
    row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
    row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
    row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

    data_set = [row_1, row_2, row_3, row_4, row_5]
    # print(data_set)
    app_data_set = [row_1, row_2, row_3, row_4, row_5]
    avg_sum = 0
    for i in app_data_set:
        avg_sum += i[-1]
    avg_rating = avg_sum / len(app_data_set)
    print(avg_rating)
    return


###
##excercise2:
##https://app.dataquest.io/m/312/lists-and-for-loops/7/opening-a-file
##
###
def exercise_2(filename):
    opened_file = open(filename)
    from csv import reader  # to read the csv file, we import the reader command from csv module
    read_file = reader(opened_file)  # dump the whole csv file to read_file
    merch_data = list(read_file)  # whole file is now being stored in merch_data as list of lists
    print('First 5 rows')
    print(merch_data[:5])  # prints only top 5 rows of the list
    print('Total rows in file:', len(merch_data))  # prints length of file, means total rows imported
    print('First row')
    print(merch_data[:1])  # prints first row
    print('Next 2 rows using slicing')
    print(merch_data[1:3])  # prints second and 3rd row
    opened_file.close()
    return


def exercise_3():
    row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
    row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
    row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
    row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
    row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

    data_set = [row_1, row_2, row_3, row_4, row_5]
    # print(data_set)
    app_data_set = [row_1, row_2, row_3, row_4, row_5]
    avg_sum = 0
    for i in app_data_set:
        print(i)

    rating_sum = 0
    for i in app_data_set:
        rating = i[4]
        rating_sum += rating
    avg_rating = rating_sum / len(app_data_set)
    print(avg_rating)
    return


# excercise4:
# https://app.dataquest.io/m/312/lists-and-for-loops/10/the-average-app-rating
##
###
def exercise_4(filename):
    opened_file = open(filename)
    from csv import reader  # to read the csv file, we import the reader command from csv module
    read_file = reader(opened_file)  # dump the whole csv file to read_file
    merch_data = list(read_file)  # whole file is now being stored in merch_data as list of lists
    # option1:
    total_sale = 0
    for i in merch_data[1:-1]:
        # print(i[5])
        sale = float(i[5])
        total_sale += sale
    avg_sale = total_sale / len(merch_data[1:])
    print('Total Sales', total_sale, 'and Average sale:', avg_sale)

    # option2:
    sale_list = []
    for i in merch_data[1:-1]:
        # print(i[5])
        sale_list.append(float(i[5]))
    avg_sale = sum(sale_list) / len(sale_list)
    print('Total Sales', total_sale, 'and Average sale:', avg_sale)

    opened_file.close()
    return


# excercise5:
# https://app.dataquest.io/m/314/dictionaries-and-frequency-tables/7/counting-with-dictionaries
# learnings in this excercise below:
#       loading unique values of a row to a list and dictionary
#       sorting a dictionary on values in reverse order
#       displaying top 20 values from the sort order
# Output:   955
#           955
#           Top 20 Merchants with most number of stores
#           910000438 58
#           910000385 29
#           910000413 24
#           etc.,
###

def exercise_5(filename):
    opened_file = open(filename)
    from csv import reader  # to read the csv file, we import the reader command from csv module
    read_file = reader(opened_file)  # dump the whole csv file to read_file
    merch_data = list(read_file)  # whole file is now being stored in merch_data as list of lists

    # create a list of unique merchant numbers first
    # and then count the stores in that merchant numbers and create a dict of the list
    # 'merchant number': count of stores

    # trying to extract particular value in list of lists
    # print(item[4] for item in merch_data)
    merch_numbers = []
    store_count = {}
    for merch in merch_data[1:]:
        if merch[4] not in store_count:
            merch_numbers.append(merch[4])      # create list of merchant number unique. This avoids multiple read list
            store_count[merch[4]] = 1           # create dict with unique merchant numbers and value 1
        else:
            store_count[merch[4]] += 1
    print(len(merch_numbers))
    print(len(store_count))

    # print top 20 merchants with more number of stores from the excel file
    import operator
    # Creates a new list of top 20 items after sorting the dictionary
    items = sorted(store_count.items(), key=operator.itemgetter(1), reverse=True)
    print('Top 20 Merchants with most number of stores:')
    for i in items[:20]:
        print(i[0], i[1])

    opened_file.close()
    return


# This basic command line argument parsing code is provided and
# calls any function defined above and keeps growing.
def main():
    if len(sys.argv) != 3:
        print('usage: ./dataquest.py {--ex1 | --ex2 etc.,} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--ex1':
        exercise_1()
    elif option == '--ex2':
        exercise_2(filename)
    elif option == '--ex3':
        exercise_3()
    elif option == '--ex4':
        exercise_4(filename)
    elif option == '--ex5':
        exercise_5(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
