import json
import boto3
from datetime import datetime



def lambda_handler(event, context):
    # TODO implement
    
    client = boto3.client('iot-data')
    
    dynamodb = boto3.resource('dynamodb')
    tableName = "Registration_D"
    table = dynamodb.Table(tableName)
    
    
    tableName1="Reg_Receive"
    table1 = dynamodb.Table(tableName1)
    
    
    table.put_item(
        Item={
            'Raspberry_Id':event['R_id'],
            'SamplePeriod':event['sample_period'],
            'Name':event['Name'],
            'Email':event['Email'],
            'Password':event['Password'],
            }
        )
    
    table1.put_item(
        Item={
            'Raspberry_Id':event['R_id'],
            'SamplePeriod':event['sample_period'],
            'Email':event['Email'],
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'headers':json.dumps( {
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials' : True,
            'Content-Type': 'application/json'
        })
    }
