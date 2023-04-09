import json

files = ['outfile0.json_output.json','outfile1.json_output.json','outfile2.json_output.json','outfile3.json_output.json','outfile4.json_output.json']
for file in files:
    with open(file,'r') as f:
        with open('merged_data.json','a+') as g:
            data = f.readlines()
            print(data[0])
            g.writelines(data) 