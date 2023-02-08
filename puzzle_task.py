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
    Function checks lines of the board.

    >>> print(check_lines(read_board('puzzle_doc.txt')))
    True
    """
    list_of_bools = []
    for line in board:
        list_of_nums = [int(i) for i in line if i.isdigit()]
        set_of_nums = set(list_of_nums)
        list_of_bools.append(len(list_of_nums) == len(set_of_nums)\
             and all(1 <= i <= 9 for i in list_of_nums))
    return all(list_of_bools)

def check_columns(board: list) -> bool:
    """
    Function checks columns of the board.

    >>> print(check_columns(read_board('puzzle_doc.txt')))
    False
    """
    columns = [''.join([elem[i] for elem in board]) for i in range(len(board[0]))]
    return check_lines(columns)

def check_blocks_of_colour(board: list) -> bool:
    """
    Function check L-shaped coloured boxes according to the rules.

    >>> print(check_blocks_of_colour(read_board('puzzle_doc.txt')))
    True
    """
    coloured_blocks = [[(i, 4) for i in range(5)] + [(4, i) for i in range(5, 9)],
    [(i, 3) for i in range(1, 6)] + [(5, i) for i in range(4, 8)],
    [(i, 2) for i in range(2, 7)] + [(6, i) for i in range(3, 7)],
    [(i, 1) for i in range(3, 8)] + [(7, i) for i in range(2, 6)],
    [(i, 0) for i in range(4, 9)] + [(8, i) for i in range(1, 5)]]

    check_blocks = [check_lines("".join(board[i][j] for i, j in block))\
                     for block in coloured_blocks]
    return all(check_blocks)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
