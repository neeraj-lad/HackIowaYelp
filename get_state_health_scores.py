import json

def list_to_dict(elements, id):
    element_tuples = {}
    for element in elements:
        element_tuples[element[id]] = element
    return element_tuples

file_business = 'dataset/business.json'
with open(file_business) as f:
    businesses = f.read().strip().split('\n')
businesses = [json.loads(business) for business in businesses]
business_dict = list_to_dict(businesses, 'business_id')

file_business_score = 'dataset/businesses_and_health_scores.json'
with open(file_business_score) as f:
    business_scores = json.load(f)
business_score_dict = list_to_dict(business_scores, 'business_id')

business_id_set = [key for key in business_score_dict]

US_STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

state_score_dict = {}
for key in business_score_dict:
    state = business_dict[key]['state']
    if state in US_STATES:
        if state not in state_score_dict:
            state_score_dict[state] = 0.0
        state_score_dict[state] += business_score_dict[key]['score']
min_val = min(state_score_dict.itervalues())
for state in state_score_dict:
    state_score_dict[state] = state_score_dict[state] + (-1) * min_val

for state in state_score_dict:
    print('%s %f' % (state, state_score_dict[state]))
