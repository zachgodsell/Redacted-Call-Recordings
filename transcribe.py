from __future__ import print_function
import time
import boto3

# Returns the transcription URI from a transcriptionn job
def transcribe(job_name, job_uri, output_bucket_name):

    transcribe = boto3.client('transcribe')

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='wav',
        LanguageCode='en-US',
        OutputBucketName=output_bucket_name,
        ContentRedaction={
        'RedactionType': 'PII',
        'RedactionOutput': 'redacted'})

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        
        print("Not ready yet...")
        
        time.sleep(5)
    
    return status['TranscriptionJob']['Transcript']['RedactedTranscriptFileUri']



