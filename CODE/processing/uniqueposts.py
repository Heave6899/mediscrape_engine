import json
files = ['outfile0.json','outfile1.json','outfile2.json','outfile3.json','outfile4.json']
count = 0
for i in files:
    with open(i,'r') as f:
        data = json.load(f)
        dict_ = {}
        for j in data:
            if j['post_url'] not in dict_:
                dict_[j['post_url']] = 0
                with open(i+'_output.json','a+') as m:
                    m.write(json.dumps(j) + ',\n')
        with open(i+'_output.txt','w+') as g:
            for k in dict_.keys():
                g.write(k + '\n')
        count += len(dict_)
print(count)