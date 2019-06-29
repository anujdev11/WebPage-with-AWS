import json,ast
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from datetime import datetime


def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    tableName = "receiveData1"
    table = dynamodb.Table(tableName)
    
    tableName1="Registration_D"
    table1=dynamodb.Table(tableName1)
    
    Raspberry_Id=event['Raspberry_Id']
    response = table.get_item(
        Key={
            'Raspberry_Id':Raspberry_Id,
        }
    )
    #item1 = response['Item']
    #item=ast.literal_eval(json.dumps(item1))
    RaspberryId=response['Item']['Raspberry_Id']
    ReceivedData=response['Item']['Received_Data']
    
    
    loginEmail=event['Email']
    
    response = table1.get_item(
        Key={
            "Email":loginEmail,
        }
    )

    User_Name=response['Item']['Name']
    return({
    "isBase64Encoded": True,
    "statusCode": 200,
    "headers": { 'Access-Control-Allow-Origin': '*'},
    "body": {
            "Name":User_Name,
            "Raspberry_Id": RaspberryId,
            "Received_Data": ReceivedData
        }
    })