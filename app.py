from flask import Flask, render_template
import boto3
import psutil
import datetime  # Add this import for datetime


app = Flask(__name__)

@app.route("/")
@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    rds_details = fetch_rds_details()  # Call the fetch_rds_details() function
    message = None
    if cpu_metric > 80 or mem_metric > 80:
        message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message, rds_details=rds_details)  # Pass rds_details to the template

def get_rds_metric(metric_name, period=300, statistics=['Average']):
    cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')  # Replace 'us-east-1' with your region
    try:
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/RDS',
            MetricName=metric_name,
            Dimensions=[
                {
                    'Name': 'DBInstanceIdentifier',
                    'Value': 'my-monitoring-db'  # Ensure this matches your DB instance identifier
                },
            ],
            StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=600),
            EndTime=datetime.datetime.utcnow(),
            Period=period,
            Statistics=statistics,
        )
        return response['Datapoints'][0][statistics[0]] if response['Datapoints'] else 'No data'
    except Exception as e:
        print("Error fetching RDS metric:", e)
        return 'Error'
def fetch_rds_details():
    cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')  # Replace 'us-east-1' with your region
    # ... rest of your code ...
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/RDS',
        MetricName='CPUUtilization',  # Replace with the appropriate metric name
        Dimensions=[
            {
                'Name': 'DBInstanceIdentifier',
                'Value': 'my-monitoring-db'  # Ensure this matches your DB instance identifier
            },
        ],
        StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=600),
        EndTime=datetime.datetime.utcnow(),
        Period=300,
        Statistics=['Average'],
    )

    rds_instance_name = 'Your RDS Instance Name'  # Replace with actual RDS instance name
    db_name = 'Your DB Name'  # Replace with actual DB name
    db_engine = 'Your DB Engine'  # Replace with actual DB engine

    return {
        'instance_name': rds_instance_name,
        'db_name': db_name,
        'db_engine': db_engine,
    }

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')