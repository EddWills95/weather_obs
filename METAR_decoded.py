import urllib2
import datetime as datetime
import os
import numpy as np
import string
import subprocess

#manual input of ICAO index
index = raw_input("Please enter your input")

#calling the script to get the METAR report
command = "python get_report.py %s" %(index)

#setting up variable for finding temp data
report = os.system(command)
var = 'temperature:'
temp_index = report.find(var)
print(temp_index)

#print out temp
temp = report[temp_index+4:temp_index+6]
print(temp)
#FTP of METAR reports
ftp = 'http://tgftp.nws.noaa.gov/data/observations/metar/stations/'


