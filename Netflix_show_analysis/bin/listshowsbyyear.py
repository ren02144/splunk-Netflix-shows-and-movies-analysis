from __future__ import absolute_import, division, print_function, unicode_literals
import os,sys
import time
import json
import requests as req
import csv
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators


@Configuration(type="reporting")
class listshowsbyyear(GeneratingCommand):

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
                        if row[2] == 'SHOW':
                            shows[row[3]] = [shows[row[3]][0] + 1, shows[row[3]][1]]
                        else:
                            shows[row[3]] = [shows[row[3]][0], shows[row[3]][1] + 1]
                    else:
                        shows[row[3]] = [0, 0]
                    line_count += 1
            return shows

    def generate(self):
        show_list = self.read_csv()
        for show in show_list:
            yield {'Year': show, 'Show': show_list[show][0], 'Movie' : show_list[show][1]}

dispatch(listshowsbyyear, sys.argv, sys.stdin, sys.stdout, __name__)