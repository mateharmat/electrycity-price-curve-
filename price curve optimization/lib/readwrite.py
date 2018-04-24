'''
Created on 2017. dec. 8.

@author: User
'''
import xlwings as xw
import pandas as pd
import numpy as np
import math
from lib.eh import Egyutthatok as eh

def data_reader(wb):
   
    result_df = wb.sheets(u'Sheet1').range('A1').expand().options(pd.DataFrame).value
    result_df.columns = result_df.columns.astype('unicode')
    result_df.columns = [column.encode('utf-8') for column in result_df.columns]
  
    result_df.index = [i.strftime("%y-%m-%d") for i in result_df.index]
    result_df.index = result_df.index.values.astype('unicode')
    result_df.index = [i.encode('utf-8') for i in result_df.index]
    return result_df

def result_writer(wb, eh):  
    wb.sheets(u'Sheet1').range('D2').value = eh.lnPricetransp  
    wb.sheets(u'Sheet1').range('K3').value =eh.value
    wb.sheets(u'Sheet1').range('G3').value = eh.simulated
    wb.sheets(u'Sheet1').range('G14').value = eh.deopteha
    wb.sheets(u'Sheet1').range('G15').value = eh.basopteha
    wb.sheets(u'Sheet1').range('K14').value = eh.deoptfv
    wb.sheets(u'Sheet1').range('K15').value = eh.basoptfv
    wb.sheets(u'Sheet1').range('E2').value = eh.seasonexcel
    wb.sheets(u'Sheet1').range('F2').value = eh.Swrite
    wb.sheets(u'Sheet1').range('M2').value=eh.S_kalresult
    wb.sheets(u'Sheet1').range('N2').value=eh.Pt_kalresult    
   