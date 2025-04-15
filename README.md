# SimpleUD

SimpleUDは、サーバーとの間でファイルをアップロード・ダウンロードするためのシンプルで使いやすいPythonライブラリです。

## 特徴

- 同期処理と非同期処理の両方をサポート
- リトライ機能を内蔵
- 環境変数からの設定読み込みをサポート
- シンプルで使いやすいAPI

## インストール

```bash
pip install simpleud
```

または、GitHubからソースコードをクローンしてインストールすることもできます：

```bash
git clone https://github.com/yourusername/simpleud.git
cd simpleud
pip install -e .
```

## 使用方法

### 基本的な使い方

```python
from simpleud import FileUploaderDownloader

# インスタンスの作成
uploader = FileUploaderDownloader(
    server_address='https://your-server.com',
    upload_path='upload.php',
    download_base_path='uploaded_files'
)

# 同期アップロード
uploader.upload('example.txt')

# 同期ダウンロード
uploader.download('example.txt', save_path='downloaded_example.txt')
```

### 非同期処理の使い方

```python
import asyncio
from simpleud import FileUploaderDownloader

async def main():
    # インスタンスの作成
    uploader = FileUploaderDownloader(
        server_address='https://your-server.com',
        upload_path='upload.php',
        download_base_path='uploaded_files'
    )
    
    # 非同期アップロード
    await uploader.async_upload('example.txt')
    
    # 非同期ダウンロード
    await uploader.async_download('example.txt', save_path='downloaded_example.txt')

# 非同期処理の実行
asyncio.run(main())
```

### 環境変数を使用する場合

環境変数を設定することで、コード内でサーバー情報を直接指定する必要がなくなります：

```bash
# 環境変数の設定
export UPLOAD_DOWNLOAD_SERVER_ADDRESS="https://your-server.com"
export UPLOAD_PATH="upload.php"
export DOWNLOAD_BASE_PATH="uploaded_files"
```

```python
from simpleud import FileUploaderDownloader

# 環境変数から設定を読み込む
uploader = FileUploaderDownloader()

# アップロード・ダウンロード
uploader.upload('example.txt')
uploader.download('example.txt')
```

## リトライ設定

アップロードとダウンロードのリトライ回数と待機時間を設定できます：

```python
# リトライ回数を5回、待機時間を2秒に設定
uploader.upload('example.txt', retries=5, retry_delay=2.0)
uploader.download('example.txt', retries=5, retry_delay=2.0)

# 非同期処理でも同様に設定可能
await uploader.async_upload('example.txt', retries=5, retry_delay=2.0)
await uploader.async_download('example.txt', retries=5, retry_delay=2.0)
```

## サーバーサイドの設定

SimpleUDを使用するには、ファイルをアップロードするためのサーバーサイドスクリプトが必要です。`examples/server`ディレクトリにサンプルのPHPスクリプトが用意されています：

```
examples/server/
├── README.md                                      # サーバーサイドスクリプトの説明
└── uploader_e5796bd71a1642e97258a1835419f431.php # アップロード処理用PHPスクリプト
```

このPHPスクリプトをWebサーバーにアップロードし、SimpleUDの設定で指定することで、ファイルのアップロード・ダウンロードが可能になります：

```python
from simpleud import FileUploaderDownloader

uploader = FileUploaderDownloader(
    server_address='https://your-server.com',
    upload_path='path/to/uploader_e5796bd71a1642e97258a1835419f431.php',
    download_base_path='uploaded_files_e5796bd71a1642e97258a1835419f431'
)
```

詳細な設定方法や注意点については、`examples/server/README.md`を参照してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。