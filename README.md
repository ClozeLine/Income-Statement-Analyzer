# Income Statement Analzer

## Graph income data from any company. 

This is by no means a professional project, just something put together to test out a free version of an API.

This program uses:
- [FMP's API](https://site.financialmodelingprep.com/developer/docs)
- [CustomTKinter](https://felipetesc.github.io/CtkDocs/#/)
- [Matplotlib](https://matplotlib.org/stable/index.html)
- [Datetime](https://docs.python.org/3/library/datetime.html)
- [Requests](https://pypi.org/project/requests/)
  
  
Here are the instructions on how to set up your environment:
1. Start off by cloning my repo:
   ```
   git clone https://github.com/ClozeLine/Income-Statement-Analyzer.git
   ```
3. Create a virtual environment *(optional but highly reccomended to avoid cluttering)*:

   - ```python3 -m venv myvenv```: replace "myvenv" with the name of your virtual environment
4. Activate the virtual environment by running the activate script:
   - **Windows:** ```myenv\Scripts\activate```
   - **Unix or MacOS:** ```source myvenv/bin/activate```
5. Make sure you have [pip](https://pypi.org/project/pip/) installed
6. run these following commands:
   - ```pip install requests``` : for making request to the FMP API
   - ```pip install matplotlib```: to be able to visualize income statements as a graph
   - ```pip install customtkinter```: to be able to run the UI
  
   
Next, you will need to create you own API key to request data from FMP's servers
1. Create your account on [FMP's website](https://site.financialmodelingprep.com/)
2. Navigate to the API details tab on the left *(key icon)* and generate your key
3. In the code, keplace the ```API_KEY``` variable with your own
  
  *--> FMP and datetime do not need to be installed*

## How it works:
You first enter the ticker symbol of the company you wish to evaluate

Three types of data is available to plot:
1. <ins>**Currency:**</ins> For metrics over 1000$
2. <ins>**Ratio:**</ins> Scales in between 0 - 1
3. <ins>**Number:**</ins> For metrics under 1000$

Graph can be created from any three types, the graph will update and replace the last each time one is created _(no plotting two types at once)_.

Seeing as this is the free API plan, historical data only accounts for the past 5 years. However, if you wish to [purchase a premium plan](https://site.financialmodelingprep.com/developer/docs/pricing), you may replace the ```API_KEY``` variable in the script with your own, and alter the ```years``` variable to your liking.

## Picture of the Program
![Screenshot of the program in use](IncomeStatementAnalyzerScreenshot.png)

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Features to be added
- Tooltip: Hovering over the elements gives you their function
- Interactive Graph: Be able to zoom and move around the embedded graph
- Be able to download graphs
