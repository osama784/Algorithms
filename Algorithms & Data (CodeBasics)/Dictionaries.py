import pandas as pd

emp_details = {'Employee': {'Dave': {'ID': '001', 'Salary': '2000', 'Designation': 'TeamLead'},
                            'Ava': {'ID': '002', 'Salary': '1000', 'Designation': 'Associate'}}}

df = pd.DataFrame(emp_details['Employee'])
print(df)

my_dict = {'Div': '001', 'Ava': '002', 'Jon': '003'}
my_dict.pop('Ava')
print(my_dict)
my_dict.popitem()
print(my_dict)
del my_dict['Div']
print(my_dict)