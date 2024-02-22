This program was created as part of the 100 Days of code course by the App Brewery.

The goal for day 93 of the course was to create a web scraping program. For the program, I created a script that scrapes housing data from homes.com and saves that data to a csv file. I tried other home listing websites however, upon testing Homes.com was the easiest one to work with and returned data. Additionally, the url created from the search parameters saved the search allowing url to return unique entries for any day the script is executed. Here is an example url for a search in San Fransico. https://www.homes.com/houses-for-sale/1-to-5-bedroom/?sk=ufdZSaiDuqN8WT539rXFSeN6IZsPGBP_xfkI_Bhk9pw&bb=l2porikn0Oqnjm25D. 

Since this program actually provided real world value to me, I added on to it by creating a second script that emails the data that is saved to a csv file and passed both the housing_collection, and housing_email scripts through a ps1 file that I scheduled to run daily on my personal computer. 

The housing_collection script first gathers data from Homes.com. First checking for the number of pages and then looping through each property and populating lists with the desired data. Afterwards, the data from those lists are combined to create a csv file which is saved in the Daily_Export folder. The created csv file has the current date in the name making it possible to search for data historically as well as email the data that was queried for the current date.

After the housing_colleciton script is finished running, the housing_email script can then be executed. The email script searches for a csv file with the current date in the title and composes the body for the email with the inforamtion from the csv. After the body is composed, the script sends an email with the data populated from the csv file.

This program has proven to be very useful for me in providing me local home listings as well as historical data for number of listings, and other statistics. For someone looking into home ownership, this was a fun project to complete!
