# This exercise contains 5 Tasks to practice a powerful feature of Python: comprehensions.
# With these, multiple-line for-loop constructions can be expressed in expressive one-liners.


def multiply_by(x, list1):
    """
    Multiplies each value in list1 by x and returns it as a new list.
    """
    return [x*i for i in list1]  # TODO: replace DONE


def check_division(x, list1):
    """
    Takes a list and returns a list indicating whether or not each element in the original list can be divided by x.
    (e.g check_division(3, [1,2,3]) -> [False, False, True])
    """
    # list_check = []
    # for i in list1:
    #     if (x / i == 1):
    #         list_check.append(True)
    #     else:
    #         list_check.append(False)
    # return list_check
    return [False for i in list1 if (x / i != 1)] + [True for i in list1 if (x / i == 1)]# TODO: replace DONE

def div_less(set1):
    """
    Return a new set only containing numbers that can`t be divided by any other number (except one and itself)
    from the original set.
    """
    # TODO: replace DONE
    return {x for x in range(set1) if (x / x == 1 & x / 1 == x)}



def map_zip(list1, list2):
    """
    It should return a dictionary mapping the 'nth' element in list1 to the 'nth' element in list2.
    Make use of the 'zip()' function in your dictionary comprehension, that can handle lists of different sizes
    automatically.
    """
    return {x for x in zip(list1,list2)}  # TODO: replace DONE


def word_to_length(list1):
    """
    Returns a dictionary mapping all words with at least 3 characters to their number of characters.
    """
    return {map(lambda x : len(x)>3,list1)}  # TODO: replace DONE
