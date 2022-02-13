import random as r
def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    
    last = 13
    rnd = r.randint( 0,last) 
    print(quotes[rnd])

if __name__== "__main__":
    primary()
