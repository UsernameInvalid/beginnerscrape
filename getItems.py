def getItems(soup):
    itemNames = soup.find_all(title='buyer-name')
    itemPrices = soup.find_all(class_='item-price')

    array = [itemNames, itemPrices]

    for column in range(len(array)):
        for row in range(len(array[column])):
            array[column][row] = array[column][row].text
    return itemNames, itemPrices
