class Courseref:
    def __init__(self):
        self.course_list = []
        self.course_list.append([36, "門別"])
        self.course_list.append([3, "帯広"])
        self.course_list.append([10, "盛岡"])
        self.course_list.append([11, "水沢"])
        self.course_list.append([22, "金沢"])
        self.course_list.append([18, "浦和"])
        self.course_list.append([19, "船橋"])
        self.course_list.append([20, "大井"])
        self.course_list.append([21, "川崎"])
        self.course_list.append([23, "笠松"])
        self.course_list.append([24, "名古屋"])
        self.course_list.append([27, "園田"])
        self.course_list.append([31, "高知"])
        self.course_list.append([32, "佐賀"])

    def getCoursecode(self, course_name):
        id = 0
        for i in range(len(self.course_list)):
            if course_name == self.course_list[i][1]:
                id = self.course_list[i][0]
        return id

    def getCoursename(self, id):
        name = "エラー"
        for i in range(len(self.course_list)):
            if id == self.course_list[i][0]:
                name = self.course_list[i][1]
        return name
