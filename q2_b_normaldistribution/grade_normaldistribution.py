#!/usr/bin/env python
# coding: utf-8

# In[1]:


arr = [47, 63, 71, 39, 47, 49, 43, 37, 81, 69, 38, 13, 29, 61, 49, 53, 57, 23, 58, 17, 73, 33, 29]

def mean(data):
    """return arithmetic mean of data"""
    n = len(data)
    if n < 1:
        raise ValueError('invalid input one data point needed')
    return sum(data)/n


def stddev(data):
    def _myss(data):
        c = mean(data)
        ss = sum((x-c)**2 for x in data)
        return ss
    """return standard deviation"""
    n = len(data)
    if n < 2:
        raise ValueError('invalid input: require atleast two data values')
    myss = _myss(data)
    value = myss/(n-1)
    return value**0.5


# In[2]:


def calculate_grades(data):
    _mean = float(mean(data))
    _stddev = float(stddev(data)/3)
    
    def assign_letter_grade(score): 
        if score >= (_mean-_stddev) and score < _mean: return "B-"
        elif score >= (_mean) and score < (_mean+_stddev): return "B"
        elif score >= (_mean+_stddev) and score < (_mean+(2*_stddev)): return "B+"
        elif score >= (_mean+(2*_stddev)) and score < (_mean+(3*_stddev)): return "A-"
        elif score >= (_mean+(3*_stddev)) and score < (_mean+(4*_stddev)): return "A"
        elif score >= (_mean+(4*_stddev)): return "A+"
        elif score >= (_mean-(2*_stddev)) and score < (_mean-_stddev): return "C+"
        elif score >= (_mean-(3*_stddev)) and score < (_mean-(2*_stddev)): return "C"
        elif score >= (_mean-(4*_stddev)) and score < (_mean-(3*_stddev)): return "C-"
        elif score >= (_mean-(5*_stddev)) and score < (_mean-(4*_stddev)): return "D+"
        elif score >= (_mean-(6*_stddev)) and score < (_mean-(5*_stddev)): return "D"
        elif score >= (_mean-(7*_stddev)) and score < (_mean-(6*_stddev)): return "D-"
        else : return "F"    
    for grade in data:
        print(grade, assign_letter_grade(grade))                


# In[3]:


calculate_grades(arr)


# In[ ]:





# In[ ]:




