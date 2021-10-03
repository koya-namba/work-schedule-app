# シフト管理アプリ

バイトのシフト管理を行うためのWebアプリ  
スタッフ（バイト）はシフトの申請，確認，削除，変更を行うことができる．  
管理者（社員）は全スタッフのシフトの登録，確認，削除，変更を行うことができる．  
また，スタッフの新規作成，登録情報の変更，削除を行うことができる．  
特別な機能として，お知らせ機能がある．この機能を用いることによりLINEなどで連絡を取る必要がなくなる．
 
# DEMO

[こちら](https://workscheduleapp.herokuapp.com/)で試すことができます．

スタッフにログインする際には，  
ID : e001  
PW : employee001

管理者にログインする際には，  
ID : m001  
PW : manager001


以下にWebアプリの画面を一部紹介します．

---

管理者の全スタッフのシフト管理画面（承認する前は黄色のバックカラーが表示される）

<img width="800" alt="スクリーンショット 2021-10-03 15 16 27" src="https://user-images.githubusercontent.com/82089820/135742481-7c8fd3ab-3fd5-4ba3-9fb5-03fcb6b3de4e.png">

スタッフのホーム画面（自分が作成したお知らせのみ編集・削除することができる）

<img width="700" alt="スクリーンショット 2021-10-03 15 15 11" src="https://user-images.githubusercontent.com/82089820/135742570-4439fa36-2ef7-42e9-87e2-554cd62976a0.png">

スタッフのシフト確認画面（管理者がシフトを確定したもののみ表示される）

<img height="800" alt="スクリーンショット 2021-10-03 15 15 45" src="https://user-images.githubusercontent.com/82089820/135742556-bf5bf475-66ec-4e69-953f-94624f46cd61.png">

# Future features
 
- [x] お知らせ機能の作成
- [ ] スタッフごとの月の総労働時間と給料
- [ ] スタッフが不足している日の表示
- [ ] 自動シフト作成機能
 
# Requirement
 
dj-database-url  0.5.0  
Django  3.1.13  
django-widget-tweaks  1.4.8   
gunicorn  20.1.0  
psycopg2  2.9.1  
whitenoise  5.3.0

# Installation
 
Dockerを用いて簡単に環境構築を行うことができます．

1.  リポジトリをクローン
```bash
git clone https://github.com/koya-namba/work-schedule-app.git
```
2. リポジトリを移動
```bash
cd work-schedule-app/work_schedule/settings/
```
3. local.pyを作成し,SECRET_KEYの作成．そして，以下を記述．
```python
DEBUG = TRUE

ALLOWED_HOSTS = []
```
4. リポジトリを移動
```bash
cd work-schedule-app/
```
5. コンテナを起動
```bash
docker-compose up
```

# Note
 
作成中のアプリのためバグがあった場合には，下記まで連絡をお願いします
 
# Author
 
* 作成者 ： 難波洸也
* 所属 ： 九州大学システム情報科学府
* E-mail ： namba.koya@arakawa-lab.com
* Portfolio : https://nmbsite.herokuapp.com/

# License
 
"シフト管理アプリ" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
