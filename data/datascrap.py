from selenium import webdriver
import csv
import time

urls=[]

def scrollclick(element):
	end=1
	start=0
	while(element.get_attribute("style")!="display: none;"):
		driver.execute_script("window.scrollTo({},{})".format(start,end))
		end+=10
		try:
			button.click()
			time.sleep(5)
			print("Loading....")
			start=end
			break
		except:
			continue

# installing chrome driver
driver = webdriver.Chrome("/home/honey/Desktop/opensource/Recommender_system/data/chromedriver")


##website 1
driver.get("https://economictimes.indiatimes.com/topic/article/news")
try:
	close=driver.find_element_by_xpath("/html/body/div[4]/span/span").click()
except:
	pass
button = driver.find_element_by_class_name("autoload_continue")
for i in range(0,10):
	scrollclick(button)
#	print(driver.find_element_by_xpath("/html/body/main/div[9]/div[1]/div[6]/div[1]/ul[2]/li[2]/div[{}]/a".format(i)).get_attribute("href"))
for i in driver.find_elements_by_xpath("//*[@class='clr flt topicstry story_list']/a"):
	urls.append(i.get_attribute("href"))
print("website 1 completed")
print("total elements:",len(urls))



##website 2
driver.get("https://economictimes.indiatimes.com/news/economy/agriculture")
try:
	close=driver.find_element_by_xpath("/html/body/div[4]/span/span").click()
except:
	pass
button = driver.find_element_by_class_name("autoload_continue")
for i in range(0,200):
	scrollclick(button)
for i in driver.find_elements_by_xpath("//*[@class='eachStory']/a"):
	urls.append(i.get_attribute("href"))
for i in driver.find_elements_by_xpath("//*[@class='eachStory']/h3/a"):
	urls.append(i.get_attribute("href"))
print("website 2 completed")
print("total elements:",len(urls))


##website 3
driver.get("https://economictimes.indiatimes.com/news/sports")
try:
	close=driver.find_element_by_xpath("/html/body/div[4]/span/span").click()
except:
    pass
button = driver.find_element_by_class_name("autoload_continue")
for i in range(0,200):
	scrollclick(button)
for i in driver.find_elements_by_xpath("//*[@class='eachStory']/a"):
	urls.append(i.get_attribute("href"))
for i in driver.find_elements_by_xpath("//*[@class='eachStory']/h3/a"):
	urls.append(i.get_attribute("href"))

print("website 3 completed")
print("total elements:",len(urls))

##website 4
driver.get("https://economictimes.indiatimes.com/news/science")
try:
	close=driver.find_element_by_xpath("/html/body/div[4]/span/span").click()
except:
	pass
button = driver.find_element_by_class_name("autoload_continue")
for i in range(0,220):
	scrollclick(button)
for i in driver.find_elements_by_xpath("//*[@class='eachStory']/a"):
	urls.append(i.get_attribute("href"))
for i in driver.find_elements_by_xpath("//*[@class='eachStory']/h3/a"):
	urls.append(i.get_attribute("href"))
	
print("website 4 completed")
print("total elements:",len(urls))

##website 5
driver.get("https://economictimes.indiatimes.com/news/international/world-news")
try:
	close=driver.find_element_by_xpath("/html/body/div[4]/span/span").click()
except:
	pass
button = driver.find_element_by_class_name("autoload_continue")
for i in range(0,220):
	scrollclick(button)
for i in driver.find_elements_by_xpath("//*[@class='eachStory']/a"):
	urls.append(i.get_attribute("href"))
for i in driver.find_elements_by_xpath("//*[@class='eachStory']/h3/a"):
	urls.append(i.get_attribute("href"))
	
print("website 5 completed")
print("total elements:",len(urls))


titles=[]
dates=[]
tags=[]
contents=[]


for url in urls:
	driver.get(url)
	try:
		titles.append(driver.find_element_by_xpath("//h1[@class='artTitle font_faus']").text)
	except:
		titles.append("")

	try:
		dates.append(driver.find_element_by_xpath("//div[@class='bylineBox']/div/div/time").text[14:])
	except:
		dates.append("")
	
	try:
		tag=[]
		for i in driver.find_elements_by_xpath("//div[@class='clearfix relTopics raltedTopics']/div/a"):
			tag.append(i.text)
		tags.append(tuple(tag))
	except:
		tags.append("")

	try:
		contents.append(driver.find_element_by_xpath("//div[@class='artText medium']").text)
	except:
		contents.append("")

	print("data adding into lists")


print("titles:",len(titles))
print("urls:",len(urls))
print("dates:",len(dates))
print("tags:",len(tags))
print("contents:",len(contents))
driver.close()


with open('dataset.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id", "title", "date of publish" , "url", "content", "tags"])
	for j in range(0 , len(titles)):
		try:
			writer.writerow([j,titles[j], dates[j], urls[j], contents[j], tags[j]])
		except:
			continue
		print("details updated on csv.....")