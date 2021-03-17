import boto3
from pgbackup import storage
client = boto3.client('s3')
infile = open('dump.sql', 'rb')
storage.s3(client, infile, 'ngoducquyetkms-db-backups', infile.name)
