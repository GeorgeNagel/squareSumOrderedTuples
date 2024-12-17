import argparse
import heapq
import itertools


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


def unique_permutations(elements):
    """
    Return the ordered list of unique permutations of elements
    """
    list_of_permutations = itertools.permutations(elements)
    unique_permutations = set(list_of_permutations)
    list_of_unique_permutations = list(unique_permutations)
    return sorted(list_of_unique_permutations)


def generate_ordered_squares(
    number_of_lists_to_generate, integer_list_size, initial_elements=None
):
    """
    Generate the first `number_of_lists_to_generate` ordered sets of size n (a, b, c, ..., `integer_list_size`) ranked by
    the sum of the squares of their elements, in non-decreasing order.
    initial_elements is the starting array, i.e. all solutions will be (a' >= a, b' >= b, ...).
    The results list will be exhaustive of all permutations of integers that satisfy the above constraints.
    """

    # Use a min heap to keep track of the list of integers with the smalled sum of squares
    heap = []
    # The list of integer lists
    ordered_lists = []
    # Keep track of which integer lists we have already added to the heap
    visited = set()

    # Initial set of integers
    if not initial_elements:
        initial_elements = []
        for i in range(integer_list_size):
            initial_elements.append(1)

    hashable_list_of_initial_elements = list_to_string(initial_elements)
    heapq.heappush(heap, (0, hashable_list_of_initial_elements))
    visited.add(hashable_list_of_initial_elements)

    while len(ordered_lists) < number_of_lists_to_generate:
        # Pop the smallest element
        current_sum, string_list_of_integers = heapq.heappop(heap)
        list_of_integers = string_to_list(string_list_of_integers)
        # Add all unique permutations of this unordered set to the output list
        permutations_of_integers = unique_permutations(list_of_integers)
        ordered_lists.extend(permutations_of_integers)

        # Generate new candidates
        for next_elements in list_of_incremented_sets(list_of_integers):
            hashable_list_of_new_elements = list_to_string(next_elements)
            if (
                list_is_strictly_increasing(next_elements)
                and hashable_list_of_new_elements not in visited
            ):
                new_sum = sum_of_squares(next_elements)

                heapq.heappush(heap, (new_sum, hashable_list_of_new_elements))
                visited.add(hashable_list_of_new_elements)

    return ordered_lists


ordered_solutions = generate_ordered_squares(20, 3, initial_elements=[1, 1, 1])


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(
        prog="Generate a list of positive integers, ordered by the sum of their squares"
    )
    parser.add_argument("-l", "--length", help="The number of elements in each tuple")
    parser.add_argument("-n", "--number", help="The number of tuples to generate")
    args = parser.parse_args()

    # Normalize arguments
    length = int(args.length or 2)
    number = int(args.number or 100)

    print(
        f"Generating the {number} tuples of size {length} ordered by the sum of squares"
    )

    ordered_list = generate_ordered_squares(number, length)
    print(ordered_list)
