import heapq


def list_to_string(_list):
    """
    Convert an unhashable list to a hashable string
    """
    return ",".join([str(element) for element in _list])


def string_to_list(_string):
    """
    Convert a string to a list of integers
    """
    _list = _string.split(",")
    integer_list = [int(element) for element in _list]
    return integer_list


def list_of_incremented_sets(elements):
    """
    Given an array of numbers representing a set of integers,
    return a list of arrays where one of each element has been incremented
    """
    new_elements_array = []
    for index, element in enumerate(elements):
        new_elements = elements[:]
        new_elements[index] = element + 1
        new_elements_array.append(new_elements)
    return new_elements_array


def sum_of_squares(elements):
    """
    Return the sum of the squares of all elements in the array
    """
    squares = [element**2 for element in elements]
    return sum(squares)


def list_is_strictly_increasing(elements):
    """
    Returns True iff a <= b <= c ... <= n for all elements (a, b, c, ... n) in the array
    """
    strictly_increasing = True
    # We can assume here that all elements are non-negative
    previous_element = -1
    for element in elements:
        if element < previous_element:
            return False
        previous_element = element
    return True


def generate_ordered_squares(m, n, initial_elements=None):
    """
    Generate the first m unordered sets of size n (a, b, c, ..., n) ranked by
    the sum of the squares of their elements, in non-decreasing order
    where (a <= b <= c ... <= n)
    initial_elements is the starting array, i.e. all solutions will be (a' >= a, b' >= b, ...)
    """

    heap = []
    result = []
    visited = set()

    # Initial set of integers
    if not initial_elements:
        initial_elements = []
        for i in range(n):
            initial_elements.append(0)

    hashable_list_of_initial_elements = list_to_string(initial_elements)
    heapq.heappush(heap, (0, hashable_list_of_initial_elements))
    visited.add(hashable_list_of_initial_elements)

    while len(result) < m:
        # Pop the smallest element
        current_sum, string_list_of_integers = heapq.heappop(heap)
        list_of_integers = string_to_list(string_list_of_integers)
        result.append(list_of_integers)

        # Generate new candidates
        for next_elements in list_of_incremented_sets(list_of_integers):
            hashable_list_of_new_elements = list_to_string(next_elements)
            # print("new", hashable_list_of_new_elements)
            if (
                list_is_strictly_increasing(next_elements)
                and hashable_list_of_new_elements not in visited
            ):
                # print("not in visited", hashable_list_of_new_elements)
                new_sum = sum_of_squares(next_elements)
                # print("new sum", new_sum)

                heapq.heappush(heap, (new_sum, hashable_list_of_new_elements))
                visited.add(hashable_list_of_new_elements)
                # print("visited", visited)

    return result


# Generate the first 15 4-ples
ordered_solutions = generate_ordered_squares(20, 4, initial_elements=[1, 1, 1, 1])
print(ordered_solutions)
