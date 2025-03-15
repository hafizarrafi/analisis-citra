<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Struktur Dataset dan File</title>
    <style>
        body { font-family: Arial, sans-serif; }
        ul { list-style-type: none; }
        .folder { font-weight: bold; color: #2E86C1; }
        .file { color: #28B463; }
    </style>
</head>
<body>
    <h2>Struktur Penempatan File dan Dataset</h2>
    <ul>
        <li class="folder">/dataset</li>
        <ul>
            <li class="folder">/train</li>
            <ul>
                <li class="folder">/batik_madura</li>
                <ul>
                    <li class="file">gambar1.jpg</li>
                    <li class="file">gambar2.jpg</li>
                </ul>
                <li class="folder">/non_batik_madura</li>
                <ul>
                    <li class="file">gambar1.jpg</li>
                    <li class="file">gambar2.jpg</li>
                </ul>
            </ul>
            <li class="folder">/test</li>
            <ul>
                <li class="folder">/batik_madura</li>
                <ul>
                    <li class="file">gambar3.jpg</li>
                </ul>
                <li class="folder">/non_batik_madura</li>
                <ul>
                    <li class="file">gambar3.jpg</li>
                </ul>
            </ul>
        </ul>
        <li class="folder">/model</li>
        <ul>
            <li class="file">model_batik.h5</li>
        </ul>
        <li class="file">cnn-batik-madura.py</li>
        <li class="file">requirements.txt</li>
    </ul>
</body>
</html>
