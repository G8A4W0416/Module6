"""
Program inner_functions_assignment.py

Author: Greg Wilhelm

Last date modified: 2/26/2020

The purpose of this program is print the perimeter and area of a rectangle or square of any given side length.

"""


def measurements(a_list):
    def area(area_list):
        list_len = len(area_list)

        if list_len == 1:
            side = area_list[0]
            answer = side * side
        elif list_len == 2:
            side1 = area_list[0]
            side2 = area_list[1]
            answer = side1 * side2
        else:
            print("Invalid number of sizes")
            raise ValueError

        return answer

    def perimeter(perimeter_list):
        list_len = len(perimeter_list)

        if list_len == 1:
            side = perimeter_list[0]
            answer = side * 4
        elif list_len == 2:
            side1 = perimeter_list[0]
            side2 = perimeter_list[1]
            answer = (side1 * 2) + (side2 * 2)
        else:
            print("Invalid number of sizes")
            raise ValueError

        return answer

    return "Perimeter = " + str(perimeter(a_list)) + " Area = " + str(area(a_list))


if __name__ == '__main__':
    pass
