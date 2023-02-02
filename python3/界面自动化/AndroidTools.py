# coding: utf-8
# 点击屏幕微信图标启动微信，点击第一个联系人/群，发送一个报时消息

import sys
import os
import re
import time
from com.dtmilano.android.viewclient import ViewClient


def test():
    # 连接手机
    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device, serialno)
    # 按HOME键
    device.press('KEYCODE_HOME')
    time.sleep(3)
    # 找到微信图标
    vc.dump()
    weixin_button = vc.findViewWithTextOrRaise(u'微信')
    # 点击微信图标
    weixin_button.touch()
    time.sleep(10)
    # 找到第一个联系人/群
    # 可以使用UI Automator Viewer查看到对应第一个联系人/群的resource-id为"com.tencent.mm:id/auj"
    vc.dump()
    group_button = vc.findViewByIdOrRaise("com.tencent.mm:id/auj")
    # 点击进群
    group_button.touch()
    time.sleep(5)
    # 找到输入框并输入当前时间
    vc.dump()
    vc.findViewByIdOrRaise("com.tencent.mm:id/aep").setText('Now:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(3)
    # 点击发送按钮
    # vc.dump()
    # vc.findViewWithTextOrRaise(u'发送').touch()


if __name__ == '__main__':
    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device, serialno)
