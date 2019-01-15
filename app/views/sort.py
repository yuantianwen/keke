#!/usr/bin/python
#coding=utf-8
import re
import collections;

from  multi_data_storage  import xlsx_save,xlsx_open,xlsx_write_row_data


new_segment_flag=0


newfile=open("sort.txt","w")
result= collections.OrderedDict()
idx = "";
theme=""
subtheme=""
segment = ""
line_type=""
def write_line(str):
	global segment
	global idx
	global line_type

	if str.startswith('旅游英语口语就该这么说'):
		new_segment_flag = 1;
		#newfile.write(segment)
		idx = "";
		theme=""
		subtheme=""
		s = str.split(' ')
		#print(s)
		searchobj = re.search('.*第(\d+)期.*',s[0])
		if searchobj:
			idx = searchobj.group(1)
		if len(s) <=2:
			theme = s[1]
		else:
			theme = s[1]
			subtheme=s[2]
		xlsx_write_row_data([idx,theme,subtheme],'title')
		line_type="zh"
		#segment="[第%s期,%s,%s]"%(idx,theme,subtheme)		
	else:
		new_segment_flag = 0;
		xlsx_write_row_data([str],line_type)
		if line_type=='zh':
			line_type='en'
		elif line_type=='en':
			line_type="zh"

		#segment = segment + str;
	#if idx !="" :
	#	result[idx]=segment 

	#print(str)

def main():

	with open('keke.txt','r',encoding="utf-8") as f:
		xlsx_open()
		for line in f.readlines():
			write_line(line)
		xlsx_save()


	
	'''for i range(1,281):
				xlsx_write_row_data(exp())
				xlsx_write_row_data([""])
				xlsx_write_row_data(["xxx3","xx3"])
				xlsx_save()'''



	#sorted_key_list = sorted(result,key=lambda x:result[x])
	#sorted_dict = dict(lambda x:{x:result[x]}, sorted_key_list)
	#print(sorted_dict)
	#for k,v in sorted_dict.items():
	#	print(k,v)

if __name__ == '__main__':
	main()