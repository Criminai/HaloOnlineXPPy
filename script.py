import math

# All avaliable ranks
rank = ['Recruit', 'Apprentice', 'Apprentice (Grade 2)', 'Private', 'Private (Grade 2)', 'Corpral', 'Copral (Grade 2)', 'Sergeant', 'Sergeant (Grade 2)', 'Sergeant (Grade 3)', 'Gunnery Sergeant', 'Gunnery Sergeant (Grade 2)', 'Gunnery Sergeant (Grade 3)', 'Gunnery Sergeant (Grade 4)', 'Lieutenant', 'Lieutentant (Grade 2)', 'Lieutenant (Grade 3)', 'Lieutenant (Grade 4)', 'Captain', 'Captain (Grade 2)', 'Captain (Grade 3)', 'Captain (Grade 4)', 'Major', 'Major (Grade 2)', 'Major (Grade 3)', 'Major (Grade 4)', 'Commander', 'Commander (Grade 2)', 'Commander (Grade 3)', 'Commander (Grade 4)', 'Colonel', 'Colonel (Grade 2)', 'Colonel (Grade 3)', 'Colonel (Grade 4)', 'Brigadier', 'Brigadier (Grade 2)', 'Brigadier (Grade 3)', 'Brigadier (Grade 4)', 'General', 'General (Grade 2)', 'General (Grade 3)', 'General (Grade 4) 5 Star General']

rankID = 0 
xp = 0

while rankID < 20:
    xp += 1
    if math.floor((math.sqrt(12100+440*max(xp-280,0))-110)/220) > rankID:
        spaces = 27 - len(rank[rankID])
        print(rank[rankID]+": "+" "*spaces+str(xp))
        rankID +=1
