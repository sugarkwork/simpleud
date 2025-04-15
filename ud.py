import os
import requests
import aiohttp
import asyncio
import time
from typing import Optional
import urllib3

# InsecureRequestWarningを非表示にする
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class FileUploaderDownloader:
    def __init__(
            self,
            server_address=None,
            upload_path=None,
            download_base_path=None
        ):
        # それぞれ未指定なら環境変数から読む
        server_address = server_address or os.environ.get('UPLOAD_DOWNLOAD_SERVER_ADDRESS')
        upload_path = upload_path or os.environ.get('UPLOAD_PATH')
        download_base_path = download_base_path or os.environ.get('DOWNLOAD_BASE_PATH')

        # いずれかがNoneの場合はエラー
        if not server_address or not upload_path or not download_base_path:
            raise ValueError(
                "server_address, upload_path, download_base_path のいずれかが指定されていません。"
                "引数で指定するか、環境変数"
                " UPLOAD_DOWNLOAD_SERVER_ADDRESS, UPLOAD_PATH, DOWNLOAD_BASE_PATH を設定してください。"
            )

        self.server_address = server_address.rstrip('/')
        self.upload_url = f"{self.server_address}/{upload_path.lstrip('/')}"
        self.download_base_url = f"{self.server_address}/{download_base_path.strip('/')}/"

    def upload(self, file_path, retries=3, retry_delay=1.0):
        filename = os.path.basename(file_path)
        for attempt in range(1, retries + 1):
            try:
                with open(file_path, 'rb') as f:
                    files = {'uploaded_file': (filename, f)}
                    response = requests.post(self.upload_url, files=files, verify=False)
                if response.status_code == 200:
                    print(f"Upload successful: {filename}")
                    return True
                elif response.status_code == 404:
                    print(f"Upload failed [404 Not Found]: {response.status_code} {response.text}")
                    return False
                else:
                    print(f"Upload failed (attempt {attempt}): {response.status_code} {response.text}")
            except Exception as e:
                print(f"Upload error (attempt {attempt}): {e}")
            if attempt < retries:
                time.sleep(retry_delay)
        print("Upload failed: max retries exceeded")
        return False

    def download(self, filename, save_path: Optional[str] = None, retries=3, retry_delay=1.0):
        url = self.download_base_url + filename
        for attempt in range(1, retries + 1):
            try:
                response = requests.get(url, verify=False)
                if response.status_code == 200:
                    if save_path is None:
                        save_path = filename
                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded: {filename} --> {save_path}")
                    return True
                elif response.status_code == 404:
                    print(f"Download failed [404 Not Found]: {response.status_code} {response.text}")
                    return False
                else:
                    print(f"Download failed (attempt {attempt}): {response.status_code} {response.text}")
            except Exception as e:
                print(f"Download error (attempt {attempt}): {e}")
            if attempt < retries:
                time.sleep(retry_delay)
        print("Download failed: max retries exceeded")
        return False

    async def async_upload(self, file_path, retries=3, retry_delay=1.0):
        filename = os.path.basename(file_path)
        for attempt in range(1, retries + 1):
            try:
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                    with open(file_path, 'rb') as f:
                        data = aiohttp.FormData()
                        data.add_field('uploaded_file', f, filename=filename)
                        async with session.post(self.upload_url, data=data) as resp:
                            status = resp.status
                            text = await resp.text()
                if status == 200:
                    print(f"Async upload successful: {filename}")
                    return True
                elif status == 404:
                    print(f"Async upload failed [404 Not Found]: {status} {text}")
                    return False
                else:
                    print(f"Async upload failed (attempt {attempt}): {status} {text}")
            except Exception as e:
                print(f"Async upload error (attempt {attempt}): {e}")
            if attempt < retries:
                await asyncio.sleep(retry_delay)
        print("Async upload failed: max retries exceeded")
        return False

    async def async_download(self, filename, save_path: Optional[str] = None, retries=3, retry_delay=1.0):
        url = self.download_base_url + filename
        for attempt in range(1, retries + 1):
            try:
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                    async with session.get(url) as resp:
                        status = resp.status
                        if status == 200:
                            if save_path is None:
                                save_path = filename
                            content = await resp.read()
                            with open(save_path, 'wb') as f:
                                f.write(content)
                            print(f"Async downloaded: {filename} --> {save_path}")
                            return True
                        elif status == 404:
                            text = await resp.text()
                            print(f"Async download failed [404 Not Found]: {status} {text}")
                            return False
                        else:
                            text = await resp.text()
                            print(f"Async download failed (attempt {attempt}): {status} {text}")
            except Exception as e:
                print(f"Async download error (attempt {attempt}): {e}")
            if attempt < retries:
                await asyncio.sleep(retry_delay)
        print("Async download failed: max retries exceeded")
        return False

# 使い方例（同期＆非同期）

if __name__ == '__main__':
    uploader = FileUploaderDownloader(
        server_address='https://api.sugar-knight.com',
        upload_path='uploader_e5796bd71a1642e97258a1835419f431.php',
        download_base_path='uploaded_files_e5796bd71a1642e97258a1835419f431'
    )

    # 同期アップロード
    uploader.upload('ud.py')

    # 同期ダウンロード
    uploader.download('ud.py', save_path='ud_temp.py')

    # 非同期アップロード＆ダウンロード
    async def main():
        await uploader.async_upload('ud_temp.py')
        await uploader.async_download('ud_temp.py', save_path='ud_temp2.py')

    asyncio.run(main())