import boto3

# Initialize a session using your credentials
session = boto3.Session(
    aws_access_key_id='AKIAZ5HFJMETEIWB6Z6P',  # Replace with your actual access key id
    aws_secret_access_key='2BqGAYNh0f2FCo1S9zLkDQuff/Pw8uWdRMq7mLrw',  # Replace with your actual secret access key
    region_name='us-east-1'  # Replace with your actual region
)

# Create an RDS client
rds_client = session.client('rds')

# Function to list RDS instances
def list_rds_instances():
    try:
        # Call to get the list of RDS DB instances
        db_instances = rds_client.describe_db_instances()
        for db_instance in db_instances['DBInstances']:
            print(f"DB Instance Identifier: {db_instance['DBInstanceIdentifier']}")
            print(f"DB Instance Class: {db_instance['DBInstanceClass']}")
            print(f"DB Engine: {db_instance['Engine']}")
            print(f"DB Engine Version: {db_instance['EngineVersion']}")
            print(f"DB Status: {db_instance['DBInstanceStatus']}\n")
    except Exception as error:
        print(f"An error occurred: {error}")

# Run the function
list_rds_instances()
