# TODO: loop through array and find two integers (if exist) that sum to value given
# vist every element in array, subtract value and see if corresponding value is available
# if list is exhausted, return no such pair exists
def find_sum_of_two(given_array, val):
    found_values = set()
    for i in given_array:
        if val - i in found_values:
            return True

        found_values.add(i)
    return False

inputted_array = [5, 7, 1, 2, 8, 4, 3]
target_sum = 10

print find_sum_of_two(inputted_array, target_sum)
