__author__ = 'Imran Khan'
# MarkerPen1 = {
#     'ink':'black',
#     'brand':'Read Leaf',
#     'Type':'Whitebroad'
# }
# MarkerPen2 = {
#     'ink':'blue',
#     'brand':'Read Leaf',
#     'Type':'parmanent',
#     'Barcode':'56446214521'
# }
# def open_cap(markar):
#     print('opening cap of',markar)
# def write_with(markar):
#     print('Writing in '+markar['ink']+' color')
class Markerpen(object):
    def __init__(self,ink,brand,type):
        self.ink = ink
        self.brand = brand
        self.type = type
    def write(self):
         print('Writing in ' + self.ink + ' color')

    def display(self):
        print('ink : ', self.ink, 'brand: ', self.brand,'type: ',self.type)

    def cap(self,action):
        # if action.lower() == 'open' or action.lower() == 'close':
        if action.lower() in ['open','close','bite']:
            print(action.lower() + 'ing cap')
        else:
            print('can not perform this '+action)
if __name__ == '__main__':
    pen1 = Markerpen('Black','Read Leaf','Whitebroad')
    pen2 = Markerpen('Blue', 'Read Leaf', 'Whitebroad')
    pen1 = pen3 = pen2
    print (pen1,pen2,pen3)
    print(pen1.display())
    print(pen2.display())
    pen1.write()
    pen1.cap('jump')
    print(type(pen1))
    print(type(1))
    # pen1.cap('opEn')
    # open_cap(MarkerPen1)
    # write_with(MarkerPen1)
    # open_cap(MarkerPen2)
    # write_with(MarkerPen2)


