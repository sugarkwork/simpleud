<?php
// アップロードされたファイルを処理する
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['uploaded_file']) && $_FILES['uploaded_file']['error'] === UPLOAD_ERR_OK) {
        // ファイル情報の取得
        $fileTmpPath = $_FILES['uploaded_file']['tmp_name'];
        $fileName = $_FILES['uploaded_file']['name'];
        $fileSize = $_FILES['uploaded_file']['size'];
        $fileType = $_FILES['uploaded_file']['type'];
        $fileNameCmps = pathinfo($fileName);
        $fileExtension = strtolower($fileNameCmps['extension']);

        // 許可する拡張子の設定（必要に応じて追加・変更）
        //$allowedfileExtensions = array('jpg', 'gif', 'png', 'txt', 'pdf', 'zip', '7z', 'tar', 'tgz', 'pt', 'safetensor');

        #if (in_array($fileExtension, $allowedfileExtensions)) {
        if (TRUE) {
            // ファイルを保存するディレクトリ
            $uploadFileDir = './uploaded_files_e5796bd71a1642e97258a1835419f431/';
            
            // ディレクトリが存在しない場合は作成
            if (!is_dir($uploadFileDir)) {
                mkdir($uploadFileDir, 0755, true);
            }

            // ファイルの保存先パス
            $dest_path = $uploadFileDir . $fileName;

            // ファイルを移動
            if(move_uploaded_file($fileTmpPath, $dest_path)) 
            {
              echo 'ファイルは正常にアップロードされました。';
            }
            else 
            {
              echo 'ファイルの移動中にエラーが発生しました。';
            }
        }
        else {
            echo 'アップロードされたファイルの拡張子が許可されていません。';
        }
    }
    else {
        echo 'ファイルのアップロード中にエラーが発生しました。';
    }
}
else {
    echo '無効なリクエストです。';
}
?>