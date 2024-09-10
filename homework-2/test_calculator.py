import pytest
import statistics
from calculator import *


@pytest.mark.parametrize('values', [[0, 10, 20, 30]])
def test_Calculator_ComputeMean_ProduceMean(values):
    assert statistics.mean(values) == compute_mean(values)


@pytest.mark.parametrize('values', [[]])
def test_Calculator_ComputeMean_ThrowError(values):
    with pytest.raises(ValueError) as exception:
        compute_mean(values)
    assert str(exception.value) == 'Values cannot be empty'


@pytest.mark.parametrize('values', [[0, 10, 20, 30]])
def test_Calculator_ComputeSquareOfDifferences_ProduceSOD(values):
    mean = statistics.mean(values)
    assert compute_square_of_differences(values, mean) != None


@pytest.mark.parametrize('values', [[]])
def test_Calculator_ComputeSquareOfDifferences_ThrowError(values):
    with pytest.raises(ValueError) as exception:
        mean = 0
        compute_square_of_differences(values, mean)
    assert str(exception.value) == 'Values cannot be empty'


@pytest.mark.parametrize('data, isPopulation', [([97,46,87,54,13,55,6,47,24,26,7], True), ([97,46,87,54,13,55,6,47,24,26,7], False)])
def test_Calculator_ComputeVariance_ProduceVariance(data, isPopulation):
    SquareOfDifferences = compute_square_of_differences(data, statistics.mean(data))
    numValues = len(data)
    # For population variance
    if isPopulation:
        assert statistics.pvariance(data) == compute_variance(SquareOfDifferences, numValues, True)
    # For sample variance
    else:
        assert statistics.variance(data) == compute_variance(SquareOfDifferences, numValues, False)


@pytest.mark.parametrize('data', [[]])
def test_Calculator_ComputeVariance_ThrowError(data):
    with pytest.raises(ValueError) as exception:
        SquareOfDifferences = 500
        numValues = len(data)
        compute_variance(SquareOfDifferences, numValues, True)
    assert str(exception.value) == 'numValues is too low (sample must be >= 1, population must be >= 2'


@pytest.mark.parametrize('values, isPopulation', [([97,46,87,54,13,55,6,47,24,26,7], True), ([97,46,87,54,13,55,6,47,24,26,7], False)])
def test_Calculator_ComputeStandardDeviation_ProduceStandardDeviation(values, isPopulation):
    if isPopulation:
        assert statistics.pstdev(values) == compute_stdev(values, True)
    else:
        assert statistics.stdev(values) == compute_stdev(values, False)


@pytest.mark.parametrize('values', [[]])
def test_Calculator_ComputeStandardDeviation_ThrowError(values):
    with pytest.raises(ValueError) as exception:
        compute_stdev(values, True)
    assert str(exception.value) == 'Values cannot be empty'


def test_Calculator_Main_Main():
    assert main() == 0


@pytest.mark.parametrize('values, expected', [(3, 'Above Average'), (-3, 'Below Average'), (0, 'Exactly Average'), (1.4, 'Near Average'), (-0.8, 'Near Average')])
def test_IntepretStandardDeviation_ProduceInterpretation(values, expected):
    assert interpret_stdev(values) == expected