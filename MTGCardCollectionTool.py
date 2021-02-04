
import requests
from django.template.defaultfilters import slugify  # To turn set and card names into URLs
from bs4 import BeautifulSoup

while True:
    print('\nWelcome to the MTG Card Collection Tool!')
    
    # Name of the card
    cardName = input('\nPlease enter an English card name: ')
    
    # Set the card was printed in
    setName = input('\nPlease enter the set name: ')
    
    # Condition of the card (NM, LP, MP, HP, D)
    cardCond = input('\nPlease enter the condition of the card as NM, LP, MP, HP, or D: ')
    
    # Determine if card is foil or not
    foilStatus = input('\nIs the card foil (y/n)?: ')
    
    # Summarize inputs and ask if correct
    print('\nCard: ' + cardName + '\nSet: ' + setName + '\nCondition: ' + cardCond + '\nFoil: ' + foilStatus)
    infoConfirm = input('\nIs the above correct? (y/n): ')
    
    # If the info is not correct, go back and input again
    if infoConfirm == 'n':
        print('\nOops! Let\'s try again.')
        continue
            
    # If the info is correct, execute the rest of the program
    elif infoConfirm == 'y':
        print('\nGreat! Let\'s get to work!')
        
    # Turn cardName into string of all lowercase characters with '-' between words using the Django slugify function    
    cardNameSearch = slugify(cardName)
    
    # Do the same with setName
    setNameSearch = slugify(setName)
    
    # Insert these into the URL
    # Example URL: https://shop.tcgplayer.com/magic/khans-of-tarkir/abzan-ascendancy
    # https://shop.tcgplayer.com/magic/<setNameSearch>/<cardNameSearch>
    
    searchTarget = requests.get(r'https://shop.tcgplayer.com/magic/' + setNameSearch + '/' + cardNameSearch)
    
    # Make a parsable response object
    searchContent = BeautifulSoup(searchTarget.text)
    
    # Find all instances of price data ( note double underscore )
    searchContent.find_all('td', {'class': 'price-point__data'}))
    
    
    break
    
    
    
    
    