from pdfquery import PDFQuery
from boto3 import Session

#requires the aws cli and to configure it

pdf = PDFQuery('sample.pdf')
pdf.load()
text_elements = pdf.pq('LTTextLineHorizontal')
text = [t.text for t in text_elements]

print(text)
text = ' '.join(text)
print(text)

session = Session(profile_name="default")
polly = session.client("polly")

response = polly.start_speech_synthesis_task(
        LanguageCode='en-US',
        OutputFormat='mp3',
        OutputS3BucketName='billingdanielgreenhalgh.com',
        Text=text,
        TextType= 'text',
        VoiceId='Amy'
    )

print(response)
print(f"You can download your file here {response['SynthesisTask']['OutputUri']}")

