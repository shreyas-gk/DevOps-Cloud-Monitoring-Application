import boto3

def create_rds_instance():
    # Initialize a boto3 RDS client for the us-west-1 region
    rds_client = boto3.client('rds', region_name='us-east-1')

    try:
        response = rds_client.create_db_instance(
            DBInstanceIdentifier='my-monitoring-db',
            AllocatedStorage=20,
            DBInstanceClass='db.t3.micro',  # Adjusted to a different instance class
            Engine='mysql',
            EngineVersion='8.0.23',  # Specify an engine version known to be supported with db.t3.micro
            MasterUsername='admin',
            MasterUserPassword='YourSecurePasswordHere123!',  # Change this to a strong, unique password
            PubliclyAccessible=True,
            # Ensure you comply with AWS's security best practices, e.g., setting up VPC, Security Groups, etc.
            # ... other parameters as needed ...
        )
        print("Creating RDS instance in us-west-1:", response['DBInstance']['DBInstanceIdentifier'])
    except rds_client.exceptions.DBInstanceAlreadyExistsFault:
        print("An instance with the given identifier already exists in us-west-1.")
    except rds_client.exceptions.ClientError as e:
        print("AWS ClientError in us-west-1:", e.response['Error']['Message'])
    except Exception as e:
        print("Error creating RDS instance in us-west-1:", e)

create_rds_instance()
