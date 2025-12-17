import boto3
sns = boto3.client("sns", region_name="il-central-1")
response = sns.publish(TopicArn="arn:aws:sns:il-central-1:436705618119:calculator-topic", Message="Calculation",
            MessageAttributes={
                "op1":{
                    "DataType":"Number",
                    "StringValue": "10.5"
                },
                "op2":{
                    "DataType":"Number",
                    "StringValue": "2.5"
                },
                "operation": {
                    "DataType":"String",
                    "StringValue":"+"
                }
                
            })
print("MessageI:", response["MessageId"])