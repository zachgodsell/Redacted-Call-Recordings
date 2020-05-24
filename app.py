import json
from pydub import AudioSegment

# with open('data/call1.json') as f:
#         cool = json.load(f)

# Returns a list of redacted timestamps
def get_redacted(data):
    
    calls = data['results']['items']
    times = []
    cnt = 1

    for i in calls:
        if i['type'] != 'punctuation':
            dic = {'item': str(cnt), 'content':i['alternatives'][0]['content'], 
            'times': [{'start': i['start_time'], 'end':i['end_time']}]}
            cnt+=1
            times.append(dic)

    return times
        



# Change the range to the nmber of count above, this should prevent errors
def trim_audio(data, count):
    files = []
    for i in range(0,count):
        try:
            time = data[i]['times'][0]
            start = float(time['start']) *1000 
            end = float(time['end']) * 1000
            dif = (float(end) - float(start)) * 1000

            if'[PII]' in time[i]['content']  :
                sound = AudioSegment.from_wav('data/silent.wav')

                # len() and slicing are in milliseconds
                trimmed = sound[start:end]


                # writing mp3 files is a one liner
                
                trimmed.export(f'data/temp/{i}-silent.wav', format="wav")
                files.append(f'data/temp/{i}-silent.wav')
            if '[PII]' not in time[i]['content']:
                sound = AudioSegment.from_wav('data/sample1.wav')

                
                trimmed = sound[start:end]


                # writing mp3 files is a one liner
                
                trimmed.export(f'data/temp/{i}-sample1.wav', format="wav")
                files.append(f'data/temp/{i}-sample1.wav')
        except Exception as e:
            print(e)
            break

    return(files)




def combine_audio(files, output_name):

    combined = AudioSegment.empty()
    for song in files:
        combined += AudioSegment.from_wav(song)

    combined.export(f"data/test_main/{output_name}", format="wav")
    print(f'Audio snippets were successfully combined')


        