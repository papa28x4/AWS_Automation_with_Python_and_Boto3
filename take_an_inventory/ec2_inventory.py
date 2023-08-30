import boto3
import csv
from pprint import pprint

#Choose one of the profiles previously configured via AWS CLI to establish an session with AWS. This step is only necessary if your using boto3 from your local machine. When writing a Lambda, you won't be needing this because you already logged into AWS
session = boto3.session.Session(profile_name="default")

#Pick the client of the service you want to interact with. 
ec2_client = session.client(service_name="ec2", region_name="us-east-1")

#Create a CSV file
fo = open("ec2_inventory.csv", "w")
csv_w = csv.writer(fo)

#Create the headers of the csv file
column_headers = ["Serial Number", "Instance ID", "Instance Type", "Architecture", "Hyervisor", "Launch Time", "Private IP Address", "Public IP Address"]

csv_w.writerow(column_headers)

#Get the ec2 instances
instances = ec2_client.describe_instances()['Reservations']

serial_number = 1

#loop over the instances to get requested details for each instance
for instance in ec2_client.describe_instances()['Reservations']:
    instance_id = instance['Instances'][0]['InstanceId']
    instance_type = instance['Instances'][0]['InstanceType']
    architecture = instance['Instances'][0]['Architecture']
    platform_details = instance['Instances'][0]['PlatformDetails']
    hypervisor = instance['Instances'][0]['Hypervisor']
    launch_time = instance['Instances'][0]['LaunchTime']
    private_ip_address = instance['Instances'][0]['PrivateIpAddress']
    public_ip_address = instance['Instances'][0]['PublicIpAddress']
    csv_w.writerow([serial_number, instance_id, instance_type, architecture, hypervisor, launch_time, private_ip_address, public_ip_address])
    serial_number += 1
fo.close()
    

    
