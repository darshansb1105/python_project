import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the machine name
    machine_name = socket.gethostname()
    
    # Get the IP address
    ip_address = socket.gethostbyname(machine_name)
    # HTML response with inline CSS for styling
    response = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
            }}
            .container {{
                text-align: center;
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
                margin: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, World!</h1>
            <p>Machine Name: {machine_name}</p>
            <p>IP Address: {ip_address}</p>
        </div>
    </body>
    </html>
    """

    return response

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port= 7000)
