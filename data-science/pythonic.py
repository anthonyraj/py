import collections
medal =  collections.namedtuple('medal',['year','name','team','event'])
medals = [medal(*line.strip('\n').split('\t')) for line in open('goldmedals.txt','r')]
print(medals)

#teams_list = [medal.team for medal in medals]
#print(teams_list) # Toomany, now the collections.Counter makes sense

#teams = collections.Counter([medal.team for medal in medals])

winners_by_country = {}

for medal in medals:
    if medal.team not in winners_by_country:
        winners_by_country[medal.team] = set({medal.name})
    else:
        winners_by_country[medal.team].add(medal.name)

def findmedals(**kwargs):
    return [medal for medal in medals 
           if all(getattr(medal,key)==value for key,value in kwargs.items())]

#print(winners_by_country)
#findmedals(team='USA')
