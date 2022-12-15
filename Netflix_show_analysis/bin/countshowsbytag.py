from __future__ import absolute_import, division, print_function, unicode_literals
import os,sys
import time
import json
import requests as req
import csv
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators


@Configuration(type="reporting")
class countshowsbytag(GeneratingCommand):

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
                        if row[4] != "[]":
                          tag = row[4].strip("[]").replace("'","").replace(" ","").split(',')
                          for co in tag:
                            if co in shows[row[3]]:
                              shows[row[3]][co] = shows[row[3]][co] + 1
                            else:
                              shows[row[3]][co] = 1
                    else:
                        shows[row[3]] = {}
                    line_count += 1
            return shows

    def generate(self):
        show_list = self.read_csv()
        for year in show_list:
          for show in show_list[year]:
            yield {'Year': year, 'TAG': show, 'Number': show_list[year][show]}

dispatch(countshowsbytag, sys.argv, sys.stdin, sys.stdout, __name__)