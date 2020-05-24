import json
import aws_s3 as aw3
import transcribe as trans
import app as a
import os
import time

files = aw3.list_files()
print(files)
# retuns a list of redacted file uris
redacted = []
for i in files:
    red_file = trans.transcribe(str(i)[:-4], f'https://axelsolutions.s3-ap-southeast-2.amazonaws.com/{i}', 'axelsolutions')
    redacted.append(red_file)


# Sleep to wait for the files to be ready. 
time.sleep(60)
redacted = ['redacted-test.json', 'redacted-sample1.json']

for i in redacted:
    aw3.download('axelsolutions',i, i)

data = os.listdir(path='data/test_main')
print(data)

for ab in data:
    with open(ab) as f:
        b = json.load(f)
    data = a.get_redacted(b)

    count = 0
    for i in data:
        count +=1
    
    t = a.trim_audio(data, count)
    print(t)

    a.combine_audio(t, f'test.wav')

    # aw3.upload('axelsolutions', f'data/test_main/{ab}', f'redacted/{ab}')


