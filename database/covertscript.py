# TODO: 3 Load each of the foods into a new file
# TODO: 3 For each food, mark it off with the filename in listoffoods.txt
# TODO: 3 Load ALL of the foods from listoffoods.txt into a new JSON_*.txt file
# TODO: 3 Add all the files to database
# TODO: 1 Clean up file so it looks nice
# TODO: 1 Rename to convertscript.py
class data_converter(object):
    '''
    This file and this class is responsible for converting data formatted like what is in the triple quote
    at the bottom of the page to a JSON format that is easily stored and read in our database.

    Input: pre-formatted data as a file name ie "X.txt"  (see triple quotes at the bottom of the page)
    Returns: Should create a file named "JSON_X.txt" populated with self.final_food_data
    '''
    def __init__(self, filename=''):
        self.filename = 'raw_nutrition_files/' +filename
        #Note: there are 43 keys in self.final_food_data
        self.final_food_data = {"Serving Size ":0,
                              "Servings Per Container ":0,
                              "Calories ":0,
                              "Calories from Fat ":0,
                              "SugarAlcohol (g)":0,
                              "Protein (g)":0,
                              "Trans Fat (g)":0,
                              "Polyunsaturated Fat (g)":0,
                              "Cholesterol (mg)":0,
                              "Sodium (mg)":0,
                              "Potassium (mg)":0,
                              "Total Carbohydrates (g)":0,
                              "Dietary Fiber (g)":0,
                              "Sugars (g)":0,
                              "Total Fat (g)":0,
                              "Saturated Fat (g)":0,
                              "Monounsaturated Fat (g)":0,
                              "Vitamin A (%)":0,
                              "Calcium (%)":0,
                              "Vitamin D (%)":0,
                              "Vitamin K (%)":0,
                              "Riboflavin (%)":0,
                              "Vitamin B6 (%)":0,
                              "Vitamin B12 (%)":0,
                              "Pantothenic Acid (%)":0,
                              "Iodine (%)":0,
                              "Zinc (%)":0,
                              "Copper (%)":0,
                              "Chromium (%)":0,
                              "Chloride (%)":0,
                              "Vitamin C (%)":0,
                              "Iron (%)":0,
                              "Vitamin E (%)":0,
                              "Thiamin (%)":0,
                              "Niacin (%)":0,
                              "Folate (%)":0,
                              "Biotin (%)":0,
                              "Phosphorus (%)":0,
                              "Magnesium (%)":0,
                              "Selenium (%)":0,
                              "Manganese (%)":0,
                              "Molybdenum (%)":0,
                              "Name": ''
                              }

    def convert(self):
        '''
        Converts pre-formatted data into a JSON data type.
        The general concept is that convert() loads all the data from the file into self.preformat_data, for each
        key in self.final_food_data search the entirety of self.preformat_data for that key, then if found load
        all the following characters into the value associated with that key until a non number character is reached
        (with all spaces and comma). Then it makes the first line the Name the first line. If converter() cannot
        find the key, it will move on.

        Issues:
        The macro-nutrient data is stored in grams where it would be helpful to have it in percentages.
        This can be solved later by converting on output.

        This could definitely be made more efficient but since it doesn't take long to run and only needs to be
        run once, it's not a concern.
        '''
        self.pre_format_data = ''
        numbers = '0123456789.'
        datainput = open(self.filename, 'r')
        dataoutput = open('json_files/JSON_'+self.filename, 'w')

        for line in datainput.readlines():
            self.pre_format_data += line

        #print len(self.final_food_data.keys())

        for key in self.final_food_data.keys():
            original_key = key
            #The following line converts "Protein (g)" to "Protein"
            key = key.split('(')[0]
            match = False
            value_add_start = 0


            #print len(self.pre_format_data), key

            for character_index in range(len(self.pre_format_data)):

                if self.pre_format_data[character_index] == key[0]:
                    #print 'ok'
                    match_amount = 0
                    for iterator_index in range(len(key)):
                        try:
                            if self.pre_format_data[iterator_index+character_index] == key[iterator_index]:
                                #print self.pre_format_data[iterator_index+character_index]
                                match_amount += 1
                                value_add_start = iterator_index+character_index
                        except: pass
                    if match_amount == len(key):
                        match = True
                        #print key, "||"

                        #should be current character index
                        current_character = value_add_start
                        value_string = ''

                        while self.pre_format_data[current_character] in numbers or self.pre_format_data[current_character] == ' ':
                            if self.pre_format_data[current_character] in numbers:
                                value_string += self.pre_format_data[current_character]
                            current_character += 1
                        #print key, "!", value_string, "||", len(key)
                        self.final_food_data[original_key] = value_string

                        break

        #print self.final_food_data
        name = self.pre_format_data.split('\n')
        name = name[0]
        self.final_food_data['Name'] = name

        dataoutput.write(str(self.final_food_data))

for i in range(100):
    fileindex = str(i+1)

    converter_object = data_converter(fileindex + '.txt')
    converter_object.convert()



'''
Hard Cooked Egg*
Nutrition Facts
Serving Size 1 each (44 g)
Servings Per Container   1
Amount Per Serving
Calories  60Calories from Fat  40
 % Daily Value*
Total Fat   4g 6%
Saturated Fat  1.5g 7%
Trans Fat  0g
Polyunsaturated Fat  1g
Monounsaturated Fat  1.5g
Cholesterol  165mg 55%
Sodium  60mg 2%
Potassium  60mg 2%
Total Carbohydrate  0g0%
Dietary Fiber  0g 0%
Sugars  0g
Protein  6g
Vitamin A  4% Vitamin C  0%
Calcium  2% Iron  4%
Thiamin  2% Riboflavin  10%
Niacin  0% Vitamin B6  4%
Folacin  6% Vitamin B12  6%
Phosphorus  8% Zinc  4%
* Percent Daily Values are based on a 2,000 calorie diet. Your daily values may be higher or lower depending on your calorie needs:
 Calories:2,0002,500
Total FatLess than65g80g
  Sat FatLess than20g25g
CholesterolLess than300mg300mg
SodiumLess than2400mg2400mg
Total Carbohydrate300g375g
  Dietary Fiber25g30g
Calories per gram:
Fat 9 * Carbohydrate 4 * Protein 4
'''