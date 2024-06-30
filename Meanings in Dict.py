dict1 = {'piece': 'portion of an object or material, produced by cutting',
         'patch': 'a piece of cloth or other material usec to mend or strengthen a torn or weak point',
         'area': 'a region or part of a town, a country, or the world',
         'visit': 'go to and see and spend time with someone',
         'with': 'having or possessing',
         'small': 'less than normal'}
keys = list(dict1.keys())
values = list(dict1.values())
lens = [len(x) for x in values]
max_lens = max(lens)
min_lens = min(lens)
max_index = lens.index(max_lens)
min_index = lens.index(min_lens)
print('MAX: ', keys[max_index], values[max_index])
print('MIN: ', keys[min_index], values[min_index])
