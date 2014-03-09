import calendar
import datetime

def javascript_timestamp(date):
    dt = datetime.datetime.strptime(date, "%Y-%m-%d")
    """Multiply by 1000 for flot. Flot time series data is
    based on javascript timestamps, that is milliseconds,
    since January 1, 1970 00:00:00 UTC"""
    return calendar.timegm(dt.timetuple()) * 1000
