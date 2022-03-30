'''Applying chosen color to lips, smoothening the application'''
import lipstick_rec as lr
import lip_detect_color as lc

"""
Color code:
1. Punch - #dc3753" - BGR = (83,55,220)
2. Rose - #e56d7e" - BGR = (126,109,229)
3. Brick red - #8b160e" - BGR = (14,22,139)
4. Dusty rose - #b8696a" - BGR = (106,105,184)
5. Nude - 	#ccac9e" - BGR = (158,172,204)
6. Royal blue - #313456" - BGR = (86,52,49)
"""


def tryon():
    '''Perform lip color tryon operation based on user's input'''
    print("What color do you want to try on:"
    + "\n1. Punch - #dc3753" + "\n2. Rose - #e56d7e"
    + "\n3. Brick red - #8b160e" + "\n4. Dusty rose - #b8696a"
    + "\n5. Nude - 	#ccac9e" + "\n6. Royal blue - #313456")

    color_choice = input()
    if color_choice == "1":
        lc.coloring_lip(imgOriginal,lmPoints,83,55,220)
    elif color_choice == "2":
        lc.coloring_lip(imgOriginal,lmPoints,126,109,229)
    elif color_choice == "3":
        lc.coloring_lip(imgOriginal,lmPoints,14,22,139)
    elif color_choice == "4":
        lc.coloring_lip(imgOriginal,lmPoints,106,105,184)
    elif color_choice == "5":
        lc.coloring_lip(imgOriginal,lmPoints,158,172,204)
    elif color_choice == "6":
        lc.coloring_lip(imgOriginal,lmPoints,86,52,49)
    else:
        print("Please enter a valid option from 1 to 6")

    print("Do you want to try on more color? (y/n)")
    ans = input()

    if ans == 'y':
        tryon()

if __name__ == '__main__':
    print("Please enter the file path to the image you want to try on lipstick:")
    file_path = input()
    imgOriginal = lc.read_image(file_path)
    img = lc.read_image(file_path)
    lmPoints = lc.get_lip_landmark(img)
    tryon()
    lr.lipstick_rec()
