import json

class Product(object):
    Name = ""
    pricePerKg = 0
    typeOfPlastic = ""
    ColourOfPlastic = ""
    WeightOfPlastic = ""
    DiameterOfPlastic = ""
    ProductCode = ""
    Brand = ""


class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
            return {
                    "Name" : obj.Name, 
                    "PricePerKg" :obj.pricePerKg, 
                    "typeOfPlastic":obj.typeOfPlastic, 
                    "ColourOfPlastic": obj.ColourOfPlastic, 
                    "WeightOfPlastic":obj.WeightOfPlastic, 
                    "DiameterOfPlastic": obj.DiameterOfPlastic,
                    "ProductCode":obj.ProductCode,
                    "Brand": obj.Brand
                   }







