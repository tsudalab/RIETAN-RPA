## Definition of pictures

COMMAND_PROMPT_ICON = "COMMAND_PROMPT_ICON.png"
COMMAND_PROMPT_WINDOW = "COMMAND_PROMPT_WINDOW.png"
COMMAND_PROMPT_MINIMUM_BUTTON = "COMMAND_PROMPT_MINIMUM_BUTTON.png"
TARGET_INS_ICON = "TARGET_INS_ICON.png"
EDIT_MENU = "EDIT_MENU.png"
TARGET_INS_WINDOW = "TARGET_INS_WINDOW.png"
CANCEL_BUTTON = "CANCEL_BUTTON.png"
RIETAN_BAT_ICON = "RIETAN_BAT_ICON.png"


## import
import math

## Minimize command prompt window when starting SikuliX
click(COMMAND_PROMPT_MINIMUM_BUTTON)

## Show start message
popup(u"Start: background determination")



###################################
# 1st change
###################################

# Open Target.ins in Notepad
rightClick(TARGET_INS_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)


# Search for "IHP1"
wait(TARGET_INS_WINDOW, 3)
type('f', Key.CTRL)
sleep(1)
type('IHP1 ')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)

type(Key.LEFT)

type(Key.DOWN, Key.SHIFT)
type(Key.DOWN, Key.SHIFT)
type(Key.DELETE)

paste("IHP1 = 0: ")
type(Key.ENTER)
paste("IKP1 = 1:  --> Preferred-orientation vector, hp1, kp1, lp1.")
type(Key.ENTER)
sleep(1)


# Search for "BKGD"
type('f', Key.CTRL)
sleep(1)
type('BKGD')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)
    
# Copy parameter lines
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

# Parameter is changed
splitted = text.split()
splitted[13] = "110000000000"
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)
sleep(1)


# Search for "SCALE"
wait(TARGET_INS_WINDOW, 3)
type('f', Key.CTRL)
sleep(1)
type('SCALE ')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)
    
# Copy parameter lines
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

# Parameter is changed
splitted = text.split()
splitted[2] = "1"
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)
sleep(1)


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

# Parameter is changed
splitted = text.split()
splitted[5] = "0000"
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

# Parameter is changed
splitted = text.split()
splitted[5] = "0000"
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

# Parameter is changed
splitted = text.split()
splitted[5] = "0000"
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)


# Search for "CELLQ"
wait(TARGET_INS_WINDOW, 3)
type('f', Key.CTRL)
sleep(1)
type('CELLQ')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)
    
# Copy parameter lines
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

# Parameter is changed
splitted = text.split()
splitted[8] = "1110000"
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)
sleep(1)


# Search for "NVOX"
wait(TARGET_INS_WINDOW, 3)
type('f', Key.CTRL)
sleep(1)
type('NVOXA ')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)

type(Key.LEFT)
type(Key.LEFT)
type(Key.LEFT)
type(Key.LEFT)

type(Key.DOWN, Key.SHIFT)
type(Key.DOWN, Key.SHIFT)
type(Key.DOWN, Key.SHIFT)
type(Key.DELETE)


paste("   NVOXA = 0: Number of voxels along the a axis.")
type(Key.ENTER)
paste("   NVOXB = 0: Number of voxels along the b axis.")
type(Key.ENTER)
paste("   NVOXC = 0: Number of voxels along the c axis.")
type(Key.ENTER)
sleep(1)


# Search for "NUPDT"
wait(TARGET_INS_WINDOW, 3)
type('f', Key.CTRL)
sleep(1)
type('NUPDT ')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)

type(Key.LEFT)

type(Key.DOWN, Key.SHIFT)
type(Key.DOWN, Key.SHIFT)
type(Key.DELETE)

paste("NUPDT = 0! Variable parameters (ID = 1, 2) in the input file remain unchanged.")
type(Key.ENTER)
paste("NUPDT = 1: Variable parameters (ID = 1, 2) are updated in the packing mode.")
type(Key.ENTER)
sleep(1)


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



