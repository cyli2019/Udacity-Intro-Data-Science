__author__ == 'Unifireseeker'

import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    df = pandas.read_csv(filename)
    avg_R = df['avg'][df['handedness']=='R']
    avg_L = df['avg'][df['handedness']=='L']
    a = numpy.array(avg_L)
    b = numpy.array(avg_R)
    
    result = tuple(scipy.stats.ttest_ind(a,b, equal_var=False))
    
    if result[1] < 0.05: 
        return (False, result)
    else:
        return (True, result)
        
 filename = './baseball_stats.csv'
 compare_averages(filename)
