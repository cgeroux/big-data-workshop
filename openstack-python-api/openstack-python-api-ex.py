#!/usr/bin/env python
from __future__ import print_function
from os import environ as env
import novaclient.client as nvclient

def main():
  
  #create the nova client
  APIVersion="2.0"
  nova=nvclient.Client(APIVersion
    ,auth_url=env['OS_AUTH_URL']#URL to connect to
    ,username=env['OS_USERNAME']#CC Cloud user name
    ,api_key=env['OS_PASSWORD']#CC cloud password
    ,project_id=env['OS_TENANT_NAME']#CC cloud project name
    ,region_name=env['OS_REGION_NAME']#CC cloud region name
    )
    
  #get a list of current servers
  servers=nova.servers.list()
  
  #print()
  #print("dir(servers)=",dir(servers[0]))
  #print()
  #print("nova.servers.list.__doc__=",nova.servers.list.__doc__)
  #print()
  
  #print out a list of the current VM names
  for server in servers:
    print(server.name)

if __name__=="__main__":
  main()