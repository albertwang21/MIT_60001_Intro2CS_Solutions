#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:13:53 2019

@author: wangdi30
"""


portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
n_month = 0


annual_salary = float(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:​ '))
total_cost = float(input('Enter the cost of your dream house: '))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal:​ '))

salary_saved = annual_salary / 12 * portion_saved
down_payment = total_cost * portion_down_payment


while current_savings < down_payment:
    interest = current_savings * r / 12
    current_savings = current_savings + interest + salary_saved
    n_month += 1
    
    if n_month % 6 == 0:
        annual_salary *= 1 + semi_annual_raise
        salary_saved = annual_salary / 12 * portion_saved


print('Number of months:', n_month)

