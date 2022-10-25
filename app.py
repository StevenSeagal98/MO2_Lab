# Nate Orona

# Dean's List Calc - app.py

# This program will utilize user input to calculate whether a 
# student will be added to the Dean's List or Honor's List.
# It will execute in a loop until the user enters "ZZZ" as the last name

def which_list():
    break_loop = False;
    l_name = 'Dudley'
    while (break_loop == False):
        l_name = input('Enter your last name, enter ZZZ to exit ');
        if (l_name == 'ZZZ'):
            break;
        else:
            f_name = input('Enter your first name ');
            gpa = float(input('Enter your gpa '));
            if (gpa >= 3.5 ):
                print(f"{l_name} made the Dean's list");
            elif (gpa < 3.25):
                print('Neither');
            else:
                print(f"{f_name} {l_name} made the Honor's list");

which_list();
