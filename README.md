# 介紹軟體

本加分系統為本人於研究所時期開發之桌上型軟體，目的為做實驗用，並撰寫碩士論文。

主要功能為收集學生於程式語言考試期間所有的鍵盤行為與Google資訊，並分析收集而來的資料，判定學生是屬於`有效學習`，`抄襲` 或 `作弊`，是否有做討論，查詢網路資源，是否有直接抄襲他人程式。

# 軟體架構

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d886.08.10.png)

本軟體分為 `client端` 與 `server端`。client端為桌機程式，使用python 2.7 與 tkinder介面完成，主要功能為驗證學生身份，以及呼叫 `側錄鍵盤` 與 `讀取瀏覽器記錄` 功能讀取活動資料，並回送資料於 server端。

server端實作`request api`，接收來自client端的`http 要求`，傳送資料，並儲存資料於資料庫待做分析，使用python之django框架實作。


![](https://minayu0416.files.wordpress.com/2019/10/addpoint.png)

桌機介面為驗證學生身份，紀錄學生學號作為資料庫儲存資料的主key，送出後即呼叫 鍵盤側錄功能 `KEY/tryclipboard.py`，於學生結束作答時觸發 `UR/UR.py`檔擷取瀏覽器記錄資料，並發送 `HTTP request`，於server。

server端由於當時架於學校伺服器，並未把程式碼載下做備份。

server端的功能為撰寫request api 接收HTTP請求，並將傳送來的資料做分類，使用django架構將資料存進資料庫，並使用django原生後台與資料庫資料作分析。

全開發耗時約半工半讀情況下一個半月左右，有和同指導老師同學一同開發。

更多詳細開發細節可參考當時撰寫的部落格文章: [[碩論也瘋狂] 加分系統開發全記錄 (PYTHON)](https://minayu.site/categories/%E7%A2%A9%E8%AB%96%E4%B9%9F%E7%98%8B%E7%8B%82-%E5%8A%A0%E5%88%86%E7%B3%BB%E7%B5%B1%E9%96%8B%E7%99%BC%E5%85%A8%E8%A8%98%E9%8C%84-python/)