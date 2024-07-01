#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            ops_count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return ops_count

test_0_minoperations.txt
'''
Run the command below to execute these test cases.
python3 -m doctest -v test_0_minoperations.txt

Operations path format:
Character in file: H
operations: copy all (bit 1) or paste (bit 0),
    e.g.; copy all and paste -> 11
    e.g.; paste only -> 01

>>> minOperations = __import__('0-minoperations').minOperations
>>> minOperations(0)
0
>>> minOperations(-1)
0
>>> minOperations(1.4)
0
>>> minOperations('1')
0

# H
>>> minOperations(1)
0

# H-(11)->HH
>>> minOperations(2)
2

# H-(11)->HH-(11)->HHHH
# H-(11)->HH-(01)->HHH-(01)->HHHH
>>> minOperations(4)
4

# H-(11)->HH-(01)->HHH-(01)->HHHH-(01)->HHHHH
>>> minOperations(5)
5

# H-(11)->HH-(01)->HHH-(01)->HHHH-(01)->HHHHH-(01)->HHHHHH-(01)->HHHHHHH
>>> minOperations(7)
7

# H-(11)->HH-(01)->HHH-(01)->HHHH-(01)->HHHHH-(01)->HHHHHH-(01)->HHHHHHH-(01)->HHHHHHHH-(01)->HHHHHHHHH-(01)->HHHHHHHHHH-(01)->HHHHHHHHHHH
>>> minOperations(11)
11

# H-(11)->HH-(01)->HHH-(11)->HHHHHH-(01)->HHHHHHHHH
>>> minOperations(9)
6

# H-(11)->HH-(01)->HHH-(11)->HHHHHH-(11)->HHHHHHHHHHHH
>>> minOperations(12)
7

# H-(11)->HH-(01)->HHH-(11)->HHHHHH-(01)->HHHHHHHHH
>>> minOperations(15)
8

'''
