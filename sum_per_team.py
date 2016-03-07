import sys, operator

teams = {}

for line in sys.stdin:
	parts = line.strip().split(", ")
	team = parts[0]
	diff = parts[1]
	diffs = []
	if team in teams:
		diffs = teams[team]
	diffs.append(float(diff))
	teams[team] = diffs

teams_to_avg_diff = {}

for team, diffs in teams.items():
	teams_to_avg_diff[team] = sum(diffs)/float(len(diffs))

for team, avg_diff in sorted(teams_to_avg_diff.items(), reverse=True, key=operator.itemgetter(1)):
	print "%s, %f" % (team, avg_diff)

#print "\n".join([str(val) for val in teams_to_avg_diff.values()])
