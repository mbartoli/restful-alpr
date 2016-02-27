# restful-alpr
RESTful Automatic License Plate Recognition
<br /><br />
Start the docker container and run the API on port 3000:
```
docker run -p 3000:3000 mbartoli/restful-alpr 
```
<br />
Example usage: 
```
curl http://localhost:3000/alpr -d "data=http://myurl.com/myimage.jpg" -X PUT
```
```
output
```
<br /><br /><br />
Note:
The current implementation requires starting the flask application manually. You can do this by running the following command
```
python /data/restful-alpr/alpr/restful-alpr.py
```

Docker Hub: [mbartoli/restful-alpr](https://hub.docker.com/r/mbartoli/restful-alpr/)
