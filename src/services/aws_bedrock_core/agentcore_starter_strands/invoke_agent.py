# import boto3
# import json
#
# client = boto3.client('bedrock-agentcore', region_name='eu-central-1')
# payload = json.dumps({
#     "input": {"prompt": "Explain machine learning in simple terms"}
# })
#
# response = client.invoke_agent_runtime(
#     agentRuntimeArn='arn:aws:bedrock-agentcore:eu-central-1:343935324247:runtime/first_agent-ilYV8GFfkN',
#     runtimeSessionId='dfmeoagmreaklgmrkleafremoigrmtesogmtrskhmtkrlshmt',  # Must be 33+ chars
#     payload=payload,
#     qualifier="DEFAULT" # Optional
# )
# response_body = response['response'].read()
# response_data = json.loads(response_body)
# print("Agent Response:", response_data)

import boto3
import json

client = boto3.client('bedrock-runtime', region_name='eu-central-1')

response = client.invoke_model(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    body=json.dumps({"prompt": "Explain machine learning in simple terms"})
)

result = json.loads(response['body'].read())
print(result)
