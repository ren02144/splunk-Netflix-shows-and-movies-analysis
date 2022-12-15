# Netflix TV Shows and Movies Analysis Splunk App

## Getting Started
This is a splunk app which used for Netflix TV Shows and Movies trend analysis.
Dataset: Kaggle Netflix TV Shows and Movies (2022 Updated) - https://www.kaggle.com/datasets/thedevastator/the-ultimate-netflix-tv-shows-and-movies-dataset?resource=download
Support library: splunk-sdk-python - https://github.com/splunk/splunk-sdk-python

#### Installation and Configuration Steps
This app can only be used in splunk. User must install splunk then copy this repo into ${SPLUNK_HOME}/etc/app
Download Splunk: https://www.splunk.com/en_us/download/splunk-enterprise.html

#### Running Steps
1. Select and click Nexflix shows analysis from header Apps dropdown list
2. In Search input '|listshowsbyyear' and click search to get number of shows and movies by each year
3. In Search input '|listshowsbycountry' and click search to get number of shows and movies by US and other countries
4. In Search input '|countshowsbytag' and click search to get occurred times of every categories by year
5. In Search input '|counttopscoretags' and click search to get occurred times of every categories for shows with score >= 8.5
6. In Search input '|counttopvotetags' and click search to get occurred times of every categories for shows with top 100 votes counting
7. In Search input '|avgscoreandvotestoptag' and click search to get average score and votes of popular categories in recent 5 years
