from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 导入WebDriverWait
from selenium.webdriver.support import expected_conditions as ec  # 导入等待条件所在的模块
from selenium.webdriver.common.by import By # 导入By
# 驱动火狐浏览器
browser = webdriver.Firefox()
# 调用get(),打开网址
browser.get("http://127.0.0.1:8080/oa")
"""
实现动态等待，判断用户名输入框出现则结束等待，立刻执行后续脚本
1、调用WebDriverWait(),需要将浏览器、等待时长、间隔时长（可以不传，默认间隔0.5秒）作为参数传入
2、调用until(),在until()方法中，使用expected_conditions模块下的presence_of_element_located()条件，
    判断用户名输入框出现
3、在presence_of_element_located()条件内，需要将元素的定位方式及对应的标示组织为一个元组作为参数传入
"""
# 设置动态等待，总共等待10秒，每个0.4秒检查一下name属性为"loginId"的元素是否出现，出现则条件成立停止等待
WebDriverWait(browser, 10, 0.4).until(ec.presence_of_element_located((By.NAME, "loginId"))).send_keys("lipw")
WebDriverWait(browser, 10, 0.4).until(ec.presence_of_element_located((By.NAME, "password"))).send_keys("l1234567")

#设置动态等待，总共等待10秒，每个0.4秒检查一下id属性为"button_submit"的元素是否可以点击，可以点击则条件成立停止等待
# 需要使用element_to_be_clickable()条件，需要将元素定位方式及对应标示组织为一个元组作为参数传入
WebDriverWait(browser, 10, 0.4).until(ec.element_to_be_clickable((By.ID, "button_submit"))).click()
# 设置动态等待，总共等待10秒，默认每隔0.5秒检查一下“新建事项”四个字是否出现在页面元素长，出现击则条件成立停止等待
# 需要使用text_to_be_present_in_element()条件，需要将元素定位方式及对应标示组织为一个元组作为参数及文本连个参数传入
xinjianshixiang_element = (By.XPATH, "/html/body/div[2]/div/div[1]/table/tbody/tr[3]/td/a")
WebDriverWait(browser, 10).until(ec.text_to_be_present_in_element(xinjianshixiang_element, "新建事项"))
browser.find_element_by_link_text("新建事项").click()
#设置动态等待，总共等待10秒，默认每隔0.5秒检查一下id为iframe_main的frame框架是否能切入，能则直接切入
# 使用frame_to_be_available_and_switch_to_it条件，参数与switch_to.frame()一样
WebDriverWait(browser, 10).until(ec.frame_to_be_available_and_switch_to_it("iframe_main"))  # 这行执行完成后，frame框架已经切入

WebDriverWait(browser, 10, 0.4).until(ec.presence_of_element_located((By.XPATH, '//input[@id="subject"]'))).send_keys("helloworld")
WebDriverWait(browser, 10, 0.4).until(ec.presence_of_element_located((By.XPATH, '//input[@id="trackInput"]'))).click()

# 流程选择框元素所在的frame框架与iframe_main框架同级，需要先从iframe_main切出再切入
# 从iframe_main框架内切出
browser.switch_to.default_content()

# 切入流程选择框所在的框架
frame_tuple = (By.XPATH, '//iframe[contains(@src, "/oa/common/components/selectemp/selectempforcollaborate.jsp?uuid")]')
# 设置动态等待10秒，每隔0.4秒检查一下xpath为'//iframe[contains(@src, "/oa/common/components/selectemp/selectempforcollaborate.jsp?uuid")]'的框架是否出现，出现则停止等待
liucheng_frame = WebDriverWait(browser, 10, 0.4).until(ec.presence_of_element_located(frame_tuple))
# 切入流程选择框所在的框架
browser.switch_to.frame(liucheng_frame)
WebDriverWait(browser, 10, 0.4).until(ec.presence_of_element_located((By.LINK_TEXT, "集团职能部"))).click()
WebDriverWait(browser, 10, 0.4).until(ec.presence_of_element_located((By.LINK_TEXT, "总经办"))).click()
# 动态等待，总经办下的张忠义是否出现，出现则执行后续脚本
person_tuple = (By.XPATH, "/html/body/div[2]/select/option[5]")
person_info = "张忠意　　　　　　副总经理"
WebDriverWait(browser, 10).until(ec.text_to_be_present_in_element(person_tuple, person_info))
# 定位全部添加按钮，并点击
browser.find_element_by_xpath('//button[@onclick="addAll()"]').click()
browser.find_element_by_xpath('//button[@title="确定"]').click()
# 流程图所在frame框架与流程框所在frame框架同级，需要先从流程框frame框架切出再切入流程图所在框架
# 切出流程框所在框架
browser.switch_to.default_content()
# 切入流程图所在的frame框架
# 先定位流程图所在框架
liuchengtu_frame = browser.find_element_by_xpath("//iframe[contains(@src, '/oa/common/components/flowchart/newflowchart_svg.jsp?uuid')]")
WebDriverWait(browser, 10).until(ec.frame_to_be_available_and_switch_to_it(liuchengtu_frame))  # 切入流程图所在的frame框架
# 动态等待流程图上的确定按钮是否出现，出现停止等待并点击
WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#button_cancel"))).click()
# 切出流程图所在框架
browser.switch_to.default_content()
# 切入iframe_main框架
browser.switch_to.frame("iframe_main")
# 切入文本框所在框架
browser.switch_to.frame("baidu_editor_0")
# 定位正文输入框，输入内容
browser.find_element_by_xpath("/html/body").send_keys("hello, world!!!")
# 立即发送按钮在iframe_main框架内，iframe_main为baidu_editor_0的上层框架，返回上层框架
browser.switch_to.parent_frame()
# 定位立即发送，并点击
browser.find_element_by_id("button_send").click()

# 发送成功的弹窗不在任何frame框架内，需要切出当前所在的iframe_main框架，再定位
browser.switch_to.default_content()
browser.find_element_by_css_selector(".d-button").click()
browser.quit()

