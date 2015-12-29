food=[
    ['Brunch', ["7-9am",
                 [['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast vegan', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal']]
                  ]],
    ['Lunch', ["11am-2.30pm",
                 [['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal']]
                  ]],
    ['Dinner', ["5pm-8pm",
                 [['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal'],
                  ['Breaded chicken breast tenderloid', 'veg,vgn,meat,hal']]
                  ]]
]

def convert_to_HTML(food):
    HTML=''
    print len(food)
    for i in range(len(food)):

        HTML += '<div class="row">\n'
        HTML += '<h3>' + food[i][0] + '</h3>\n'
        HTML += '<h5>' + food[i][1][0] +'</h5>\n'
        HTML += '</div>\n'

        HTML += '<div class="row"">\n'#
        HTML += '<div class="col-xs-6">\n'##
        for j in range(len(food[i][1][1])):
             HTML += '<h5>' + food[i][1][1][j][0] + '</h5>\n'
        HTML += '</div>\n'

        HTML += '<div class="col-xs-6" align="right">\n'
        for j in range(len(food[i][1][1])):
            HTML += '<h5>' + food[i][1][1][j][1] + '</h5>\n'
        HTML += '</div>\n'##
        HTML += '</div>\n'#
    print HTML

convert_to_HTML(food)