import boto3

def lambda_handler(event, context):
    sns_client = boto3.client("sns", "us-east-1")
    
    # Getting ec2_client because I need the availability zone
    ec2_client = boto3.client("ec2", "us-east-1")
    
    response = ec2_client.describe_instance_status(
         InstanceIds=[
            event['detail']['instance-id']
        ],
        IncludeAllInstances=True
    )
    
    message = 'Your EC2 Instance with id, {}, in availability zone, {}, is {}.'.format(
                event['detail']['instance-id'],
                response['InstanceStatuses'][0]['AvailabilityZone'],
                event['detail']['state']
            )
    
    
    sns_client.publish(TargetArn="arn:aws:sns:us-east-1:287635713150:instance-state-notification", Message=message)
   
    print(message)