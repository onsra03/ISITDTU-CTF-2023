<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="UploadImage.aspx.cs" Inherits="Dotnet101.Admin.UploadImage" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Upload file</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        .dropzone {
            border: 2px dashed #ccc;
            padding: 20px;
            text-align: center;
            font-size: 20px;
            cursor: pointer;
            margin-bottom: 20px;
        }

        .dropzone.highlight {
            border-color: #333;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div class="container">
            <h1>Upload ZIP File</h1>
            <div id="dropzone" class="dropzone" ondragover="dragOver(event)" ondrop="drop(event)">
                Drag and drop your ZIP file here or <asp:FileUpload ID="fileUpload" runat="server" />
            </div>
            <asp:Button ID="btnConvert" runat="server" Text="Upload" OnClick="btnUpload_Click" />
        </div>
    </form>

    <script>
        function dragOver(event) {
            event.preventDefault();
            document.getElementById('dropzone').classList.add('highlight');
        }

        function drop(event) {
            event.preventDefault();
            document.getElementById('dropzone').classList.remove('highlight');
            var files = event.dataTransfer.files;
            var fileUpload = document.getElementById('fileUpload');
            fileUpload.files = files;
        }
    </script>
</body>
</html>