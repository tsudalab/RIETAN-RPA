## Definition of pictures

OPT_PARA_ICON="OPT_PARA_ICON.png"
OPT_PARA_WINDOW="OPT_PARA_WINDOW.png"
COMBO_ICON = "COMBO_ICON.png"
COMMAND_PROMPT_ICON = "COMMAND_PROMPT_ICON.png"
COMMAND_PROMPT_WINDOW = "COMMAND_PROMPT_WINDOW.png"
NEXT_POINT_STRING = "NEXT_POINT_STRING.png"
DATA_CSV_ICON = "DATA_CSV_ICON.png"
DATA_ICON = "DATA_ICON.png"
DATA_CSV_WINDOW = "DATA_CSV_WINDOW.png"
DATA_CSV_COFIRMATION_WINDOW = "DATA_CSV_COFIRMATION_WINDOW.png"
COMMAND_PROMPT_MINIMUM_BUTTON = "COMMAND_PROMPT_MINIMUM_BUTTON.png"
TARGET_INS_ICON = "TARGET_INS_ICON.png"
TARGET_INS_WINDOW = "TARGET_INS_WINDOW.png"
EDIT_MENU = "EDIT_MENU.png"
CANCEL_BUTTON = "CANCEL_BUTTON.png"
RIETAN_BAT_ICON = "RIETAN_BAT_ICON.png"
TARGET_LST_ICON = "TARGET_LST_ICON.png"
TARGET_LST_WINDOW = "TARGET_LST_WINDOW.png"
NOT_FOUND_DIALOG = "NOT_FOUND_DIALOG.png"
NOT_FOUND_REL = "NOT_FOUND_REL.png"

RESULT_ICON = "RESULT_ICON.png"
RESULT_WINDOW = "RESULT_WINDOW.png"

RESULT_OPT_ICON = "RESULT_OPT_ICON.png"
RESULT_OPT_WINDOW = "RESULT_OPT_WINDOW.png"


## import
import math

## Number of cycles
LOOP_COUNT = 10


## Minimize command prompt window when starting SikuliX
click(COMMAND_PROMPT_MINIMUM_BUTTON)

## Show start message
popup(u"Start: profile paraemters determination")



### 0. Enter initial parameters

## 0.1. Get initial values from "opt_para.txt"

# Open "opt_para.txt" in Notepad
rightClick(OPT_PARA_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)

wait(OPT_PARA_WINDOW, 3)
    
# Copy parameter lines
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

# Get values
splitted = text.split()
score_max = splitted[0]
U_opt = splitted[1]
V_opt = splitted[2]
W_opt = splitted[3]
a0_opt = splitted[4]
a1_opt = splitted[5]
a2_opt = splitted[6]
eta_L0_opt = splitted[7]
eta_L1_opt = splitted[8]
eta_H0_opt = splitted[9]
eta_H1_opt = splitted[10]

type(Key.F4, Key.ALT)



### 1. Iterations

