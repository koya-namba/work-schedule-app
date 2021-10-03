# シフト管理アプリ

[Heroku](https://workscheduleapp.herokuapp.com/)で試してみる

スタッフログイン  
ID：e001  
PW:employee001


管理者ログイン  
ID:m001  
PW:manager001

<img width="1327" alt="スクリーンショット 2021-10-03 15 16 27" src="https://user-images.githubusercontent.com/82089820/135742481-7c8fd3ab-3fd5-4ba3-9fb5-03fcb6b3de4e.png">
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
- Heroku
- Docker

## Future features

- [x] お知らせ機能の作成
- [ ] スタッフごとの月の総労働時間と給料
- [ ] スタッフが不足している日の表示
- [ ] 自動シフト作成機能

## License
[MIT](https://choosealicense.com/licenses/mit/)
