# https://www.educative.io/blog/crack-amazon-coding-interview-questions#prepare 
# sum the array provided should be (in example) 36
# sum of values 1 to n, missing value is missing from the sum of 1 to n
# TODO: find highest value, compute 1 to n, return desired sum - actual sum
def find_missing(given_array):
    desired_sum = 0
    highest_value = max(given_array) + 1  # determining the highest value in the array provided
    for i in range(1,highest_value):  # create a range from 1 to highest value -looping through array and calculating the desired sum without missing input (O(n))
        desired_sum += i

    actual_sum = sum(given_array)  # calculating the sum of the array with missing input
    missing_value = desired_sum - actual_sum  # finding the missing value
    return missing_value
  
given_array = [3, 7, 1, 8, 6, 9, 2, 4]

result = find_missing(given_array)
print result
