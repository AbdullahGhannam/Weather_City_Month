def Weather_City_Month(url_city_month):
    
    import bs4 as bs
    import time
    from selenium import webdriver
    import numpy as np
    
    browser = webdriver.Chrome()
    browser.get(url_city_month)
    time.sleep(30)
    WebPage = bs.BeautifulSoup(browser.page_source, "html.parser")
    browser.quit()
    
    DailyObservaionSection = WebPage.find_all('div',{"class":"small-12 columns has-sidebar"})[-1]
    DailyObservaionTable = DailyObservaionSection.table.tbody
        
    Values = []
    for tr in DailyObservaionTable.find_all('tr')[1:]:
        t_row = []
        for td in tr.find_all('td'): 
           t_row.append(td.text.replace('\n','').strip())
        Values.append(t_row)
    
    nDays = int(len(Values)/7)
    Wthr_CTY_MMMYY = np.reshape(Values, (7, nDays)).T
    
    # Temperature
    Wthr_CTY_MMMYY[0][1] = ['TMax', 'TAvg', 'TMin']
    # Dew Point
    Wthr_CTY_MMMYY[0][2] = ['DPMax', 'DPAvg', 'DPMin']
    # Humidity (%)	  
    Wthr_CTY_MMMYY[0][3] = ['HMax', 'HAvg', 'HMin']
    # Wind Speed
    Wthr_CTY_MMMYY[0][4] = ['WSMax', 'WSAvg', 'WSMin']
    # Pressure
    Wthr_CTY_MMMYY[0][5] = ['PMax', 'PAvg', 'PMin']
    # Precipitation 
    Wthr_CTY_MMMYY[2][6] = ['PrecTot']
    return (Wthr_CTY_MMMYY)
