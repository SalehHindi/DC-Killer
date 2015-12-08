####################################################################
# This is the portion of the DC Killer program that is responsible for
# downloading the menu for today, turning the menu into a breakfast,
# lunch, and dinner section and then returns a dictionary of what is
# available for that day
import urllib2


class Webget():
    """
    This is the portion of the DC Killer program that is responsible for
    downloading the menu for today, turning the menu into a breakfast,
    lunch, and dinner section and then returns a dictionary of what is
    available for that day.
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
                #print self.preformattedMenu
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
        self.mealPositions=[False]*5
        self.mealNames=['Continental Breakfast', 'Brunch', 'Breakfast', 'Lunch', 'Dinner']
        self.split1=self.preformattedMenu.split('<')
        #for T in self.split1:
        #    print T,"\n"*1

        for checkItem in self.split1:
            if not checkItem.find('p>') or not checkItem.find('br>') or not checkItem.find('h4>') or not checkItem.find('h3>'):
                if checkItem.split('>')[1]!='':
                    self.formattedMenu.append(checkItem.split('>')[1])

        del self.formattedMenu[0]
        print self.formattedMenu
        print len(self.formattedMenu)

        for t in range(len(self.mealNames)):
            for s in range(len(self.formattedMenu)):
                if self.formattedMenu[s]==self.mealNames[t]:
                    self.mealPositions[t]=s
                    break
        print self.mealPositions

        for t in range(len(self.formattedMenu)):
            for n in range(len(self.mealNames)):
                if self.mealNames[n] == self.formattedMenu[t]:
                    self.mealPositions[n]=t

        #TODO: Condense this to make it more elegant of a solution. Low Priority.
        #TODO: Remove print statements. High priority.
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

    def meal_times(self):
        """
        Formats the menu so that it includes information about meal time

        :returns: nothing. Changes self.menu so that it includes meal time information
        """
        pass


test = Webget()
test.download_menu()
test.format_menu()

'''
Today's menu:
[
meal1: [item1,item2,item3],
meal2: [x,y,z]
'''
