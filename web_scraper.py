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

        returns: self.menuString ie a string that contains all relevant info for the menu preformatted
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

        returns: list of menu items
        """
        self.mealPositions=[-1,-1,-1,-1,-1]
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

        test=[[],[],[],[],[]]
        testposition=0
        for t in range(len(self.formattedMenu)):
            breakflag=0
            for names in self.mealNames:
                if self.formattedMenu[t] == names:
                    testposition+=1

            test[testposition].append(self.formattedMenu[t])

        print test
        #rename variables but otherwise this is finished
        '''
        for dictionary in range(len(self.mealNames)):
            #calculate range of values to draw from formattedMenu
            start=dictionary
            for t in range(start, 5-1):
                if not self.mealPositions[t+1]+1:
                    end=self.mealPositions[t]
                    break
                if self.mealPositions[t+1]+1:
                    end=self.mealPositions[t+1]
                    break
            print start, "\\", end
            #iterate through those items and add it to
        '''
    def meal_format(self):
        """
        Formats the menu into list with three tuples, each tuple representing a meal

        returns: list with three tuples of menu items
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
