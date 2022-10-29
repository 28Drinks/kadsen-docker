
# All basic traits breakdown by RollbitWhitePaper

# [ amount , odds , rlb-amount ]
import json


Background = {
    "Special": [26, 0.26, 1000000],
    "Purple": [1650, 16.50, 75000],
    "Red": [1650, 16.50, 65000],
    "Orange" : [1650, 16.50, 55000],
    "Green" : [1650, 16.50, 45000],
    "Blue" : [1650, 16.50, 35000],
    "Grey" : [1724, 17.24, 25000]
}

# [amount, odds, comboboost ]
Teeth = {
    "Special" : [26, 0.26, 1.20],
    "Golden V1 in V2 Mouth": [50, 0.50, 1.20],
    "Golden Bot Mouth" : [75, 0.75, 1.20],
    "Golden Gamepad Mouth" : [100, 1.00, 1.20],
    "Golden Moustache Mouth" : [125, 1.25, 1.19],
    "Golden Lips Mouth" : [150, 1.50, 1.19],
    "Golden Cyborg Mouth" : [200, 2.00, 1.19],
    "Golden Repaired Mouth" : [250, 2.50, 1.18],
    "Silver and Gold Mouth" : [300, 3.00, 1.18],
    "V1 in V2 Mouth" : [350, 3.50, 1.18],
    "Bot Mouth" : [400, 4.00, 1.17],
    "Gamepad Mouth" : [450, 4.50, 1.17],
    "Silver Moustache Mouth" : [500, 5.00, 1.17],
    "Silver Lips Mouth" : [550, 5.50, 1.16],
    "Silver Repaired Mouth" : [600, 6.00, 1.16],
    "Silver Mouth" : [650, 6.50, 1.16],
    "Cyborg Mouth" : [700, 7.00, 1.15],
    "Wink Mouth" : [750, 7.50, 1.15],
    "Robot Mouth" : [800, 8.00, 1.15],
    "Wink Rusted Mouth" : [850, 8.50, 1.14],
    "Happy Rusted Mouth" : [900, 9.00, 1.14],
    "Corrosion Mouth" : [1224, 12.24, 1.14]
}

# [ amount, odds, freebet-value ]
Eyes = {
    "Rollbit Glasses" : [20, 0.20, 500],
    "Special" :	[26, 0.26, 1000],
    "Golden Rollbot Glasses" : [30, 0.30, 300],
    "Special Golden Bitcoin Eyes" : [40, 0.40, 250],
    "Special Green Bitcoin Eyes" : [50, 0.50, 225],
    "Lucky 7 Glasses" : [60, 0.60, 200],
    "Special Diamond Eyes" : [70, 0.70, 190],
    "Pink Hypnotic Special Eyes" : [80, 0.80, 180],
    "Special Hypnotic Glasses" : [90, 0.90, 170],
    "Golden Globe Eyes" : [100, 1.00, 160],
    "Golden Eyes" : [110, 1.10, 150],
    "Brain Eyes" : [120, 1.20, 140],
    "Blue Rollbot Glasses" : [130, 1.30, 130],
    "Golden Bitcoin Eyes" : [140, 1.40, 120],
    "Green Bitcoin Eyes" : [150, 1.50, 110],
    "3D Glasses" : [160, 1.60, 100],
    "Diamond Eyes" : [170, 1.70, 90],
    "Aquarium Eyes" : [180, 1.80, 80],
    "Globe Eyes" : [190, 1.90, 70],
    "Hypnotic Illusion Eyes" : [200, 2.00, 70],
    "Hypnotic Eyes" : [220, 2.20, 65],
    "Start Lights Eyes" : [240, 2.40, 60],
    "Golden Cyborg Eyes" : [260, 2.60, 55],
    "VR Eyes" : [280, 2.80, 50],
    "Olympic XXL Eyes" : [300, 3.00, 48],
    "Pixel Heart Eyes" : [320, 3.20, 46],
    "Red Angry Glasses" : [340, 3.40, 44],
    "Olympic Eyes" : [360, 3.60, 42],
    "Target Eyes" : [380, 3.80, 40],
    "Red Eyes" : [400, 4.00, 38],
    "Steampunk Eyes" : [420, 4.20, 36],
    "Broken Eyes" : [440, 4.40, 34],
    "Crying Eyes" : [460, 4.60, 32],
    "Cyborg Eyes" : [480, 4.80, 30],
    "Deep Eyes" : [500, 5.00, 28],
    "Narrow Rusted Eyes" : [520, 5.20, 26],
    "Narrow Eyes" : [540, 5.40, 24],
    "Jealousy Eyes" : [560, 5.60, 22],
    "Black Eyes" : [864, 8.64, 20]
}

# [ amount, odds, sportshare ]
Body = {
    "Special" : [26, 0.26, 100],
    "Engraved Gold Skin" : [500, 5.00, 10],
    "Aqua Style Skin" : [1000, 10.00, 5],
    "Lava Skin" : [1474, 14.74, 4],
    "Electric Space Skin" : [1750, 17.50, 3],
    "Flame Ceramic Skin" : [2250, 22.50, 2],
    "Steel Skin" : [3000, 30.00, 1]
}


#ahh yes wtf is this xD
#to get it to the same format as my json request thingy gives me XD
class Traits():
    def all_trait_number():

        all_trait_list = []

        newlel = {}
        newformat = {}
        for key in Eyes:
            newformat[key] = Eyes[key] #[0]
        newlel["Eyes"] = newformat
        all_trait_list.append(newlel)

        # 4x times for the other dicts

        newlelt = {}
        newformatt = {}
        for key in Teeth:
            newformatt[key] = Teeth[key]#[0]
        newlelt["Teeth"] = newformatt
        all_trait_list.append(newlelt)


        newlelb = {}
        newformatb = {}
        for key in Body:
            newformatb[key] = Body[key]#[0]
        newlelb["Body"] = newformatb
        all_trait_list.append(newlelb)


        newlelbb = {}
        newformatbb = {}
        for key in Background:
            newformatbb[key] = Background[key]#[0]
        newlelbb["Background"] = newformatbb
        all_trait_list.append(newlelbb)


        return all_trait_list

if __name__ ==  '__main__':
    Traits.all_trait_number()



