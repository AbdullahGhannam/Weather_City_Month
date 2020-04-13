# Weather_City_Month

The purpose of this code is to extract monthly weather details for a city from "www.wunderground.com" website

## Prerequisites

### Software

ChromeDriver


### Packages

bs4

selenium

time

## Examples

### Saudi Arabia - Dammam, Riyadh, Jeddah and Taif Cities

```
url_DMM_Mar20 = 'https://www.wunderground.com/history/monthly/sa/dammam/OEDF/date/2020-3'
Wthr_DMM_Mar20 = Weather_City_Month(url_DMM_Mar20)

url_RUH_Mar20 = 'https://www.wunderground.com/history/monthly/sa/riyadh/OERK/date/2020-3'
Wthr_RUH_Mar20 = Weather_City_Month(url_RUH_Mar20)

url_JED_Mar20 = 'https://www.wunderground.com/history/monthly/sa/jeddah/OEJN/date/2020-3'
Wthr_JED_Mar20 = Weather_City_Month(url_JED_Mar20)

url_TIF_Mar20 = "https://www.wunderground.com/history/monthly/sa/ta'if/OETF/date/2020-3"
Wthr_TIF_Mar20 = Weather_City_Month(url_TIF_Mar20)
```

## Built With

* [Spyder](https://www.spyder-ide.org/) - Python IDE 
* [Python 3.7](https://www.python.org/downloads/release/python-370/) - Progrmaming Language


## Author

* **Abdullah Ghannam** - *Initial work* - [AbdullahGhannam](https://github.com/AbdullahGhannam)
