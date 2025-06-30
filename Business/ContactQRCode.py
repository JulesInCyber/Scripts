from segno import helpers
# qrcode = helpers.make_vcard(name='Doe;John', displayname='John Doe',
#                             email='me@example.org', phone='+1234567')

'5-L'

# Input Variables
given_name = input("Vorname: ")
family_name = input("Nachname: ")
street_name = input("Straße + Hausnummer: ")
zip_code = input("Postleitzahl: ")
city_name = input("Stadt: ")
country_name = input("Land: ")
e_mail = input("E-Mail: ")
website_url = input("Webseite: ")
phone_num = input("Mobilnummer: ")
job_title = input("Job-Bezeichnung: ")
org_name = input("Arbeitgeber: ")

save_name = given_name + "_" + family_name

# Some params accept multiple values, like email, phone, url
vcard = helpers.make_vcard(name=f'{family_name}:{given_name}', 
                            displayname=f'{given_name} {family_name}',
                            street=street_name,
                            zipcode=zip_code,
                            city=city_name,
                            country=country_name,
                            email=e_mail,
                            url=website_url,
                            phone=phone_num,
                            title=job_title,
                            org=org_name
                            )
vcard.designator
vcard.save(f'{save_name}.svg', scale=5)