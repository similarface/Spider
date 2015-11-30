#coding:utf-8

import json
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import demjson
from urllib.request import urlopen
"""
获取IP 电话 邮编  等基础信息工具
"""
class APIER():
    def getIpInfoFromFreefeoip(self,ipAddress):
        response=urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
        responseJson=json.loads(response)
        return responseJson

    def getIPinfoFromIP138(self,ipAddress):
        response=urlopen("http://www.ip138.com/ips138.asp?action=2&ip="+ipAddress).read().decode("gb2312")
        print(response)

    def getIpInfoFromTaobao(self,IPaddres):
        response=urlopen("http://ip.taobao.com/service/getIpInfo.php?ip="+IPaddres).read().decode('utf-8')
        responseJson=json.loads(response)
        return responseJson

    def getIpInfoFromSina(self,IPaddres):
        '''
        Sina Ip 信息查询
        '''
        response=urlopen("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip="+IPaddres).read().decode('utf-8')
        #responseJson=json.loads(response.split("=")[1].strip())
        return response.split("=")[1].strip()

    def getPhoneInfoFromIP138(self,phone,brekNum=5):
        '''
        获取电话号码信息
        phone:电话
        breakNum：如果不能正常获取次数进行5次重试 5次后返回空对象
        '''
        response=urlopen('http://www.ip138.com:8080/search.asp?action=mobile&mobile='+phone)
        soup=BeautifulSoup(response.read())
        table=soup.find_all("table")
        flag=True
        phoneList=[]
        phoneInfo={}
        #获取页面上的tab
        for tab in table:
            #因为页面tab没有id 而且有2个tab 这个flag开关将过滤掉第一个tab
            if flag:
                flag=False
            else:
                #tab的tr
                for tr in tab:
                    #TR下的td
                    for td in tr:
                        if td !=None and td!='\n':
                            try:
                                #将数据装入list
                                trText=td.get_text().strip()
                                if "++ ip138.com查询结果 ++"!=trText:
                                    phoneList.append(trText)
                            except AttributeError:
                                #如果出现错误将进行重新reload尝试
                                if brekNum<0:
                                    return json.dumps('')
                                return self.getPhoneInfoFromIP138(phone,brekNum-1)

        index=0
        lenList=len(phoneList)
        while index<lenList-1:
            phoneInfo[phoneList[index]]=phoneList[index+1]
            index=index+2
        return self.dictConvertJson(phoneInfo)

    def ListConvertdict(self,listType,flag=1):
        '''
        将list转换成字典
        :param listType:list
        :param dictType:dict
        :param flag:1:奇数位是key key＋1 是vlaue  2：偶数位是key key－1是values
        :return:
        '''
        dictType={}
        lenList=len(listType)
        index=0
        #奇数位index是key index＋1是vlaue
        if  flag==1:
            while index<lenList-1:
                dictType[listType[index]]=listType[index+1]
                index=index+2
        # 偶数index位是key index－1是value
        if flag==2:
            while index<lenList:
                dictType[listType[index+1]]=listType[index]
                index=index+2
        return dictType

    def dictConvertJson(self,dict):
        '''
        将字典转化成Json进行返回
        :param dict:字典
        :return:json对象
        '''
        return json.dumps(dict,sort_keys=True)

    '''
    outlook 12345.A
    Your API Key: NZ7AMCIHYO4UEKE8U
    Your Consumer Key: 3b3956728c1f7930636762e4eabf6516
    Your Shared Secret: 5WbJoFHEQr+lSL4YLH2upg
    '''
    def echonest(self):
        #http://developer.echonest.com/docs/v4
        #http://developer.echonest.com/api/v4/artist/songs?api_key=NZ7AMCIHYO4UEKE8U&id=AR5HF791187B9ABAF4&format=json&start=0&results=10
        #http://developer.echonest.com/api/v4/artist/songs?api_key=NZ7AMCIHYO4UEKE8U&name=see%20you%20again
        pass

    def Twitter(self):
        #https://dev.twitter.com/overview/api
        pass

    def google(self):

        pass

    def getIpCountry(self,json):
        return json.get("country_code")

if __name__ == "__main__":
    iper=APIER()
    #print(demjson.decode(iper.getPhoneInfoFromIP138('18080959929')))
    print(iper.getIpCountry(iper.getIpInfoFromFreefeoip("50.78.253.58")))