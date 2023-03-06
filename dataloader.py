import csv

fields = ['id', 'name', 'element', 'weapon', 'body_type', 'region', 'rarity', 'version']

# anemo-0, geo-1, electro-2, dendro-3, hydro-4, pyro-5, cryo-6
elements = ['anemo', 'geo', 'electro', 'dendro', 'hydro', 'pyro', 'cryo']
# mondstadt-0, liyue-1, inazuma-2, sumeru-3, fontaine-4, natlan-5, snezhnaya-6
regions = ['Mondstadt', 'Liyue', 'Inazuma', 'Sumeru', 'Fontaine', 'Natlan', 'Snezhnaya']
# sword-0, claymore-1, polearm-2, bow-3, catalyst-4
weapons = ['sword', 'claymore', 'polearm', 'bow', 'catalyst']
# sf-0, mf-1, mm-2, tf-3, tm-4
body_types = ['small_female', 'medium_female', 'medium_male', 'tall_female', 'tall_male']
rarities = ['4', '5']
versions = [
    # 0     1       2       3       4   5       6
    '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', # 0-6
    # 7     8       9       10      11  12      13      14  15 
    '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', # 7-15
    # 16    17      18      19      20  21      22
    '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6' # 16-22
    ]

characters = [
    [0, 'Amber', elements[5], weapons[3], body_types[1], regions[0], rarities[0], versions[0]],
    [1, 'Kaeya', elements[6], weapons[0], body_types[4], regions[0], rarities[0], versions[0]],
    [2, 'Lisa', elements[2], weapons[4], body_types[3], regions[0], rarities[0], versions[0]],
    [3, 'Barbara', elements[4], weapons[4], body_types[1], regions[0], rarities[0], versions[0]],
    [4, 'Razor', elements[2], weapons[1], body_types[2], regions[0], rarities[0], versions[0]],
    [5, 'Xiangling', elements[5], weapons[2], body_types[1], regions[1], rarities[0], versions[0]],
    [6, 'Beidou', elements[2], weapons[1], body_types[3], regions[1], rarities[0], versions[0]],
    [7, 'Xingqiu', elements[4], weapons[0], body_types[2], regions[1], rarities[0], versions[0]],
    [8, 'Ningguang', elements[1], weapons[4], body_types[3], regions[1], rarities[0], versions[0]],
    [9, 'Fischl', elements[2], weapons[3], body_types[1], regions[0], rarities[0], versions[0]],
    [10, 'Bennett', elements[5], weapons[0], body_types[2], regions[0], rarities[0], versions[0]],
    [11, 'Noelle', elements[1], weapons[1], body_types[1], regions[0], rarities[0], versions[0]],
    [12, 'Chongyun', elements[6], weapons[1], body_types[2], regions[1], rarities[0], versions[0]],
    [13, 'Sucrose', elements[0], weapons[4], body_types[1], regions[0], rarities[0], versions[0]],
    [14, 'Jean', elements[0], weapons[0], body_types[3], regions[0], rarities[1], versions[0]],
    [15, 'Diluc', elements[5], weapons[1], body_types[4], regions[0], rarities[1], versions[0]],
    [16, 'Qiqi', elements[6], weapons[0], body_types[0], regions[1], rarities[1], versions[0]],
    [17, 'Mona', elements[4], weapons[4], body_types[1], regions[0], rarities[1], versions[0]],
    [18, 'Keqing', elements[2], weapons[0], body_types[1], regions[1], rarities[1], versions[0]],
    [19, 'Venti', elements[0], weapons[3], body_types[2], regions[0], rarities[1], versions[0]],
    [20, 'Klee', elements[5], weapons[4], body_types[0], regions[0], rarities[1], versions[0]],
    [21, 'Diona', elements[6], weapons[3], body_types[0], regions[0], rarities[0], versions[1]],
    [22, 'Tartaglia', elements[4], weapons[3], body_types[4], regions[6], rarities[1], versions[1]],
    [23, 'Xinyan', elements[5], weapons[1], body_types[1], regions[1], rarities[0], versions[1]],
    [24, 'Zhongli', elements[1], weapons[2], body_types[4], regions[1], rarities[1], versions[1]],
    [25, 'Albedo', elements[1], weapons[0], body_types[2], regions[0], rarities[1], versions[2]],
    [26, 'Ganyu', elements[6], weapons[3], body_types[1], regions[1], rarities[1], versions[2]],
    [27, 'Xiao', elements[0], weapons[2], body_types[2], regions[1], rarities[1], versions[3]],
    [28, 'Hutao', elements[5], weapons[2], body_types[1], regions[1], rarities[1], versions[3]],
    [29, 'Rosaria', elements[6], weapons[2], body_types[3], regions[0], rarities[0], versions[4]],
    [30, 'Yanfei', elements[5], weapons[4], body_types[1], regions[1], rarities[0], versions[5]],
    [31, 'Eula', elements[6], weapons[1], body_types[3], regions[0], rarities[1], versions[5]],
    [32, 'Kazuha', elements[0], weapons[0], body_types[2], regions[2], rarities[1], versions[6]],
    [33, 'Kamisato_Ayaka', elements[6], weapons[0], body_types[1], regions[2], rarities[1], versions[7]],
    [34, 'Sayu', elements[0], weapons[1], body_types[0], regions[2], rarities[0], versions[7]],
    [35, 'Yoimiya', elements[5], weapons[3], body_types[1], regions[2], rarities[1], versions[7]],
    # [36, 'Aloy', elements[6], weapons[3], body_types[1], regions[1], rarities[1], versions[0]],
    [37, 'Kujou_Sara', elements[2], weapons[3], body_types[3], regions[2], rarities[0], versions[8]],
    [38, 'Raiden_Shogun', elements[2], weapons[2], body_types[3], regions[2], rarities[1], versions[8]],
    [39, 'Sangonomiya_Kokomi', elements[4], weapons[4], body_types[1], regions[2], rarities[1], versions[8]],
    [40, 'Thoma', elements[5], weapons[2], body_types[4], regions[2], rarities[0], versions[9]],
    [41, 'Gorou', elements[1], weapons[3], body_types[2], regions[2], rarities[0], versions[10]],
    [42, 'Arataki_Itto', elements[1], weapons[1], body_types[4], regions[2], rarities[1], versions[10]],
    [43, 'Yunjin', elements[1], weapons[2], body_types[1], regions[1], rarities[0], versions[11]],
    [44, 'Shenhe', elements[6], weapons[2], body_types[3], regions[1], rarities[1], versions[11]],
    [45, 'Yae Miko', elements[2], weapons[4], body_types[3], regions[2], rarities[1], versions[12]],
    [46, 'Kamisato_Ayato', elements[4], weapons[0], body_types[4], regions[2], rarities[1], versions[13]],
    [47, 'Yelan', elements[4], weapons[3], body_types[3], regions[1], rarities[1], versions[14]],
    [48, 'Kuki_Shinobu', elements[2], weapons[0], body_types[1], regions[2], rarities[0], versions[14]],
    [49, 'Shikanoin_Heizou', elements[0], weapons[4], body_types[2], regions[2], rarities[0], versions[15]],
    [50, 'Collei', elements[3], weapons[3], body_types[1], regions[3], rarities[0], versions[16]],
    [51, 'Tighnari', elements[3], weapons[3], body_types[2], regions[3], rarities[1], versions[16]],
    [52, 'Dori', elements[2], weapons[1], body_types[0], regions[3], rarities[0], versions[16]],
    [53, 'Candace', elements[4], weapons[2], body_types[3], regions[3], rarities[0], versions[17]],
    [54, 'Cyno', elements[2], weapons[2], body_types[2], regions[3], rarities[1], versions[17]],
    [55, 'Nilou', elements[4], weapons[0], body_types[1], regions[3], rarities[1], versions[17]],
    [56, 'Nahida', elements[3], weapons[4], body_types[0], regions[3], rarities[1], versions[18]],
    [57, 'Layla', elements[6], weapons[0], body_types[1], regions[3], rarities[0], versions[18]],
    [58, 'Faruzan', elements[0], weapons[3], body_types[1], regions[3], rarities[0], versions[19]],
    [59, 'Wanderer', elements[0], weapons[4], body_types[2], regions[3], rarities[1], versions[19]],
    [60, 'Yaoyao', elements[3], weapons[2], body_types[0], regions[1], rarities[0], versions[20]],
    [61, 'Alhaitham', elements[3], weapons[0], body_types[4], regions[3], rarities[1], versions[20]],
    [62, 'Dehya', elements[5], weapons[1], body_types[3], regions[3], rarities[1], versions[21]],
    # [63, 'Mika', elements[6], weapons[2], body_types[2], regions[0], rarities[0], versions[21]],
    # [64, 'Baizhu', elements[3], weapons[4], body_types[4], regions[1], rarities[1], versions[22]],
    # [65, 'Kaveh', elements[3], weapons[1], body_types[4], regions[3], rarities[0], versions[22]],
]

filename = 'characters.csv'

def create_csv():
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(characters)