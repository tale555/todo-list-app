# ngrok URL確認方法

## 問題

入力されたURL: `https://aeromarine-colt-catoptrical.ngrok-free.dav`

このURLは間違っています。ngrokのURLは通常以下のいずれかで終わります：
- `.ngrok-free.app`
- `.ngrok-free.dev`

## 正しいURLの確認方法

### ステップ1: ngrokのターミナルを確認

ngrokを起動したターミナルで、以下のような行を探してください：

```
Forwarding  https://xxxx-xxxx-xxxx.ngrok-free.app -> http://localhost:5000
```

または

```
Forwarding  https://xxxx-xxxx-xxxx.ngrok-free.dev -> http://localhost:5000
```

### ステップ2: 正しいURLをコピー

`https://` から `.ngrok-free.app` または `.ngrok-free.dev` までの部分をコピーしてください。

例：
- ✅ 正しい: `https://aeromarine-colt-catoptrical.ngrok-free.dev`
- ❌ 間違い: `https://aeromarine-colt-catoptrical.ngrok-free.dav`

### ステップ3: LINE Developers Consoleで設定

正しいURL + `/line/webhook` を設定：

```
https://aeromarine-colt-catoptrical.ngrok-free.dev/line/webhook
```

## 注意事項

- ngrokのURLは起動するたびに変わります
- 必ずngrokのターミナル出力から最新のURLをコピーしてください
- ドメインが `.dav` で終わることはありません

