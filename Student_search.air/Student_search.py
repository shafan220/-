# -*- encoding=utf8 -*-
__author__ = "shafan"

from airtest.core.api import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

driver.get("https://cn.student.com")
driver.implicitly_wait(20)
#打开网页
driver.maximize_window()
driver.implicitly_wait(20)
#最大化窗口

inputvalue = "伦敦"
number = 10
driver.find_element_by_xpath("//input[@class='banner-search__search js-autocomplete autocomplete__input']").send_keys(inputvalue)
driver.implicitly_wait(20)
#在首页搜索框中输入内容
name="#home-hero-banner > div.banner-search > div > form > div:nth-child(1) > div "
def isCssElementExist(css):
    s = driver.find_elements_by_css_selector(css)
    driver.implicitly_wait(20)
    if len(s) ==  0:
        return False
    else :
        return driver.find_element_by_css_selector(css).is_displayed()
    #<editor-fold desc="搜索数据正确性检查">
def search_data_correct_check(inputname,number,name):
    i = 1
    allname = name + "> div > ul > li:nth-child("+ str(i) +")"
    msgresult = "下拉列表的选择项都包含输入数据"
    print(isCssElementExist(allname))
    while isCssElementExist(allname):  #循环判断数据正确性
        print(i)
        print("进入循环")
        print(isCssElementExist(allname))
        SchoolName = driver.find_element_by_css_selector(allname).text
        i = i + 1
        allname=name + "> div > ul > li:nth-child("+ str(i) +")"
        #header__search-suggestion > div > ul > li:nth-child(3)
        msgresult = "下拉列表的选择项都包含输入数据"
        assert_equal(inputvalue in SchoolName, True)
    assert_equal(i,number+1)
    #</editor-fold>          

search_data_correct_check(inputvalue,number,name)
#首页合法输入验证
driver.find_element_by_xpath("//input[@class='banner-search__search js-autocomplete autocomplete__input']").clear()
driver.implicitly_wait(20)
#首页删除输入内容
noneinputvalue = "      "
driver.find_element_by_xpath("//input[@class='banner-search__search js-autocomplete autocomplete__input']").send_keys(noneinputvalue)
driver.implicitly_wait(20)
nodataexist="//span[contains(text(),'搜索结果为零。试试其他关键字吧。')]"
driver.implicitly_wait(20)
driver.assert_exist(nodataexist, "xpath")
driver.implicitly_wait(20)
#首页搜索内容为不存在
#首页修改输入内容


inputvalue = "美国"
number = 10
driver.find_element_by_xpath("//*[@id=\"top\"]/header/div[2]/nav/ul[2]/li[3]/a").click()
driver.find_element_by_xpath("//input[@class='js-autocomplete header__search-input autocomplete__input']").send_keys(inputvalue)
name="#header__search-suggestion "
search_data_correct_check(inputvalue,number,name)
#头部搜索框合法输入验证
driver.find_element_by_xpath("//input[@class='js-autocomplete header__search-input autocomplete__input']").clear()
driver.implicitly_wait(20)
#头部搜索框删除输入内容
noneinputvalue = "      "
driver.find_element_by_xpath("//input[@class='js-autocomplete header__search-input autocomplete__input']").send_keys(noneinputvalue)
driver.implicitly_wait(20)
nodataexist="//span[contains(text(),'搜索结果为零。试试其他关键字吧。')]"
driver.implicitly_wait(20)
driver.assert_exist(nodataexist, "xpath")
driver.implicitly_wait(20)
#头部搜索框搜索内容为不存在
#头部搜索框修改输入内容




driver.quit()
        