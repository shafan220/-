# -*- encoding=utf8 -*-
__author__ = "atyun0"

from airtest.core.api import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)


driver.get("https://cms-uat.moteach.com.cn/login")
driver.implicitly_wait(20)
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element_by_name("username").send_keys("superadmin@163.com")
driver.find_element_by_xpath("/html/body/mz-root/mz-login/div/div/div/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input").send_keys("atyun728")
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("/html/body/mz-root/mz-login/div/div/div/form/nz-form-item[3]/nz-form-control/div/span/button").click()
'''登录'''



driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-sider/div/ul/li[6]/div/span[2]").click()
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-sider/div/ul/li[6]/ul/ul/li[2]/a").click()
'''点击课程分类'''
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course-category/mz-search-group/div[2]/div/mz-table-button-list/div/button").click()

driver.find_element_by_name("name").send_keys("自动化测试课程分类")
driver.find_element_by_name("remark").send_keys("自动化测试")
driver.find_element_by_xpath("//button[@nztype='primary']").click()
'''新建课程分类'''


driver.find_elements_by_xpath("//a[contains(text(),'编辑')]")[0].click()
driver.find_element_by_name("name").send_keys("728")

driver.find_element_by_xpath("//button[@nztype='primary']").click()

driver.assert_template(Template(r"tpl1581687574894.png", record_pos=(3.84, 4.555), resolution=(100, 100)), "课程分类编辑功能正常")


driver.find_elements_by_xpath("//a[contains(text(),'添加子分类')]")[0].click()

driver.find_element_by_name("name").send_keys("auto课程子分类")
driver.find_element_by_xpath("//button[@nztype='primary']").click()

driver.find_element_css_selector("#cdk-drop-list-12 > tr:nth-child(1) > td:nth-child(1) > span.ant-table-row-expand-icon.ant-table-row-collapsed.ng-star-inserted").click()

driver.assert_template(Template(r"tpl1581687869673.png", record_pos=(3.755, 5.12), resolution=(100, 100)), "课程子分类新建功能正常")

driver.find_elements_by_xpath("//a[contains(text(),'删除')]")[1].click()
driver.airtest_touch(Template(r"tpl1581687982335.png", record_pos=(7.785, 2.445), resolution=(100, 100)))

driver.find_elements_by_xpath("//a[contains(text(),'删除')]")[0].click()

driver.airtest_touch(Template(r"tpl1581687982335.png", record_pos=(7.785, 2.445), resolution=(100, 100)))



'''
课程分类功能
'''
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-sider/div/ul/li[6]/ul/ul/li[3]/a").click()
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-gift/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[6]/a[2]").click()
driver.find_element_by_name("name").send_keys("728")


driver.find_element_by_xpath("//button[@nztype='primary']").click()


driver.assert_exist("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-gift/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[2]", "xpath", "赠品编辑功能正常")

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-gift/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[6]/a[2]").click()

driver.find_element_by_name("name").clear()
driver.find_element_by_name("name").send_keys("自动化测试赠品（勿删）")
driver.find_element_by_xpath("//button[@nztype='primary']").click()

driver.find_element_by_xpath("//input[@placeholder='请输入赠品名称']").send_keys("自动化测试赠品")
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-gift/mz-search-group/div[2]/div[2]/button").click()
driver.assert_exist("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-gift/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[2]", "xpath", "搜索功能正常")
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-gift/mz-search-group/div[2]/div[2]/button[2]").click()
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-gift/mz-search-group/div[2]/div[2]/button").click()
driver.assert_exist("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-gift/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr[2]/td[2]", "xpath", "清空搜索条件后搜索正常")












































'''
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-sider/div/ul/li[5]/div/span[2]").click()
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-sider/div/ul/li[5]/ul/ul/li/a").click()
driver.implicitly_wait(20)

driver.find_element_by_xpath("//a[@href='/dashboard/homework_module/homeworks/a6c53e85-47c7-4373-a934-43f0b6c14346/show']").click()

driver.assert_exist("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-show-homework/nz-spin/div/div/div", "xpath", "基本信息存在")
driver.assert_exist("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-show-homework/nz-spin/div/div[2]/div", "xpath", "布置作业数据存在")
driver.find_element_by_xpath("//a[@style='margin-left: 10px;']").click()

target = driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout")
driver.execute_script("arguments[0].scrollIntoView();",target)
下拉方法
以上为作业详情页面信息验证'''


