# サーバーサイドサンプルスクリプト

このディレクトリには、SimpleUDライブラリと連携するためのサーバーサイドのサンプルスクリプトが含まれています。

## uploader_e5796bd71a1642e97258a1835419f431.php

このPHPスクリプトは、SimpleUDライブラリからアップロードされたファイルを受け取り、サーバー上に保存するためのサンプルです。

### 機能

- POSTリクエストでアップロードされたファイルを処理
- アップロードされたファイルを`uploaded_files_e5796bd71a1642e97258a1835419f431`ディレクトリに保存
- 保存先ディレクトリが存在しない場合は自動的に作成

### 使用方法

1. このスクリプトをWebサーバー（Apache、Nginxなど）が実行できる場所に配置します
2. 必要に応じて、ファイルの保存先ディレクトリやファイル拡張子の制限などを編集します
3. SimpleUDライブラリの設定で、このスクリプトのURLを指定します

```python
from simpleud import FileUploaderDownloader

uploader = FileUploaderDownloader(
    server_address='https://your-server.com',
    upload_path='path/to/uploader_e5796bd71a1642e97258a1835419f431.php',
    download_base_path='uploaded_files_e5796bd71a1642e97258a1835419f431'
)
```

### セキュリティ上の注意

このスクリプトはサンプルであり、本番環境で使用する前に以下の点を考慮してください：

- ファイル拡張子の制限を設定する（現在はコメントアウトされています）
- ファイルサイズの制限を追加する
- ユーザー認証を実装する
- アップロードされたファイルのウイルススキャンを実施する
- 適切なエラーハンドリングを追加する