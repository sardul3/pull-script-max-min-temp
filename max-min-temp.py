import csv

tups_arr = []

def populate_data(filename):	
	with open(filename) as csv_file:
		  csv_reader = csv.reader(csv_file, delimiter=',')
		  line_count = 0
		  for row in csv_reader:
		     temp = row[1]
		     tup_time = str(row[0])
		     tup_data = (tup_time, temp)
		     tups_arr.append(tup_data)
		    	
	
def get_data(start, end):
	f = open("output.txt", "w")
	while(start<=end):	
		temps = []
		times = []

		for val in tups_arr:
			if str(start) in val[0]:
				if val[1] == 'M':
					print("found a missing data @ %s" % (val[0]))
				else:
					temps.append(float(val[1]))
					times.append(val[0])
			
		temp_max = max(temps)
		temp_min = min(temps)
		temp_max_date = times[temps.index(max(temps))]
		temp_min_date = times[temps.index(min(temps))]

		f.write("-----------------------------------------\n")
		f.write("Year --> "+ str(start) +"\n")
		f.write("Max--> "+ str(temp_max) +"\n")
		f.write("Min --> "+ str(temp_min) +"\n")
		f.write("Max_date --> "+ str(temp_max_date) +"\n")
		f.write("Min_date --> "+ str(temp_min_date) +"\n")
		f.write("-----------------------------------------\n")
		start = start + 1

populate_data('Colby_19892018_hrly.csv')
get_data(1989, 2018)
	
	




		
		

