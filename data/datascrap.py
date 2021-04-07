from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import csv
import time

def scrollclick(element):
	end=1
	start=0
	while(element.get_attribute("style")!="display: none;"):
		driver.execute_script("window.scrollTo({},{})".format(start,end))
		end+=10
		try:
			button.click()
			time.sleep(3)
			print("pressed")
			start=end
			break
		except:
			continue

# installing chrome driver
driver = webdriver.Chrome("/home/honey/Desktop/opensource/Recommender_system/data/chromedriver")


##website 1
driver.get("https://economictimes.indiatimes.com/topic/article/news")
time.sleep(5)
button = driver.find_element_by_class_name("autoload_continue")
close=driver.find_element_by_xpath("/html/body/div[4]/span/span").click()
for i in range(0,10):
	scrollclick(button)
#	print(driver.find_element_by_xpath("/html/body/main/div[9]/div[1]/div[6]/div[1]/ul[2]/li[2]/div[{}]/a".format(i)).get_attribute("href"))
urls=[]
for i in driver.find_elements_by_xpath("//*[@class='clr flt topicstry story_list']/a"):
	urls.append(i.get_attribute("href"))
	print("adding1")
print(len(urls))



##website 2
driver.get("https://economictimes.indiatimes.com/news/india")
time.sleep(5)
button = driver.find_element_by_class_name("autoload_continue")
for i in range(0,100):
	scrollclick(button)

#	print(driver.find_element_by_xpath("/html/body/main/div[9]/div[1]/div[6]/div[1]/ul[2]/li[2]/div[{}]/a".format(i)).get_attribute("href"))
for i in driver.find_elements_by_xpath("//*[@class='eachStory']/a"):
	urls.append(i.get_attribute("href"))
	print("adding2")

for i in driver.find_elements_by_xpath("//*[@class='eachStory']/h3/a"):
	urls.append(i.get_attribute("href"))
	print("adding3")

print(len(urls))


driver.close()
