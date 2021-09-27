# AddPoint System | 加分系統

There are two languages in this README, please take the elevator of `Table of Contents`

此README有兩個語言版本，可以透過下列`目錄`抵達：


## Table of Contents | 目錄

- [[English Version] AddPoint System](#en-introduction)
- [[中文介紹] 加分系統](#cn-introduction)

<br>

# <span id="en-introduction">AddPoint System</span>

# Introduction

`Add Point System` developed when period of master degree for thesis experiment, which collects students activities on computer when courses and exams of programming. Analyze data of activies to know the learning is effective, ineffective, cheat or plagiarize. The students who are effective in learning can get points.

(Due to the lack of time, I didn't develop the feature of showing the adding points)

# Software Structure

![](https://mingjungyu.files.wordpress.com/2021/09/screen-shot-2021-09-27-at-5.53.47-pm.png)

The structure divided to `client` and `server`.

In client part is a desktop execute file developed by Python 2.7 and Tkinder interface package. Main features are identify the students number, call function of keyboard trace and getting website history, send activities data back to server after ending of courses or exams.

In server part, implemented api for receiving the request from client, process and store data in database, developed by Python and Django.

![](https://minayu0416.files.wordpress.com/2019/10/addpoint.png)

**Sorry, I didn't develop English version**

So this is the login page of AddPoint in desktop, students need to type their student number for identify in a grey square on the middle, press the button at the bottom and begin to take courses or exams of programming.

After press button, the program will call the feature of keyboard trace (`KEY/tryclipboard.py`) and when student finish the courses, it will call getting website history (`UR/UR.py`) and send data as request to the server.

The code in server is not exist, because it built on server of university before and I didn't backup the code.

The feature of server side was writing api for receiving HTTP request from client, process and save into database, developed by Django and analyze it.

Total cost time are 1.5 months in the situation of study and doing part-time job, developed with professor.

<br>

# <span id="cn-introduction">加分系統</span>

# 介紹

加分系統為本人於研究所時期為實驗所需開發之桌上型軟體，並撰寫碩士論文。

主要功能為收集學生於程式語言課程以及考試期間所有的電腦操作行為，並分析收集而來的資料，判定學生是屬於`有效學習`，`抄襲` 或 `作弊`，是否有做討論，查詢網路資源，是否有直接抄襲他人程式。

# 軟體架構

![](https://minayu0416.files.wordpress.com/2019/10/e89ea2e5b995e5bfabe785a7-2019-10-15-e4b88be58d886.08.10.png)

軟體架構分為 `client端` 與 `server端`。

client端為桌機程式，使用python 2.7 與 tkinder介面完成，主要功能為驗證學生身份，以及呼叫 `側錄鍵盤` 與 `讀取瀏覽器記錄` 功能讀取活動資料，並回送資料於 server端。

server端實作`api`，接收來自client端的`Request`，傳送資料，並儲存資料於資料庫待做分析，使用python之django框架實作。


![](https://minayu0416.files.wordpress.com/2019/10/addpoint.png)

桌機介面為驗證學生身份，紀錄學生學號作為資料庫儲存資料的primary key，送出後即呼叫 鍵盤側錄功能 `KEY/tryclipboard.py`，於學生結束作答時觸發 `UR/UR.py`檔擷取瀏覽器記錄資料，並發送 `request` 於server，將資料往server端傳輸。

server端由於當時架於學校伺服器，並未把程式碼載下做備份。

server端的功能為撰寫api 接收HTTP請求，並將傳送來的資料做分類，使用django架構將資料存進資料庫，並使用django原生後台與資料庫資料作分析。

全開發耗時約半工半讀情況下一個半月左右，有和同指導老師同學一同開發。

更多詳細開發細節可參考當時撰寫的部落格文章: [[碩論也瘋狂] 加分系統開發全記錄 (PYTHON)](https://minayu.site/categories/%E7%A2%A9%E8%AB%96%E4%B9%9F%E7%98%8B%E7%8B%82-%E5%8A%A0%E5%88%86%E7%B3%BB%E7%B5%B1%E9%96%8B%E7%99%BC%E5%85%A8%E8%A8%98%E9%8C%84-python/)