#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:41:56 2019

@author: wangdi30
"""
 

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
n_month = 0


annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:​ '))
total_cost = float(input('Enter the cost of your dream house: '))

salary_saved = annual_salary / 12 * portion_saved
down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    interest = current_savings * r / 12
    current_savings = current_savings + interest + salary_saved
    n_month += 1

print('Number of months:', n_month)

