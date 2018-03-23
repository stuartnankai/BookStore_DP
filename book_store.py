# return the total money, should be DP algorithm--Jian
def calculate_total(books):
    if len(books) == 0:
        return 0
    temp_book_list = [1, 2, 3, 4, 5]
    # the number of books for book ID 1,2,3,4,5
    bookList = [books.count(x) for x in temp_book_list]

    y1, y2, y3, y4, y5 = bookList[0], bookList[1], bookList[2], bookList[3], bookList[4]

    total_value = buy_book_question(y1, y2, y3, y4, y5)

    return int(total_value)


def buy_book_question(y1, y2, y3, y4, y5):
    bookList = []
    bookList.append(y1)
    bookList.append(y2)
    bookList.append(y3)
    bookList.append(y4)
    bookList.append(y5)
    bookList.sort(reverse=True)  # [2,1,0,3,0] to [3,2,1,0,0] which means we can use 3 different books discount

    y1, y2, y3, y4, y5 = bookList[0], bookList[1], bookList[2], bookList[3], bookList[4]

    if len(bookList) == 5:
        if y1 == y2 == y3 == y4 == y5 == 0:  # no book any more
            return 0
        else:
            if y5 >= 1:  # have 5 different books
                x1 = 5 * 800 * 0.75 + buy_book_question(y1 - 1, y2 - 1, y3 - 1, y4 - 1, y5 - 1)
            else:
                x1 = 10 ** 10  # punishment
            if y4 >= 1:  # have 4 different books
                x2 = 4 * 800 * 0.8 + buy_book_question(y1 - 1, y2 - 1, y3 - 1, y4 - 1, y5)
            else:
                x2 = 10 ** 10
            if y3 >= 1:
                x3 = 3 * 800 * 0.9 + buy_book_question(y1 - 1, y2 - 1, y3 - 1, y4, y5)
            else:
                x3 = 10 ** 10
            if y2 >= 1:
                x4 = 2 * 800 * 0.95 + buy_book_question(y1 - 1, y2 - 1, y3, y4, y5)
            else:
                x4 = 10 ** 10
            if y1 >= 1:
                x5 = 800 + buy_book_question(y1 - 1, y2, y3, y4, y5)
            else:
                x5 = 10 ** 10

            minVal = min(x1, x2, x3, x4, x5) # get the best solution
            return minVal
    else:
        return 0

# test_list = [1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]
# # test_list = [1, 1, 2, 2, 3, 4]
# # test_list = [1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]
# print("This is : ", calculate_total(test_list))
