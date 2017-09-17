import json

def list_to_dict(elements, id):
    element_dict = {}
    for element in elements:
        element_dict[element[id]] = element
    return element_dict

file1 = 'state_county.json'
with open(file1) as f:
    state_counties = f.read().strip().split('\n')
state_counties = [json.loads(state_county) for state_county in state_counties]
state_county_dict = list_to_dict(state_counties, 'state')

file2 = 'state_health_score.json'
with open(file2) as f:
    state_health_scores = json.load(f)
state_health_score_dict = list_to_dict(state_health_scores, 'state')

state_set = [key for key in state_county_dict]

county_score_dict = {}
for key in state_health_score_dict:
    state_health_score = state_health_score_dict[key]['health_score']
    for county in state_county_dict[key]['counties']:
        county_score_dict[county] = state_health_score

for county in county_score_dict:
    print('%s %f' % (county, county_score_dict[county]))
