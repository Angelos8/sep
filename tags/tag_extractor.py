import json
import collections

"""
yes, i know the script isnt the best and i should probably have generalised it
but honestly i couldnt be bothered
"""

f_enterprise = open('enterprise-attack.json', encoding='utf-8')
f_ics = open('enterprise-attack.json', encoding='utf-8') 
f_mobile = open('enterprise-attack.json', encoding='utf-8')

enterprise_data = json.load(f_enterprise)
ics_data = json.load(f_ics)
mobile_data = json.load(f_mobile)

files = {
    'enterprise-tags': enterprise_data,
    'ics-tags': ics_data,
    'mobile-tags': mobile_data
}

for file, dataset in files.items():
    tags = {
        object['external_references'][0]['external_id']: {
            'name': object['name'],
            'description': object['description'] if 'description' in object else ''
        } for object in dataset['objects'] if object['type'] == 'attack-pattern'
    }
    
    tags = collections.OrderedDict(sorted(tags.items()))

    with open(f'{file}.json', 'w') as fp:
        json.dump(tags, fp, indent=4)
        fp.close()

f_enterprise.close()
f_ics.close()
f_mobile.close()
