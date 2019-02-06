#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 18:10:35 2019

@author: madeline
"""

import os
import csv
import pandas as pd
import itertools as it
import datetime
import operator

monthly_sales_dataframe = pd.read_csv('/Users/madeline/Desktop/SPRING_2019/OPIM_243/sales-reporting-exercise/data/sales-201710.csv')
attributes = monthly_sales_dataframe.columns.tolist()
monthly_sales_dataframe['date'] = monthly_sales_dataframe['date'].to_datetime()

print('SALES REPORT (', )
print('TOTAL SALES : $', str('%0.2f'%monthly_sales_dataframe['sales price'].sum()))

products = monthly_sales_dataframe['product'].unique().tolist()

product_subtotals = {}

for item in products:
    product_subset = monthly_sales_dataframe[monthly_sales_dataframe['product'] == item]
    product_total = product_subset['sales price'].sum()
    product_subtotals[item] = product_total

sorted_product_subtotals = sorted(product_subtotals.items(), key = operator.itemgetter(1))
product_subtotals = dict(sorted_product_subtotals)

