from email import header
import json
from Objects.product import Product
from Objects.product import ProductEncoder
import os

def start_processing():
    f = open("items.json", "r")
    filedata = f.read()
    data = json.loads(filedata)
    os.remove("processeditems.json")
    newf = open("processeditems.json", "a")
    jsonstring = "["
    for product in data:
        newObject = Product()
        if(product['text'] is not None):
            newObject.pricePerKg = float(product['text'].encode("ascii", "ignore").decode().replace("/kg","").replace(',', '.'))
        else:
            newObject.pricePerKg = 0
        newObject.Brand = product['brand']
        newObject.typeOfPlastic = product['material']
        product['headers'].remove('Merken (Producent):')
        product['headers'].remove('Productsoorten:')
        for x in range(len(product['headers'])):
            header = product['headers'][x]
            if(header == 'Diameter:'):
                newObject.DiameterOfPlastic = product['values'][x]
            elif(header == 'Nettogewicht:'):
                newObject.WeightOfPlastic = product['values'][x]
            elif(header == 'Producentnummer:'):
                newObject.ProductCode = product['values'][x]
            elif(header == 'Kleur:'):
                newObject.ColourOfPlastic = product['values'][x]
            elif(header == 'Art. nr.:'):
                newObject.Name = product['values'][x]
        jsonstring = jsonstring + json.dumps(newObject, cls=ProductEncoder, indent = 4)
    newf.write(jsonstring + ']')

    f.close()
    #os.remove("items.json")
