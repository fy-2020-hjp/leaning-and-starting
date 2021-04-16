# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:34:29 2021

@author: JD
"""
import calendar
print(calendar.isleap(2020))
import datetime
Today=datetime.date.today()
firstday=datetime.date(Today.year,1,1)
daysDelta=Today-firstday+datetime.timedelta(days=1)
print(daysDelta.min)