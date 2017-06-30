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
import boto.dynamodb2
import boto.dynamodb2.types
import boto.dynamodb2.table
from boto.dynamodb2.table import Table
from boto.dynamodb2.items import Item

dynamodb = boto3.resource('dynamodb')

parser = argparse.ArgumentParser(description="MongoDB JSON to dynamoDB importer")
parser.add_argument("-j", "--json", required=True, help="JSON file name")

args = parser.parse_args(sys.argv[1:])

jsonIn = args.json

test3 = Table('test3')

with open(jsonIn, 'r') as f:
    lines = f.read().splitlines()
    f.close()

for line in lines:
    with open(line, 'r') as l:
        data = json.load(l)
        dynamodb_json = json.dumps(data)
        test3.put_item(data=json.loads(dynamodb_json))
        print line + " added to test2 dynamoDB"
        l.close()



'''
with open(jsonIn, 'r') as f:
    for line in f:
        line = line.strip()
        with open(line, 'r') as l:
            data = json.load(l)
            dynamodb_json = json.dumps(data)
            test3.put_item(data=json.loads(dynamodb_json))
            print line + " added to test2 dynamoDB"
            l.close()

'''




