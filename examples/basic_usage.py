"""
SimpleUDの基本的な使用例
"""
import os
from simpleud import FileUploaderDownloader

# サーバー情報を設定
SERVER_ADDRESS = "https://your-server.com"
UPLOAD_PATH = "upload.php"
DOWNLOAD_BASE_PATH = "uploaded_files"

def main():
    # インスタンスの作成
    uploader = FileUploaderDownloader(
        server_address=SERVER_ADDRESS,
        upload_path=UPLOAD_PATH,
        download_base_path=DOWNLOAD_BASE_PATH
    )
    
    # テスト用のファイルを作成
    with open("test_file.txt", "w") as f:
        f.write("This is a test file for SimpleUD.")
    
    print("=== 同期アップロードのテスト ===")
    upload_result = uploader.upload("test_file.txt")
    
    if upload_result:
        print("=== 同期ダウンロードのテスト ===")
        uploader.download("test_file.txt", save_path="downloaded_test_file.txt")
    
    # ファイルの内容を確認
    if os.path.exists("downloaded_test_file.txt"):
        with open("downloaded_test_file.txt", "r") as f:
            content = f.read()
            print(f"ダウンロードしたファイルの内容: {content}")

if __name__ == "__main__":
    main()