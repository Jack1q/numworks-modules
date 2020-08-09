# Stats module by Jack Donofrio
# Made as a clone of the python statistics library for use on NumWorks calculator
# Not everything is included, just stuff I use a lot on the calculator

class StatisticsError(Exception):
    pass

# Auxiliary functions

def prod(list):
    product = 1
    for num in list:
        product *= num
    return product

def check_stats_error(list):
    if list == None or len(list) == 0:
        raise StatisticsError('Data empty or not list')

# Main Functions

def mean(list):
    check_stats_error(list)
    return round(sum(list) / len(list), 5)

def fmean(list):
    check_stats_error(list)
    return round(sum([float(x) for x in list]) / len(list), 5)

def geometric_mean(list):
    check_stats_error(list)
    return round(pow(prod([float(x) for x in list]), 1 / len(list)), 5)

def harmonic_mean(list):
    check_stats_error(list)
    return round(len(list) / sum([1 / x if x != 0 else 0 for x in list]), 5)

def median(list):
    check_stats_error(list)
    if len(list) % 2 == 0:
        return round((list[len(list) // 2] + list[len(list) // 2 - 1]) / 2, 5)
    else:
        return list[len(list) // 2]

def median_low(list):
    check_stats_error(list)
    if len(list) % 2 == 0:
        return list[len(list) // 2 - 1]
    else:
        return list[len(list) // 2]

def median_high(list):
    check_stats_error(list)
    return list[len(list) // 2]

# def median_grouped(list, interval=1):
#     pass

def mode(list):
    check_stats_error(list)
    list = sorted(list)
    longest_streak = 1
    longest_streak_value = list[0]
    current_streak = 1
    for i in range(len(list) - 1):
        if list[i] == list[i+1]:
            current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
                longest_streak_value = list[i]
        else:
            current_streak = 1
    return longest_streak_value

# returns all modes
def multimode(list):
    check_stats_error(list)
    list = sorted(list)
    modes = []
    current_streak = 1
    longest_streak = 1
    longest_value = list[0]
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
                longest_value = list[i]
        else:
            current_streak = 1
    modes.append(longest_value)
    current_streak = 1
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            current_streak += 1
            if current_streak == longest_streak and list[i] not in modes:
                modes.append(list[i])
        else:
            current_streak = 1
    return modes

# population variance
def pvariance(list):
    check_stats_error(list)
    population_mean = mean(list)
    return sum([pow(x - population_mean, 2) for x in list]) / len(list)

# population stdev
def pstdev(list):
    check_stats_error(list)
    return pow(pvariance(list), 0.5)

# Sample variance
def variance(list):
    check_stats_error(list)
    sample_mean = mean(list)
    return sum([pow(x - sample_mean, 2) for x in list]) / (len(list) - 1)

# Sample stdev
def stdev(list):
    check_stats_error(list)
    return pow(variance(list), 0.5)

# def quantiles(list, n=4):
#     pass