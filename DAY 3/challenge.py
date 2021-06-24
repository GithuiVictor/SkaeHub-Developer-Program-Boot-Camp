import numpy as np

#Get yesterdays date
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print('The date yesterday was: ', yesterday)

print('\n=================================')

#Get today's date
today = np.datetime64('today', 'D')
print('\nThe date today is: ', today)

print('\n=================================')

#Get tomorrows date
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print('\nTomorrows date is: ', tomorrow)