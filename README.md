# auto-sgin

## 前言
由于使用的是 基于微信web内核的api定位接口
所以不得不用python的pyautogui库来实现 找图 点击的操作来实现自动打卡

程序大致说明
输入网址->刷新界面->（登录用户）->点击进入打卡->循环点击直至出现确认提交按钮
中间为了更好的debug和确认打卡是否成功加入了用pythone的yagmail库来实现发送邮件输出打卡成功与否

使用说明：
建议对文件夹内的图片都进行重新截图 保存同样文件名覆盖

