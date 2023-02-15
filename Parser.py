import re
from bs4 import BeautifulSoup

def parse_email(filepath):
    # Read the HTML from the file
    with open(filepath, 'r') as f:
        html = f.read()

    #Make the HTML text lowercase
    html = html.lower()

    # Use Beautiful Soup to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    
    # Search for the shipping number    shipping_number = None
    shipping_number_patterns = ['tracking number', 'shipping number', 'shipping #', 'tracking #']
    for pattern in shipping_number_patterns: 
        shipping_number = soup.find(string=re.compile(pattern))
        if shipping_number:
            ##shipping_number = shipping_number.findNext('td').text[:40] 
            shipping_number = shipping_number.split(pattern)[1].strip()
            shipping_number = re.split(r'(\W+)', shipping_number)[2]
            shipping_number = shipping_number.upper()
            print("SN found from SOUP")
            break
    if not shipping_number:
        for pattern in shipping_number_patterns:
            shipping_number = re.search(r'{}\s*(\w+)'.format(pattern), text)
            if shipping_number:
             shipping_number = shipping_number.group(1)[:15]
             print("SN found from TEXT")
    if not shipping_number:
        shipping_number = ('Shipping Number Not Found')


    # Search for the shipping company
    shipping_company = None
    shipping_company_names = ['usps', 'amazon', 'ups', 'fedex', "dhl"]
    for name in shipping_company_names:
        shipping_company = soup.find(string=re.compile(name))
        if shipping_company:
            shipping_company = name.upper()
            break
    #If shipping company not found in html, search plain text 
    if not shipping_company:
        for name in shipping_company_names:
            shipping_company = re.search(r'{}'.format(name), text)
            if shipping_company:
             shipping_company = shipping_company.group(1)
    if not shipping_company:
        shipping_company = ('Shipping Company Not Found')


    # Search for the expected delivery date
    expected_delivery = None
    expected_delivery_patterns = ['expected delivery', 'estimated delivery', 'delivery date', 'shipping status', 'arriving']
    for pattern in expected_delivery_patterns:
        expected_delivery = soup.find(string=re.compile(pattern))
        if expected_delivery:
            expected_delivery = expected_delivery.findNext('td').text
            break
    #If expected delivery not found in html, search the plain text of the html file 
    if not expected_delivery:
        for pattern in expected_delivery_patterns:
            expected_delivery = re.search(r'{}\s*(\w+)'.format(pattern), text)
            if expected_delivery:
             expected_delivery = expected_delivery.group(1)
             break
    if not expected_delivery:
        expected_delivery = ('Expected Delivery Date Not Found')


    # Search for the order number
    order_number = None
    order_number_patterns = ['order number', 'order id', 'order number:', 'order #']
    for pattern in order_number_patterns:
        order_number = soup.find(string=re.compile(pattern))
        if order_number:
            ##order_number = order_number.findNext('td').text[:15]
            order_number = order_number.split(pattern)[1].strip()
            order_number = re.split(r'(\W+)', order_number)[2]
            print("ON found from SOUP")
            break
    #If order number not found in html, search the plain text of the html file 
    if not order_number:
        for pattern in order_number_patterns:
            order_number = re.search(r'{}\s*(\w+)'.format(pattern), text)
            if order_number:
             order_number = order_number.group(1)[:15]
             print("ON found from SOUP")
             break
    if not order_number:
        order_number = ('Order number not found')

    return shipping_number, shipping_company, expected_delivery, order_number.upper()


print(parse_email('/Users/User/Desktop/test.txt'))