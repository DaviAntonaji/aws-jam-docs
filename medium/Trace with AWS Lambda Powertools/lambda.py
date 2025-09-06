import os
import boto3
from boto3.dynamodb.types import TypeDeserializer

# Powertools (v3 para Python 3.13) + X-Ray
from aws_lambda_powertools import Tracer
from aws_xray_sdk.core import patch_all

# Habilita subsegments automáticos para boto3/requests/etc (DynamoDB incluso)
patch_all()

# service name vem da env var POWERTOOLS_SERVICE_NAME=jam
tracer = Tracer()

table_name = os.environ["TABLE_NAME"]
client = boto3.client("dynamodb")
deserializer = TypeDeserializer()

@tracer.capture_method
def get_user(user_id: str):
    # Este método aparecerá como subsegmento; além disso, o boto3 criará
    # automaticamente o subsegmento AWS::DynamoDB::GetItem
    response = client.get_item(
        TableName=table_name,
        Key={"id": {"S": user_id}},
        ConsistentRead=True,
    )
    return response["Item"]

@tracer.capture_method
def deserialise(item: dict) -> dict:
    # Também como subsegmento, útil para evidência do código
    return {k: deserializer.deserialize(v) for k, v in item.items()}

@tracer.capture_lambda_handler
def handler(event, context):
    # aceita userId do evento; default mantém seu "jammer"
    user_id = (event or {}).get("userId", "jammer")

    # Subsegmento explícito do seu código para ficar visível no trace
    with tracer.provider.in_subsegment("GetUserById"):
        item = get_user(user_id)
        user = deserialise(item)

    # Pode retornar JSON direto; se preferir padrão API Gateway, envolva em statusCode/body
    return user
    # return {"statusCode": 200, "body": user}
