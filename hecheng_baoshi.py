# -*- coding: utf-8 -*-
heibaoshi = 140000
shelizi = 100000
yueliangshi = 70000
hongmanao = 75000
guangmangshi = 45000
taiangshi = 65000
xinghuishi = 120000

heibaoshi_1 = '黑宝石'
shelizi_1 = '舍利子'
yueliangshi_1 = '月亮石'
hongmanao_1 = '红玛瑙'
guangmangshi_1 = '光芒石'
taiangshi_1 = '太阳石'
xinghuishi_1 = '星辉石'

baoshi = {1:heibaoshi,2:shelizi,3:yueliangshi,4:hongmanao,5:guangmangshi,6:taiangshi,7:xinghuishi}
baoshi_1 = {1:'黑宝石',2:'舍利子',3:'月亮石',4:'红玛瑙',5:'光芒石',6:'太阳石',7:'星辉石'}

def wujia_list():
    print '==========================宝石物价=========================='
    print heibaoshi_1,heibaoshi
    print shelizi_1,shelizi
    print yueliangshi_1,yueliangshi
    print hongmanao_1,hongmanao
    print guangmangshi_1,guangmangshi
    print taiangshi_1,taiangshi 
    print xinghuishi_1,xinghuishi
    print '==========================宝石物价=========================='

class mul(object):
 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def show_mul(self):
        a = self.x * (2 ** (self.y - 1))
        return a
    
    def show_mul_1(self):
        a = self.x * (2 ** (self.y - 1))
        return a
    
    def show_dev(self):
        a = self.x / (2 ** (self.y - 1))
        return a

    def show_dev_1(self):
        a = self.x / (2 ** (self.y - 1))
        return a
        

def baoshijisuan():
    baoshi_name = int(input('请输入要计算的宝石:1.黑宝石,2舍利子,3月亮石,4红玛瑙,5光芒石,6太阳石,7星辉石:'))
    if baoshi_name < 1 or baoshi_name > 7:
        print '============================='
        print'宝石类型输入错啦！输入数字1~7哦'
        print '============================='
        return kaishi()
    baoshi_level = int(input('请输入要计算的等级:')) 
    if baoshi_level <0:
        print '============================='
        print'宝石最低等级是1级哦！'
        print '============================='
        return kaishi()

    if baoshi_name == 7 in baoshi.keys():
        zongjia = mul(baoshi[baoshi_name],baoshi_level,0)
        print '============================='
        print '计算宝石:',baoshi_1[baoshi_name],'等级:',baoshi_level,'总价为:',zongjia.show_mul_1()
        print '============================='
        kaishi()
    else:
        zongjia = mul(baoshi[baoshi_name],baoshi_level,0)
        print '============================='
        print '计算宝石:',baoshi_1[baoshi_name],'等级:',baoshi_level,'总价为:',zongjia.show_mul()
        print '============================='
        kaishi()

def baoshijisuan_1():
    baoshi_zongjia = int(input('请输入宝石价格:'))

    baoshi_leixing = int(input('请输入宝石种类1.黑宝石,2舍利子,3月亮石,4红玛瑙,5光芒石,6太阳石,7星辉石:'))

    baoshi_level = int(input('请输入要计算的等级:'))

    if baoshi_leixing < 1 or baoshi_leixing > 7:
        print '============================='
        print'宝石类型输入错啦！输入数字1~7哦'
        print '============================='
        return kaishi()

    if baoshi_level <0:
        print '============================='
        print'宝石等级没有0哦！'
        print '============================='
        return kaishi()

    if baoshi_leixing == 7 in baoshi.keys():
        zongjia = mul(baoshi_zongjia,baoshi_level,baoshi_leixing)
        print '============================='
        print '计算宝石:',baoshi_1[baoshi_leixing],'等级:',baoshi_level,'宝石单价为:',zongjia.show_dev_1(),'市场单价为:',baoshi[baoshi_leixing]
        print '============================='
        
        kaishi()  
    else:
        zongjia = mul(baoshi_zongjia,baoshi_level,baoshi_leixing)
        print '============================='
        print '计算宝石:',baoshi_1[baoshi_leixing],'等级:',baoshi_level,'宝石单价为:',zongjia.show_dev(),'市场单价为:',baoshi[baoshi_leixing]
        print '============================='
        
        kaishi()

def xiugai():
    xiugai_baoshi = input('请输入要修改的宝石类型1.黑宝石,2舍利子,3月亮石,4红玛瑙,5光芒石,6太阳石,7星辉石:')

    if xiugai_baoshi < 1 or xiugai_baoshi > 7:
        print '============================='
        print'宝石类型输入错啦！输入数字1~7哦'
        print '============================='
        return kaishi()

    xiugai_jiage = input('请输入要修改的价格:')

    if xiugai_baoshi in baoshi.keys():
        baoshi[xiugai_baoshi] = xiugai_jiage
        print '已修改宝石:',baoshi_1[xiugai_baoshi],'单价为:',baoshi[xiugai_baoshi]
        return kaishi()
def kaishi():
    xuqiu = int(input('请输入需要计算的内容:1.计算宝石价格,2.计算宝石单价,3.修改宝石价格:'))

    if xuqiu == 1:
        baoshijisuan()
    if xuqiu == 2:
        baoshijisuan_1()
    if xuqiu ==3:
        xiugai()

    if xuqiu != 1 or 2 or 3:
        print '输入错啦，请输入1/2/3'
        return kaishi()

wujia_list()
kaishi()