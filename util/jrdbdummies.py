import numpy as np
class CategoryGetter():
    #開催データ
    def getKaisaikbn(kaisaikbn):
        kaisaikbn_d = self.getThreecat(kaisaikbn)
        return kaisaikbn_d
            
    def getDayofweek(dayofweek):
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
        
    def getTenko(tenko):
        tenko_d = self.getSixcat(tenko)
        return tenko_d
        
    def getBaba_abst(baba):
        baba_d = getFourcat(baba)
        return baba_d
        
    def getBaba_detail(baba):
        baba_d = getThreecat(baba)
        return baba_d
        
    def getTurfkind(kind):
        kind_d = self.getTreecat(kind)
        return kind_d
        
    def getTennatsu(ten):
        ten_d = getTwocat(ten)
        return ten_d
        
    def getStopfreeze(st):
        stf_d = getTwocat(st)
        return stf_d
        
    #番組データ
    def getDistance(dis):
        dis_d = dis
        return dis_d
        
    def getTdscode(tds):
        tds_d = getThreecat(tds)
        return tds_d
        
    def getRightleft(rl):
        rl_d = self.getFourcat(rl)
        return lr_d
        
    def getInout(inout):
        io_d = self.getFourcat(inout)
        return io_d
        
    def getShubetsu(s):
        s_d = self.getFivecat(s)
        return s_d
        
    def getJoken(j):
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
        
    def getJuryo(j):
        j_d = self.getFourcat(j)
        return j_d
        
    def getGrade(g):
        g_d = self.getFivecat(g)
        return g_d
        
    def getCourse(c):
        c_d = self.getFivecat(c)
        return c_d
        
    #汎用メソッド
    def getSixcat(num):
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
        
    def getThreecat(num):
        three_d = np.zeros([3])
        if num == 1:
            three_d[0] = 1
        elif num == 2:
            three_d[1] = 1
        else:
            three_d[2] = 1
            
    def getFourcat(num):
        four_d = np.zeros([4])
        if  num == 1:
            four_d[0] = 1
        elif num == 2:
            four_d[1] = 1
        elif num == 3:
            four_d[2] = 1
        else:
            four_d[3] = 1
            
    def getTwocat(num):
        four_d = np.zeros([2])
        if  num == 1:
            four_d[0] = 1
        else:
            four_d[1] = 1
            
    def getFivecat(num):
        four_d = np.zeros([5])
        if  num == 1:
            four_d[0] = 1
        elif num == 2:
            four_d[1] = 1
        elif num == 3:
            four_d[2] = 1
        elif num == 4:
            four_d[3] = 1
        else:
            four_d[4] = 1
