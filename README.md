<img src="./resource/logo/logo.007.png" alt="SecHuv-logo" style="width: 650px" />

# SecHuv
Security Hub for Human-vulnerabilities.

## システム構成
- SecHuv
    - SecHuv:Web
    - SecHuv:Mail
    - SecHuv:CHVE
    - SecHuv:Heart

## コミットルール
|emoji|意味|
|:-:|:-|
|✨|新規機能の追加|
|✏️|コードの追記|
|🐛|バグフィックス|
|🎨|リファクタリング|
|🔥|不要なデータの削除|
|📚|ドキュメントの追加|
|🐳|Docker関連|
|🔧|コンフィグファイルの追加|
|📦|外部モジュールの追加|

## Server
- `0.0.0.0:8080`: API Server
- `0.0.0.0:8000`: Web Server
- `0.0.0.0:5000`: Swagger-ui