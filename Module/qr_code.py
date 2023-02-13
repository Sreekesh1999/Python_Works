import pyqrcode
from pyqrcode import QRCode

w = "https://web.whatsapp.com/"


url = pyqrcode.create(w)
url.svg("Testqrcode.svg",scale=8)