def fractional_part(numerator, denominator):
    if denominator == 0:
        result = 0
    elif numerator%denominator == 0:
        result = 0
    else:
        result = ( numerator % denominator) / denominator
    return result