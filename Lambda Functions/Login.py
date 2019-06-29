import json
import boto3
from datetime import datetime



def lambda_handler(event, context):
    # TODO implement
    
    client = boto3.client('iot-data')
    
    dynamodb = boto3.resource('dynamodb')
    tableName = "Registration_D"
    table = dynamodb.Table(tableName)
    loginEmail=event['LEmail']
    loginPassword=event['LPassword']
    response = table.get_item(
        Key={
            'Email':loginEmail,
        }
    )
    item1=response['Item']
    email=item1['Email']
    password=item1['Password']
    raspberry_id=item1['Raspberry_Id']
    
    if(loginEmail==email and loginPassword==password):
        return {
        'statusCode': 200,
        "Raspberry_Id":raspberry_id,
        'body': json.dumps('Hello from Lambda!'),
        'headers':json.dumps( {
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials' : True,
            'Content-Type': 'application/json'
        })
    }
    else:
        return{
            "message":"Failed"
        }
        
