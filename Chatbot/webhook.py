import requests, pycountry

from bs4 import BeautifulSoup
from flask import Flask, request, abort, make_response, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])

def webhook():
    req = request.get_json(force=True, silent=True)
    res = webHookResponse(req)
    msg = []
    for i in range(len(res)):
      temp = {
                "text": {
                    "text": [
                        res[i]
                    ]
                }
            }
      msg.append(temp)
    return make_response(jsonify({"fulfillmentMessages": msg
                                  }))
  

def webHookResponse(req):
    if req.get('queryResult').get('action') != 'Import/Export_Requirements':
        return None
    else:
        result = req.get('queryResult')
        parameters = result.get('parameters')
        CountryFrom = parameters.get('CountryFrom')
        CountryTo = parameters.get('CountryTo')
        return getRequirements(CountryFrom, CountryTo)
        
def getRequirements(countryA, countryB):
    msg = []
    url = 'https://www.ups.com/ga/CountryRegs?loc=en_MY'
    myobj = {'origcountry': str((pycountry.countries.get(name=countryA)).alpha_2), 
            'destcountry':str((pycountry.countries.get(name=countryB)).alpha_2), 
            'cat':['015', '016', '004', '007008', '002', '003'], 
            'ShowRegulations':'Show+Regulations'}
    htmlText = requests.post(url, data=myobj).text
    soup = BeautifulSoup(htmlText,'lxml')
    regulations = soup.find_all('div', class_="stepModFlex")
    for regulation in regulations:
        regulation_ls = []
        regulationTitle = regulation.find('h3', class_="nostep").text
        regulation_ls.append(('【' + regulationTitle + '】\n'))
        labels = regulation.find_all('label')
        for label in labels:
            content = label.find_next('dd').text
            regulation_ls.append(('~'+(label.text).strip()+'\n'))
            regulation_ls.append(((content.replace("UPS Malaysia Brokerage will provide advices on the contact details of SIRIM only.",""))+'\n'))
        msg.append(regulation_ls)

    output = []
    for i in msg:
        tempString = ''
        for n in i:
            tempString += str(n) + ' '
        tempString = tempString[:-1]
        output.append(tempString)
    return output
    

if __name__ == '__main__':
   app.run()   
   
