import json

healthy_id = ['3BCsAgo_1i4xMuTyLKMLRQ', 'XMMLRvV4IMxIGyc4H37LxA', 'VLDFjeqpUgWhnVuB_8GuEg', 'zRqi6L1u-YmmVAHjeUbGMQ', 'p5rpYtxS5xPQjt3MXYVEwA', 'JIETwXSEGIHMNyxZVEnNKQ']

file_business = 'dataset/business.json'
with open(file_business) as f:
    businesses = f.read().strip().split('\n')
businesses = [json.loads(business) for business in businesses]

healthy_businesses = [business for business in businesses if business['business_id'] in healthy_id]
for healthy_business in healthy_businesses:
    print(('id: %r, name:  %r, stars: %r, city: %r, state: %r, postal_code: %r, longitude: %r, latitude: %r') % (healthy_business['business_id'], healthy_business['name'], healthy_business['stars'], healthy_business['city'], healthy_business['state'], healthy_business['postal_code'], healthy_business['longitude'], healthy_business['latitude']))
