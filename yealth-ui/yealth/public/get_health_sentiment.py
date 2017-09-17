import json

def list_to_dict(elements, id):
    element_tuples = {}
    for element in elements:
        element_tuples[element[id]] = element
    return element_tuples

file1 = 'state_county.json'
with open(file1) as f:
    state_counties = f.read().strip().split('\n')
    print(type(state_counties[0]))
state_counties = [json.loads(state_county) for state_county in state_counties]
state_county_dict = list_to_dict(state_counties, 'state')
'''
with open(file1) as f:
    state_counties = json.load(f)
state_county_dict = list_to_dict(state_counties, 'state')
'''

file2 = 'state_health_score.json'
with open(file2) as f:
    state_health_scores = json.load(f)
state_health_score_dict = list_to_dict(state_health_scores, 'state')

state_set = [key for key in state_county_dict]

US_STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

county_score_dict = {}
for key in state_county_dict:
    state_health_score = state_health_score_dict[key]['state']
    for county in state_county_dict[key]['county']:
        county_score_dict[county] = state_health_score

for county in county_score_dict:
    print('%s' '%f' % (state, state_score_dict[state]));

