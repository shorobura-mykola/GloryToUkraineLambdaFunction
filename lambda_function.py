import json


def lambda_handler(event, context):
    return {
      'statusCode': 200,
      'body': json.dumps('Glory to Ukraine! Glory to the heroes!')
    }
