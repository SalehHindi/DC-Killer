"""
This is the part of the program responsible for all database related operations and data
"""
# TODO: 3 Write script that converts nutirition info as in foodbase.txt to a easily manipulatable database format
# TODO: 3 Generate a food_list document for the DC Collection
# TODO: 2 Document the design of the database
import pymongo as mongo
import datetime

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
        if 1:
            newConnect = mongo.MongoClient()              #A connection
            DCKiller = newConnect['DCKillerdb']       #A Database

            DCMeals = DCKiller['DCMeals']             #A Collection
            HaffnerMeals = DCKiller['HaffnerMeals']   #A Collection
            ErdmanMeals = DCKiller['ErdmanMeals']     #A Collection
            SpecialMeals = DCKiller['Special Meals']  #A Collection

            self.Collections={'DC':DCMeals, 'Haffner':HaffnerMeals, 'Erdman':ErdmanMeals, 'Special': SpecialMeals}
         
           
       # except:
       #     print 'Database connection error!'
           

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

test=Data()
a={'breakfast':[['7am-9am'], ['pancakes']*5, ['600']*5], 
'lunch': [['1pm-2pm'], ['bagels']*5, ['500']*5]}
b={'breakfast':[['7am-9am'], ['pes']*5, ['700']*5], 
'lunch': [['1pm-2pm'], ['bls']*5, ['800']*5]}
c={'breakfast':[['7am-9am'], ['paijijoncakes']*5, ['900']*5], 
'lunch': [['1pm-2pm'], ['bojpokpoagels']*5, ['1000']*5]}
#test.new_entry('DC', a)
#test.new_entry('DC', b, date=20160103)
#test.new_entry('DC', c, date=20160102)

x= test.Collections['DC'].find()
for i in x:
    if 'lunch' in i:
        print i['lunch']
