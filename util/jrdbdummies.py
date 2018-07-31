import numpy as np
class CategoryGetter:
    #開催データ
    def getKaisaikbn(self,kaisaikbn):
        kaisaikbn_d = self.getThreecat(kaisaikbn)
        return kaisaikbn_d
            
    def getDayofweek(self,dayofweek):
        dayofweek_d = np.zeros([7])
        if dayofweek == '日':
            dayofweek_d[0] = 1
        elif dayofweek == '月':
            dayofweek_d[1] = 1
        elif dayofweek == '火':
            dayofweek_d[2] = 1
        elif dayofweek == '水':
            dayofweek_d[3] = 1
        elif dayofweek == '木':
            dayofweek_d[4] = 1
        elif dayofweek == '金':
            dayofweek_d[5] = 1
        elif dayofweek == '土':
            dayofweek_d[6] = 1
        return dayofweek_d
        
    def getTenko(self,tenko):
        tenko_d = self.getSixcat(tenko)
        return tenko_d
        
    def getBaba_abst(self,baba):
        baba_d = getFourcat(baba)
        return baba_d
        
    def getBaba_detail(self,baba):
        baba_d = getThreecat(baba)
        return baba_d
        
    def getTurfkind(self,kind):
        kind_d = self.getTreecat(kind)
        return kind_d
        
    def getTennatsu(self,ten):
        ten_d = getTwocat(ten)
        return ten_d
        
    def getStopfreeze(self,st):
        stf_d = getTwocat(st)
        return stf_d
        
    #番組データ
    def getDistance(self,dis):
        dis_d = dis
        return dis_d
        
    def getTdscode(self,tds):
        tds_d = getThreecat(tds)
        return tds_d
        
    def getRightleft(self,rl):
        rl_d = self.getFourcat(rl)
        return lr_d
        
    def getInout(self,inout):
        io_d = self.getFourcat(inout)
        return io_d
        
    def getShubetsu(self,s):
        s_d = self.getFivecat(s)
        return s_d
        
    def getJoken(self,j):
        j_d = np.zeros([11])
        if j == '04':
            j_d[0] = 1
        elif j == '05':
            j_d[1] = 1
        elif j == '08':
            j_d[2] = 1
        elif j == '09':
            j_d[3] = 1
        elif j == '10':
            j_d[4] = 1
        elif j == '15':
            j_d[5] = 1
        elif j == '16':
            j_d[6] = 1
        elif j == 'A1':
            j_d[7] = 1
        elif j == 'A2':
            j_d[8] = 1
        elif j == 'A3':
            j_d[9] = 1
        elif j == 'OP':
            j_d[10] = 1
        return j_d
        
    def getJuryo(self,j):
        j_d = self.getFourcat(j)
        return j_d
        
    def getGrade(self,g):
        g_d = self.getFivecat(g)
        return g_d
        
    def getCourse(self,c):
        c_d = self.getFivecat(c)
        return c_d
        

    #競走馬データ
    #汎用メソッド利用
    def getNum(num):
        num_d = self.getEighteencat(num)
        return num_d

    def getLeg_type(leg_type):
        leg_type_d = self.getSevencat(leg_type)
        return leg_type_d

    def getOmotekisei_code(omotekisei_code):
        omotekisei_code_d = self.getFourcat(omotekisei_code)
        return omotekisei_code_d

    def getBrinkers(brinkers):
        brinkers_d = self.getFourcat(brinkers)
        return brinkers_d

    def getMinarai(minarai):
        minarai_d = self.getFourcat(minarai)
        return minarai_d

    def getWaku(waku):
        waku_d = self.getEightcat(waku)
        return waku_d

    def getTurf_adjust_code(turf_adjust_code):
        turf_adjust_code_d = self.getFivecat(turf_adjust_code)
        return turf_adjust_code_d

    def getTorikeshi(torikeshi):
        torikeshi_d = self.getTwocat(torikeshi)
        return torikeshi_d

    def getSex(sex):
        sex_d = self.getThreecat(sex)
        return sex_d

    def getBanushikai_code(banushikai_code):
        banushikai_code_d = self.getElevencat(banushikai_code)
        return banushikai_code_d

    def getYuso(yuso):
        yuso_d = self.getFivecat(yuso)
        return yuso_d

    def getKokyu_flg(kokyu_flg):
        kokyu_flg_d = self.getThreecat(kokyu_flg)
        return kokyu_flg_d

    def getTurf_dart_steeple_flg(turf_dart_steeple_flg):
        turf_dart_steeple_flg_d = self.getThreecat(turf_dart_steeple_flg)
        return turf_dart_steeple_flg_d

    def getDistance_flg(distance_flg):
        distance_flg_d = self.getTwocat(distance_flg)
        return distance_flg_d

    def getClass_flg(class_flg):
        class_flg_d = self.getFourcat(class_flg)
        return class_flg_d

    def getTenkyu_flg(tenkyu_flg):
        tenkyu_flg_d = self.getFourcat(tenkyu_flg)
        return tenkyu_flg_d

    def getKyosei_flg(kyosei_flg):
        kyosei_flg_d = self.getFourcat(kyosei_flg)
        return kyosei_flg_d

    def getTrain_course_kind(train_course_kind):
        train_course_kind_d = self.getSixcat(train_course_kind)
        return train_course_kind_d

    def getSaka(saka):
        saka_d = self.getTwocat(saka)
        return saka_d

    def getWood(wood):
        wood_d = self.getTwocat(wood)
        return wood_d

    def getDart(dart):
        dart_d = self.getTwocat(dart)
        return dart_d

    def getTurf(turf):
        turf_d = self.getTwocat(turf)
        return turf_d

    def getPool(pool):
        pool_d = self.getTwocat(pool)
        return pool_d

    def getSteeple(steeple):
        steeple_d = self.getTwocat(steeple)
        return steeple_d

    def getPolitruck(politruck):
        politruck_d = self.getTwocat(politruck)
        return politruck_d

    def getTrain_distance(train_distance):
        train_distance_d = self.getFivecat(train_distance)
        return train_distance_d

    def getTrain_juten(train_juten):
        train_juten_d = self.getFivecat(train_juten)
        return train_juten_d

    def getOikiri_kind(oikiri_kind):
        oikiri_kind_d = self.getFourcat(oikiri_kind)
        return oikiri_kind_d

    def getZenso_ijo_kbn(zenso_ijo_kbn):
        zenso_ijo_kbn_d = self.getSevencat(zenso_ijo_kbn)
        return zenso_ijo_kbn_d

    def getZenso_course_position(zenso_course_position):
        zenso_course_position_d = self.getNinecat(zenso_course_position)
        return zenso_course_position_d

    def getZenso_race_leg_type(zenso_race_leg_type):
        zenso_race_leg_type_d = self.getSevencat(zenso_race_leg_type)
        return zenso_race_leg_type_d

    def getZenso_corner4_course_position(zenso_corner4_course_position):
        zenso_corner4_course_position = self.getEightcat(zenso_corner4_course_position)
        return zenso_corner4_course_position

    #競走馬データ
    #独自メソッド利用
    def getBacode(b):
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
        
    def getDistance_adjust(d):
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

    def getJockye_shirushi(j):
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
        if d == 9:
            j_d[7] = 1
        return j_d

    def getDart_adjust_code(d):
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

    def getGekiso_type(g):
        g_d = np.zeros([7])
        if g == '00':
            g_d[0] = 1
        if g == 'A1':
            g_d[1] = 1
        if g == 'A2':
            g_d[2] = 1
        if g == 'A3':
            g_d[3] = 1
        if g == 'A4':
            g_d[4] = 1
        if g == 'B1':
            g_d[5] = 1
        if g == 'B2':
            g_d[6] = 1
        return g_d

    def getRest_reason_code(r):
        r_d = np.zeros([7])
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

    def getNorikae_flg(n):
        n_d = np.zeros([3])
        if n == 0:
            n_d[0] = 1
        if n == 1:
            n_d[1] = 1
        if n == 9:
            n_d[2] = 1
        return n_d

    def getHobokusaki_rank(h):
        h_d = np.zeros([6])
        if h == '0':
            h_d[0] = 1
        if h == 'A':
            h_d[1] = 1
        if h == 'B':
            h_d[2] = 1
        if h == 'C':
            h_d[3] = 1
        if h == 'D':
            h_d[4] = 1
        if h == 'E':
            h_d[5] = 1
        return h_d

    def getTrain_type(t):
        t_d = np.zeros([12])
        if t == '01':
            t_d[0] = 1
        if t == '02':
            t_d[1] = 1
        if t == '03':
            t_d[2] = 1
        if t == '04':
            t_d[3] = 1
        if t == '05':
            t_d[4] = 1
        if t == '06':
            t_d[5] = 1
        if t == '07':
            t_d[6] = 1
        if t == '08':
            t_d[7] = 1
        if t == '09':
            t_d[8] = 1
        if t == '10':
            t_d[9] = 1
        if t == '11':
            t_d[10] = 1
        return t_d

    def getTrain_vol_hyoka(t):
        t_d = np.zeros([5])
        if t == 'A':
            t_d[0] = 1
        if t == 'B':
            t_d[1] = 1
        if t == 'C':
            t_d[2] = 1
        if t == 'D':
            t_d[3] = 1
        if t == ' ':
            t_d[4] = 1
        return t_d


    #汎用メソッド

    def getTwocat(self,num):
        two_d = np.zeros([2])
        if  num == 1:
            two_d[0] = 1
        else:
            two_d[1] = 1
        return two_d
        
    def getThreecat(self,num):
        three_d = np.zeros([3])
        if num == 1:
            three_d[0] = 1
        elif num == 2:
            three_d[1] = 1
        else:
            three_d[2] = 1
        return three_d
            
    def getFourcat(self,num):
        four_d = np.zeros([4])
        if  num == 1:
            four_d[0] = 1
        elif num == 2:
            four_d[1] = 1
        elif num == 3:
            four_d[2] = 1
        else:
            four_d[3] = 1
        return four_d
            
    def getFivecat(self,num):
        five_d = np.zeros([5])
        if  num == 1:
            five_d[0] = 1
        elif num == 2:
            five_d[1] = 1
        elif num == 3:
            five_d[2] = 1
        elif num == 4:
            five_d[3] = 1
        else:
            five_d[4] = 1

    def getSixcat(self,num):
        six_d = np.zeros([6])
        if num == 1:
            six_d[0] = 1
        elif num == 2:
            six_d[1] = 1
        elif num == 3:
            six_d[2] = 1
        elif num == 4:
            six_d[3] = 1
        elif num == 5:
            six_d[4] = 1
        else:
            six_d[5] = 1
        return six_d

    def getSevencat(self,num):
        seven_d = np.zeros([7])
        if num == 1:
            seven_d[0] = 1
        elif num == 2:
            seven_d[1] = 1
        elif num == 3:
            seven_d[2] = 1
        elif num == 4:
            seven_d[3] = 1
        elif num == 5:
            seven_d[4] = 1
        elif num == 6:
            seven_d[5] = 1
        else:
            seven_d[6] = 1
        return seven_d

    def getEightcat(self,num):
        eight_d = np.zeros([8])
        if num == 1:
            eight_d[0] = 1
        elif num == 2:
            eight_d[1] = 1
        elif num == 3:
            eight_d[2] = 1
        elif num == 4:
            eight_d[3] = 1
        elif num == 5:
            eight_d[4] = 1
        elif num == 6:
            eight_d[5] = 1
        elif num == 7:
            eight_d[6] = 1
        else:
            eight_d[7] = 1
        return eight_d

    def getNinecat(self,num):
        nine_d = np.zeros([9])
        if num == 1:
            nine_d[0] = 1
        elif num == 2:
            nine_d[1] = 1
        elif num == 3:
            nine_d[2] = 1
        elif num == 4:
            nine_d[3] = 1
        elif num == 5:
            nine_d[4] = 1
        elif num == 6:
            nine_d[5] = 1
        elif num == 7:
            nine_d[6] = 1
        elif num == 8:
            nine_d[7] = 1
        else:
            nine_d[8] = 1
        return nine_d

    def getTencat(self,num):
        ten_d = np.zeros([10])
        if num == 1:
            ten_d[0] = 1
        elif num == 2:
            ten_d[1] = 1
        elif num == 3:
            ten_d[2] = 1
        elif num == 4:
            ten_d[3] = 1
        elif num == 5:
            ten_d[4] = 1
        elif num == 6:
            ten_d[5] = 1
        elif num == 7:
            ten_d[6] = 1
        elif num == 8:
            ten_d[7] = 1
        elif num == 9:
            ten_d[8] = 1
        else:
            ten_d[9] = 1
        return ten_d

    def getElevencat(self,num):
        eleven_d = np.zeros([11])
        if num == 1:
            eleven_d[0] = 1
        elif num == 2:
            eleven_d[1] = 1
        elif num == 3:
            eleven_d[2] = 1
        elif num == 4:
            eleven_d[3] = 1
        elif num == 5:
            eleven_d[4] = 1
        elif num == 6:
            eleven_d[5] = 1
        elif num == 7:
            eleven_d[6] = 1
        elif num == 8:
            eleven_d[7] = 1
        elif num == 9:
            eleven_d[8] = 1
        elif num == 10:
            eleven_d[9] = 1
        else:
            eleven_d[10] = 1
        return eleven_d

    def getTwelvecat(self,num):
        twelve_d = np.zeros([12])
        if num == 1:
            twelve_d[0] = 1
        elif num == 2:
            twelve_d[1] = 1
        elif num == 3:
            twelve_d[2] = 1
        elif num == 4:
            twelve_d[3] = 1
        elif num == 5:
            twelve_d[4] = 1
        elif num == 6:
            twelve_d[5] = 1
        elif num == 7:
            twelve_d[6] = 1
        elif num == 8:
            twelve_d[7] = 1
        elif num == 9:
            twelve_d[8] = 1
        elif num == 10:
            twelve_d[9] = 1
        elif num == 11:
            twelve_d[10] = 1
        else:
            twelve_d[11] = 1
        return eleven_d




