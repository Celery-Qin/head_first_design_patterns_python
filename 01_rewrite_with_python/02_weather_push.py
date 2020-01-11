# ---------------- Subject ---------------- #

class Subject():

    observer_list = list()

    def register_observer(self, observer): # 注册加入一个观察者
        self.observer_list.append(observer)

    def remove_observer(self, observer): # 注销取消一个观察者
        self.observer_list.remove(observer)

    def notify_observers(self):
        pass


class WeatherData(Subject):

    def notify_observers(self, temp, humidity, pressure):
        for observer in self.observer_list:
	        observer.update(temp, humidity, pressure)
        
    def measurementsChanged(self, temp, humidity, pressure):
        self.notify_observers(temp, humidity, pressure)

    def set_measurements(self, temp, humidity, pressure):
        self.measurementsChanged(temp, humidity, pressure)
   

# ---------------- Observer ---------------- #

class Observer():

    def __init__(self, subject):
        subject.register_observer(self)

    def update(self, temp, humidity, pressure): # 这样真的好吗？
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure


class DisplayElement():

    def display(self):
        print('print something')


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        weather_data.register_observer(self)

    def display(self, temp, humidity):
        print('今天的温度是{}，湿度是{}'.format(temp, humidity))

    def update(self, temp, humidity, pressure):
        self.display(temp, humidity)


class StatisticsDisplay(Observer, DisplayElement):

    temp_list = list()
    
    def __init__(self, weather_data):
        weather_data.register_observer(self)

    def display(self, temp_max, temp_min, temp_avg):
        print('最高温度是{}，最低温度是{}，平均温度是{}'.format(temp_max, temp_min, temp_avg))

    def update(self, temp, humidity, pressure):
        self.temp_list.append(temp)
        temp_max = max(self.temp_list)
        temp_min = min(self.temp_list)
        temp_avg = sum(self.temp_list)/len(self.temp_list)
        self.display(temp_max, temp_min, temp_avg)


class ForecastDisplay(Observer, DisplayElement):

    current_pressure = 0
    last_pressure = 0
    
    def __init__(self, weather_data):
        weather_data.register_observer(self)

    def display(self, current_pressure, last_pressure):
        if current_pressure > last_pressure:
            print("Improving weather on the way!")
        elif current_pressure == last_pressure:
            print("More of the same")
        else:
            print("Watch out for cooler, rainy weather")

    def update(self, temp, humidity, pressure):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure
        self.display(self.current_pressure, self.last_pressure)


class HeadIndex(Observer, DisplayElement):
    
    def __init__(self, weather_data):
        weather_data.register_observer(self)

    def display(self, heat_index):
        print("Heat index is {:.2f}".format(heat_index))

    def update(self, t, rh, pressure):
        heat_index =  ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) +
		(0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) +
		(0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
		(0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *  
		(rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) +
		(0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +     
		0.000000000843296 * (t * t * rh * rh * rh)) -
		(0.0000000000481975 * (t * t * t * rh * rh * rh)))
        self.display(heat_index)

# ---------------- WeatherStation ---------------- #

weather_data = WeatherData()

current_conditions_display = CurrentConditionsDisplay(weather_data)
statistics_display = StatisticsDisplay(weather_data)
forecast_display = ForecastDisplay(weather_data)
heat_index = HeadIndex(weather_data)

weather_data.set_measurements(80, 65, 30.45)
weather_data.set_measurements(82, 70, 29.24)
weather_data.set_measurements(78, 90, 29.21)



