class detect_setting:
    def __init__(self):
        self.handlen = 14

        self.filepath = [
                        'tmpl/man0','tmpl/man1','tmpl/man2','tmpl/man3','tmpl/man4','tmpl/man5','tmpl/man6','tmpl/man7','tmpl/man8','tmpl/man9',
                        'tmpl/pin0','tmpl/pin1','tmpl/pin2','tmpl/pin3','tmpl/pin4','tmpl/pin5','tmpl/pin6','tmpl/pin7','tmpl/pin8','tmpl/pin9',
                        'tmpl/sou0','tmpl/sou1','tmpl/sou2','tmpl/sou3','tmpl/sou4','tmpl/sou5','tmpl/sou6','tmpl/sou7','tmpl/sou8','tmpl/sou9',
                        'tmpl/_emp','tmpl/ton_','tmpl/nan_','tmpl/sha_','tmpl/pe__','tmpl/haku','tmpl/hatu','tmpl/chun','tmpl/_emp','tmpl/_emp'
                        ]
        
        self.threshold = [
                        0.8,0.6,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.6,
                        0.8,0.7,0.8,0.8,0.8,0.6,0.8,0.8,0.8,0.5,
                        0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.6,
                        0.8,0.8,0.6,0.6,0.8,0.8,0.8,0.8,0.6,0.6
                        ]
        
        self.rectgbr = {
                        0: (0, 0, 255), 1: (255, 0, 0), 2: (255, 0, 0), 3: (255, 0, 0),
                        4: (255, 0, 0), 5: (255, 0, 0), 6: (255, 0, 0), 7: (255, 0, 0),
                        8: (255, 0, 0), 9: (255, 0, 0), 10: (0, 0, 255), 11: (128, 0, 128),
                        12: (128, 0, 128), 13: (128, 0, 128), 14: (128, 0, 128), 15: (128, 0, 128),
                        16: (128, 0, 128), 17: (128, 0, 128), 18: (128, 0, 128), 19: (128, 0, 128),
                        20: (0, 0, 255), 21: (0, 255, 0), 22: (0, 255, 0), 23: (0, 255, 0),
                        24: (0, 255, 0), 25: (0, 255, 0), 26: (0, 255, 0), 27: (0, 255, 0),
                        28: (0, 255, 0), 29: (0, 255, 0), 30: (0, 0, 255), 31: (0, 165, 255),
                        32: (0, 165, 255), 33: (0, 165, 255), 34: (0, 165, 255), 35: (0, 165, 255),
                        36: (0, 255, 0), 37: (0, 0, 255), 38: (0, 165, 255), 39: (0, 165, 255),
                        40: (0, 165, 255)
                        }
        
        self.skippx = 100

        self.hand_windowsize = 1500

class cam_setting:
    def __init__(self):
        #self.url = 'https://192.168.1.92:8080/video'
        self.url = 'https://10.140.132.171:8080/video'
        self.cam_ratio = [16,9,50,75]
        self.gridcolor = (255,255,255)

        self.cliplimit = 0.9

class tile_setting:
    def __init__(self):
        self.yaochu = [1,9,11,19,21,29,31,32,33,34,35,36,37]
        self.wind = [31,32,33,34]
        self.sangen = [35,36,37]

"""
class hand_setting:
    def __init__(self):
        self.tilenum = list(range(40))
        self.mt_tiles = [
                         1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,
                         11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15,15,15,16,16,16,16,17,17,17,17,18,18,18,18,19,19,19,19,
                         21,21,21,21,22,22,22,22,23,23,23,23,24,24,24,24,25,25,25,25,26,26,26,26,27,27,27,27,28,28,28,28,29,29,29,29,
                         31,31,31,31,32,32,32,32,33,33,33,33,34,34,34,34,35,35,35,35,36,36,36,36,37,37,37,37
                        ]
        self.valid_liangmian = [3,4,5,6,7,
                                13,14,15,16,17,
                                23,24,25,26,27]
        self.isolate_grade = [[1, 9, 11, 19, 21, 29],[2, 8, 12, 18, 22, 28],[3, 7, 13, 17, 23, 27]]
        self.kokushi_tiles = {1, 9, 11, 19, 21, 29, 31, 32, 33, 34, 35, 36, 37}
        self.tile_emoji = [
                        "🀝", "🀙", "🀚", "🀛", "🀜", "🀝", "🀞", "🀟", "🀠", "🀡",
                        "🀋", "🀇", "🀈", "🀉", "🀊", "🀋", "🀌", "🀍", "🀎", "🀏",
                        "🀔", "🀐", "🀑", "🀒", "🀓", "🀔", "🀕", "🀖", "🀗", "🀘",
                        " ", "🀀", "🀁", "🀂", "🀃", "🀆", "🀅", "🀄"," "," "
                        ]
"""

    

detect_const = detect_setting()
cam_const = cam_setting()
tile_const = tile_setting()

#hand_const = hand_setting()