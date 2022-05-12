SELECT COUNT(calibratedPM25) numberOfReadings,
       AVG(calibratedPM25) avgCalibratedPM25,
       msrDeviceNbr,
       deploymentName,
       deviceFriendlyName,
       DATE(readingDateTimeLocal) readingDateLocal,
       strftime('%H', readingDateTimeLocal) readingHourLocal,
       latitude,
       longitude,
       AVG(tempC) avgTempC,
       AVG(humidity) avgHumidity,
       AVG(pressure) avgPressure,
       AVG(pM25) avgPM25,
       AVG(pM10) avgPM10,
       AVG(pM1) avgPM1,
       AVG(aqi) avgAqi

FROM Readings

GROUP BY msrDeviceNbr, readingDateLocal, readingHourLocal