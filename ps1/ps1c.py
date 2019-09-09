#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:26:34 2019

@author: wangdi30
"""


semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
n_month = 36
epsilon = 100
n_step = 0


down_payment = total_cost * portion_down_payment


low = 0.0
high = 1.0


x = float(input('Enter your starting annual salary: '))


while True:
    
    if n_step == 0:
        
        portion_saved = 1.0
        current_savings = 0.0
        annual_salary = x
        salary_saved = annual_salary / 12 * portion_saved
        
        for i in range(1, n_month+1):
            interest = current_savings * r / 12
            current_savings = current_savings + interest + salary_saved    
            if i % 6 == 0:
                annual_salary *= 1 + semi_annual_raise
                salary_saved = annual_salary / 12 * portion_saved
        
        if current_savings + epsilon < down_payment:
            print('It is not possible to pay the down payment in three years.')
            break
    
    portion_saved = (high+low)/2
    current_savings = 0.0
    annual_salary = x
    salary_saved = annual_salary / 12 * portion_saved
    
    for i in range(1, n_month+1):
        interest = current_savings * r / 12
        current_savings = current_savings + interest + salary_saved    
        if i % 6 == 0:
            annual_salary *= 1 + semi_annual_raise
            salary_saved = annual_salary / 12 * portion_saved
    
    if abs(current_savings - down_payment) > epsilon:
        n_step += 1
        if current_savings > down_payment:
            high = portion_saved
        else:
            low = portion_saved
        
    else:
        print('Best saving rate: ', round(portion_saved, 4))
        print('Steps in bisection search: ', n_step)
        break





