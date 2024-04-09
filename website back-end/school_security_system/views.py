from django.shortcuts import render
from rfid_helper.rfid_reader import read_rfid
import threading


def home_page(request):

    # Start the RFID reading thread
    t = threading.Thread(target=read_rfid)
    t.start()
    return render(request, 'home_page.html')