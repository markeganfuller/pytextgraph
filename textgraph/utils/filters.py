'''
Useful Filters
'''


def lower_limit(input_list, limit):
    '''
    Remove values below or equal to limit
    '''
    return [i for i in input_list if i > limit]


def upper_limit(input_list, limit):
    '''
    Remove values above limit
    '''
    return [i for i in input_list if i < limit]


def limits(input_list, lower, upper):
    '''
    Filter list to only contain values between lower
    and upper values
    '''
    input_list = lower_limit(input_list, lower)
    input_list = upper_limit(input_list, upper)
    return input_list
