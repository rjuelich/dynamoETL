import boto3
import os
import csv
import sys
import argparse
import time
import json
import uuid
from datetime import datetime
from decimal import Decimal
import boto.dynamodb2.types
import boto.dynamodb2.table
from boto.dynamodb2.table import Table
from boto.dynamodb2.items import Item

dynamodb = boto3.resource('dynamodb')

parser = argparse.ArgumentParser(description="MongoDB JSON to dynamoDB importer")
parser.add_argument("-j", "--json", required=True, help="JSON file name")

args = parser.parse_args(sys.argv[1:])

jsonIn = args.json

with open(jsonIn, 'r') as f:
    data = json.load(f)

dynamodb_json = json.dumps(data)


test3 = Table('test3')

test3.put_item(data=json.loads(dynamodb_json))

print jsonIn + " added to test2 dynamoDB"
