# Chicago Air Quality Project

## What we did to analyze Microsoft’s air quality data
Microsoft gave us access to its Eclipse sensor data through the project’s API. The API acts as a pipeline to the 115 sensors around Chicago and the information those sensors have recorded for 10 months — every five minutes, every hour of the day.

To analyze this dataset the readings were first queried through the API, and then averaged by hour, day and month. At each aggregation step, a “data completion criteria” was applied to match the data quality standards laid out by the EPA for Hotspot Identification and Characterization. Any sensor’s aggregated reading which had a sampling rate of less than 75% in the defined aggregation period was excluded. We also looked for hyperlocal correlations of these sensors and removed any sensor that had anomalous readings.

To estimate how the reading of an individual sensor might explain pollution in specific zones, we used Inverse Distance Weighting, or IDW. This is a popular interpolation technique, which makes use the aggregated readings based on the sensor’s distance, to estimate the level of PM2.5 pollution in regions between sensors.

The reporters used this technique to estimate air quality levels at more than 50,000 uniformly distributed geocoordinates in the entire Chicago region and then generated tract level aggregated estimates. These estimates were then normalized based on the average estimated air quality in Chicago.

#### Note:
While IDW is a popular approach for modeling the spread of pollution in neighborhoods, estimates are not as accurate in regions with few nearby sensors. Microsoft’s research team also cautioned that interpolations outside the edges of the sample, like those in Cicero, will be more uncertain because the network was designed for the city of Chicago.

### Average particulate matter 2.5, or PM2.5, readings, July to October 2021, by census tract, and sensor locations
![image](https://user-images.githubusercontent.com/91643874/168393842-9a50fe95-61e6-492b-97f3-2f17e250b023.png)


## Project Setup

### Install the dependencies

``` pip install -r requirements.txt ```

### Setup Config

- Run the following to generate a `config.py` file

```cp config.sample config.py```

- Add the Microsoft API Token in the `config.py` file

```access_token = "..."```
