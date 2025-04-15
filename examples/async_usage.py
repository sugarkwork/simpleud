"""
SimpleUDの非同期処理の使用例
"""
import os
import asyncio
from simpleud import FileUploaderDownloader

# サーバー情報を設定
SERVER_ADDRESS = "https://your-server.com"
UPLOAD_PATH = "upload.php"
DOWNLOAD_BASE_PATH = "uploaded_files"

async def main():
    # インスタンスの作成
    uploader = FileUploaderDownloader(
        server_address=SERVER_ADDRESS,
        upload_path=UPLOAD_PATH,
        download_base_path=DOWNLOAD_BASE_PATH
    )
    
    # テスト用のファイルを作成
    with open("test_file_async.txt", "w") as f:
        f.write("This is an async test file for SimpleUD.")
    
    print("=== 非同期アップロードのテスト ===")
    upload_result = await uploader.async_upload("test_file_async.txt")
    
    if upload_result:
        print("=== 非同期ダウンロードのテスト ===")
        await uploader.async_download("test_file_async.txt", save_path="downloaded_test_file_async.txt")
    
    # ファイルの内容を確認
    if os.path.exists("downloaded_test_file_async.txt"):
        with open("downloaded_test_file_async.txt", "r") as f:
            content = f.read()
            print(f"ダウンロードしたファイルの内容: {content}")

if __name__ == "__main__":
    # 非同期処理の実行
    asyncio.run(main())