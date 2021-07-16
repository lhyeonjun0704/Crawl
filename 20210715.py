import pyautogui

# 파일 이미지를 통해서 좌표를 알아내고 클릭하는 코드
# num7 = pyautogui.locateCenterOnScreen('이미지파일')
# pyautogui.click(num7)


# 커서 위치를 스크린 샷을 찍고 파일로 저장을 시킨 뒤, 그 부분을 클릭하는 코드
# pyautogui.scrrenshot('저장할 이름', region=(1324, 789, 30, 30)) 커서위치 / 파일의 크기

# num1 = pyautogui.locateCenterOnScreen('파일이름')
# pyautogui.click(num1)


pyautogui.moveTo(40,10, 1)

pyautogui.click(clicks=2, interval=1)
