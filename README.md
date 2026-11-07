# エイメイ水谷 小学生イベントLP

小学生イベント（今回：11/28 板橋区科学館遠足）の告知ページ。静的HTMLのみ（ビルド不要）。

- `index.html` … ページ本体
- `img/` … チラシなどの画像

Vercel: 「Framework Preset: Other」、Build Command なし、Output Directory はルートのまま。

## 小学生イベントLP（どの校舎でも使えるテンプレート）

- テンプレート：`event.html`（設定ファイルを読みこんでページを作ります）
- 設定ファイル：`events/<校舎>-<イベント>-<年>.json` → 公開URLは `/e/<ファイル名>`
  - 例：`events/mizutani-kagakukan-2026.json`（LPメーカーの見本。水谷の遠足は元のページ `/` を使うので、このURLは `/` に転送）
- LPメーカー：https://eimei-event-lp.vercel.app/maker
  - フォームに入力するとプレビューが出ます。「設定ファイルを保存」で .json を書き出します。
  - 写真は「確認用リンク」には入りません。公開のときは画像を `img/` に置き、設定ファイルの画像欄を `/img/…` にします。
- テーマ：`sky`（遠足）、`space`（科学館）、`lab`（実験教室）、`halloween`、`christmas`、`summer`
