import os
import sys
from dotenv import load_dotenv
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.transforms import *

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

load_dotenv()

path = os.environ["S3_PATH"]

dynamicframe = glueContext.create_dynamic_frame.from_options(
    connection_type='s3',
    connection_options={
        'paths': [path],
        'recurse': True
    },
    format_options={
        "withHeader": True,
        # "optimizePerformance": True,
    },
    format='csv'
)
# dynamicframe.printSchema()

print(f"Count: {dynamicframe.count()}")