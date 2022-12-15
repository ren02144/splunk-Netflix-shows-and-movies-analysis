from __future__ import absolute_import, division, print_function, unicode_literals
import os,sys
import time
import json
import requests as req
import csv
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators


@Configuration(type="reporting")
class counttopscoretags(GeneratingCommand):

    def read_csv(self):
        with open('top_scores.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            shows = {}
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if row[4] != "[]":
                      tag = row[4].strip("[]").replace("'","").replace(" ","").split(',')
                      for co in tag:
                        if co in shows:
                          shows[co] = shows[co] + 1
                        else:
                          shows[co] = 1
                    line_count += 1
            return shows

    def generate(self):
        show_list = self.read_csv()
        for tag in show_list:
            yield {'Tag': tag, 'Number': show_list[tag]}

dispatch(counttopscoretags, sys.argv, sys.stdin, sys.stdout, __name__)