from bs4 import BeautifulSoup
import requests

URL = "https://www.nonprofitnewyork.org/join/directory/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# all_content = soup.find_all("div", class_="tab-pane")
# #Returns a nested list with all the li elements containing nonprofit info
# buisnesses = [letter.find_all("li") for letter in all_content]
# #all li elements containing nonprofits
# all_non_profits = [b for buisnesses_of_letter in buisnesses for b in buisnesses_of_letter]
# instead of all the above just use the CSS selector obviously
all_non_profits = soup.select('.tab-pane > ul > li')

for np in all_non_profits:
    a = np.find("a")
    if a:
        print(a.contents[0])
        print(a['href'])
    else:
        print("EXAMPLEEEEEEEEEEEEEEEE")
        #text of the non linked nps is the second child of the li tag
        print(np.contents[1])

