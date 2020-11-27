import numpy as np
import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt


def tableToArray (soupTable):
    
    pandasTable = pd.read_html(str(soupTable))[0]
    years       = pandasTable.values[:, 0]
    population  = pandasTable.values[:, 1]
    
    shorty = False
    
    if type(population[0]) == float:
        shorty     = True
        population = population.astype(str)
    
    for i in range(len(years)):
        
        years[i]      = years[i][-5:].strip()
        years[i]      = years[i][0:4]
        population[i] = population[i].replace(".", "")
        population[i] = population[i].replace(" ", "")
        population[i] = population[i].replace("[17]", "")    # only for table2
        
        if shorty == True:
            population[i] = population[i][0:6]
        
        if len(population[i]) < 6:
            population[i] += "0"
    
    return(np.array([years, population]).astype(int))


def getTableInformation ():
    
    websiteInformation      = requests.get("https://de.wikipedia.org/wiki/Einwohnerentwicklung_von_Berlin")
    websiteInformation_soup = bs4.BeautifulSoup(websiteInformation.text, "lxml")
    
    tables = websiteInformation_soup.select("table")
    
    table1 = tables[12]
    table2 = tables[13]
    table3 = tables[14]
    
    table1 = tableToArray(table1)
    table2 = tableToArray(table2)
    table3 = tableToArray(table3)
    
    return(np.concatenate((table1, table2, table3), axis=1))


def plotPopulation ():

    data       = getTableInformation()
    year       = data[0]
    population = data[1]
    
    plt.figure(figsize=(5.9, 3.8))
    ax = plt.gca()
    plt.subplots_adjust(top=0.98, bottom=0.19, left=0.30, right=0.98)
    plt.rcParams.update({"font.size": 18})
    plt.plot(year, population, color="black", linewidth="2.0")
    ax.ticklabel_format(axis="y", style="plain")
    plt.xlabel("year", labelpad=5.0)
    plt.ylabel("population of Berlin", labelpad=5.0)
    plt.xlim(1834, 1906)
    plt.yticks([0, 500000, 1000000, 1500000, 2000000], ["0", "500.000", "1.000.000", "1.500.000", "2.000.000"])
    plt.ylim(0, 2350000)
    plt.grid(color="lightgray")
    plt.show()


plotPopulation()
