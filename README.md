The aim of this repo is to scrape NGOs/Nonprofits from the following websites:\
[Nonprofit New York](https://www.nonprofitnewyork.org/join/directory/)\
[Queens' Borough President](https://queensbp.org/nonprofits/)\
[NYC Service](https://www.nycservice.org/organizations/)\
With more to be added eventually.



# To get the final csv file:
1. run scraper.ipynb (note this may take some time as it makes a lot of requests) to scrape all nonprofits from the source sites
2. run combine_sets.ipynb to combine the csv's created by the scraper
3. run clean.ipynb to output a csv with a single name, website, description, and address for each NGO
