import numpy as np


class CategoryGetter:
    # 開催データ
    def getKaisaikbn(self, value):
        return self.categories(3, value)

    def getDayofweek(self, dayofweek):
        dayofweek_d = np.zeros([7])
        if dayofweek == "日":
            dayofweek_d[0] = 1
        elif dayofweek == "月":
            dayofweek_d[1] = 1
        elif dayofweek == "火":
            dayofweek_d[2] = 1
        elif dayofweek == "水":
            dayofweek_d[3] = 1
        elif dayofweek == "木":
            dayofweek_d[4] = 1
        elif dayofweek == "金":
            dayofweek_d[5] = 1
        elif dayofweek == "土":
            dayofweek_d[6] = 1
        return dayofweek_d

    def getTenko(self, value):
        return self.categories(6, value)

    def getBabaabst(self, value):
        return self.categories(4, value)

    def getBabadetail(self, baba):
        return self.categories(3, baba)

    def getTurfkind(self, kind):
        return self.categories(3, kind)

    def getTennatsu(self, ten):
        return self.categories(2, ten)

    def getStopfreeze(self, st):
        return self.categories(2, st)

    # 番組データ
    def getDistance(self, dis):
        dis_d = np.zeros([13])
        if dis == 1000:
            dis_d[0] = 1
        elif dis > 1000 and dis <= 1200:
            dis_d[1] = 1
        elif dis > 1200 and dis <= 1400:
            dis_d[2] = 1
        elif dis > 1400 and dis <= 1600:
            dis_d[3] = 1
        elif dis > 1600 and dis <= 1800:
            dis_d[4] = 1
        elif dis > 1800 and dis <= 2000:
            dis_d[5] = 1
        elif dis > 2000 and dis <= 2200:
            dis_d[6] = 1
        elif dis > 2200 and dis <= 2400:
            dis_d[7] = 1
        elif dis > 2400 and dis <= 2500:
            dis_d[8] = 1
        elif dis > 2500 and dis <= 3000:
            dis_d[9] = 1
        elif dis > 3000 and dis <= 3200:
            dis_d[10] = 1
        elif dis > 3000 and dis <= 3200:
            dis_d[11] = 1
        else:
            dis_d[12] = 1
        return dis_d

    def getTdscode(self, tds):
        return self.categories(3, tds)

    def getRightleft(self, rl):
        return self.categories(4, rl)

    def getInout(self, inout):
        return self.categories(4, inout)

    def getShubetsu(self, s):
        return self.categories(5, s)

    def getJoken(self, j):
        j_d = np.zeros([11])
        if j == "04":
            j_d[0] = 1
        elif j == "05":
            j_d[1] = 1
        elif j == "08":
            j_d[2] = 1
        elif j == "09":
            j_d[3] = 1
        elif j == "10":
            j_d[4] = 1
        elif j == "15":
            j_d[5] = 1
        elif j == "16":
            j_d[6] = 1
        elif j == "A1":
            j_d[7] = 1
        elif j == "A2":
            j_d[8] = 1
        elif j == "A3":
            j_d[9] = 1
        elif j == "OP":
            j_d[10] = 1
        return j_d

    def getJuryo(self, j):
        return self.categories(4, j)

    def getGrade(self, g):
        return self.categories(5, g)

    def getCourse(self, c):
        return self.categories(5, c)

    # WORKTABLEデータ
    # 汎用メソッド利用
    def getNum(self, num):
        return self.categories(18, num)

    def getLegtype(self, leg_type):
        return self.categories(7, int(leg_type))

    def getOmotekiseicode(self, omotekisei_code):
        return self.categories(4, omotekisei_code)

    def getBrinkers(self, brinkers):
        return self.categories(4, brinkers)

    def getMinarai(self, minarai):
        return self.categories(4, minarai)

    def getWaku(self, waku):
        return self.categories(8, waku)

    def getTurfadjustcode(self, turf_adjust_code):
        return self.categories(5, turf_adjust_code)

    def getTorikeshi(self, torikeshi):
        return self.categories(2, torikeshi)

    def getSex(self, sex):
        return self.categories(3, sex)

    def getBanushikaicode(self, banushikai_code):
        return self.getElevencat(banushikai_code)

    def getYuso(self, yuso):
        return self.categories(5, yuso)

    def getKokyuflg(self, kokyu_flg):
        return self.categories(3, kokyu_flg)

    def getTurfdartsteepleflg(self, turf_dart_steeple_flg):
        return self.categories(3, turf_dart_steeple_flg)

    def getDistanceflg(self, distance_flg):
        return self.categories(2, distance_flg)

    def getClassflg(self, class_flg):
        return self.categories(4, class_flg)

    def getTenkyuflg(self, tenkyu_flg):
        return self.categories(4, tenkyu_flg)

    def getKyoseiflg(self, kyosei_flg):
        return self.categories(4, kyosei_flg)

    def getTraincoursekind(self, train_course_kind):
        return self.categories(6, train_course_kind)

    def getSaka(self, saka):
        return self.categories(2, saka)

    def getWood(self, wood):
        return self.categories(2, wood)

    def getDart(self, dart):
        return self.categories(2, dart)

    def getTurf(self, turf):
        return self.categories(2, turf)

    def getPool(self, pool):
        return self.categories(2, pool)

    def getSteeple(self, steeple):
        return self.categories(2, steeple)

    def getPolitruck(self, politruck):
        return self.categories(2, politruck)

    def getTraindistance(self, train_distance):
        return self.categories(5, train_distance)

    def getTrainjuten(self, train_juten):
        return self.categories(5, train_juten)

    def getOikirikind(self, oikiri_kind):
        return self.categories(4, oikiri_kind)

    def getZensoIjokbn(self, zenso_ijo_kbn):
        return self.categories(7, zenso_ijo_kbn)

    def getZensoCourseposition(self, zenso_course_position):
        return self.categories(9, zenso_course_position)

    def getZensoRacelegtype(self, zenso_race_leg_type):
        return self.categories(7, zenso_race_leg_type)

    def getZensoCorner4courseposition(self, zenso_corner4_course_position):
        return self.categories(8, zenso_corner4_course_position)

    def getUmakigocode(self, uk):
        return self.categories(28, uk)

    # WORKTABLEデータ
    # 独自メソッド利用
    def getBacode(self, b):
        b_d = np.zeros([11])
        if b == 1:
            b_d[0] = 1
        elif b == 2:
            b_d[1] = 1
        elif b == 3:
            b_d[2] = 1
        elif b == 4:
            b_d[3] = 1
        elif b == 5:
            b_d[4] = 1
        elif b == 6:
            b_d[5] = 1
        elif b == 7:
            b_d[6] = 1
        elif b == 8:
            b_d[7] = 1
        elif b == 9:
            b_d[8] = 1
        elif b == 10:
            b_d[9] = 1
        else:
            b_d[10] = 1
        return b_d

    def getDistanceadjust(self, d):
        d_d = np.zeros([8])
        if d == 0:
            d_d[0] = 1
        if d == 1:
            d_d[1] = 1
        if d == 2:
            d_d[2] = 1
        if d == 3:
            d_d[3] = 1
        if d == 4:
            d_d[4] = 1
        if d == 5:
            d_d[5] = 1
        if d == 6:
            d_d[6] = 1
        if d == 9:
            d_d[7] = 1
        return d_d

    def getJockeyshirushi(self, j):
        j_d = np.zeros([8])
        if j == 0:
            j_d[0] = 1
        if j == 1:
            j_d[1] = 1
        if j == 2:
            j_d[2] = 1
        if j == 3:
            j_d[3] = 1
        if j == 4:
            j_d[4] = 1
        if j == 5:
            j_d[5] = 1
        if j == 6:
            j_d[6] = 1
        if j == 9:
            j_d[7] = 1
        return j_d

    def getDartadjustcode(self, d):
        d_d = np.zeros([5])
        if d == 0:
            d_d[0] = 1
        if d == 1:
            d_d[1] = 1
        if d == 2:
            d_d[2] = 1
        if d == 3:
            d_d[3] = 1
        if d == 5:
            d_d[4] = 1
        return d_d

    def getGekisotype(self, g):
        g_d = np.zeros([7])
        if g == "00":
            g_d[0] = 1
        if g == "A1":
            g_d[1] = 1
        if g == "A2":
            g_d[2] = 1
        if g == "A3":
            g_d[3] = 1
        if g == "A4":
            g_d[4] = 1
        if g == "B1":
            g_d[5] = 1
        if g == "B2":
            g_d[6] = 1
        return g_d

    def getRestreasoncode(self, r):
        r_d = np.zeros([15])
        if r == 0:
            r_d[0] = 1
        if r == 1:
            r_d[1] = 1
        if r == 2:
            r_d[2] = 1
        if r == 3:
            r_d[3] = 1
        if r == 4:
            r_d[4] = 1
        if r == 5:
            r_d[5] = 1
        if r == 6:
            r_d[6] = 1
        if r == 7:
            r_d[7] = 1
        if r == 11:
            r_d[8] = 1
        if r == 12:
            r_d[9] = 1
        if r == 13:
            r_d[10] = 1
        if r == 14:
            r_d[11] = 1
        if r == 15:
            r_d[12] = 1
        if r == 16:
            r_d[13] = 1
        if r == 21:
            r_d[14] = 1
        return r_d

    def getNorikaeflg(self, n):
        n_d = np.zeros([3])
        if n == 0:
            n_d[0] = 1
        if n == 1:
            n_d[1] = 1
        if n == 9:
            n_d[2] = 1
        return n_d

    def getHobokusakirank(self, h):
        h_d = np.zeros([6])
        if h == "0":
            h_d[0] = 1
        if h == "A":
            h_d[1] = 1
        if h == "B":
            h_d[2] = 1
        if h == "C":
            h_d[3] = 1
        if h == "D":
            h_d[4] = 1
        if h == "E":
            h_d[5] = 1
        return h_d

    def getTraintype(self, t):
        t_d = np.zeros([12])
        if t == "01":
            t_d[0] = 1
        if t == "02":
            t_d[1] = 1
        if t == "03":
            t_d[2] = 1
        if t == "04":
            t_d[3] = 1
        if t == "05":
            t_d[4] = 1
        if t == "06":
            t_d[5] = 1
        if t == "07":
            t_d[6] = 1
        if t == "08":
            t_d[7] = 1
        if t == "09":
            t_d[8] = 1
        if t == "10":
            t_d[9] = 1
        if t == "11":
            t_d[10] = 1
        return t_d

    def getTrainvolhyoka(self, t):
        t_d = np.zeros([5])
        if t == "A":
            t_d[0] = 1
        if t == "B":
            t_d[1] = 1
        if t == "C":
            t_d[2] = 1
        if t == "D":
            t_d[3] = 1
        if t == " ":
            t_d[4] = 1
        return t_d

    # 汎用メソッド

    def categories(self, category_count, value):
        cat = np.zeros([category_count])
        cat[value - 1] = 1
        return cat
