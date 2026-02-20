import datetime

def get_greeting():
    """Returns a greeting based on the current time of day."""
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def get_creator_info():
    """Returns information about the creator."""
    return "Karl Al Robot was created by Marx Muronzi."

def get_current_time_ampm():
    """Returns the current time in AM/PM format."""
    return datetime.datetime.now().strftime("%I:%M %p")