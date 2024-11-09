import VariavelResposta as vr
import CriaVetores as cv

vr.price_change_indicator("AAPL", "2024-10-04", "2024-11-11")
# cv.criavetores("2024-11-11", "AAPL")

VT = cv.criavetores("2024-11-09", "AAPL")

a = [int (a) for a in "2024-11-09".split("-")]
print(a)