from datetime               import datetime
from utils.birthday_finder  import get_persons_celebtrating
from utils.sender           import send_notif_date, send_birthday_message
from utils.message_builder  import customize_message

if __name__ == "__main__":
    
    date                = datetime.now().strftime('%Y-%m-%d')
    persons_celebrating = get_persons_celebtrating(date)

    send_notif_date(persons_celebrating)
    for person_name in persons_celebrating:
        message = customize_message(person_name)
        send_birthday_message(person_name, message)