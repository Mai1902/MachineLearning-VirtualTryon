'''Lipstick reccomendation based on client's chosen color after virtual tryon'''
def lipstick_rec():
    print("What color code do you think you like the most?"
        + "\n1. Punch - #dc3753" + "\n2. Rose - #e56d7e"
        + "\n3. Brick red - #8b160e" + "\n4. Dusty rose - #b8696a"
        + "\n5. Nude - 	#ccac9e" + "\n6. Royal blue - #313456")

    color_choice = input()
    if color_choice == '1':
        print("List of lipstick share the same color code with your desired color are:"
        + "\n1. Drug store option: L'Oreal Paris Colour Riche Original Satin Lipstick For Moisturized Lips - 810 Sandstone"
        + "\n2. Mid-end option: MAC Lipstick Cream - Creme in Your Coffee"
        + "\n3. High-end option: YSL - ROUGE VOLUPTÉ SHINE LIPSTICK BALM")
    elif color_choice == '2':
        print("List of lipstick share the same color code with your desired color are:"
        + "\n1. Drug store option: Milani Color Statement Lipstick - Naturally Chic"
        + "\n2. Mid-end option: Clinique Dramatically Different Lipstick Shaping Lip Colour - 26 Vintage"
        + "\n3. High-end option: CHANEL ROUGE COCO - 432 Cecile")
    elif color_choice == '3':
        print("List of lipstick share the same color code with your desired color are:"
        + "\n1. Drug store option: Revlon Super Lustrous Lipstick - Gold Pearl Plum (610)"
        + "\n2. Mid-end option: NARS INTRIGUE - Scarlet red"
        + "\n3. High-end option: Lancome L'Absolu Rouge Lipstick - 238 Luxe")
    elif color_choice == '4':
        print("List of lipstick share the same color code with your desired color are:"
        + "\n1. Drug store option: e.l.f. Sheer Slick Lipstick - Black Cherry 82158 "
        + "\n2. Mid-end option: Estee Lauder Pure Color Envy Sculpting Lipstick - Inescapable"
        + "\n3. High-end option: Dior 999 Velvet Rouge")
    elif color_choice == '5':
        print("List of lipstick share the same color code with your desired color are:"
        + "\n1. Drug store option: Maybelline - Midnight Blue"
        + "\n2. Mid-end option: M·A·C Lipstick - Mehr"
        + "\n3. High-end option: Charlotte Tilbury - Nude Kate"
        )
    else:
        print("List of lipstick share the same color code with your desired color are:"
        + "\n1. Drug store option: SEPHORA COLLECTION Natural Wonders Lipstick - Tan Lines"
        + "\n2. Mid-end option: Smashbox Always On Matte Liquid Lipstick - Stepping out"
        + "\n3. High-end option: Gucci Rouge à Lèvres Gothique Metallic Lipstick - 707 Charlotte"
        )
