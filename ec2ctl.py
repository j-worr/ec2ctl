#!/usr/bin/python3

import argparse
import boto3

ec2 = boto3.client('ec2')
region = ec2.meta.region_name


def my_start():
    response=ec2.start_instances(InstanceIds=[my_instance])
    print(response)

def my_stop():
    response=ec2.stop_instances(InstanceIds=[my_instance])
    print(response)

def my_reboot():
    response=ec2.reboot_instances(InstanceIds=[my_instance])
    print(response)

def my_list():
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            for tag in instance["Tags"]:
                if tag["Key"] == 'Name':
                    my_instancename = ''
                    my_instancename = tag["Value"]
                    print(my_instancename + " " + instance["InstanceId"])

parser = argparse.ArgumentParser(description='Action to perform on ec2 instances')
parser.add_argument('action', choices={"start", "stop", "reboot", "list"}, help='Start,stop, or list EC2 instance(s)')
parser.add_argument('--instanceid', '-i', help='EC2 instance ID. Required for start or stop actions')
my_instance = args.instanceid

if args.action == "start":
    my_start()
if  args.action == "stop":
    my_stop()
if  args.action == "reboot":
    my_reboot()
if args.action == "list":
    my_list()
