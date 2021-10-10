import machine
import socket
relay=machine.Pin(2,machine.Pin.OUT)
relay.off()

x=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x.bind(('',80))
x.listen(5)
def web_page():
    if relay.value()==1:
        relay_state = 'ON'
        print('relay is ON')
    elif relay.value()==0:
        relay_state = 'OFF'
        print('relay is OFF')

    html_page = """   
      <html>   
      <head>   
       <meta content="width=device-width, initial-scale=1" name="viewport"></meta>   
      </head>   
      <body>   
        <center><h2>Relay Web Server</h2></center>   
        <center>   
         <form>   
          <button name="relay" type="submit" value="1"> relay ON</button>   
          <button name="relay" type="submit" value="0"> relay OFF </button>   
         </form>   
        </center>   
        <center><p>relay is now <strong>""" + relay_state + """</strong>.</p></center>   
      </body>   
      </html>"""  
    return html_page   

while True:
    # Socket accept() 
    conn, addr = x.accept()
    print("Got connection from %s" % str(addr))
    
    # Socket receive()
    request=conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))

    # Socket send()
    request = str(request)
    relay_on = request.find('/?relay=1')
    relay_off = request.find('/?relay=0')
    if relay_on == 6:
        print('relay ON')
        print(str(relay_on))
        relay.value(1)
    elif relay_off == 6:
        print('relay OFF')
        print(str(relay_off))
        relay.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    
    # Socket close()
    conn.close()