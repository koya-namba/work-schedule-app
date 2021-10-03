# シフト管理アプリ

[HEROKU](https://workscheduleapp.herokuapp.com/)で試してみる

スタッフログイン  
ID：e001  
PW:employee001


管理者ログイン  
ID:m001  
PW:manager001

## About

シフトの管理をwebアプリで簡単に行うとができます．  
管理者はスタッフ，スタッフのシフト，お知らせを登録，修正，削除することができます．  
スタッフは自分のシフト，お知らせを登録，修正，削除することができます．

## Development

Dockerを用いて簡単に環境構築を行うことができます．

1.  リポジトリをクローン
```
git clone https://github.com/koya-namba/work-schedule-app.git
```
2. リポジトリを移動
```
cd work-schedule-app/work_schedule/settings/
```
3. local.pyを作成し,SECRET_KEYの作成．そして，以下を記述．
```
DEBUT = TRUE

ALLOWED_HOSTS = []
```
4. リポジトリを移動
```
cd work-schedule-app/
```
5. コンテナを起動
```
docker-compose up
```

## Technology used
- Python
- Django
- Postgresql
- HEROKU
- Docker

