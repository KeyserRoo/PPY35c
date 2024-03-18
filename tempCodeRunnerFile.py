ange(1000,10000):
        if m.pow(liczba%100,2)+m.pow((liczba-(liczba%100))/100,2) == item:
            print(item)
            liczba+=1