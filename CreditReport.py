# encoding:utf-8
import json
import time
import os
from selenium import webdriver
from CreditReportContent import CreditReportContent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CreditReport:
    def __init__(self, driver, url='http://10.107.97.132:23226/member/index'):
        self.list = []
        self.driver = driver
        self.url = url

    def login(self, account, password):
        driver = self.driver
        file_url = self.url
        driver.get(file_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        # 点击切换至AD密码验证
        # try:
        #     el = driver.find_element_by_xpath("//*[@id='ad']/a")
        #     el.click()
        # except:
        #     pass
        # 登录帐号密码
        try:
            try:
                driver.find_element_by_link_text('切换至AD密码验证').click()
            except Exception as e:
                print(e)

            elem = driver.find_element_by_xpath("//div[@class='ui-g-9']/input[@id='account']")
            elem.clear()
            elem.send_keys(account)
            elem = driver.find_element_by_xpath("//div[@class='ui-g-9']/input[@id='password']")
            elem.clear()
            elem.send_keys(password)
            # 登录
            elem = driver.find_element_by_xpath("//div[@class='ui-g-12']/button")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)

        #     try:
        #         driver.find_element_by_xpath('//p[contains(text(), "用户名或密码不正确")]')
        #     except Exception:
        #         print('用户名或密码正确')
        #     else:
        #         print('用户名或密码错误')
        #         raise Exception('用户名或密码错误')
        #
        except Exception as e:
            raise Exception('用户名或密码错误')


    def get_report(self, tax):
        driver = self.driver
        file_url = self.url
        driver.get(file_url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        # 从tax中提取comp_name,comp_code
        # 判断tax长度不能超过200,企业柜面系统一次访问只能查询200次任务
        name_list = []
        code_list = []
        for comp in tax:
            comp_name = comp['名称']
            comp_code = comp['基础信息']['组织机构代码 ']
            # tax去重
            if comp_name not in name_list:
                name_list.append(comp_name)
                code_list.append(comp_code)
        # 判断comp_code<=10
        for i in range(len(name_list)):
            content_dict = {}
            comp_name = name_list[i]
            comp_code = code_list[i]
            if len(comp_code) > 10:
                # return "企业组织机构代码不能超过10位"
                self.list.append(list)
                continue
                
            driver.implicitly_wait(10)
            # 点击人行企业征信
            el = driver.find_element_by_xpath("//ul[@class='sidebar-menu']/li[3]")
            el.click()
            # el.find_element_by_xpath("./ul/li[1]/a").click()
            el.find_element_by_link_text("查询任务提交").find_element_by_xpath("../a").click()
            # 切换到iframe标签,输入查询内容
            # frame = driver.find_element_by_id("mainFrame")
            frame = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id("mainFrame"))
            driver.switch_to.frame(frame)

            try:
                # 提交查询任务
                self.get_submit(comp_name, comp_code)

                # 点击查询报告
                self.click_submit(comp_name, comp_code)

                # 提取数据
                frame1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("//div[@class='layui-layer-content']/iframe"))
                driver.switch_to.frame(frame1)
                time.sleep(2)
                content_dict = CreditReportContent(driver).run()
                # self.list.append(content_dict)

            except:
                pass

            self.list.append(content_dict)            
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[0])

    def get_submit(self, comp_name, comp_code):
        driver = self.driver
        form = driver.find_element_by_id("myForm")
        name = form.find_element_by_id("entName")
        code = form.find_element_by_id("invecorpBorrcode")
        queryReason = form.find_element_by_id("queryReason")
        org = form.find_element_by_id("org")
        isAuth = form.find_element_by_xpath(".//input[@value='1']")
        search_login = form.find_element_by_id("search_button")
        photo = form.find_element_by_id("photo")
        authorize = form.find_element_by_id("authorize")
        name.clear()
        name.send_keys(comp_name)
        code.clear()
        code.send_keys(comp_code)
        # 获取证件照,授权书路径
        path = os.path.realpath('./查询结果已授权.png')
        photo.clear()
        photo.send_keys(path)
        authorize.clear()
        authorize.send_keys(path)
        s1 = Select(queryReason)
        s1.select_by_value("01")
        s2 = Select(org)
        s2.select_by_value("本部")
        isAuth.click()
        search_login.click()
        time.sleep(2)
        # 点击提交审批
        commit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dataGrid']/tbody/tr[1]/td[1]/a[1]")))
        commit.click()
        sure1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'layui-layer-btn0')))
        sure1.click()
        # 点击刷新
        refresh = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'refresh')))
        refresh.click()

    # 点击查看报告
    def click_submit(self, comp_name, comp_code):
        driver = self.driver
        time.sleep(5)
        statu = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("//*[@id='dataGrid']/tbody/tr[1]/td[9]"))
        # 判断报告状态是否成功,成功即生成了新查询报告
        if statu.text == '成功':
            t1 = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='dataGrid']/tbody/tr[1]/td[1]/a")))
            t1.click()
        elif statu.text == '查询中':
            num = 0
            while True:
                time.sleep(1)
                num += 1
                statu = WebDriverWait(driver, 20).until(
                    lambda driver: driver.find_element_by_xpath("//*[@id='dataGrid']/tbody/tr[1]/td[9]"))
                if statu.text == '成功':
                    t1 = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@id='dataGrid']/tbody/tr[1]/td[1]/a")))
                    t1.click()
                    break
                elif num == 50:
                    raise Exception('系统网络异常')
        else:
            # 报告状态出错,判断是否已有该企业查询报告
            # 分页
            ul_li = driver.find_elements_by_xpath("//ul[@class='pagination']/li")
            len_li = len(ul_li)
            num = True
            for i in range(len_li - 2):
                if num == False:
                    break
                if i > 0:
                    # 点击下一页
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    time.sleep(2)
                    next = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='page-next']/a")))
                    next.click()
                trs = WebDriverWait(driver, 50).until(lambda driver:driver.find_elements_by_xpath("//*[@id='dataGrid']/tbody/tr"))
                for ii in range(len(trs)):
                    # 等待tr下td标签加载完
                    tds = WebDriverWait(driver, 50).until(lambda driver: driver.find_elements_by_xpath("//*[@id='dataGrid']/tbody/tr[{}]/td".format(ii + 1)))
                    if (tds[2].text == comp_name or tds[3].text == comp_code) and tds[8].text == '成功':
                        t2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dataGrid']/tbody/tr[{}]/td[1]/a".format(ii + 1))))
                        driver.execute_script("arguments[0].scrollIntoView();", t2)
                        t2.click()
                        num = False
                        break
            else:
                raise Exception('无该企业查询报告')
        time.sleep(1)
        sure2 = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CLASS_NAME, "layui-layer-btn0")))
        sure2.click()
        time.sleep(3)

