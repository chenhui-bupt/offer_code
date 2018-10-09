
hashMap = {'gender':[0, 1], 'age': [1,2,3], 'city': list(range(10))}
features = ['gender', 'age']
def combine(hashMap, features):
    feature = features[0]
    res = [[feature, str(val)] for val in hashMap[feature]]
    for i in range(1, len(features)):
        feature = features[i]
        vals = hashMap[feature]
        tmp = []
        for t in res:
            for val in vals:
                tt = t[::]
                tt.insert(len(t)//2, feature)
                tt.append(str(val))
                tmp.append(tt[::])
        res = tmp[::]
    return ['comb_' + '_'.join(tmp) for tmp in res]


print(combine(hashMap, features))