'''
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-sider/div/ul/li[6]/div/span[2]").click()
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-sider/div/ul/li[6]/ul/ul/li[1]/a").click()
driver.implicitly_wait(20)


driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/mz-search-group/div[2]/div/mz-table-button-list/div/button").click()
driver.find_element_by_name("name").send_keys("自动化测试课程")
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-edit-course/nz-spin/div/div/div/nz-row/form/nz-form-item[2]/nz-form-control/div/span/mz-path-cascader/nz-cascader/div/div/span").click()


driver.airtest_touch(Template(r"tpl1581591506080.png", record_pos=(10.035, 3.96), resolution=(100, 100)))



driver.find_element_by_name("duration").send_keys("100")

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div[1]/mz-edit-course/nz-spin/div/div[1]/div[1]/nz-row/form/nz-form-item[5]/nz-form-control/div/span/nz-select/div/div/div").click()
driver.airtest_touch(Template(r"tpl1581591241579.png", record_pos=(4.825, 3.395), resolution=(100, 100)))



选择课程赠品，方法暂未找到



driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-edit-course/nz-spin/div/div[2]/button[2]").click()

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-edit-course/nz-spin/div/div[2]/button[2]").click()

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-edit-course/nz-spin/div/div/form/div[2]/nz-row/nz-form-item[2]/nz-form-control[3]/div/span/label/span/input").click()
driver.find_element_by_xpath("//div[@style='display: block;']").click()

driver.airtest_touch(Template(r"tpl1581663610685.png", record_pos=(4.935, 2.685), resolution=(100, 100)))
driver.airtest_touch(Template(r"tpl1581663720833.png", record_pos=(3.16, 4.26), resolution=(100, 100)))
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-edit-course/nz-spin/div/div[2]/button[2]").click()

driver.find_element_by_xpath("//button[@style='margin-top: 46px;']").click()

driver.assert_exist("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[2]", "xpath", "新建课程功能正常")




driver.find_element_by_xpath("//a[@href='/dashboard/course/courses/a318e9fd-e6c6-4a9d-a6da-5f93d9372f26']").click()
driver.implicitly_wait(20)

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-edit-course/nz-spin/div/div[2]/button[2]").click()

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-edit-course/nz-spin/div/div[2]/button[2]").click()

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-edit-course/nz-spin/div/div[2]/button[2]").click()

driver.assert_exist("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[2]", "xpath", "查看课程详情功能正常")
driver.implicitly_wait(20)

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[10]/a[4]").click()

driver.find_element_by_name("cost_price").clear()
driver.find_element_by_name("cost_price").send_keys("110")

driver.find_element_by_name("original_price").clear()
driver.find_element_by_name("original_price").send_keys("100")

driver.find_element_by_name("guide_price").clear()
driver.find_element_by_name("guide_price").send_keys("100")
driver.find_element_by_name("remark").send_keys("自动化测试输入备注信息")
driver.implicitly_wait(20)

driver.find_element_by_xpath("//button[@nztype='primary']").click()


driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[10]/a[4]").click()
driver.assert_exist("cost_price", "name", "课程成本价正常显示")
driver.assert_exist("original_price", "name", "课程原价正常显示")
driver.assert_exist("guide_price", "name", "课程销售指导价正常显示")
driver.assert_exist("remark", "name", "课程备注信息正常显示")

driver.find_element_by_xpath("//button[@nztype='default']").click()

driver.find_element_by_xpath("//input[@placeholder='请输入课程名称']").send_keys("自动化测试课程")
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/mz-search-group/div[2]/div[2]/button").click()

driver.assert_exist("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[2]", "xpath", "搜索功能正常")


driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/mz-search-group/div[2]/div[2]/button[2]").click()
driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/mz-search-group/div[2]/div[2]/button").click()


driver.assert_exist("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr[2]/td[2]", "xpath", "清空搜索条件后搜索正常")

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[10]/a[3]").click()

driver.airtest_touch(Template(r"tpl1581665992477.png", record_pos=(7.115, 2.435), resolution=(100, 100)))

driver.find_element_by_xpath("/html/body/mz-root/mz-dashboard/nz-layout/nz-layout/nz-content/div/mz-course/nz-table/nz-spin/div/div/div/div/div/table/tbody/tr/td[10]/a[3]").click()

driver.airtest_touch(Template(r"tpl1581666008713.png", record_pos=(7.79, 2.445), resolution=(100, 100)))

'''





















