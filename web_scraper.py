'''
This is the portion of the DC Killer program that is responsible for
downloading the menu for today, turning the menu into a breakfast,
lunch, and dinner section and then append to today's database what is available
'''
# TODO: 2 Include a time element to self.menu. It could look like {'Dinner': [[Time as string], [item1, item2, item3]] }
# TODO: 1 Retrieve the menu from the Coop (our on campus cafe)
# TODO: 1 Retrieve the menu from Lunt Cafe
# TODO: 1 Retrieve menu from Bryn Mawr Equivalents
# TODO: 1 Make any meals that are currently available (by time) glow

import urllib2


class Webget():
    """
    This is the portion of the DC Killer program that is responsible for
    downloading the menu for today, turning the menu into a breakfast,
    lunch, and dinner section and then returns a dictionary of what is
    available for that day.

    Currently it is also responsible for formatting the menu in the proper
    HTML format. I might divide this class into 4 different classes, one
    for each Haverford menu, Haffner Menu, Erdman, and specialty menus.

    In the future this will have to import the user database and food
    database in order to retrieve favorites and category information.

    """

    def __init__(self):
        """
        Initializes the variables
        """
        self.download = ""
        self.preformattedMenu = ""
        self.formattedMenu = []
        self.menu = {'Continental Breakfast': [], 'Brunch': [], 'Breakfast': [], 'Lunch': [], 'Dinner': []}

    def download_menu(self):
        """
        Downloads the menu and outputs into a list where each line is a line in the menu HTML file that is relevant
        to the menu ie it excludes all other parts of the page. It does this by looping through all the characters
        in the html file until it find a 't' (the haverford menu starts where "today_menu_1" is located in the
        html file). if it finds 't' then it checks if the next letter is 'o', then 'd', then 'a', etc until it finds
        all of 'today_menu_1'.

        :returns: self.menuString ie a string that contains all relevant info for the menu preformatted
        """
        self.download = urllib2.urlopen('https://www.haverford.edu/dining-services/dining-center').read()
        self.startString = "today_menu_1"
        self.menuStart = 0
        self.match = 12

        # print self.download

        for characterNumber in range(len(self.download)):
            if self.download[characterNumber] == 't':
                for characterNumber2 in range(len(self.startString)):
                    if self.download[characterNumber + characterNumber2] == self.startString[characterNumber2]:
                        self.match -= 1
                    else:
                        self.match = 12
            if not self.match:
                for T in range(1100):
                    self.preformattedMenu += self.download[characterNumber + T]
                # print self.preformattedMenu
                break

    def format_menu(self):
        """
        Formats the menu into a nice format.
        Idea: It takes preformattedMenu and splits it based on '<'. Every item in the list that starts with 'br>' or
        'p>' contains a menu item so the method loops through each item in the list and appends it, with the first
        characters removed, to a self.formattedMenu. Note: everything that starts with 'h4>' will be a meal name.
        Everything that starts with 'h3>' is a date.

        :returns: list of menu items
        """
        self.mealPositions = [False] * 5
        self.mealNames = ['Continental Breakfast', 'Brunch', 'Breakfast', 'Lunch', 'Dinner']
        self.split1 = self.preformattedMenu.split('<')

        for checkItem in self.split1:
            if not checkItem.find('p>') or not checkItem.find('br>') or not checkItem.find('h4>') or not checkItem.find(
                    'h3>'):
                if checkItem.split('>')[1] != '':
                    self.formattedMenu.append(checkItem.split('>')[1])

        del self.formattedMenu[0]
        print self.formattedMenu
        print len(self.formattedMenu)

        for t in range(len(self.mealNames)):
            for s in range(len(self.formattedMenu)):
                if self.formattedMenu[s] == self.mealNames[t]:
                    self.mealPositions[t] = s
                    break
        print self.mealPositions

        for t in range(len(self.formattedMenu)):
            for n in range(len(self.mealNames)):
                if self.mealNames[n] == self.formattedMenu[t]:
                    self.mealPositions[n] = t

        '''
        # Given ('Continental Breakfast', '1', '2', '3', '4', '5', 'breakfast', '6','7','8', 'dinner', '9', '10')
        # Turn into {Continental Breakfast: 'sdsdsd', breakfast: sdasd, dinner, ada}

        given = ('Continental Breakfast', '1', '2', '3', '4', '5', 'Breakfast', '6','7','8', 'Dinner', '9', '10')
        meals = ('Continental Breakfast', 'Breakfast', 'Dinner')
        menu  = {'Continental Breakfast': [], 'Brunch': [], 'Breakfast': [], 'Lunch': [], 'Dinner': []}

        key=''
        for items in given:
            if items in meals:
                key=items
            else:
                menu[key].append(items)

        print menu
        '''

        # TODO: Replace with the above multiline comment
        '''
        for t in range(len(self.formattedMenu)):
            if (self.mealPositions[0]):
                print "yup1"
                if self.mealPositions[0] < t and t < self.mealPositions[1]:
                    self.menu[self.mealNames[0]].append(self.formattedMenu[t])
                    print "yup2"
            elif (self.mealPositions[1]):
                print "yup3"
                if self.mealPositions[1] < t and t < self.mealPositions[2]:
                    self.menu[self.mealNames[1]].append(self.formattedMenu[t])
                    print "yup4"
            elif (self.mealPositions[2]):
                print "yup5"
                if self.mealPositions[2] < t and t < self.mealPositions[3]:
                    self.menu[self.mealNames[2]].append(self.formattedMenu[t])
                    print "yup6"
            elif (self.mealPositions[3]):
                print "yup7", self.formattedMenu[t],self.mealPositions[3], t, self.mealPositions[4]
                if self.mealPositions[3] < t and t < self.mealPositions[4]:
                    self.menu[self.mealNames[3]].append(self.formattedMenu[t])
                    print "yup8"
                #TODO: Add the two lines underneath this to all the if statements. High Priority.
                if t == self.mealPositions[4]:
                    self.mealPositions[3]=False
            elif (self.mealPositions[4]):
                print "yup9"
                if self.mealPositions[4] < t and t < len(self.formattedMenu):
                    self.menu[self.mealNames[4]].append(self.formattedMenu[t])
                    print "yup10"

        print self.menu
        '''
        return {'Continental Breakfast': ['1', '2', '3', '4', '5'], 'Brunch': [], 'Dinner': ['9', '10'],
                'Breakfast': ['6', '7', '8'], 'Lunch': []}

    def meal_times(self):
        """
        Formats the menu so that it includes information about meal time

        :returns: nothing. Changes self.menu so that it includes meal time information
        """
        # TODO: This is part of the TODO about time.
        pass

    def format_to_HTML(self, data=None):
        # Replace this food with a properly formatted menu
        # Currently, the dining hall is closed so I am using an example menu 'food' but when it opens I will replace with live data.
        # data should be of the format {'meal': ['time', ['food1', 'food2', 'etc']]}

        food = [
            ['Breakfast', ["7-9am",
                           [['Chocolate Pancakes', 'veg,vgn,meat,hal'],
                            ['Bagels', 'veg,vgn,meat,hal'],
                            ['Breaded chicken breast tenderloin', 'veg,vgn,meat,hal'],
                            ['Vegan Chicken Tenders', 'veg,vgn,meat,hal'],
                            ['Salad', 'veg,vgn,meat,hal'],
                            ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal']]
                           ]],
            ['Lunch', ["11am-2.30pm",
                       [['Gourmet Steak', 'veg,vgn,meat,hal'],
                        ['Soup de Jour', 'veg,vgn,meat,hal'],
                        ['Super Sundae Sunday', 'veg,vgn,meat,hal'],
                        ['Breaded Shark', 'veg,vgn,meat,hal'],
                        ['Tuna Salad', 'veg,vgn,meat,hal'],
                        ['Selection of Gourmet Cookies', 'veg,vgn,meat,hal']]
                       ]],
            ['Dinner', ["5pm-8pm",
                        [['Breakfast Bar', 'veg,vgn,meat,hal'],
                         ['General Tso\' Chicken', 'veg,vgn,meat,hal'],
                         ['Cuban Sandwhiches', 'veg,vgn,meat,hal'],
                         ['Other Sandwiches', 'veg,vgn,meat,hal'],
                         ['Vegan Steak', 'veg,vgn,meat,hal'],
                         ['Pizza', 'veg,vgn,meat,hal']]
                        ]]
        ]

        HTML = ''
        print len(food)
        for i in range(len(food)):

            # This is the meal name and associate time
            HTML += '<br><br>\n'
            HTML += '<div id="container"><div id="container" class="demo-card-wide mdl-card mdl-shadow--4dp">\n'
            HTML += '<div class="mdl-card__title">\n'
            HTML += '<h2 class="mdl-card__title-text">' + food[i][0] + '</h2>\n'
            HTML += '<div id="time" class="mdl-card__subtitle-text">' + '&nbsp;'*6 + food[i][1][0] + '</div>\n'
            HTML += '</div>\n'

            # This is all of the menu items
            HTML += '<div class="mdl-card__supporting-text">\n'
            for j in range(len(food[i][1][1])):
                #This is where I'd do the if-then for lighting up the menu if it's currently available
                #Color #4A148C ie primary color
                HTML += '<font name="sec" href="javascript:void(0);" onclick="this.style.color="#DD2C00";" id="xx' \
                        + str(i)\
                        + str(j) \
                        +'" size="3" color="#424242">'\
                        +'<a name="sec" href="javascript:void(0);" onclick="this.style.color=\'#DD2C00\';">' \
                        + food[i][1][1][j][0]\
                        + '</a>' \
                        + '</font><br><div class="mdl-tooltip" for="xx' \
                        +str(i) \
                        + str(j) \
                        + '">' \
                        +food[i][1][1][j][1] +'</div>'
            HTML += '</div>\n'
            HTML += '<div class="mdl-card__actions mdl-card--border">\n'
            HTML += '<a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect sh-section-btn">Comment</a>\n'

            # This is the place to add comment section (Line below)
            HTML += '<div class="h-section-cont shw-box">Hello world!<br>'+ 'comments comments<br>'*5 + '<form action="#"><div class="mdl-textfield mdl-js-textfield"><input class="mdl-textfield__input" type="text" id="sample1"><label class="mdl-textfield__label" for="sample1">Type your comment...</label></div></form>' +'</div>\n'
            HTML += '</div>\n'
            HTML += '<div class="mdl-card__menu">\n'
            HTML += '<button class="mdl-button mdl-button--icon mdl-js-button mdl-js-ripple-effect">\n'
            HTML += '<i class="material-icons">share</i>\n'
            HTML += '</button>\n'
            HTML += '</div>\n'
            HTML += '</div></div>\n'
            HTML += '<br><br>'

        return HTML

'''
The below is how you'd use this class to get the menu for the day.
test = Webget()        Create and object from class
test.download_menu()   Download Menu into raw data format
test.format_menu()     Format menu into easy manipulable format
test.meal_times()      Add in the meal times to the menu
test.nutrition()       Add categorization like vegan, vegetarian, etc, and caloric information
test.preferences()     Add in if the food is a favorite food. Users will soon be able to favorite foods they like
test.format_to_HTML()  Output the menu to HTML

There will instead be a self.run() function which does all the above
The idea is that the menu will update every day at midnight or 1am and change the database as necessary.
Then when a user visits the site, there will be an updated menu
'''
