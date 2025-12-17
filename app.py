import http.server
import socketserver
import os

PORT = 8000

# Cambiar al directorio del proyecto
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor corriendo en http://localhost:{PORT}")
    print("Presiona Ctrl+C para detener el servidor")
    httpd.serve_forever()
