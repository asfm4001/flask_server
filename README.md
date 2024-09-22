# Flasl簡單入門~
Hi there 👋🏼 如果你想要使用Flask架設一個網站，或許可以參考這個project
這裡幫助我紀錄如何建立flask server與你如何使用這個project(既使你完全沒有任何基礎知識也👌🏻)

---

##### clone project(複製project到你的電腦中)
首先，確定你的電腦已經安裝好python, git與vscode，接著使用vscode開啟儲存flask server位置。
我在"文件"當中新增一個名為 **"learnFlask"** 的檔案夾並開啟它，你可以任意決定想要位置建立你的flask server。
在下方終端機中執行 `git clone git@github.com:asfm4001/flask_server.git`

當下載完成後，執行 `ls`

可以看到learnFlask中有一個剛剛下載好的 **"flask_server"** 資料夾
> 如果你覺得終端機訊息太多看起來啊雜 🤯，試試 `clear` 清空畫面

這時，我們需要進入這個檔案夾當中，執行 `cd flask_server` 進入此檔案夾
> 你可以再次執行 `ls` 查看 **"flask_server"** 有哪些檔案

##### create enverment(建立虛擬環境)
在開始執行前，我們還有兩件事情要準備
1. 建立虛擬環境
2. 安裝flask使用的模組
   
每一台電腦的版本不盡相同，我們建立一個虛擬環境就像買了一台全新的電腦 🖥️ 一樣~
執行 `python3 -m venv .venv` 建立一個名為 **".venv"** 的虛擬環境。

> 一如往常，你可以決定任何想要的名稱，名稱前有 **`.`** 是因爲linux系統與mac os預設會將這些檔案設為隱藏

接著我們要進入 **.venv** ，執行 `source .venv/bin/activate` 後，可以看到命令列前多了 **(.venv)** 代表成功了！
> 退出虛擬環境可以執行 `deactivate` ，前方的 **(.venv)** 就會消失 😶‍🌫️

##### install models(安裝模組)
再來我們要安裝flask會使用到的模組，

執行 `pip list` 查看目前安裝的模組與版本 (沒意外目前應該只有 **pip** 與 **setuptools** 😂)
> 如果顯示以下警告訊息也不用太緊張，只是建議你將pip更新成新的版本~ 執行 `python3 -m pip install --upgrade pip` 即可
> <span style="color: GoldenRod ;">WARNING: 
> You are using pip version 21.x.x; however, version 24.2 is available.
> You should consider upgrading via the '/Users/username/Documents/learnFlask/flask_server/.venv/bin/python3 -m pip install --upgrade pip' command.</span>


我們會用到的模組都在 **"requirements.txt"** ，不過別擔心，逐一安裝太麻煩，執行 `pip install -r requirements.txt` 安裝此次用到的所有模組
> 下載完成後可以再次執行 `pip list` 查看我們安裝的模組 ✅

執行 `flask run` 我們的flask server就已經在運行了~ 🥳
在瀏覽器中進入http://127.0.0.1:5000 就可以看到網站
> 終端機出現以下訊息只是提醒你目前使用的是開發用的伺服器，避免使用在正式的網站
> <span style="color: Tomato ;">WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.</span>

最後，在終端機按下<kbd>Ctrl</kbd> + <kbd>c</kbd>即可關閉剛剛執行的flask server

##### what's you learn?
最後，我們再次複習一下使用到的操作
* git操作
  * `clone` &rarr; 將remote(雲端)的project下載到local(本地端)
* linux系統操作
  * `ls` &rarr; 顯示當前位置所有的檔案
  * `clear` &rarr; 清空當前頁面
* python虛擬環境操作
  * `python3 -m venv yourVenvName` &rarr; 建立一個名為 **"yourVenvName"** 的虛擬環境
  * `source yourVenvName/bin/activate` &rarr; 進入 **"yourVenvName"** 虛擬環境
  * `deactivate` &rarr; 退出虛擬環境
  * `pip list` &rarr; 查看已安裝的模組
* flask部署
  * `flask run` &rarr; 執行flask server
  * <kbd>Ctrl</kbd> + <kbd>c</kbd> &rarr; 終止程序
