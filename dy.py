from appium import webdriver
import time
server = r'http://localhost:4723/wd/hub'
desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',
}
driver = webdriver.Remote(server, desired_capabilities)
while True:
    time.sleep(5)
    x = 300
    y = 1000
    distance = 800
    driver.swipe(x, y, x, y - distance)