loop_num = 0
while loop_num < LOOP_COUNT:
    loop_num += 1


    ## 1.1. Run COMBO.exe

    # Launch command prompt    
    doubleClick(COMMAND_PROMPT_ICON)
   
    # Wait until the command prompt appears
    wait(COMMAND_PROMPT_WINDOW, 5);
   
    # Drag and drop "COMBO.exe" to the command prompt
    dragDrop(COMBO_ICON,COMMAND_PROMPT_WINDOW)
    click(COMMAND_PROMPT_WINDOW) 
    sleep(1)
   
    # Press enter to execute
    type(Key.ENTER)    
    sleep(1)    
    type(Key.ENTER)    
    sleep(1)    
    type(Key.ENTER)
   
   
    ## 1.2. Check results by COMBO.exe
   
    # Wait for the result to appear in the command prompt
    while not exists(NEXT_POINT_STRING):        
       wait(1)    
       
    # Copy all strings on command prompt to the clipboard
    type('a', Key.CTRL)    
    sleep(1)    
    type('c', Key.CTRL)
   
    # Get string from clipboard    
    text = App.getClipboard()
   
    # Get "Next Point" and "Row Number"
    splitted = text.splitlines()    
    sp_count = len(splitted)    
    items = splitted[sp_count-1].split()

    if items[2] == "[":
        next_point1 = items[3]
        next_point2 = items[4]
        next_point3 = items[5]

        if items[7] == "]":
            next_point4=items[6]
            row_number = items[10]
        else:
            str_count = len(items[6])    
            next_point4 = items[6][:str_count-1]    
            row_number = items[9]

    else:
    
        next_point1 = items[2][1:]
        next_point2 = items[3]
        next_point3 = items[4]
    
        if items[6] == "]":
            next_point4=items[5]
            row_number = items[9]
        else:
            str_count = len(items[5])    
            next_point4 = items[5][:str_count-1]    
            row_number = items[8]


    next_point1=str(10**math.fabs(float(next_point1))*0.0001*float(next_point1)/math.fabs(float(next_point1)))
    next_point2=str(10**math.fabs(float(next_point2))*0.0001*float(next_point2)/math.fabs(float(next_point2)))
    next_point3=str(10**math.fabs(float(next_point3))*0.0001*float(next_point3)/math.fabs(float(next_point3)))
    next_point4=str(10**math.fabs(float(next_point4))*0.0001*float(next_point4)/math.fabs(float(next_point4)))


    # Close command prompt 
    click(COMMAND_PROMPT_WINDOW)    
    type(Key.F4, Key.ALT)   
   
    # Wait until command prompt closes
    while exists(NEXT_POINT_STRING):        
       wait(1)

    U_ini = next_point1
    V_ini = next_point2 
    W_ini = next_point3

    a0_ini = next_point4
    a1_ini = next_point4
    a2_ini = str(-float(next_point4))

    eta_L0_ini = next_point4
    eta_L1_ini = next_point4
    eta_H0_ini = next_point4
    eta_H1_ini = next_point4


    ## 1.3. Calculate properties corresponding to Next point

    # Open "Target.ins" in Notepad
    rightClick(TARGET_INS_ICON)
    wait(EDIT_MENU, 3)
    click(EDIT_MENU)

    # Search for "FWHM12"
    wait(TARGET_INS_WINDOW, 3)
    type('f', Key.CTRL)
    sleep(1)
    type('FWHM12')
    type(Key.ENTER)
    sleep(1)
    click(CANCEL_BUTTON)
    sleep(1)
    
    # Copy parameter lines
    type(Key.DOWN, Key.SHIFT)
    type('c', Key.CTRL)
    
    # Get string from clipboard
    text = App.getClipboard()

    # Values of U, V, and W are changed
    splitted = text.split()
    splitted[1] = U_ini
    splitted[2] = V_ini
    splitted[3] = W_ini
    new_text = '  '.join(splitted)
    type(new_text)
    type(Key.ENTER)
    sleep(1)


    # Search for "ASYM12"
    type('f', Key.CTRL)
    sleep(1)
    type('ASYM12')
    type(Key.ENTER)
    sleep(1)
    click(CANCEL_BUTTON)
    sleep(1)
    
    # Copy parameter lines
    type(Key.DOWN, Key.SHIFT)
    type('c', Key.CTRL)
    
    # Get string from clipboard
    text = App.getClipboard()

    # Values of a0, a1, and a2 are changed
    splitted = text.split()
    splitted[1] = a0_ini
    splitted[2] = a1_ini
    splitted[3] = a2_ini
    new_text = '  '.join(splitted)
    type(new_text)
    type(Key.ENTER)
    sleep(1)


    # Search for "ETA12"
    type('f', Key.CTRL)
    sleep(1)
    type('ETA12')
    type(Key.ENTER)
    sleep(1)
    click(CANCEL_BUTTON)
    sleep(1)
    
    # Copy parameter lines
    type(Key.DOWN, Key.SHIFT)
    type('c', Key.CTRL)
    
    # Get string from clipboard
    text = App.getClipboard()

    # Values of eta_L0, eta_L1, eta_H0, and eta_H1 are changed
    splitted = text.split()
    splitted[1] = eta_L0_ini
    splitted[2] = eta_L1_ini
    splitted[3] = eta_H0_ini
    splitted[4] = eta_H1_ini
    new_text = '  '.join(splitted)
    type(new_text)
    type(Key.ENTER)


    # Save and exit    
    type('s', Key.CTRL)    
    sleep(1)    
    type(Key.F4, Key.ALT)


    
    # Launch command prompt    
    doubleClick(COMMAND_PROMPT_ICON)
    
    # Wait until the command prompt appears
    wait(COMMAND_PROMPT_WINDOW, 5);
    
    # Move execution directory
    type('cd ')
    dragDrop(RIETAN_BAT_ICON,COMMAND_PROMPT_WINDOW)
    click(COMMAND_PROMPT_WINDOW) 
    sleep(1)
    for i in range(10):
        type(Key.BACKSPACE)
    sleep(1)
    type(Key.ENTER)
    
    # Run RIETAN
    type('RIETAN.bat Target')
    sleep(1)
    type(Key.ENTER)
    
    # Wait until the command prompt closes
    waitVanish(COMMAND_PROMPT_WINDOW, FOREVER)
    sleep(3)



    ## 1.4. Get Results

    # Open "Target.lst" in Notepad
    rightClick(TARGET_LST_ICON)
    click(EDIT_MENU)
    
    # Search for "Final parameters and their estimated standard uncertainties"
    wait(TARGET_LST_WINDOW, 3)
    type('f', Key.CTRL)
    type('Final parameters and their estimated standard uncertainties')
    type(Key.ENTER)
    sleep(1)

    # If not found
    if exists(NOT_FOUND_REL):
        sleep(1)
        type(Key.ENTER)
        click(CANCEL_BUTTON)
        sleep(1)
        score = '-100'

    # If found
    else:

        click(CANCEL_BUTTON)
        sleep(1)

        # Search for "FWHM parameter, U"
        type('f', Key.CTRL)
        type('FWHM parameter, U')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()
        U = splitted[1]


        # Search for "FWHM parameter, V"
        type('f', Key.CTRL)
        type('FWHM parameter, V')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()
        V = splitted[1]

        
        # Search for "FWHM parameter, W"
        type('f', Key.CTRL)
        type('FWHM parameter, W')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()
        W = splitted[1]


        # Search for "Asymmetry parameter, a0"
        type('f', Key.CTRL)
        type('Asymmetry parameter, a0')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()
        a0 = splitted[1]


        # Search for "Asymmetry parameter, a1"
        type('f', Key.CTRL)
        type('Asymmetry parameter, a1')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()
        a1 = splitted[1]


        # Search for "Asymmetry parameter, a2"
        type('f', Key.CTRL)
        type('Asymmetry parameter, a2')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()
        a2 = splitted[1]


        # Search for "Mixing parameter, eta_L0"
        type('f', Key.CTRL)
        type('Mixing parameter, eta')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()
        eta_L0 = splitted[1]

        type(Key.DOWN)


        # Search for "Mixing parameter, eta_L1"
        type('f', Key.CTRL)
        type('Mixing parameter, eta')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.RIGHT, Key.SHIFT)
        type(Key.RIGHT, Key.SHIFT)
        type(Key.RIGHT, Key.SHIFT)
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()

        
        # Get values
        splitted = text.split()
        eta_L1 = splitted[1]

        type(Key.DOWN)


        # Search for "Mixing parameter, eta_H0"
        type('f', Key.CTRL)
        type('Mixing parameter, eta')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.RIGHT, Key.SHIFT)
        type(Key.RIGHT, Key.SHIFT)
        type(Key.RIGHT, Key.SHIFT)
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()
        eta_H0 = splitted[1]

        type(Key.DOWN)
        

        # Search for "Mixing parameter, eta_H1"
        type('f', Key.CTRL)
        type('Mixing parameter, eta')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)
        
        # Copy parameter lines
        type(Key.RIGHT, Key.SHIFT)
        type(Key.RIGHT, Key.SHIFT)
        type(Key.RIGHT, Key.SHIFT)
        type(Key.UP, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()
        eta_H1 = splitted[1]


        # Search for "Rwp"
        type('f', Key.CTRL)
        type('Rwp')
        type(Key.ENTER)
        sleep(1)

        click(CANCEL_BUTTON)
        sleep(1)


        # Copy parameter lines
        type(Key.DOWN, Key.SHIFT)
        type('c', Key.CTRL)
        
        # Get string from clipboard
        text = App.getClipboard()
        
        # Get values
        splitted = text.split()

        if splitted[2] == "Rp":
            score = '-' + str(float(splitted[1][1:]))

        else:
            score = '-' + str(float(splitted[2]))
 

        # If the smallest Rwp was obtained
        if float(score) > float(score_max):
            U_opt=U
            V_opt=V
            W_opt=W
            a0_opt=a0
            a1_opt=a1
            a2_opt=a2
            eta_L0_opt=eta_L0
            eta_L1_opt=eta_L1
            eta_H0_opt=eta_H0
            eta_H1_opt=eta_H1

            score_max=score
        

    
    # Close the file
    sleep(1)
    type(Key.F4, Key.ALT)
    


    ## 1.4. Open Excel and add data    
   
    # Open data.csv
    doubleClick(DATA_CSV_ICON) 
   
    # Wait for data.csv to open
    wait(DATA_CSV_WINDOW, 10)   

    # Jump to specified line
    type('g',Key.CTRL)
    target = 'A' + row_number   
    type(target)
    type(Key.ENTER)

   
    # Input values
    type(score)
   
    # Save and exit    
    type('s', Key.CTRL)    
    sleep(1)    
    type(Key.F4, Key.ALT)
    
    # Close the confirmation dialog
    if exists(DATA_CSV_COFIRMATION_WINDOW):
        type(Key.ENTER)
        type(Key.F4, Key.ALT)

    sleep(2)



    ## 1.5. Write the results in "result.txt"

    # Open "result.txt" in Notepad
    rightClick(RESULT_ICON)
    wait(EDIT_MENU, 3)
    click(EDIT_MENU)

    wait(RESULT_WINDOW, 3)

    type('a',Key.CTRL)
    type(Key.DOWN)

    type(Key.ENTER)

    new_text = score + '  ' + U_ini + '  ' + V_ini + '  ' + W_ini + '  ' + a0_ini + '  ' + a1_ini + '  ' + a2_ini + '  ' + eta_L0_ini + '  ' + eta_L1_ini + '  ' + eta_H0_ini + '  ' + eta_H1_ini

    type(new_text)

    type(Key.F4, Key.ALT)

    sleep(1)
    type(Key.ENTER)
    

    if score != '-100':

        # Open "result_opt.txt" in Notepad
        rightClick(RESULT_OPT_ICON)
        wait(EDIT_MENU, 3)
        click(EDIT_MENU)

        wait(RESULT_OPT_WINDOW, 3)

        type('a',Key.CTRL)
        type(Key.DOWN)

        type(Key.ENTER)

        new_text = score + '  ' + U + '  ' + V + '  ' + W + '  ' + a0 + '  ' + a1 + '  ' + a2 + '  ' + eta_L0 + '  ' + eta_L1 + '  ' + eta_H0 + '  ' + eta_H1

        type(new_text)

        type(Key.F4, Key.ALT)

        sleep(1)
        type(Key.ENTER)



### 2. Output optimized parameters

# Open "opt_para.txt" in Notepad
rightClick(OPT_PARA_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)

wait(OPT_PARA_WINDOW, 3)
    
# Copy parameter lines
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

splitted = text.split()
splitted[0] = score_max
splitted[1] = U_opt
splitted[2] = V_opt
splitted[3] = W_opt
splitted[4] = a0_opt
splitted[5] = a1_opt
splitted[6] = a2_opt
splitted[7] = eta_L0_opt
splitted[8] = eta_L1_opt
splitted[9] = eta_H0_opt
splitted[10] = eta_H1_opt
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)

type(Key.F4, Key.ALT)

sleep(1)
type(Key.ENTER)



## Show finish message
popup(u"Finish")
