import boto3
session = boto3.Session(profile_name='justdo')
ec2 = session.resource('ec2')
for n in ec2.instances.all():
   print(n)
