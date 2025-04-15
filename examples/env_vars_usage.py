"""
SimpleUDの環境変数を使用した例
"""
import os
import asyncio
from simpleud import FileUploaderDownloader

def setup_env_vars():
    """環境変数を設定する（実際の使用時は.envファイルやシステムの環境変数として設定することを推奨）"""
    os.environ["UPLOAD_DOWNLOAD_SERVER_ADDRESS"] = "https://your-server.com"
    os.environ["UPLOAD_PATH"] = "upload.php"
    os.environ["DOWNLOAD_BASE_PATH"] = "uploaded_files"

async def main():
    # 環境変数を設定
    setup_env_vars()
    
    # 環境変数から設定を読み込む
    uploader = FileUploaderDownloader()
    
    # テスト用のファイルを作成
    with open("test_file_env.txt", "w") as f:
        f.write("This is a test file using environment variables.")
    
    # 同期処理
    print("=== 同期アップロードのテスト（環境変数使用）===")
    uploader.upload("test_file_env.txt")
    
    # 非同期処理
    print("=== 非同期アップロードのテスト（環境変数使用）===")
    await uploader.async_upload("test_file_env.txt")
    
    print("=== 非同期ダウンロードのテスト（環境変数使用）===")
    await uploader.async_download("test_file_env.txt", save_path="downloaded_test_file_env.txt")

if __name__ == "__main__":
    # 非同期処理の実行
    asyncio.run(main())