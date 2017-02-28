# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:23:51 2016

@author: eardo
"""
import xlrd
import numpy as np

file_location="C:\Users\eardo\Desktop\Sampling log.xlsx"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
sheet.cell_value(0,0)
numrow=sheet.nrows
numcol=sheet.ncols

#for col in range(sheet.ncols):
 #   print sheet.cell_value(1,col)
    
data=[[sheet.cell_value(r,c) for c in range (sheet.ncols)]for r in range (sheet.nrows)]



