import os, smtplib, csv
from datetime import date

today = date.today()

### CONFIGURE SMTP
print("Setting up connection with SMTP server...")
email = os.environ.get("email")
password = os.environ.get("password")
to_address = os.environ.get("to_address")
smtp_server = os.environ.get("smtl_server")

connection = smtplib.SMTP(smtp_server)
connection.starttls()
connection.login(user=email, password=password)
print("SUCCESS: Connection established!")

try:
    ### IMPORT DATA
    print("Importing data...")
    exports_folder = "./Daily_Export/"
    list_exports = os.listdir(exports_folder)
    # Todays export file
    todays_export = exports_folder
    for file in list_exports:
        if str(today) in file:
            todays_export += file

    # Create list with rows from export file
    todays_listings = []
    with open(todays_export) as data_file:
        data = csv.reader(data_file)
        for row in data:
            todays_listings.append(row)

    ## COMPOSE & SEND EMAIL
    # Compose body
    print("Composing email.")
    email_body = f"Total homes that meet search criteria: {len(todays_listings) - 1}\nCSV file can be found under Daily_Export folder.\nSearch criteria:\n\$MINPRICE-$MAXPRICE\n\tSingle Family\n\tLocation: QUERY LOCATION: \n\nLISTINGS\n\n"
    for home in todays_listings[1:]:
        email_body += (f"-> {home[2]}\n\tListing Price: {home[1]}\n\tHome overview: {home[3]} - {home[4]} - {home[5]} - Link to home: {home[6]}\n")

    # Send email
    connection.sendmail(from_addr=email,to_addrs=to_address, msg=f"Subject: Housing Data from Homes.com - {today}\n\n{email_body}")
    connection.close()
    print("SUCCESS: Email sent!")

except:
    email_body = "Error with emailing data. Check Daily Export folder and verify that files were uploaded properly. If file upload correct, troubleshoot housing_email.py file."
    connection.sendmail(from_addr=email,to_addrs=to_address, msg=f"Subject: ERROR: Housing Data from Homes.com - {today}\n\n{email_body}")
    connection.close()
    print("ERROR: No Data")