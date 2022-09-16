#pip install python-dateutil or
# pip3 install python-dateutil
# Input= "2022-06-20 21:26:45+08:00"
# from dateutil import parser
# date = parser.parse(Input)
# print(date.isoformat())
# from pymongo import MongoClient
# from pymongo import MongoClient
# client = MongoClient()
# client = MongoClient(‘host’, port_number)
# example:- client = MongoClient(‘localhost’, 27017)

# from datetime import datetime, tzinfo, timedelta
# class simple_utc(tzinfo):
#     def tzname(self,**kwargs):
#         return "UTC"
#     def utcoffset(self, dt):
#         return timedelta(0)
# from datetime import datetime, timezone
#
# date_form = datetime.isoformat(Input)
# print(date_form)
# datetime.now(timezone.utc).isoformat()

