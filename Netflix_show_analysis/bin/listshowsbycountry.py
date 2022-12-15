from __future__ import absolute_import, division, print_function, unicode_literals
import os,sys
import time
import json
import requests as req
import csv
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators


@Configuration(type="reporting")
class listshowsbycountry(GeneratingCommand):

    def read_csv(self):
        with open('raw_titles_new.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            shows = {}
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if row[3] in shows:
                        country = row[5].strip("[]").replace("'","").replace(" ","").split(',')
                        for co in country:
                          if co == 'US':
                            shows[row[3]]['US'] += 1
                          else:
                            shows[row[3]]['OTHERS'] += 1
                    else:
                        shows[row[3]] = {'US':0, 'OTHERS':0}
                    line_count += 1
            return shows

    def generate(self):
        show_list = self.read_csv()
        for year in show_list:
            yield {'Year': year, 'US': show_list[year]['US'], 'OTHERS': show_list[year]['OTHERS']}

dispatch(listshowsbycountry, sys.argv, sys.stdin, sys.stdout, __name__)