from  horseview.horsemodel import KaisaiData, db
import schedule

def missing_days(year):
    open_days = schedule.annual_schedule(year)
    diff = list(set(open_days) - set(db_days(year)))
    diff.sort()
    return diff

def db_days(year):
    start_date = int("{}0101".format(year))
    end_date = int("{}1231".format(year))
    kaisais = KaisaiData.query.filter(KaisaiData.ymd >= start_date, KaisaiData.ymd <= end_date ).all()
    db_days = list(set([k.ymd for k in kaisais]))
    db_days.sort()
    return db_days
