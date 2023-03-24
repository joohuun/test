# selenium_uitest


- docker build
```
docker build -t chromedriver .
```

- run chromedriver
```
docker run --rm -d -v /tmp/.X11-unix:/tmp/.X11-unix --name chrome chromedriver
```

- test
```
docker exec -it chrome pytest app/test/wiprex/
```
```
docker exec -it chrome pytest app/test/tower/
```
- asaasd