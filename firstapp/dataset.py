import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mapproject.settings")
django.setup()

#from firstapp.models import Seouldata

# CSV_PATH = '../Seouldataset2.csv'

#with open(CSV_PATH, newline='') as csvfile:
#    data_reader = csv.DictReader(csvfile)
 #   for row in data_reader:
  #      print(row)
   #     Seouldata.objects.create(
    #        sisulname = row['sisulname'],
     #       sisuladdr = row['sisuladdr'],
      #      tel = row['tel'],
       # )

from firstapp.models import Sample

CSV_PATH = '../seouldatasample.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        Sample.objects.create(
            name = row['name'],
            addr = row['addr'],
            tel = row['tel'],
            lat = row['lat'],
            lng = row['lng'],
            kind = row['kind'],
            kind_detail =row['kind_detail'],
        )

