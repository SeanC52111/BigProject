from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

wd = webdriver.Firefox()
urladdr = "https://uc.tiup.cn/account/login?redirect_uri=https%3A%2F%2Fuc.tiup.cn%2Foauth2%2Fauthorize%3Fclient_id%3Dcn.tiup.ruc%26redirect_uri%3Dhttp%3A%2F%2Fapp.ruc.edu.cn%3A80%2Fidc%2Feducation%2Freport%2Fxscjreport%2FXscjReportAction.do%3Fmethod%253DprintXscjReport%2526xnd%253D2015-2016%2526xq%253D2%2526xh%253D2013201375%2526redirect_uri%253Dhttp%3A%2F%2Fapp.ruc.edu.cn%3A80%2Fidc%2Feducation%2Freport%2Fxscjreport%2FXscjReportAction.do%3Fmethod%25253DprintXscjReport%252526xnd%25253D2015-2016%252526xq%25253D2%252526xh%25253D2013201375%26response_type%3Dcode%26scope%3Dall%26state%3D0.8461759818958479%3A0.6265973001333563%26theme%3Dschools%26school_code%3Druc%26sso%3Dtrue&school_code=ruc&theme=schools"
wd.get(urladdr)

try:
    email = WebDriverWait(wd,timeout=10).until(EC.presence_of_element_located((By.ID,'username')),message=u'element load out of time')
    email.send_keys("2013201375")
    passwd = WebDriverWait(wd,timeout=10).until(EC.presence_of_element_located((By.ID,'password')),message=u'element load out of time')
    passwd.send_keys("220106199408129218")
    wd.find_element_by_xpath("//input[@value='登录']").click()
except NoSuchElementException as e:
    print(e.message)

somedom = WebDriverWait(wd,60).until(lambda brow: brow.find_elements_by_tag_name("table"))[0]
data = somedom.find_element_by_xpath("//*").get_attribute("outerHTML")
fp = open("web.txt",'w')
fp.write(data)
fp.close()
