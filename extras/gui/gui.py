import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import json, requests


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title = "Bork"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500

		self.InitWindow()


	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()

	def api_call(self):
		api_token = '31df5488194dc5669a4d8c1b5800ef60'
		url = 'https://api.darksky.net/forecast/31df5488194dc5669a4d8c1b5800ef60/40.7128,-74.0060'
		# call data
		data = requests.get(url).json()
		#parse data
		current = data['currently']
		summary = current['summary']
		temp = current['temperature']
		wind = current['windSpeed']
		uv = current['uvIndex']
		min_cast = data['minutely']['data'][0]
		min_sum = data['minutely']['summary']
		daily = data['daily']['data'][0]
		moon = daily['moonPhase']
		#loop through data
		weather_forecast = [summary, temp, wind, uv, min_sum, moon]
		#for x in weather_forecast:
			#print(x)
		print(min_sum)
		print('The temp is ' + str(temp))
		print('The wind is blowing at ' + str(wind))
		print('UV index is at ' + str(uv))
		print('The moon is at ' + str(moon))



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())