#!/usr/bin/python

from xml.dom.minidom import parse
from json import dumps
import codecs

def item_text(item,field):
    ret = item.getElementsByTagName(field)
    if ret is None: return "missing"
    if len(ret) < 1: return "missing"
    ret = ret[0]
    if ret is None: return "missing"
    ret = ret.childNodes
    if ret is None: return "missing"
    if len(ret) < 1: return "missing"
    ret = ret[0]
    ret = ret.wholeText
    if ret is None: return "missing"
    return ret

#BLOCKSIZE = 1024 * 1024
#with codecs.open('PriceFull7290055700007-0493-201506060350.xml', 'r', 'iso-8859-8') as src:
#        with codecs.open('PriceFull7290055700007-0493-201506060350.unicode.xml', 'w', 'utf-8') as dest:
#                while True:
#                        contents = src.read(BLOCKSIZE)
#                        if not contents: break
#                        dest.write(contents)

dom = parse('PriceFull7290055700007-0493-201506060350.xml')
root = dom.childNodes[0]
json_items = []
for item in root.getElementsByTagName('Item'):
        json_items.append({'PriceUpdateDate': item_text(item,'PriceUpdateDate')
                          ,'ItemCode': item_text(item,'ItemCode')
                          ,'ItemType': item_text(item,'ItemType')         
                          ,"ItemName": item_text(item,'ItemName')
                          ,"ManufacturerName": item_text(item,'ManufacturerName')
                          ,"ManufacturerCountry": item_text(item,'ManufacturerCountry')
                          ,"ManufacturerItemDescription": item_text(item, 'ManufacturerItemDescription')
                          ,"Quantity": item_text(item, 'Quantity')
                          ,"UnitOfMeasure": item_text(item, 'UnitOfMeasure')
                          ,"QtyInPackage": item_text(item, 'QtyInPackage')
                          ,"UnitOfMeasurePrice": item_text(item, 'UnitOfMeasurePrice')
                          ,"AllowDiscount": item_text(item, 'AllowDiscount')
                          ,"bIsWeighted": item_text(item, 'bIsWeighted')
                          ,"ItemPrice": item_text(item, 'ItemPrice')
                          ,"ItemStatus": item_text(item, 'ItemStatus')})

json = {'XmlDocVersion': item_text(root,'XmlDocVersion')
       ,'DllVerNo': "missing"
       ,'ChainId': item_text(root,'ChainId')
       ,"SubChainId": item_text(root,'SubChainId')
       ,"StoreId": item_text(root,'StoreId')
       ,"BikoretNo": item_text(root,'BikoretNo')
       ,"Items": json_items}
open('output','w').write(dumps(json, sort_keys=True, indent=4, separators=(',',': ')))
        
