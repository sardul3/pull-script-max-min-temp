import csv

data = []
temps = []
times = []

def populate_data(filename):	
	f = open("output_daily.txt", "w")
	with open(filename) as csv_file:
		  csv_reader = csv.reader(csv_file, delimiter=',')
		  for row in csv_reader:
		     data.append(row)
		     if row[1] == 'M' or row[0].isalpha(): 
					print('ignoring an entry')
		     else:		  
					temps.append(float(row[1]))
					times.append(row[0])
		  i = 0
		  while(i<len(temps)):
		  	temp_data = temps[3:][i:i+24]
			i = i + 24
			if len(temp_data)>0:
				max_ind = temps.index(max(temp_data))
				min_ind = temps.index(min(temp_data))

				f.write("-----------------------------------------\n")
				f.write("Day --> "+ str(times[max_ind].split(" ")[0]) +"\n")
				f.write("Max--> "+ str(max(temp_data)) +"\n")
				f.write("Min --> "+ str(min(temp_data))  +"\n")
				f.write("Max_date --> "+ str(times[max_ind]) +"\n")
				f.write("Min_date --> "+ str(times[min_ind]) +"\n")
				f.write("-----------------------------------------\n")

populate_data('Colby_19892018_hrly.csv')


	
	




		
		

