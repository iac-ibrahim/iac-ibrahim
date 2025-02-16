# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nTQpB63inY7LniPR8IVuqOfDyARx1gup
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

term_test_1 = pd.read_csv('/content/drive/MyDrive/pds-course/lectures/practice-project/term-test-1.csv')

term_test_1.head()

# term_test_1[["first_name","last_name"]]= term_test_1["name"].str.split(" ",expand=True)
# term_test_1.head()

term_test_2 = pd.read_csv('/content/drive/MyDrive/pds-course/lectures/practice-project/term-test-2.csv')

term_test_1.info()

# raname marks as marks1
term_test_1 = term_test_1.rename(columns={'marks': 'marks1'})
term_test_2 = term_test_2.rename(columns={'marks': 'marks2'})

# drop name from term_test_2
term_test_2 = term_test_2.drop(columns=['name'])

term_test_1.head()

term_test_2.head()

# merge 2 df
joined_result = pd.merge(term_test_1, term_test_2, on='reg_no', how='outer')

joined_result.tail()

# create another column final_marks as max(marks1, marks2)
joined_result['final_marks'] = joined_result[['marks1', 'marks2']].max(axis=1)

joined_result.head()

final_result = joined_result

final_result['name'] = final_result['name'].str.upper()

final_result.head()

