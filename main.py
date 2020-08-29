import looker_sdk
import os
import json
import sys
from flask import abort

def looker_api_call(request):

  if request.method != 'POST':
    return 'Unauthorized', 401
  if not ('connection_name' in request.args and len(request.args['connection_name']) > 0):
    return 'Missing connection_name parameter', 404
  if not ('table' in request.args and len(request.args['table']) > 0):
    return 'Missing table parameter', 404
  if not ('schema' in request.args and len(request.args['schema']) > 0):
    return 'Missing schema parameter', 404
  
  try:  
    sdk = looker_sdk.init31()
    sql_query = "INSERT INTO %s.%s values ('%s')" % ( request.args['schema'], request.args['table'], json.dumps(request.json))

    model = looker_sdk.models31.SqlQueryCreate(
        sql=sql_query, 
        connection_name=request.args['connection_name']
    )
    create_query = sdk.create_sql_query( model )
    run_query = sdk.run_sql_query(
        slug=create_query.slug, 
        result_format="json"
    )
    return 'Success', 200
  except:
    return 'Uh Oh' + " Unexpected error:" + sys.exc_info()[0], 500