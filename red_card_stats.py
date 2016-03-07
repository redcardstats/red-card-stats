import csv, sys, operator

reader = csv.DictReader(open(sys.argv[1]))

total_reds_in_game = {}

reds_per_team = {}

for row in reader:
	home_team = row["HomeTeam"]
	away_team = row["AwayTeam"]
	home_red = row["HR"]
	away_red = row["AR"]

	if home_team in reds_per_team:
		reds_per_team[home_team] += int(home_red)
	else:
		reds_per_team[home_team] = int(home_red)
	if away_team in reds_per_team:
		reds_per_team[away_team] += int(away_red)
	else:
		reds_per_team[away_team] = int(away_red)

	if home_team in total_reds_in_game:
		total_reds_in_game[home_team] += int(home_red) + int(away_red)
	else:
		total_reds_in_game[home_team] = int(home_red) + int(away_red)

	if away_team in total_reds_in_game:
		total_reds_in_game[away_team] += int(home_red) + int(away_red)
	else:
		total_reds_in_game[away_team] = int(home_red) + int(away_red)

#for (key, val) in sorted(total_reds_in_game.items(), reverse=True, key=operator.itemgetter(1)):
#	print "%s, %d" % (key, val)
	
#for (key, val) in reds_per_team.items():
#	print "%s, %d" % (key, val)

avg = sum([item[1] for item in reds_per_team.items()])/float(len(reds_per_team))
#print avg
for (key, val) in reds_per_team.items():
	print "%s, %f" % (key, val - avg)
#print ",".join([str(x) for x in total_reds_in_game.values()])
