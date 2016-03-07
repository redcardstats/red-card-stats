import urllib2

BASE_URL = "http://www.football-data.co.uk/mmz4281"
CSV_NAME = "E0.csv"

years = range(1993, 2015)

for year in years:
	year_start = year
	year_end = year + 1
	year_start_string = str(year % 100)
	year_end_string = str((year + 1) % 100)
	if len(year_start_string) == 1:
		year_start_string = "0" + year_start_string
	if len(year_end_string) == 1:
		year_end_string = "0" + year_end_string
	year_string = year_start_string + year_end_string

	year_data = urllib2.urlopen(BASE_URL + "/" + year_string + "/" + CSV_NAME).read()

	with open("premier_league_data_" + year_string + ".csv", "w") as f:
		f.write(year_data)


