# univ-scraping-remake

## References  
[Refs](https://docs.djangoproject.com/ja/2.2/intro/tutorial01/)

- プログラムの流れ 
  1.フォームよりログイン 
    1. SQLよりチームIDに紐づいているデータベースを編集して表示
  1. フォームより登録
    1. チームリーダの場合、ID送付
      - 送付をformに入れてもらったところでデータベース使用可能
  
      
      

  データべース構造
 ```
table test(
id integer primary key,
team_id integer,
class integer);

外部キー
↓
table test2(
id integer primary key,
password integer,
foreign key (id) references test(team_id));


```


  
- Beautiful Soup(以下bs4)関数の設計

```python
  clacces1= {"spring1":{"Mondey":[(1,1,1)]}}
             #春　　　#月　　　#時限　 #あり1なし0 #前期後期判定
```
