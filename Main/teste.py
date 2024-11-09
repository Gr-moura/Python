import VariavelResposta as vr
import CriaVetores as cv
from datetime import datetime, timedelta

#vr.price_change_indicator("AAPL", "2024-10-04", "2024-11-11")
# cv.criavetores("2024-11-11", "AAPL")

#VT = cv.criavetores("2024-11-09", "AAPL")

date_str = "2024-10-01"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
new_date_obj = date_obj - timedelta(days=1)

a = [int(part) for part in new_date_obj.strftime("%Y-%m-%d").split("-")]



print(a)