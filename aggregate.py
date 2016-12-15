import os, sys, json
import pandas as pd
import numpy as np

def process_file(file_name):

	file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
	print "File path: %s" % file_path

	data = []

	with open(file_path) as infile:
		for line in infile:
			if not line.startswith("#"):
				file_json = json.loads(line)
				data.append(file_json)

	
	#Create Pandas DataFrame
	df = pd.DataFrame(data, columns=["tid", "timestamp", "amount", "type", "price"])
	df['amount'] = df['amount'].astype('float64')
	df['price'] = df['price'].astype('float64')
	df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', errors='coerce')
	df = df.sort_values(by='timestamp')
	
	#print "Original Data Frame:-----------------------------------------------------------------------"
	#print df

	#Calculating total time span for the data
	total_time_span = df['timestamp'].iat[-1] - df['timestamp'].iat[0]
	print "Total time span for the data: %s" % total_time_span

	#Group By Hour
	group_by = df.groupby(df.timestamp.dt.to_period("H"))
	#group_by = df.groupby(pd.TimeGrouper(freq='30Min'))

	print "GroupBy Data Frame:---------------------------------------------------"
	rslt = group_by.agg({'amount' : np.sum, 'price' : [np.min, np.max, 'first', 'last']})

	for key, item in rslt:
		print rslt.get_group(key), "\n\n"

if __name__ == '__main__':
	file_name = None
	if len(sys.argv) > 1:
		file_name = sys.argv[1]
	process_file(file_name)