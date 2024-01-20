from sommatoria import Sommatoria
def media(array):
    lenght=len(array)
    sommatoria=Sommatoria(array)
    media=sommatoria/lenght
    print(media)
    return media
a=[1,2,3,4,5,6,7,8,9,10]
media(a)