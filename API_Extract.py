# Exercise1

#libraries needed for the script
import xml.etree.ElementTree as ET
import pandas as pd
import urllib.request
 

#1. Creates the access to the API gameday
###############################################################################                                                       
date = input('Enter the date of interest in the format YYYY-MM-DD:  ')         #asks for input date (ex: 2018-05-09)
year, month, day, = date[0:4], date[5:7], date[8:10];                          #separates date to year, month, day
 
#creates the link to the API game data                                                                                                         
url  = 'http://gd2.mlb.com/components/game/mlb/year_'+year+'/month_'+month+'/day_'+day+'/grid.xml'
###############################################################################

 

#2. Parses the XML formatted data into a pandas dataframe
###############################################################################                                                                        
gameday_tree = urllib.request.urlopen(url).read()                              #reads the url
games=ET.fromstring(gameday_tree)                                              #stores url data as element tree

#creates the data frame for the xml parsed data to be inserted to
#each row will represent a game on the specified date
df1 = pd.DataFrame(columns = ['away_code', 'away_file_code', 'away_name_abbrev', \
      'away_score', 'away_team_id', 'away_team_name', 'calendar_event_id', \
      'double_header_sw', 'event_time', 'game_nbr', 'game_pk', 'game_type', \
      'gameday_sw', 'group', 'home_code', 'home_file_code', 'home_name_abbrev',\
      'home_score', 'home_team_id', 'home_team_name', 'id', 'ind', 'inning', \
      'media_state', 'series', 'series_num', 'status', 'tbd_flag', 'top_inning', \
      'venue', 'venue_id'])

i = 0                                                                          #row counter for data frame df1
for game in games:                                                             #loop iterates through each 'game' branch in xml tree of 'games'
    #away team information
     df1.loc[i, 'away_code'] = game.attrib.get('away_code')
     df1.loc[i, 'away_file_code'] = game.attrib.get('away_file_code')
     df1.loc[i, 'away_name_abbrev'] = game.attrib.get('away_name_abbrev')
     df1.loc[i, 'away_score'] = game.attrib.get('away_score')
     df1.loc[i, 'away_team_id'] = game.attrib.get('away_team_id')
     df1.loc[i, 'away_team_name'] = game.attrib.get('away_team_name')

     #game information
     df1.loc[i, 'calendar_event_id'] = game.attrib.get('calendar_event_id')
     df1.loc[i, 'double_header_sw'] = game.attrib.get('double_header_sw')
     df1.loc[i, 'event_time'] = game.attrib.get('event_time')
     df1.loc[i, 'game_nbr'] = game.attrib.get('game_nbr')
     df1.loc[i, 'game_pk'] = game.attrib.get('game_pk')
     df1.loc[i, 'game_type'] = game.attrib.get('game_type')
     df1.loc[i, 'gameday_sw'] = game.attrib.get('gameday_sw')
     df1.loc[i, 'group'] = game.attrib.get('group')

     #home team information
     df1.loc[i, 'home_code'] = game.attrib.get('home_code')
     df1.loc[i, 'home_file_code'] = game.attrib.get('home_file_code')
     df1.loc[i, 'home_name_abbrev'] = game.attrib.get('home_name_abbrev')
     df1.loc[i, 'home_score'] = game.attrib.get('home_score')
     df1.loc[i, 'home_team_id'] = game.attrib.get('home_team_id')
     df1.loc[i, 'home_team_name'] = game.attrib.get('home_team_name')

     #other game information
     df1.loc[i, 'id'] = game.attrib.get('id')
     df1.loc[i, 'ind'] = game.attrib.get('ind')
     df1.loc[i, 'inning'] = game.attrib.get('inning')
     df1.loc[i, 'media_state'] = game.attrib.get('media_state')
     df1.loc[i, 'series'] = game.attrib.get('series')
     df1.loc[i, 'series_num'] = game.attrib.get('series_num')
     df1.loc[i, 'status'] = game.attrib.get('status')
     df1.loc[i, 'tbd_flag'] = game.attrib.get('tbd_flag')
     df1.loc[i, 'top_inning'] = game.attrib.get('top_inning')
     df1.loc[i, 'venue'] = game.attrib.get('venue')
     df1.loc[i, 'venue_id'] = game.attrib.get('venue_id')
                                                          
     i += 1                                                                    #next row ("game")  
##############################################################################    
 


#3. Outputs the data frame to .csv    
##############################################################################    
output_csv = date + '.csv'                                                     #creates the .csv file name titled 'date'
df1.to_csv(output_csv, index = False)                                          #outputs data frame to .csv
##############################################################################
#end of script

