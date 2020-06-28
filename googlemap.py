import requests
from bs4 import BeautifulSoup
import bcolors
import sys,argparse

def banner():
          print("""
                
░██████╗░░░░░░░███╗░░░███╗░█████╗░██████╗░██╗░░██╗███████╗██╗░░░██╗███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██╔════╝░░░░░░░████╗░████║██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚██╗░██╔╝██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██║░░██╗░█████╗██╔████╔██║███████║██████╔╝█████═╝░█████╗░░░╚████╔╝░█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██║░░╚██╗╚════╝██║╚██╔╝██║██╔══██║██╔═══╝░██╔═██╗░██╔══╝░░░░╚██╔╝░░██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
╚██████╔╝░░░░░░██║░╚═╝░██║██║░░██║██║░░░░░██║░╚██╗███████╗░░░██║░░░██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
░╚═════╝░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝░
                                                                                                  Code By: NG
              """
             )

if len(sys.argv) >1:
    banner()
    if(sys.argv[1] != 'u'):
        try:
            input_url = sys.argv[2]
            parser = argparse.ArgumentParser()
            parser.add_argument("-d", required=True)

            input_code = requests.get(input_url)
            soup = BeautifulSoup(input_code.text,'html.parser')
            try:
                for search in soup.find_all('script'):
                    text = search.get('src',search.get('src'))

                    if(text!=None):
                        if 'https://maps.googleapis.com/maps/api/js?key' in text:
                            print(bcolors.OKMSG + "GOOGLE MAP Api Key Found:" + input_url)
                            print(text)
            except:
                print(bcolors.ERRMSG + 'Key does not exists in given URL')
        except:
            print(bcolors.OKMSG + 'Please enter python googlemap.py -u <valid URL with https:// or http://> ')
    elif (sys.argv[1] == '-h') :
        print(bcolors.BOLD + 'usage: googlemap.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-u URL,   --url URL where you want to search google map api key')
    elif (sys.argv[1] != '-u') :
        print(bcolors.OKMSG + 'Please enter -u < valid URL with http:// or https:// >')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -u or -h, with a valid URL')




