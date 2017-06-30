# dynamoETL

Script(s) and supporting files for batch importation of individual Stansberry content MongoDB JSON exports, into dynamoDB.

# Description of contents

   ## 'templates' directory = directory of files defining the schema used when creating a given dynamoDB table
   
 Included for the purpose of documentation, not implementation.
 
 I will update README to include description of how 'templates' directory files are in fact implemented (i.e., how to create new dynamoDB tables). It will be a summary of the boto documentation: https://boto.readthedocs.io/en/latest/dynamodb2_tut.html
 
   ## 'scripts' directory = Home of core functionality (currently just 'json2dyno.py')
  
  USEAGE:
  python /path/to/dynamoETL/scripts/json2dyno.py -j /path/to/file.list -t {table name}

  In other words:
  
  parser = argparse.ArgumentParser(description="MongoDB JSON to dynamoDB importer")
  parser.add_argument("-j", "--json", required=True, help="list of JSON file names to import, one per line")
  parser.add_argument("-t", "--table", required=True, help="dynamoDB table to import into")
  
  
  Further documentation and functionality, to come.
