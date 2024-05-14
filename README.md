# Income Statement Analzer

## Graph income data from any company. 

This is by no means a professional project, just something put together to test out a free version of an API.

This program uses:
- [FMP's API](https://site.financialmodelingprep.com/developer/docs)
- [CustomTKinter](https://felipetesc.github.io/CtkDocs/#/)
- [Matplotlib](https://matplotlib.org/stable/index.html)

## How it works:
You first enter the ticker symbol of the company you wish to evaluate

Three types of data is available to plot:
1. <ins>**Currency:**</ins> For metrics over 1000$
2. <ins>**Ratio:**</ins> Scales in between 0 - 1
3. <ins>**Number:**</ins> For metrics under 1000$

Graph can be created from any three, the graph will update and replace the last each time one is created.

Seeing as this is the free API plan, historical data only accounts for the past 5 years.

However, if you wish to buy a premium plan, you may replace the ```API_KEY``` variable in the script, and alter the ```years``` variable to your liking.

## Picture of the Program
![Screenshot of the program in use](IncomeStatementAnalyzerScreenshot.png)
