# Auto_Driving-Lane_Recognition
這個程式是用於自駕車道路識別的應用，主要透過影像處理和機器視覺技術，對道路進行線段檢測和識別。以下是程式的基本介紹和使用方法。

## 程式結構
這個程式分為兩個檔案：

auto.py: 主程式檔案，包含道路識別的主要邏輯。
auto_module.py: 自定義的函式，包含影像處理和機器視覺的相關功能。

## 使用方法
1. 確保你的環境中已經安裝了以下套件：
  ```bash
   pip install opencv-python numpy
  ```
2. 運行程式
  ```bash
   python auto.py
  ```
3. 影片輸入：程式會讀取路徑為 vedio\\road2.mp4 的影片檔案

4. 關閉程式：在視窗中按下 Q 鍵，或直接關閉視窗，程式將結束執行。

## 程式邏輯
1. 影片讀取：使用 OpenCV 的 VideoCapture 物件讀取影片。

2. 邊緣偵測：使用 Canny 邊緣檢測函數，將影片轉換為黑白並找到邊緣。

3. 取得 Region of Interest：定義一個多邊形區域（ROI），將邊緣影像中不需要的部分遮罩掉。

4. Hough 轉換：使用 HoughLinesP 函數檢測影像中的直線。

5. 取得平均直線：根據斜率將檢測到的直線分為左右兩組，並計算每組的平均直線。

6. 繪製直線：根據計算得到的平均直線，將其繪製在原始影像上，並繪製到圖片上緣1/3處位置。








