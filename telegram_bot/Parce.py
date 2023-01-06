def filterCategories_and_GetUserCategory(html_Categ):

	for every_categ in html_Categ:
		non_filt_Categ = every_categ.get_text()
		filtCateg = re.sub(r"\t|\r|\n", "", non_filt_Categ)
		filtCateg = ' '.join(filtCateg.split())  #filter repeating spaces
		Categories.append(filtCateg)

	#output prompting the user to select a category
	del Categories[0:32]  #slice unnecessary categories like languages

	# output all categories(Genres) of games in console
	print(*Categories, sep="\n")
	print('-'*50)

	# ctg - category
	# input Category from User
	ctg = input('Выберете нужную вам категорию(Учитывайте регистр): ')
	while True:
		if ctg not in Categories:
			print('\nВы не учли регистр или ошиблись в слове, попробуйте снова')
			ctg = input('Выберете нужную вам категорию(Учитывайте регистр): ')
		elif ctg in Categories:
			print(f'Выбранная вами категория: {ctg}')
			return ctg

def GetCategoryPage(Category):
	#Search user's category on site and keep in variable
	for every_categ in html_Steam.find_all('a'):
		non_filt_Categ = every_categ.get_text()
		filtCateg = re.sub(r"\t|\r|\n", "", non_filt_Categ)
		filtCateg = ' '.join(filtCateg.split())
		if filtCateg == Category:
			CategoryPage = every_categ.get('href')
			return CategoryPage

def GetRandomGameFromSteam_OnCategoryPage(browser):

	#Start that page from Selenium
	url = CategoryPage
	browser.get(url)

	#Output popularity Genres
	print('Выберете один из популярных жанров: ')
	for quantityGenre in browser.find_elements(By.CLASS_NAME, 'partnersaledisplay_SaleTabLabel_1mvCC'):
		print(f"{browser.find_elements(By.CLASS_NAME, 'partnersaledisplay_SaleTabLabel_1mvCC').index(quantityGenre)+1}.", quantityGenre.text.title())

	#Click on Button of this Genre on Button "Popular Genres"
	ChoiceGenre = input("Выбранный вами жанр: ").upper()
	for ClickButtonThisGenre in browser.find_elements(By.CLASS_NAME, 'partnersaledisplay_SaleTabLabel_1mvCC'):
		if ClickButtonThisGenre.text == f"{ChoiceGenre}":
			time.sleep(1)
			ClickButtonThisGenre.click()
			break

	#Output popular Games that Category, Genre
	print("Популярные игры этой категории и жанра сейчас:\n")



	# Fix Here

	for Games in browser.find_elements(By.CLASS_NAME, 'salepreviewwidgets_HeaderCapsuleImageContainer_Cqh49'):
		print(Games.find_element(By.CSS_SELECTOR, 'img').get_attribute('alt'))

	print("Ready")


if __name__ == "__main__":
	import requests
	from bs4 import BeautifulSoup

	# filter all categories of games from \t \r \n and repeating spaces
	import re  # lib for filter from \t \r \n

	# Подгружаем Селениум для парсинга того, что не спарсить супом и lxml
	from selenium.webdriver import Chrome
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.wait import WebDriverWait as wait
	import time
	import random

	# Find genre of games for class 'popup_menu_item'
	URL = 'https://store.steampowered.com/?l=russian'

	# HTML-Pages
	html_Steam = BeautifulSoup(requests.get(URL).content, 'lxml')
	html_Categ = html_Steam.find_all('a', { 'class': 'popup_menu_item' })

	# Create list where will be kept categories of games
	Categories = []

	# Game's Category
	Category = filterCategories_and_GetUserCategory(html_Categ)

	# CategoryPage
	CategoryPage = GetCategoryPage(Category)

	# подгружаем хром драйвер с https://chromedriver.chromium.org/downloads
	browser = Chrome('D:\ChromeDriver\chromedriver')

	# Genre's Game
	wait(browser, timeout = 5).until(GetRandomGameFromSteam_OnCategoryPage)







