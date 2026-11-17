from http.server import HTTPServer,BaseHTTPRequestHandler
content='''
<html>
<head>
<title> Acer Laptop configuration </title>
<style>
    h1,h2{
       text-decoration: underline double;
       text-decoration-skip-ink:none;
    }
       html,body{
      height:100%;
       margin:0;
    }
        
html,body{
            height:100%;
            margin:0;
        }
        
        table,tr,th,td{
            border:5px solid rgb(89,169,72);
            border-collapse: collapse;
            padding:10px,15px;
            text-align:center;

        }
        body {
            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;
            heighy:100vh;
            margin:0;
            background-color:cyan;
        }
h1 
    {
    text-align:center;
    margin-bottom:20px;
    }
table
   {
     margin:0 auto;
    }

    </style>
    </head>
    <body>
<h2> R.Nithish B Tech(AIDS)</h2>
<h1> Acer laptop configuration </h1>

<table>
     <tr>
        <th>NO.</th>
        <th>Feature/component</th>
        <th>Laptop configuration</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Processor</td>
        <td>Intelcore</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Memory(RAM)</td>
        <td>16 GB DDR4</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Storage</td>
        <td>512 GB NVMe SSD</td>
    </tr>
    <tr>
       <td>4</td>
       <td>Display</td>
       <td>15.6-inch Full HD IPS</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Graphics (GPU)</td>
        <td> Intel Iris Xe Graphics</td>
    <tr>
       <td>6</td>
       <td>Operating system</td>
       <td>Windows 11 pro</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Connectivity & ports</td>
        <td>Wi-fi 6,Bluetooth,Usb-c,HDMI</td>
    <tr>
</table>
</body>
</html>'''
class Myserver(BaseHTTPRequestHandler):
 def do_GET(self):
    print("Get request received...")
    self.send_response(200)
    self.send_header("content-type","text/html")
    self.end_headers()
    self.wfile.write(content.encode())
print("This is my webserver")
server_address=('127.0.0.1',8000)
httpd = HTTPServer(server_address,Myserver)
httpd.serve_forever()