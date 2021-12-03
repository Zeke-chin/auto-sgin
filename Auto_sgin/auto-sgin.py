'''
Author: zeke
Date: 2021-11-26 22:04:14
LastEditTime: 2021-12-04 02:50:00
LastEditors: Please set LastEditors
Description: 
FilePath: /undefined/Users/zeke/Downloads/自动打卡/auto-sgin.py
'''
import sys
import time
import pyautogui
import os
import yagmail


# 定义全局变量global_conten
global_conten = []


def conten(info):
    global global_conten
    global_conten += [info]


def send_email(sign):
    # 连接服务器
    # 用户名、授权码、服务器地址
    yag_server = yagmail.SMTP(user="zeke.chin@qq.com", password="lnyulwliwpgodjbe",
                              host='smtp.qq.com')

    # 发送对象列表
    email_to = ['zeke.chin@qq.com', ]
    email_title = '每日打卡'
    error_title = '今日打卡失败'
    success_content = '打卡成功'
    error_content = global_conten
    # 附件列表
    # email_attachments = ['./attachments/report.png', ]

    # 发送邮件
    if sign == 'success':
        yag_server.send(email_to, email_title, success_content, )
    else:
        yag_server.send(email_to, error_title, error_content, )
    # yag.send('taaa@126.com', 'subject', contents)

    # 关闭连接
    yag_server.close()


def choose_click(name):
    # 判断刷新按钮
    if name == "dad":
        if pyautogui.locateOnScreen('...1.png') is not None:
            only_click('...1.png')
            time.sleep(1)
            only_click('...2.png')
            time.sleep(1)
        elif pyautogui.locateOnScreen('...1_1.png') is not None:
            only_click('...2.png')
        else:
            conten("进入web出错")
            send_email(0)
            sys.exit()
            # print('进不去web')
            # send_email('进不去web')

    # 判断有未打卡
    if name == "clock":
        if pyautogui.locateOnScreen('clock_no.png') is not None:
            only_click('clock_no.png')
            return 0
        if pyautogui.locateOnScreen('clock_ok.png') is not None:
            conten('已打卡')
            # send_email('已打卡')
            send_email(0)
            sys.exit()


def only_click(png):
    x_png, y_png, width_png, height_png = pyautogui.locateOnScreen(png)
    pyautogui.click(x=x_png + 15, y=y_png + 15, button='left')


def click_png(png):
    if pyautogui.locateOnScreen('yes.png') is None:
        if pyautogui.locateOnScreen(png) is not None:
            only_click(png)
        else:
            conten("warning:{}".format(png))
    else:
        only_click('yes.png')
        send_email('success')



# 打开微信开发者工具
# os.system('D:\微信web开发者工具\微信开发者工具.exe')
# time.sleep(2)

# x_scrm,y_scrm = pyautogui.size()
# print ("当前屏幕的分辨率是{}*{}".format(x_scrm,y_scrm))
# x,y = pyautogui.position()
# print ("当前鼠标的X轴的位置为：{}，Y轴的位置为：{}".format(x,y))
# a = 'bar.png'
# x,y,width,height =  pyautogui.locateOnScreen(a)
# print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))


# 点击bar并输入地址
def in_web():
    # 输入地址
    x_bar, y_bar, width_bar, height_bar = pyautogui.locateOnScreen('bar.png')
    pyautogui.click(x=x_bar - 200, y=y_bar + 15, button='left')
    pyautogui.hotkey('ctrlleft', 'a', )
    time.sleep(2)
    pyautogui.typewrite(message="http://dk.zjsru.edu.cn/ILL_COLLEGE/index_Stu.aspx",
                        interval=0.01)
    pyautogui.hotkey('\n')
    time.sleep(2)

    # 刷新页面
    choose_click('dad')

    # time.sleep(1)
    # click_png('...2.png')
    # time.sleep(1)


def rec_prime():
    # 进入打卡

    count = 0  # while循环标志位
    while pyautogui.locateOnScreen('success.png') is None:
        click_png('clock_in1.png')
        time.sleep(2)
        click_png('clock_in2.png')
        time.sleep(3)
        click_png('clock_in3.png')
        time.sleep(2)
        click_png('clock_in4.png')
        time.sleep(2)
        click_png('yes_2.png')
        time.sleep(5)
        count = count + 1

        # 判断是否成功并发送邮件
        if count == 3:
            conten('rec_prime出错')
            send_email(0)
            sys.exit()

# 切换用户
def switch_user():
    click_png('user1.png')
    time.sleep(1)
    click_png('user2.png')
    time.sleep(1)
    click_png('user3.png')


def main():
    in_web()
    # switch_user()
    # pyautogui.typewrite(message='201904020811',
    #                     interval=0.01)
    # pyautogui.press('tab')
    # pyautogui.typewrite(message='021049',
    #                     interval=0.01)
    # choose_click('clock')
    if choose_click('clock') != 0:
        conten('已打卡')
        # send_email('已打卡')
        send_email(0)
    else:
        conten('未打卡 进入打卡0')

    rec_prime()


    # pyautogui.press('\n')
    # send_email("text2")
    # nd_two = np.array([[1, 2, 3], [4, 5, 6]])
    # print(nd_two)
    # in_web()
    #


if __name__ == '__main__':
    main()
