#!/usr/bin/python
#coding=utf-8
import xlwings as xw;
import os

g_row=1
xlsx_filename="旅游口语.xlsx"
workbook = None

def xlsx_open():
	global app
	global workbook;
	#xw.App(visible=False,add_book=False)
	if not os.path.exists(xlsx_filename):
		workbook = xw.Book()
	else:
		workbook = xw.Book(xlsx_filename)	


def xlsx_write_row_data(col_value_list,type):
	global workbook
	global g_row	
	
	if type=='title':
		data_range = workbook.sheets("sheet1").range((g_row,1),(g_row,len(col_value_list)))
		g_row +=1
	if type=='zh':
		data_range = workbook.sheets("sheet1").range((g_row,4),(g_row,4+len(col_value_list)))
	elif type=='en':
		data_range = workbook.sheets("sheet1").range((g_row,5),(g_row,5+len(col_value_list)))
		g_row +=1
	else:
		data_range = workbook.sheets("sheet1").range((g_row,1),(g_row,len(col_value_list)))
		g_row +=1
	data_range.value = col_value_list

def xlsx_save():
	global workbook
	if not os.path.exists(xlsx_filename):
		workbook.save(xlsx_filename)
	else:
		workbook.save()
	workbook.app.kill()
	#app.quit()

if __name__ == '__main__':
	xlsx_open()
	xlsx_write_row_data(["xxx","xx2"])
	xlsx_write_row_data([""])
	xlsx_write_row_data(["xxx3","xx3"])
	xlsx_save()


