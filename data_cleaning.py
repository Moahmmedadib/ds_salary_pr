# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

df = df[df['Salary Estimate'] != '-1']

minus_kd = df['Salary Estimate'].apply(lambda x: x.replace('K','').replace('$',''))

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary',''))

df['min_salary'] = min_hr.apply(lambda x: x.split('-')[0])
