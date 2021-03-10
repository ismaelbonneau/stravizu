from geopy import distance 

def moving_time(points, interval=1):
    """returns moving time in seconds"""
    moving_time = 0
    for i in range(len(points) - 1):
        lat1, lon1, ele1, t1 = points[i]
        lat2, lon2, ele2, t2 = points[i+1]
        if (t2 - t1).seconds == interval:
            moving_time += interval
    return moving_time

def moving_distance(points, interval=1):
    """returns moving distance in km"""
    moving_distance = 0
    for i in range(len(points) - 1):
        lat1, lon1, ele1, t1 = points[i]
        lat2, lon2, ele2, t2 = points[i+1]
        dist = distance.distance((lat1, lon1), (lat2, lon2)).m # distance in meters
        if (t2 - t1).seconds == interval:
            moving_distance += dist
    return moving_distance / 1000

def average_moving_speed(points, interval=1):
    """returns average moving speed in km/h"""
    total_moving_meters = 0
    total_moving_time_s = 0
    for i in range(len(points) - 1):
        lat1, lon1, ele1, t1 = points[i]
        lat2, lon2, ele2, t2 = points[i+1]
        if (t2 - t1).seconds == interval:
            total_moving_time_s += interval
            total_moving_meters += distance.distance((lat1, lon1), (lat2, lon2)).m # distance in meters
    # convert meters per sec to km per hour
    return (total_moving_meters / total_moving_time_s) * 3.6