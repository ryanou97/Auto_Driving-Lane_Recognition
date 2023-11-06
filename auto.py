import cv2
import auto_module as m  # function皆放在這裡
import numpy as np
import Auto_info  # 儲存影片位置

# 建立 VideoCapture 物件
capture = cv2.VideoCapture(f'{Auto_info.path}\\road2.mp4')      # 建立 VideoCapture 物件

   
if capture.isOpened():
    while True:
        sucess, img = capture.read()
        if sucess:
            edge = m.get_edge(img)  # 邊緣偵測
            roi = m.get_roi(edge)   # 取得 ROI
            lines = cv2.HoughLinesP(image=roi,      # Hough 轉換
                                    rho=3,
                                    theta=np.pi/180,
                                    threshold=30,
                                    minLineLength=50,
                                    maxLineGap=40)
            # 取得左右 2 條平均線方程式
            avglines = m.get_avglines(lines)    
     
            if avglines is not None:

                # 取得要畫出的左右 2 條線段
                lines = m.get_sublines(img, avglines) 
                img = m.draw_lines(img, lines)      
             
            # 顯示影像
            cv2.imshow('Frame', img)      
        
        # 等待按鍵輸入，按下 Q or q 結束迴圈、關閉視窗與攝影機
        k = cv2.waitKey(1)               
        if k == ord('q') or k == ord('Q'): 
            print('exit')
            cv2.destroyAllWindows()
            capture.release()
            break
else:
    print('開啟攝影機失敗')
    
    