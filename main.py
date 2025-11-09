from datetime               import datetime
from utils.birthday_finder  import get_persons_celebtrating
from utils.send_notif       import send_notif_date


if __name__ == "__main__":
    
    # date                = datetime.now().strftime('%Y-%m-%d')
    date = '2025-11-20'
    persons_celebrating = get_persons_celebtrating(date)

    send_notif_date(persons_celebrating)