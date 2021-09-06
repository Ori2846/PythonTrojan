import webbrowser,time
from win10toast import ToastNotifier
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'

while True:
    webbrowser.open_new(url)
    toast = ToastNotifier()
    toast.show_toast("L", "Give me your cpu power - anton", duration=1)
    time.sleep(0.5)