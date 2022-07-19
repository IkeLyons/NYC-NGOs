The aim of the scripts in the repo are to scrape NGOs/Nonprofits from the following websites:
https://www.nonprofitnewyork.org/join/directory/
https://queensbp.org/nonprofits/
https://www.nycservice.org/organizations/


# To get the final csv file:
1. run scraper.ipynb (note this may take some time as it makes a lot of requests) to scrape all nonprofits from the source sites
2. run combine_sets.ipynb to combine the csv's created by the scraper
3. run clean.ipynb to output a csv with a single name, website, description, and address for each NGO