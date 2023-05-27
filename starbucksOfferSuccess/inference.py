def inference(hardcoded_data):
    import boto3
    import json
    # Convert the hardcoded data to a list of values
    input_data = [list(hardcoded_data.values())]
    
    # Create a low-level SageMaker client
    sagemaker_client = boto3.client('sagemaker-runtime')
    
    # Specify the endpoint name
    endpoint_name = 'xgboost-tunned-endpoint'
    
    # Convert the input data to CSV format
    input_data_csv = ','.join([str(val) for val in input_data[0]])
    
    # Make a request to the endpoint
    response = sagemaker_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='text/csv',
        Body=input_data_csv
    )

    # Parse the response
    prediction = response['Body'].read().decode()
    prediction = json.loads(prediction)
    
    return prediction 