from selenium import webdriver


import os
import time









def saveHTMLText(urlstr,filename):
    #driver=webdriver.PhantomJS()
    driver = webdriver.PhantomJS()
    time.sleep(2)
    driver.get(urlstr)
    time.sleep(2)
    file1=open(filename,'w',encoding='utf-8')
    file1.write(driver.page_source)
    file1.close()
    driver.close()




def getStrFromInt(intnum):
    strnum=str(intnum)

    while len(strnum)<8:
        strnum='0'+strnum
    return strnum





cwd = os.getcwd()
for ii in range(1000,1010):
    numstr = getStrFromInt(ii)
    print(numstr)

    txtFile1 = cwd + '/data/LN'+numstr+'.html'
    urlStr = r'https://www.labnetwork.com/frontend-app/p/#!/moleculedetails/LN' + numstr
    saveHTMLText(urlStr,txtFile1)



    #urlstr=r"https://www.labnetwork.com/frontend-app/p/#!/moleculedetails/LN00010025"




