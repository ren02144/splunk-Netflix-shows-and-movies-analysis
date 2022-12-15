from __future__ import absolute_import, division, print_function, unicode_literals
import os,sys
import time
import json
import requests as req
import csv
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators


@Configuration(type="reporting")
class avgscoreandvotestoptag(GeneratingCommand):

    def read_csv(self):
        with open('recent_five_years.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            shows = {}
            tag_list = ['thriller', 'crime', 'documentation', 'romance', 'action']
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if row[4] != "[]":
                      tag = row[4].strip("[]").replace("'","").replace(" ","").split(',')
                      for co in tag:
                        if (co in tag_list) and (row[7] != ""):
                          if co in shows:
                            shows[co] = [shows[co][0] + 1, shows[co][1] + float(row[6]), shows[co][2] + float(row[7])]
                          else:
                            shows[co] = [1, float(row[6]), float(row[7])]
                    line_count += 1
            return shows

    def generate(self):
        show_list = self.read_csv()
        for tag in show_list:
            yield {'Category': tag, 'Avg_score': show_list[tag][1]/show_list[tag][0], 'Avg_vote': show_list[tag][2]/show_list[tag][0]}

dispatch(avgscoreandvotestoptag, sys.argv, sys.stdin, sys.stdout, __name__)