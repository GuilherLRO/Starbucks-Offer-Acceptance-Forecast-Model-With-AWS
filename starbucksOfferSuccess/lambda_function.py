import json
import boto3
from inference import inference

def lambda_handler(event, context):
    
    prediction = inference(event)

    if prediction > 0.5:
        answer = 'The offer will likely be completed. (probability: {:.2f}%)'.format(prediction*100)
    else:
        answer = 'The offer will likely not be completed. (probability: {:.2f}%)'.format(prediction*100)
    
    return {'statusCode': 200,
            'Inference': answer}