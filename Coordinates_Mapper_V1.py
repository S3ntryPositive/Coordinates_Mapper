import webbrowser

url = 'https://www.google.com/maps/place/'

place = input("Please Enter Coordinates: ")

webbrowser.open(url + place)