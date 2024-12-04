# GitHubの使い方

Gitはインストールしてあるものとする  

## ユーザー名の登録
 ```Git
git config --global user.name 名前
 ```

## メールアドレスの登録  
```git
git config --global user.email アドレス
```

## 正常に登録されているかの確認
```git
git config --list
```  
コンフィグの設定項目がずらーっと出てくる  
  
githubのアカウント作成は省略します。  
  
## ローカルリポジトリを作る
プロジェクトのルートに移動した状態で  
```git
git init
```

## ローカルリポジトリにコミットする
コミットとはリポジトリへ追加や変更履歴を保存したるすること  

addで一時的に保存して  
```git
git add ファイル名
```  

commitでコミットする
```git
git commit -m "[Add] ファイル名 
```  
-mオプションはどういう変更なのか参照するためのメッセージを追加する  

logで変更履歴を確認する  
```git
git log
```

## リモートリポジトリにプッシュする
pushとは変更した内容をリモートリポジトリに反映させること  
  
ローカルリポジトリとリモートリポジトリを紐づける  
```git
git remote add origin https://github.com/ユーザー名/リモートリポジトリ名.git
```
  
pushする  
```git
git push origin master
```

## ブランチを作る
ブランチとは変更履歴を分岐すること  
他のブランチの影響を受けない  
  
ブランチを作成する  
```git
git branch sub1(ブランチ名) 
```  
  
ブランチが作成されたか確認  
```git
git branch
```


ブランチを移動する  
```git
git checkout sub1
```
  
作業中のブランチには*が付く  
```git
master  
*sub1
```
  
## ブランチにプッシュする
リモートリポジトリの時と同じでpushしたいブランチ名を指定する  
```git
git add ファイル名
git commit -m "変更内容コメント"
git push origin sub1
```

## ブランチからプルする  
プルとはこのように変更しますよという通知をする  
該当のブランチに移動して  
```git
git checkout sub1
```
  
プルする  
```git
git pull
```

## ブランチのマージをする  
マージとはプルされた変更等を反映させること  
主にmasterとマージさせる  
  
masterに移動して  
```git
git checkout master
```
  
マージしたいブランチを指定してマージする  
```git
git merge sub1
```

そしてリモートリポジトリにも反映させる  
```git
git push origin master
```

## ブランチを削除する  
必要なくなったブランチは削除する  
```git
git branch -d sub1
```
  
リモートリポジトリからも削除する  
```git
git push --delete origin sub1
```