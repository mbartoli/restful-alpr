# restful-alpr
RESTful API for Automatic License Plate Recognition
<br /><br />
##Setup##
Start the docker container and run the API on port 3000:
```
docker run -p 3000:3000 mbartoli/restful-alpr 
```
<br />
##Example usage##
Consider the following image:
<br /><br />
![](http://www.plateshack.com/y2k/Pennsylvania5/pa2013invertcar.jpg)
<br />We can send the URL of the image to the API using the following curl request:
```
curl http://localhost:3000/alpr /
   -d "data=http://www.plateshack.com/y2k/Pennsylvania5/pa2013invertcar.jpg" -X PUT
```
<br /> 
```
{
    "data_type": "alpr_results", 
    "epoch_time": 1456566569022, 
    "img_height": 923, 
    "img_width": 1577, 
    "processing_time_ms": 218.515839, 
    "regions_of_interest": [], 
    "results": [
        {
            "candidates": [
                {
                    "confidence": 91.700233, 
                    "matches_template": 0, 
                    "plate": "HSD4671"
                }, 
                {
                    "confidence": 84.521851, 
                    "matches_template": 0, 
                    "plate": "H5D4671"
                }, 
                {
                    "confidence": 83.895523, 
                    "matches_template": 0, 
                    "plate": "HSD467I"
                }, 
                {
                    "confidence": 83.370445, 
                    "matches_template": 0, 
                    "plate": "HSD467"
                }, 
                {
                    "confidence": 82.676369, 
                    "matches_template": 0, 
                    "plate": "HS04671"
                }, 
                {
                    "confidence": 82.327644, 
                    "matches_template": 0, 
                    "plate": "HSO4671"
                }, 
                {
                    "confidence": 81.877251, 
                    "matches_template": 0, 
                    "plate": "HSQ4671"
                }, 
                {
                    "confidence": 81.036522, 
                    "matches_template": 0, 
                    "plate": "HSB4671"
                }, 
                {
                    "confidence": 77.992264, 
                    "matches_template": 0, 
                    "plate": "HSU4671"
                }, 
                {
                    "confidence": 76.71714, 
                    "matches_template": 0, 
                    "plate": "H5D467I"
                }
            ], 
            "confidence": 91.700233, 
            "coordinates": [
                {
                    "x": 643, 
                    "y": 602
                }, 
                {
                    "x": 915, 
                    "y": 598
                }, 
                {
                    "x": 920, 
                    "y": 726
                }, 
                {
                    "x": 644, 
                    "y": 730
                }
            ], 
            "matches_template": 0, 
            "plate": "HSD4671", 
            "plate_index": 0, 
            "processing_time_ms": 11.670319, 
            "region": "", 
            "region_confidence": 0, 
            "requested_topn": 10
        }
    ], 
    "version": 2
}
```

Docker Hub: [mbartoli/restful-alpr](https://hub.docker.com/r/mbartoli/restful-alpr/)
