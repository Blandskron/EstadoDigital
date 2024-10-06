from datetime import datetime
from django.utils import timezone
import pytz

def event_date_processor(request):
    # Define la zona horaria de Santiago de Chile
    tz = pytz.timezone('America/Santiago')

    # Define la fecha y hora del evento (reemplaza con la fecha de tu evento)
    event_date_naive = datetime(2024, 10, 9, 8, 00, 00)
    event_date = tz.localize(event_date_naive)

    return {'event_date': event_date}
