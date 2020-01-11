# ---------------- Subject ---------------- #

class Subject():

    def __init__(self):
        self.observer_list = list()  # 要做成实例变量，而不是类变量
        self.changed = False

    def register_observer(self, observer): # 注册加入一个观察者
        self.observer_list.append(observer)

    def remove_observer(self, observer): # 注销取消一个观察者
        self.observer_list.remove(observer)

    def set_changed(self):
        self.changed = True

    def notify_observers(self):
        if self.changed:
            for observer in self.observer_list:
                observer.update(self) # 观察者数据更新指定主题
            self.changed = False


class WeatherData(Subject):

    def __init__(self):
        Subject.__init__(self)
        self.temp = 0
        self.humidity = 0
        self.pressure = 0
        
    def measurementsChanged(self):
        self.set_changed()
        self.notify_observers()

    def set_measurements(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    def getTemperature(self):
	    return self.temp

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure
   

# ---------------- Observer ---------------- #

class Observer():

    def __init__(self, subject): # 要让这个观察者记住自己观察了哪些主题，好随时去pull主题的data
        self.subject = subject # 观察多个主题可能需要一个列表
        subject.register_observer(self)

    def update(self, subject): 
        pass


class DisplayElement():

    def display(self):
        print('print something')


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        Observer.__init__(self, weather_data) # 注册 + 记住subject
        self.temp = 0 
        self.humidity = 0 

    def display(self, temp, humidity):
        print('今天的温度是{}，湿度是{}'.format(self.temp, self.humidity))

    def update(self, weather_data): # 要先判断这个主题是我注册过的主题
        self.temp = weather_data.getTemperature()
        self.humidity = weather_data.getHumidity()
        self.display(self.temp, self.humidity)


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        Observer.__init__(self, weather_data) # 注册 + 记住subject
        self.temp_list = list()

    def display(self, temp_max, temp_min, temp_avg):
        print('最高温度是{}，最低温度是{}，平均温度是{}'.format(temp_max, temp_min, temp_avg))

    def update(self, weather_data):
        temp = weather_data.getTemperature()
        self.temp_list.append(temp)
        temp_max = max(self.temp_list)
        temp_min = min(self.temp_list)
        temp_avg = sum(self.temp_list)/len(self.temp_list)
        self.display(temp_max, temp_min, temp_avg)


class ForecastDisplay(Observer, DisplayElement):
    
    def __init__(self, weather_data):
        Observer.__init__(self, weather_data) # 注册 + 记住subject
        self.current_pressure = 0
        self.last_pressure = 0

    def display(self, current_pressure, last_pressure):
        if current_pressure > last_pressure:
            print("Improving weather on the way!")
        elif current_pressure == last_pressure:
            print("More of the same")
        else:
            print("Watch out for cooler, rainy weather")

    def update(self, weather_data):
        self.last_pressure = self.current_pressure
        self.current_pressure = weather_data.getPressure()
        self.display(self.current_pressure, self.last_pressure)


# class HeadIndex(Observer, DisplayElement):
    
#     def __init__(self, weather_data):
#         weather_data.register_observer(self)

#     def display(self, heat_index):
#         print("Heat index is {:.2f}".format(heat_index))

#     def update(self, t, rh, pressure):
#         heat_index =  ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) +
# 		(0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) +
# 		(0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
# 		(0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *  
# 		(rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) +
# 		(0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +     
# 		0.000000000843296 * (t * t * rh * rh * rh)) -
# 		(0.0000000000481975 * (t * t * t * rh * rh * rh)))
#         self.display(heat_index)

# ---------------- WeatherStation ---------------- #

weather_data = WeatherData()

current_conditions_display = CurrentConditionsDisplay(weather_data)
statistics_display = StatisticsDisplay(weather_data)
forecast_display = ForecastDisplay(weather_data)
# heat_index = HeadIndex(weather_data)

weather_data.set_measurements(80, 65, 30.45)
weather_data.set_measurements(82, 70, 29.24)
weather_data.set_measurements(78, 90, 29.21)



