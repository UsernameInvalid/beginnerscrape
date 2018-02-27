def getItems(soup):
    itemNames = soup.find_all(title='buyer-name')
    itemPrices = soup.find_all(class_='item-price')

    array = [itemNames, itemPrices]

    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = array[i][j].text
    return itemNames, itemPrices
