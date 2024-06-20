def get_quotes_from_page(url):
    quotes = []
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad responses (e.g., 404)
        soup = BeautifulSoup(r.content, 'html5lib')

        # Find the div with id 'all_quotes'
        table = soup.find('div', attrs={'id': 'all_quotes'})

        if table:
            for row in table.findAll('div', attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
                quote = {}
                try:
                    # Check if h5 tag exists
                    h5_tag = row.find('h5')
                    if h5_tag:
                        quote['theme'] = h5_tag.text.strip()
                    else:
                        quote['theme'] = 'Unknown'

                    # Check if a tag exists
                    a_tag = row.find('a')
                    if a_tag and 'href' in a_tag.attrs:
                        quote['url'] = a_tag['href']
                    else:
                        quote['url'] = ''

                    # Check if img tag exists
                    img_tag = row.find('img')
                    if img_tag and 'src' in img_tag.attrs:
                        quote['img'] = img_tag['src']
                    else:
                        quote['img'] = ''

                    # Check if alt attribute of img tag exists
                    if img_tag and 'alt' in img_tag.attrs:
                        alt_text = img_tag['alt']
                        if " #" in alt_text:
                            quote['lines'], quote['author'] = alt_text.split(" #")
                        else:
                            quote['lines'] = alt_text
                            quote['author'] = 'Unknown'
                    else:
                        quote['lines'] = ''
                        quote['author'] = 'Unknown'

                    quotes.append(quote)
                except AttributeError as e:
                    print(f"Error processing row: {e}")
        else:
            print("Table with id 'all_quotes' not found on the page.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
    
    return quotes
