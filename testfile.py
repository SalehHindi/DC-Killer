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