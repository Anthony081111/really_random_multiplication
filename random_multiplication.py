# This program creates a multiplication table...maybe, idk
import numpy


def display_list(randomnum):
    table = []
    table = [[x*y for x in range(1, randomnum)]for y in range(1, randomnum)]
    print(table)
    return table


if __name__ == "__main__":
    a = display_list(4)
    table_array = numpy.array(a)
    print(table_array)
    # print(table_array[2][3])
