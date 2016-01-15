class data_converter(object):
    '''
    This file and this class is responsible for converting data formatted like what is in the triple quote
    at the bottom of the page to a JSON format that is easily stored and read in our database.

    Input: pre-formatted data (see triple quotes at the bottom of the page)
    Returns: Should return self.final_food_data to be put into the database
    '''
    def __init__(self):
        self.final_food_data={}

