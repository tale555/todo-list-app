# cron-job.orgでLINE通知を自動化する方法

## 🎯 目的

Renderの無料プランでは、15分間アクセスがないとスリープします。外部スケジューラーサービスを使って、定期的にアプリにアクセスして通知を送信します。

## 📋 手順

### ステップ1: cron-job.orgに登録

1. https://cron-job.org/ にアクセス
2. 「Sign up」をクリック
3. 無料アカウントを作成（メールアドレスとパスワード）

### ステップ2: 新しいcronジョブを作成

1. ダッシュボードで「Create cronjob」をクリック
2. 以下の設定を行う：

   - **Title**: `Todo List LINE通知`
   - **Address**: `https://todo-list-app-h6za.onrender.com/send-line-notifications`
   - **Schedule**: 
     - **Minutes**: `0`（毎時の0分）
     - **Hours**: `9`（9時）
     - **Days**: `*`（毎日）
     - **Months**: `*`（毎月）
     - **Weekdays**: `*`（毎週）
   - **Request method**: `GET`（または`POST`）
   - **Save**をクリック

### ステップ3: 動作確認

1. 「Test now」ボタンをクリックしてテスト
2. アプリのログを確認（Renderの「Logs」タブ）
3. LINEアプリで通知が届くか確認

## ⏰ 推奨設定

### 毎日1回（朝9時）

```
Minutes: 0
Hours: 9
Days: *
Months: *
Weekdays: *
```

### 毎日2回（朝9時と夜9時）

2つのcronジョブを作成：
1. 朝9時: `0 9 * * *`
2. 夜9時: `0 21 * * *`

### 毎時間

```
Minutes: 0
Hours: *
Days: *
Months: *
Weekdays: *
```

## 🔧 動作の流れ

1. **cron-job.orgがHTTPリクエストを送信**
   - 設定した時刻に、`https://todo-list-app-h6za.onrender.com/send-line-notifications`にアクセス

2. **アプリが起動**
   - スリープ中の場合、30秒程度で起動
   - 起動後、通知チェックを実行

3. **通知が送信**
   - 期日が3日前・前日・当日のTodoがある場合、LINEに通知が送信される

## ⚠️ 注意事項

1. **スリープからの復帰**: 初回アクセス時に30秒程度かかる
2. **通知のタイミング**: 設定した時刻に通知が送信される（少し遅れる可能性あり）
3. **無料プランの制限**: Renderの無料プランは月750時間まで

## 📝 その他の無料スケジューラーサービス

- **UptimeRobot**: https://uptimerobot.com/
- **Cronitor**: https://cronitor.io/
- **EasyCron**: https://www.easycron.com/

## ✅ 完了確認

設定後、以下を確認：

- [ ] cron-job.orgでcronジョブが作成された
- [ ] テスト実行が成功した
- [ ] アプリのログに通知送信の記録がある
- [ ] LINEアプリで通知が届いた

