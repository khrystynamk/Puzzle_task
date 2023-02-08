"""File for puzzle task"""
def validate_board(board: list) -> bool:
    """
    Function checks board according to the rules.

    >>> print(validate_board(read_board('puzzle_doc.txt')))
    False
    """
    return check_lines(board) and check_columns(board) and check_blocks_of_colour(board)

def read_board(path: str) -> list:
    """
    Function read board from file.

    >>> print(read_board('puzzle_doc.txt'))
    ['**** ****', '***1 ****', '**  3****',\
 '* 4 1****', '9 5', '6  83  *', '3   1  **', '8  2***', '2  ****']
    """
    with open(path, 'r', encoding = 'utf-8') as file:
        content = [line.replace(' ', '.').replace('\n', '') for line in file.readlines()]
    return content

def check_lines(board: list) -> bool:
    """
    Function check lines of board.

    >>> print(check_lines(read_board('puzzle_doc.txt')))
    False
    """
    list_of_nums = [int(i) for elem in board for i in elem if i.isdigit()]
    set_of_nums = set(list_of_nums)
    if list_of_nums == set_of_nums and all(1 <= i <= 9 for i in list_of_nums):
        return True
    return False

def check_columns(board: list) -> bool:
    result =[]
    for i in board:
        for j in board:
            if board.index(i) != board.index(j):
                for elem in i:
                    for num in j:
                        if i.index(elem) == j.index(num) and elem.isdigit() and num.isdigit():
                            if int(elem) == int(num):
                                result.append('False')
                            else:
                                result.append('True')
    if 'False' in result:
        return False
    else:
        return True
        
def check_blocks_of_colour(board: list) -> bool:
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())