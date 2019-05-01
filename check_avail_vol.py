import boto3
ec2 = boto3.resource('ec2', region_name='ap-*')
volumes = ec2.volumes.all()
for vol in volumes:
  if vol.state=='available':
	  if vol.tags is None:
      print "VolumeID:"+ vol.id, "Volume Name:"+tag['Value']