###################################
# 2nd change
###################################

# Open Target.ins in Notepad
rightClick(TARGET_INS_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)
click(TARGET_INS_WINDOW)

# Search for "BKGD"
type('f', Key.CTRL)
sleep(1)
type('BKGD')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)
    
# Copy parameter lines
type(Key.DOWN)
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

# Parameter is changed
splitted = text.split()
splitted[-1] = "111100000000"
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)
sleep(1)

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



###################################
# 3rd change
###################################

# Open Target.ins in Notepad
rightClick(TARGET_INS_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)
click(TARGET_INS_WINDOW)

# Search for "BKGD"
type('f', Key.CTRL)
sleep(1)
type('BKGD')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)
    
# Copy parameter lines
type(Key.DOWN)
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

# Parameter is changed
splitted = text.split()
splitted[-1] = "111111000000"
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)
sleep(1)

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



###################################
# 4th change
###################################

# Open Target.ins in Notepad
rightClick(TARGET_INS_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)
click(TARGET_INS_WINDOW)

# Search for "BKGD"
type('f', Key.CTRL)
sleep(1)
type('BKGD')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)
    
# Copy parameter lines
type(Key.DOWN)
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

# Parameter is changed
splitted = text.split()
splitted[-1] = "111111110000"
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)
sleep(1)

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



###################################
# 5th change
###################################

# Open Target.ins in Notepad
rightClick(TARGET_INS_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)
click(TARGET_INS_WINDOW)

# Search for "BKGD"
type('f', Key.CTRL)
sleep(1)
type('BKGD')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)
    
# Copy parameter lines
type(Key.DOWN)
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

# Parameter is changed
splitted = text.split()
splitted[-1] = "111111111100"
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)
sleep(1)

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



###################################
# 6th change
###################################

# Open Target.ins in Notepad
rightClick(TARGET_INS_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)
click(TARGET_INS_WINDOW)

# Search for "BKGD"
type('f', Key.CTRL)
sleep(1)
type('BKGD')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)
    
# Copy parameter lines
type(Key.DOWN)
type(Key.DOWN, Key.SHIFT)
type('c', Key.CTRL)
    
# Get string from clipboard
text = App.getClipboard()

# Parameter is changed
splitted = text.split()
splitted[-1] = "111111111111"
new_text = '  '.join(splitted)
type(new_text)
type(Key.ENTER)
sleep(1)

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



###################################
# 7th change
###################################

# Open Target.ins in Notepad
rightClick(TARGET_INS_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)
click(TARGET_INS_WINDOW)


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

# Parameter is changed
splitted = text.split()
splitted[5] = "1110"
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

# Parameter is changed
splitted = text.split()
splitted[5] = "1110"
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

# Parameter is changed
splitted = text.split()
splitted[5] = "1111"
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



###################################
# 8th change
###################################

# Open Target.ins in Notepad
rightClick(TARGET_INS_ICON)
wait(EDIT_MENU, 3)
click(EDIT_MENU)
click(TARGET_INS_WINDOW)


# Search for "NUPDT"
wait(TARGET_INS_WINDOW, 3)
type('f', Key.CTRL)
sleep(1)
type('NUPDT ')
type(Key.ENTER)
sleep(1)
click(CANCEL_BUTTON)
sleep(1)

type(Key.LEFT)

type(Key.DOWN, Key.SHIFT)
type(Key.DOWN, Key.SHIFT)
type(Key.DELETE)

paste("NUPDT = 0: Variable parameters (ID = 1, 2) in the input file remain unchanged.")
type(Key.ENTER)
paste("NUPDT = 1! Variable parameters (ID = 1, 2) are updated in the packing mode.")
type(Key.ENTER)
sleep(1)

# Save and exit    
type('s', Key.CTRL)    
sleep(1)    
type(Key.F4, Key.ALT)



## Show finish message
popup(u"Finish")
