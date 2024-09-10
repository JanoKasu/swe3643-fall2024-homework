import math
from statistics import stdev


def main():
    sampleValues = [9,6,8,5,7]
    sampleStDev = compute_sample_stdev(sampleValues)
    print('Sample StDev =', sampleStDev)

    populationValues = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]
    popStDev = compute_population_stdev(populationValues)
    print('Population StDev =', popStDev)
    return 0


def compute_mean(values):
    if not values:
        raise ValueError('Values cannot be empty')

    sum = 0
    for value in values:
        sum += value

    return sum / len(values)

def compute_square_of_differences(values, mean):
    if not values:
        raise ValueError('Values cannot be empty')

    squareAccumulator = 0
    for value in values:
        difference = value - mean
        squareOfDifference = difference * difference
        squareAccumulator += squareOfDifference

    return squareAccumulator


def compute_variance(squareOfDifferences, numValues, isPopulation):
    if not isPopulation:
        numValues -= 1

    if numValues < 1:
        raise ValueError('numValues is too low (sample must be >= 1, population must be >= 2')

    return squareOfDifferences / numValues


def compute_stdev(values, isPopulation):
    if not values:
        raise ValueError('Values cannot be empty')

    mean = compute_mean(values)
    squareOfDifferences = compute_square_of_differences(values, mean)
    variance = compute_variance(squareOfDifferences, len(values), isPopulation)

    return math.sqrt(variance)


def compute_sample_stdev(sampleValues):
    return compute_stdev(sampleValues, False)


def compute_population_stdev(populationValues):
    return compute_stdev(populationValues, True)


def interpret_stdev(stDev):
    stDev = round(stDev, 1)

    if stDev > 2.0:
        return "Above Average"
    elif stDev < -2.0:
        return "Below Average"
    elif stDev == 0.0:
        return "Exactly Average"
    else:
        return "Near Average"