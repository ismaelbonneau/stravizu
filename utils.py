MONTH = {
    1: "Janvier",
    2: "Février",
    3: "Mars",
    4: "Avril",
    5: "Mai",
    6: "Juin",
    7: "Juillet",
    8: "Août",
    9: "Septembre",
    10: "Octobre",
    11: "Novembre",
    12: "Décembre"
}

DAY = {
    0: "Lundi",
    1: "Mardi",
    2: "Mercredi",
    3: "Jeudi",
    4: "Vendredi",
    5: "Samedi",
    6: "Dimanche"
}

def get_month(d):
    return MONTH[d.month]
def get_weekday(d):
    return DAY[d.weekday()]
def get_year(d):
    return d.year

def track_total_time(t1, t2):
    delta = (t2 - t1).seconds
    hours = delta // 3600
    minutes = (delta // 60) % 60
    seconds = delta - (hours * 3600 + minutes * 60)
    return hours, minutes, seconds