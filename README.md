This program was created as part of the 100 Days of code course by the App Brewery.

The goal for day 93 of the course was to create a web scraping program. For the program, I created a script that scrapes housing data from homes.com and saves that data to a csv file. I tried other home listing websites however, upon testing Homes.com was the easiest one to work with and returned data.

Since this program actually provided real world value to me, I added on to it by creating a second script that emails the data that is saved to a csv file and passed both the housing_collection, and housing_email scripts through a ps1 file that I scheduled to run daily on my personal computer. 

The housing_collection script first gathers data from Homes.com. First checking for the number of pages and then looping through each property and populating lists with the desired data. Afterwards, the data from those lists are combined to create a csv file which is saved in the Daily_Export folder.

After the housing_colleciton script is finished running, the housing_email script can then be executed. The email script searches for a csv file with the current date in the title and composes and sends an email with that data populated from the csv file.
