"""
This is the part of the program responsible for all database related operations and data
"""
# TODO: 3 Write script that converts nutirition info as in foodbase.txt to a easily manipulatable database format
# TODO: 3 Generate a food_list document for the DC Collection
# TODO: 2 Document the design of the database
#import pymongo as mongo
import datetime
import json


class Data(object):
    '''
    The Data class handles all database related operations.
    '''

    def __init__(self):
        '''
        This method initializes the connection to the database.
        Make sure the database (mongod) is running!
        Usage:
        d=Date()
        if d: foo
        else: return 'error!'
        '''

        '''
        newConnect = mongo.MongoClient()          #A connection
        DCKiller = newConnect['DCKillerdb']       #A Database

        DCMeals = DCKiller['DCMeals']             #A Collection
        HaffnerMeals = DCKiller['HaffnerMeals']   #A Collection
        ErdmanMeals = DCKiller['ErdmanMeals']     #A Collection
        SpecialMeals = DCKiller['SpecialMeals']  #A Collection
        NutritionCollection = DCKiller['NutritionCollection']

        self.Collections={'DC':DCMeals, 'Haffner':HaffnerMeals, 'Erdman':ErdmanMeals, 'Special': SpecialMeals, 'NutritionCollection':NutritionCollection}
        '''

    def today_date(self):
        '''
        Returns today's date in a YYYYMMDD format as an integer.
        This date format is used as a unique ID for each document
        in each collection in our database.
        ''' 
        today = datetime.date.today()
        formatted_date_str = ''
        formatted_date_int = 0

        formatted_date_str += str(today.year)
        if len(str(today.month)) == 1:
            formatted_date_str += "0" + str(today.month)
        else:
            formatted_date_str += str(today.month)
        if len(str(today.day)) == 1:
            formatted_date_str += "0" + str(today.day)
        else:
            formatted_date_str += str(today.day)

        formatted_date_int = int(formatted_date_str)
        return formatted_date_int

    def new_entry(self, location, entry, date=False):
        """
        Enters a new entry into the database.
        Arguments: location (either 'DC', 'Haffner', 'Erdman', 'Special')
        entry (in the format described in web_scraper.py)
        date in the YYYYMMDD format as an integer to uniquely idenity the entry

        Returns: Nothing
        """
        if not date:
            date = self.today_date()

        entry['_id']=date
        
        self.Collections[location].insert(entry)

    def get_today_entry(self, location):
        today=self.today_date() 

        entry = self.Coollections.get_one({'_id':today})
        return entry

    def add_food_JSON_data_to_database(self, number_of_foods):
        '''

        takes number_of_foods which is the number of *.txt files in /json_files
        :return: nothing. Adds all the foods in /json_files to the database
        '''
        self.change_paren(number_of_foods)
        for fileindex in range(number_of_foods):
            pass
            food = []
            afile = open('json_files/JSON_' +str(fileindex + 1) + '.txt')
            food = afile.readline()
            food = json.loads(food)
            print food

            #for each JSON element, create a list of all the information for each food
            #add that element to the list
            #make id==name
            #add the temporary list into the database

    def change_paren(self, number):
        '''
        Goes thru /json_files and converts all single parentheses to double parentheses for the JSON library
        :return:
        '''
        pass
        for index in range(number):
            afile = open('json_files/JSON_' + str(index + 1) + '.txt', "r")
            filecontents = afile.read()
            afile.close()

            afile = open('json_files/JSON_' + str(index + 1) + '.txt', "w")
            filecontents = filecontents.replace('\'', '"')
            afile.write(filecontents)
        #Load the contents of the file into a string
        #Replace ' with "
        #Write file

test=Data()
test.add_food_JSON_data_to_database(100)

#test.new_entry('DC', a)
#test.new_entry('DC', b, date=20160103)
#test.new_entry('DC', c, date=20160102)



x= test.Collections['DC'].find()
for i in x:
    if 'lunch' in i:
        #print i['lunch']
        pass
