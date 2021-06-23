import statistics

statistic_mode = [54,24,36.09,55.37,92]

print('MD\t', statistics.median(statistic_mode))
print('mean\t', statistics.fmean(statistic_mode))
print('Geometry\t', statistics.geometric_mean(statistic_mode))
print('Med\t', statistics.median_low(statistic_mode))
print('medH\t', statistics.median_high(statistic_mode))
print('mode\t', statistics.mode(statistic_mode))
print('Median\t', statistics.median(statistic_mode))