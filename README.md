# GSimpleHTTPServer
GSimpleHTTPServer is a tool provided a feature to run SimpleHTTPServer with gevent.

## Getting Started
 1. Change you directory to project root.
 2. Make GSimpleHTTPServer virtualenv:
  ```
  $ make dev-init
  ```
  
 3. Activate the GSimpleHTTPServer virtualenv:
  ```
  $ source .dev/toggle
  ```
  
 4. Run `./demo/run_at_resources.py` to serve under the directory `./demo/resources/`
  ```
  $ env PYTHONPATH=. ./demo/run_at_resources.py 9096
  ```
  
 5. Put your files under the directory `./demo/resources/`

## Use upstart script
 1. Open the upstart script under the directory `./demo/` and change the paths
  ```
  $ vim ./demo/GSimpleHTTPServer.conf
  ```
  
 2. Copy the upstart script to `/etc/init/`
 3. Use `start GSimpleHTTPServer` to start and `stop GSimpleHTTPServer` to stop
