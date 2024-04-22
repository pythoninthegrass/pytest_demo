#!/usr/bin/env python

import os
import psutil
import signal
import sys
from app import app
from decouple import config
from psutil import AccessDenied

port = config('PORT', default=8080, cast=int)


def start_server():
    print("Starting server")
    app.run(host='0.0.0.0',
            port=port,
            debug=True,
            use_reloader=True)


def stop_server(port):
    stopped = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for conns in proc.connections(kind='inet'):
                if conns.laddr.port == port:
                    os.kill(proc.pid, signal.SIGTERM)
                    stopped.append(proc.pid)
                    print(f"Successfully stopped process {proc.pid} on port {port}")
        except (AccessDenied, PermissionError):
            pass

    if not stopped:
        print(f"No process is running on port {port}")


def usage():
    print("Usage: python server.py <start|stop>")


def main():
    if len(sys.argv) >= 2:
        command = sys.argv[1]
    else:
        command = ""
    match command:
        case "start"|"":
            start_server()
        case "stop":
            stop_server(port)
        case _:
            usage()


if __name__ == '__main__':
    main()
