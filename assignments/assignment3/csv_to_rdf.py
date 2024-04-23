import pandas as pd

assigned_hours = pd.read_csv('path/to/assigned_hours.csv')
reported_hours = pd.read_csv('path/to/reported_hours.csv')

teacher_hours = assigned_hours.merge(reported_hours, on=['Course code', 'Teacher Id'], how='left')
teacher_hours['hoursStatus'] = ~teacher_hours['Reported hours'].isnull()
teacher_hours.drop('Reported hours', axis=1, inplace=True)