def login(driver, account, password, url='http://10.107.97.132:23226/member/index'):
    cr = CreditReport(driver, url)
    cr.login(account, password)

def run(driver, tax, url='http://10.107.97.132:23226/member/index'):
    cr = CreditReport(driver, url)
    cr.get_report(tax)
    return cr.list

# 调用test
# if __name__ == '__main__':
#     import utils
#     tax = [{'名称':'深圳市浩邦服饰有限公司27','基础信息':{'组织机构代码 ':'5586683827'}},{'名称':'深圳市浩邦服饰有限公司28','基础信息':{'组织机构代码 ':'5586683828'}},{'名称':'深圳市浩邦服饰有限公司13','基础信息':{'组织机构代码 ':'5586683813'}},{'名称':'深圳市浩邦服饰有限公司14','基础信息':{'组织机构代码 ':'5586683814'}},{'名称':'深圳市浩邦服饰有限公司15','基础信息':{'组织机构代码 ':'5586683815'}},{'名称':'深圳市浩邦服饰有限公司16','基础信息':{'组织机构代码 ':'5586683816'}},{'名称':'深圳市浩邦服饰有限公司17','基础信息':{'组织机构代码 ':'5586683817'}},{'名称':'深圳市浩邦服饰有限公司18','基础信息':{'组织机构代码 ':'5586683818'}},{'名称':'深圳市浩邦服饰有限公司8','基础信息':{'组织机构代码 ':'55866838-8'}},{'名称':'深圳市浩邦服饰有限公司9','基础信息':{'组织机构代码 ':'55866838-9'}},{'名称':'深圳市浩邦服饰有限公司10','基础信息':{'组织机构代码 ':'55866838'}}]
#     # driver = utils.ChromeBrowser()
#     driver = webdriver.Chrome()
#     try:
#         login(driver, 'lucaszxu', 'Abcd1234')
#         ll = run(driver, tax[:1])
#         # for l in ll:
#             # print(l)
#     except Exception as e:
#         print(e.args)
#     driver.close()
