import os
import subprocess
import time
import requests

def check_emulator():
    result = os.popen('adb devices').read()
    if '127.0.0.1:7555' not in result:
        print("模拟器未连接，正在尝试连接...")
        os.system('adb connect 127.0.0.1:7555')
        time.sleep(5)  # 等待模拟器连接
    else:
        print("模拟器已连接。")

def start_appium():
    print("Appium 服务器未启动，正在启动...")
    subprocess.Popen('appium', shell=True)
    time.sleep(10)  # 等待 Appium 启动

def check_appium():
    try:
        response = requests.get("http://127.0.0.1:4723/status")
        if response.status_code == 200:
            print("Appium 服务器已启动。")
        else:
            start_appium()
    except requests.exceptions.ConnectionError:
        start_appium()

        # 再次验证 Appium 是否启动成功
        for _ in range(5):
            try:
                response = requests.get("http://127.0.0.1:4723/status")
                if response.status_code == 200:
                    print("Appium 服务器已成功启动。")
                    return
            except requests.exceptions.ConnectionError:
                print("等待 Appium 服务器启动...")
                time.sleep(5)

        print("Appium 服务器启动失败，请检查配置。")
        exit(1)

def setup_environment():
    check_emulator()
    check_appium()

if __name__ == "__main__":
    setup_environment()
