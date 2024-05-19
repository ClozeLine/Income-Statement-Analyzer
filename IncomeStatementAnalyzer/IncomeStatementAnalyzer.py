import requests
import matplotlib.pyplot as plt
from tooltip import Tooltip
from matplotlib.ticker import FuncFormatter, FormatStrFormatter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import datetime
import customtkinter as ctk

# Custom tkinter settings and initiation
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+%d+%d" % (width, height, 0, 0))
root.title("Income Statement Analyzer")

# Set up URL for request
base_url = 'https://financialmodelingprep.com/api'
data_type = "income-statement"
API_KEY = "929oEJGUb1m3ssPjHwgSPcyf2thP2Ym9"  # This is not a real key
years = 5


def manage_display():
    """
    ---> This function plots a sample chart to give visual indication to the user as to the position of
    to-be generated graphs
    :return: n/a
    """
    plot(None, [], "ratio")
    root.mainloop()


def get_input_ticker():
    """
    -> This function will retrieve the user input. If input is a valid ticker (requested json is not empty),
    then returns the user input as ticker symbol.
    :return:
    """
    global data
    user_input = ticker_entry.get().upper()
    url = f'{base_url}/v3/{data_type}/{user_input}?limit={years}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if len(data) == 0:
        ticker_message_label.configure(text="Invalid Ticker", text_color="#DC392E")
    else:
        ticker_message_label.configure(text=f"Currently Viewing: {user_input}", text_color="white")
        return user_input


def make_currency_graph():
    """
    --> This function checks which checkboxes are checked, to then retrieve the necessary data
    :return: n/a
    """
    # Check for revenue
    if revenue_var.get() == 1:
        checked_currency_box_list.add("revenue")
    else:
        if "revenue" in checked_currency_box_list:
            checked_currency_box_list.remove("revenue")

    # Check for cost of revenue
    if cost_of_revenue_var.get() == 1:
        checked_currency_box_list.add("cost of revenue")
    else:
        if "cost of revenue" in checked_currency_box_list:
            checked_currency_box_list.remove("cost of revenue")

    # Check for gross profit
    if gross_profit_var.get() == 1:
        checked_currency_box_list.add("gross profit")
    else:
        if "gross profit" in checked_currency_box_list:
            checked_currency_box_list.remove("gross profit")

    # Check for research and development expenses
    if r_n_d_expenses_var.get() == 1:
        checked_currency_box_list.add("research and development expenses")
    else:
        if "research and development expenses" in checked_currency_box_list:
            checked_currency_box_list.remove("research and development expenses")

    # Check for general and administrative expenses
    if general_and_admin_expenses_var.get() == 1:
        checked_currency_box_list.add("general and administrative expenses")
    else:
        if "general and administrative expenses" in checked_currency_box_list:
            checked_currency_box_list.remove("general and administrative expenses")

    # Check for selling and marketing expenses
    if marketing_expenses_var.get() == 1:
        checked_currency_box_list.add("selling and marketing expenses")
    else:
        if "selling and marketing expenses" in checked_currency_box_list:
            checked_currency_box_list.remove("selling and marketing expenses")

    # Check for other expenses
    if other_expenses_var.get() == 1:
        checked_currency_box_list.add("other expenses")
    else:
        if "other expenses" in checked_currency_box_list:
            checked_currency_box_list.remove("other expenses")

    # Check for operating expenses
    if operating_expenses_var.get() == 1:
        checked_currency_box_list.add("operating expenses")
    else:
        if "operating expenses" in checked_currency_box_list:
            checked_currency_box_list.remove("operating expenses")

    # Check for cost and expenses
    if cost_and_expenses_var.get() == 1:
        checked_currency_box_list.add("cost and expenses")
    else:
        if "cost and expenses" in checked_currency_box_list:
            checked_currency_box_list.remove("cost and expenses")

    # Check for interest income
    if interest_income_var.get() == 1:
        checked_currency_box_list.add("interest income")
    else:
        if "interest income" in checked_currency_box_list:
            checked_currency_box_list.remove("interest income")

    # Check for interest expense
    if interest_expense_var.get() == 1:
        checked_currency_box_list.add("interest expense")
    else:
        if "interest expense" in checked_currency_box_list:
            checked_currency_box_list.remove("interest expense")

    # Check for depreciation and amortization
    if depreciation_and_amortization_var.get() == 1:
        checked_currency_box_list.add("depreciation and amortization")
    else:
        if "depreciation and amortization" in checked_currency_box_list:
            checked_currency_box_list.remove("depreciation and amortization")

    # Check for gross operating margin
    if gross_operating_margin_var.get() == 1:
        checked_currency_box_list.add("gross operating margin")
    else:
        if "gross operating margin" in checked_currency_box_list:
            checked_currency_box_list.remove("gross operating margin")

    # Check for operating income
    if operating_income_var.get() == 1:
        checked_currency_box_list.add("operating income")
    else:
        if "operating income" in checked_currency_box_list:
            checked_currency_box_list.remove("operating income")

    # Check for income before tax
    if income_before_tax_var.get() == 1:
        checked_currency_box_list.add("income before tax")
    else:
        if "income before tax" in checked_currency_box_list:
            checked_currency_box_list.remove("income before tax")

    # Check for income tax expense
    if income_tax_expense_var.get() == 1:
        checked_currency_box_list.add("income tax expense")
    else:
        if "income tax expense" in checked_currency_box_list:
            checked_currency_box_list.remove("income tax expense")

    # Check for net income
    if net_income_var.get() == 1:
        checked_currency_box_list.add("net income")
    else:
        if "net income" in checked_currency_box_list:
            checked_currency_box_list.remove("net income")

    # Check for weighted average shs out
    if weighted_avg_shs_out_var.get() == 1:
        checked_currency_box_list.add("weighted average shs out")
    else:
        if "weighted average shs out" in checked_currency_box_list:
            checked_currency_box_list.remove("weighted average shs out")

    # Check for weighted average shs out diluted
    if weighted_avg_shs_out_dil_var.get() == 1:
        checked_currency_box_list.add("weighted average shs out diluted")
    else:
        if "weighted average shs out diluted" in checked_currency_box_list:
            checked_currency_box_list.remove("weighted average shs out diluted")

    if data is not None:
        plot(data, checked_currency_box_list, "currency")


def make_ratio_graph():
    """
    --> This function checks which checkboxes are checked, to then retrieve the necessary data
    :return: n/a
    """
    # Check for gross profit ratio
    if gross_profit_ratio_var.get() == 1:
        checked_ratio_box_list.add("gross profit ratio")
    else:
        if "gross profit ratio" in checked_ratio_box_list:
            checked_ratio_box_list.remove("gross profit ratio")

    # Check for gross operating margin ratio
    if gross_operating_margin_ratio_var.get() == 1:
        checked_ratio_box_list.add("gross operating margin ratio")
    else:
        if "gross operating margin ratio" in checked_ratio_box_list:
            checked_ratio_box_list.remove("gross operating margin ratio")

    # Check for operating income ratio
    if operating_income_ratio_var.get() == 1:
        checked_ratio_box_list.add("operating income ratio")
    else:
        if "operating income ratio" in checked_ratio_box_list:
            checked_ratio_box_list.remove("operating income ratio")

    # Check for net income ratio
    if net_income_ratio_var.get() == 1:
        checked_ratio_box_list.add("net income ratio")
    else:
        if "net income ratio" in checked_ratio_box_list:
            checked_ratio_box_list.remove("net income ratio")

    if data is not None:
        plot(data, checked_ratio_box_list, "ratio")


def make_number_graph():
    """
    --> This function checks which checkboxes are checked, to then retrieve the necessary data

    :return: n/a
    """
    # Check for eps
    if eps_var.get() == 1:
        checked_number_box_list.add("eps")
    else:
        if "eps" in checked_number_box_list:
            checked_number_box_list.remove("eps")

    # Check for eps diluted
    if eps_diluted_var.get() == 1:
        checked_number_box_list.add("eps diluted")
    else:
        if "eps diluted" in checked_number_box_list:
            checked_number_box_list.remove("eps diluted")

    if data is not None:
        plot(data, checked_number_box_list, "currency")


def format_currency(x, pos, currency):
    return f"{x:,.0f}{currency}"


def print_statements(financial_statements):
    """
    ---> This function prints out the dictionary format data line by line
    PLEASE NOTE: By default, it only generates the MOST RECENT income statement.
    If you wish to visualize all or more, please either omit the "[0]" or alter it.

    :param financial_statements: list of financial statements from the last x years
    :return: n/a
    """

    for name, metric in financial_statements[0].items():
        print(name, ":", metric)


def get_ratio_metric(financial_statements, metric_name):
    """
    --> This function gathers the requested data on ratios (eg: operating income ratio, net income ratio, etc.)

    :param financial_statements: list of financial statements from the last x years
    :param metric_name: the data the user would like to view (eg: revenue, interest income, etc.)
    :return: list of data the user wanted from the last x years
    """
    metric_list = []
    for financial_statement in financial_statements:
        metric_list.append(financial_statement[metric_name])

    return metric_list


def get_number_metric(financial_statements, metric_name):
    """
    --> This function gathers the requested data on numbers (eg: eps, weighted average shs out, etc.)

    :param financial_statements: list of financial statements from the last x years
    :param metric_name: the data the user would like to view (eg: revenue, interest income, etc.)
    :return: list of data the user wanted from the last x years
    """
    metric_list = []
    for financial_statement in financial_statements:
        metric_list.append(financial_statement[metric_name])

    return metric_list


def get_money_metric(financial_statements, metric_name):
    """
    --> This function gathers the requested data on currency (eg: net income, gross profit, etc.)

    :param financial_statements: list of financial statements from the last x years
    :param metric_name: the data the user would like to view (eg: revenue, interest income, etc.)
    :return: list of data the user wanted from the last x years
    """
    metric_list = []
    for financial_statement in financial_statements:
        metric_list.append(financial_statement[metric_name])

    return metric_list


def get_matching_function(desired_data, financial_statements):
    """
    --> Making this in a dictionary format for if ever I want to eventually make requests text
    based and clean user input to deduct the data they desire.
    --> This function serves to route requests to the appropriate function, as some returned values can not be
    plotted with others (eg: numbers & ratios)
    :param desired_data: the data the user would like to view (eg: revenue, interest income, etc.)
    :param financial_statements: list of financial statements from the last x years
    :return: list of data the user wanted from the last x years
    """
    string_to_func_name_dict = {
        "net income": get_money_metric(financial_statements, "netIncome"),
        "net income ratio": get_ratio_metric(financial_statements, "netIncomeRatio"),
        "revenue": get_money_metric(financial_statements, "revenue"),
        "cost of revenue": get_money_metric(financial_statements, "costOfRevenue"),
        "gross profit": get_money_metric(financial_statements, "grossProfit"),
        "gross profit ratio": get_ratio_metric(financial_statements, "grossProfitRatio"),
        "general and administrative expenses": get_money_metric(financial_statements,
                                                                "generalAndAdministrativeExpenses"),
        "selling and marketing expenses": get_money_metric(financial_statements, "sellingAndMarketingExpenses"),
        "other expenses": get_money_metric(financial_statements, "otherExpenses"),
        "operating expenses": get_money_metric(financial_statements, "operatingExpenses"),
        "cost and expenses": get_money_metric(financial_statements, "costAndExpenses"),
        "interest income": get_money_metric(financial_statements, "interestIncome"),
        "interest expense": get_money_metric(financial_statements, "interestExpense"),
        "depreciation and amortization": get_money_metric(financial_statements, "depreciationAndAmortization"),
        "ebitda": get_money_metric(financial_statements, "ebitda"),
        "gross operating margin": get_money_metric(financial_statements, "ebitda"),
        "ebitda ratio": get_ratio_metric(financial_statements, "ebitdaratio"),
        "gross operating margin ratio": get_ratio_metric(financial_statements, "ebitdaratio"),
        "operating income": get_money_metric(financial_statements, "operatingIncome"),
        "operating income ratio": get_ratio_metric(financial_statements, "operatingIncomeRatio"),
        "total other income expenses": get_money_metric(financial_statements, "totalOtherIncomeExpensesNet"),
        "income before tax": get_money_metric(financial_statements, "incomeBeforeTax"),
        "income before tax ratio": get_ratio_metric(financial_statements, "incomeBeforeTaxRatio"),
        "income tax expense": get_money_metric(financial_statements, "incomeTaxExpense"),
        "eps": get_ratio_metric(financial_statements, "eps"),
        "earnings per share": get_number_metric(financial_statements, "eps"),
        "eps diluted": get_number_metric(financial_statements, "epsdiluted"),
        "earnings per share diluted": get_number_metric(financial_statements, "epsdiluted"),
        "weighted average shs out": get_number_metric(financial_statements, "weightedAverageShsOut"),
        "weighted average shs out diluted": get_number_metric(financial_statements, "weightedAverageShsOutDil"),
        "research and development expenses": get_number_metric(financial_statements, "researchAndDevelopmentExpenses")
    }

    return string_to_func_name_dict.get(desired_data, None)


def get_dates_of_reports(financial_statements):
    """
    --> This function gets the dates from the financial statements and returns them to be plotted

    :param financial_statements: list of financial statements from the last x years
    :return: list of dates
    """
    date_list = []
    for financial_statement in financial_statements:
        date_list.append(financial_statement["date"])

    dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in date_list]

    return dates


def plot(financial_statements, metrics, abscisse_data_type):
    """
    --> This function handles plotting the data

    :param abscisse_data_type: what kind of data is being plotted (currency, ratio, numerical)
    :param financial_statements: list of financial statements from the last x years
    :param metrics: what data to plot
    :return: n/a
    """

    # Params for the plot (tweak if necessary)
    plt.figure(figsize=(12, 10))  # window size
    plt.rcParams['font.size'] = 15  # font size
    plt.xticks(rotation=45)  # x-axis values set on an incline (instead of horizontal --> overlap issue)
    plt.subplots_adjust(left=0.185, bottom=0.15)  # adjust margins to not cut off values

    # Going through the list of data to plot
    for metric in metrics:
        plt.plot_date(
            get_dates_of_reports(financial_statements),
            get_matching_function(metric, financial_statements),
            linestyle='solid', label=metric
        )

    # Check whether the abscisse should represent numerical values or monetary ones
    plt.legend()
    if abscisse_data_type == "currency":
        plt.gca().yaxis.set_major_formatter(
            FuncFormatter(lambda x, _: format_currency(x, _, get_currency(financial_statements))))
    elif abscisse_data_type == "ratio":
        plt.gca().set_ylim(0, 1)
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%0.2f'))

    fig_plot = plt.gcf()
    embed_plot(fig_plot)


def embed_plot(figure):
    # Remove existing canvas widget
    for widget in plot_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(figure, master=plot_frame)
    toolbar = NavigationToolbar2Tk(canvas=canvas, window=plot_frame, pack_toolbar= False)
    toolbar.update()
    canvas.get_tk_widget().pack()
    toolbar.pack(anchor="w")


def get_currency(financial_statements):
    currency = financial_statements[0]["reportedCurrency"]

    curr_symbol = "€" if currency == "EUR" else "$" if currency == "USD" \
        else "£" if currency == "GBP" else "¥" if currency == "JPY" \
        else "₹" if currency == "INR" else "CHF" if currency == "CHF" \
        else "CAD" if currency == "CAD" else "AUD" if currency == "AUD" \
        else "NT$" if currency == "TWD" else "N/A"

    return curr_symbol


main_frame = ctk.CTkFrame(master=root)
main_frame.pack(fill="both", expand=True)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

# Ticker frame
ticker_frame = ctk.CTkFrame(master=main_frame, width=20, height=40)
ticker_frame.grid(row=0, columnspan=2, sticky="n", pady=(25, 0), padx=25)

ticker_frame.columnconfigure(0, weight=1)
ticker_frame.columnconfigure(1, weight=1)
ticker_frame.columnconfigure(2, weight=1)
ticker_frame.rowconfigure(0, weight=1)
ticker_frame.rowconfigure(1, weight=1)

ticker_label = ctk.CTkLabel(master=ticker_frame, text="Ticker Symbol", font=("Roboto", 24))
ticker_entry = ctk.CTkEntry(master=ticker_frame, placeholder_text="Ex: AAPL", width=100, height=30)
ticker_search_button = ctk.CTkButton(master=ticker_frame, text="Search", width=20, height=30, command=get_input_ticker)
ticker_message_label = ctk.CTkLabel(master=ticker_frame, text="Please input a ticket", font=("Roboto", 15))

ticker_label.grid(row=0, column=0, pady=15, padx=15)
ticker_entry.grid(row=0, column=1, sticky="w", padx=(0, 15), pady=15)
ticker_search_button.grid(row=0, column=2, sticky="w", pady=15, padx=(0, 15))
ticker_message_label.grid(row=1, columnspan=3, pady=(0, 10))

# Plot frame
plot_frame = ctk.CTkFrame(master=main_frame, width=400, height=200)
plot_frame.grid(rowspan=2, column=1)

# Graph options frame
options_frame = ctk.CTkFrame(master=main_frame, width=20, height=20)
options_frame.grid(row=1, column=0, sticky="n", pady=25, padx=25)

options_frame.columnconfigure(0, weight=1)
options_frame.columnconfigure(1, weight=1)
options_frame.rowconfigure(0, weight=1)
options_frame.rowconfigure(1, weight=1)
options_frame.rowconfigure(2, weight=1)

options_label = ctk.CTkLabel(master=options_frame, text="Available data", font=("Roboto", 24))
options_label.grid(row=0, columnspan=2, pady=15, padx=15)

# Graph options --> Currency frame
currency_frame = ctk.CTkFrame(master=options_frame)
currency_frame.grid(row=1, columnspan=2, sticky="nw", padx=25, ipadx=25)

currency_frame.columnconfigure(0, weight=1)
currency_frame.columnconfigure(1, weight=1)
currency_frame.rowconfigure(0, weight=1)
currency_frame.rowconfigure(1, weight=1)
currency_frame.rowconfigure(2, weight=1)
currency_frame.rowconfigure(3, weight=1)
currency_frame.rowconfigure(4, weight=1)
currency_frame.rowconfigure(5, weight=1)
currency_frame.rowconfigure(6, weight=1)
currency_frame.rowconfigure(7, weight=1)
currency_frame.rowconfigure(8, weight=1)
currency_frame.rowconfigure(9, weight=1)
currency_frame.rowconfigure(10, weight=1)

checked_currency_box_list = set()
revenue_var = ctk.IntVar()
cost_of_revenue_var = ctk.IntVar()
gross_profit_var = ctk.IntVar()
r_n_d_expenses_var = ctk.IntVar()
general_and_admin_expenses_var = ctk.IntVar()
marketing_expenses_var = ctk.IntVar()
other_expenses_var = ctk.IntVar()
operating_expenses_var = ctk.IntVar()
cost_and_expenses_var = ctk.IntVar()
interest_income_var = ctk.IntVar()
interest_expense_var = ctk.IntVar()
depreciation_and_amortization_var = ctk.IntVar()
gross_operating_margin_var = ctk.IntVar()
operating_income_var = ctk.IntVar()
income_before_tax_var = ctk.IntVar()
income_tax_expense_var = ctk.IntVar()
net_income_var = ctk.IntVar()
weighted_avg_shs_out_var = ctk.IntVar()
weighted_avg_shs_out_dil_var = ctk.IntVar()

currency_label = ctk.CTkLabel(master=currency_frame, text="Currency", font=("Roboto", 24))
create_currency_graph_button = ctk.CTkButton(master=currency_frame, text="Create Graph", width=20,
                                             command=make_currency_graph)
revenue_box = ctk.CTkCheckBox(master=currency_frame, text="Revenue", variable=revenue_var, onvalue=1, offvalue=0,
                              checkbox_width=15, checkbox_height=15)
cost_of_revenue_box = ctk.CTkCheckBox(master=currency_frame, text="Cost of Revenue", variable=cost_of_revenue_var,
                                      onvalue=1, offvalue=0, checkbox_width=15, checkbox_height=15)
gross_profit_box = ctk.CTkCheckBox(master=currency_frame, text="Gross Profit", variable=gross_profit_var, onvalue=1,
                                   offvalue=0, checkbox_width=15, checkbox_height=15)
r_n_d_expenses_box = ctk.CTkCheckBox(master=currency_frame, text="R&D Expenses", variable=r_n_d_expenses_var, onvalue=1,
                                     offvalue=0, checkbox_width=15, checkbox_height=15)
general_and_admin_expenses_box = ctk.CTkCheckBox(master=currency_frame, text="General and Admin Expenses",
                                                 variable=general_and_admin_expenses_var, onvalue=1, offvalue=0,
                                                 checkbox_width=15, checkbox_height=15)
marketing_expenses_box = ctk.CTkCheckBox(master=currency_frame, text="Marketing Expenses",
                                         variable=marketing_expenses_var, onvalue=1, offvalue=0, checkbox_width=15,
                                         checkbox_height=15)
other_expenses_box = ctk.CTkCheckBox(master=currency_frame, text="Other Expenses", variable=other_expenses_var,
                                     onvalue=1, offvalue=0, checkbox_width=15, checkbox_height=15)
operating_expenses_box = ctk.CTkCheckBox(master=currency_frame, text="Operating Expenses",
                                         variable=operating_expenses_var, onvalue=1, offvalue=0, checkbox_width=15,
                                         checkbox_height=15)
cost_and_expenses_box = ctk.CTkCheckBox(master=currency_frame, text="Cost and Expenses", variable=cost_and_expenses_var,
                                        onvalue=1, offvalue=0, checkbox_width=15, checkbox_height=15)
interest_income_box = ctk.CTkCheckBox(master=currency_frame, text="Interest Income", variable=interest_income_var,
                                      onvalue=1, offvalue=0, checkbox_width=15, checkbox_height=15)
interest_expense_box = ctk.CTkCheckBox(master=currency_frame, text="Interest Expense", variable=interest_expense_var,
                                       onvalue=1, offvalue=0, checkbox_width=15, checkbox_height=15)
depreciation_and_amortization_box = ctk.CTkCheckBox(master=currency_frame, text="Depreciation and Amortization",
                                                    variable=depreciation_and_amortization_var, onvalue=1, offvalue=0,
                                                    checkbox_width=15, checkbox_height=15)
gross_operating_margin_box = ctk.CTkCheckBox(master=currency_frame, text="Gross Operating Margin",
                                             variable=gross_operating_margin_var, onvalue=1, offvalue=0,
                                             checkbox_width=15, checkbox_height=15)
operating_income_box = ctk.CTkCheckBox(master=currency_frame, text="Operating Income", variable=operating_income_var,
                                       onvalue=1, offvalue=0, checkbox_width=15, checkbox_height=15)
income_before_tax_box = ctk.CTkCheckBox(master=currency_frame, text="Income Before Tax", variable=income_before_tax_var,
                                        onvalue=1, offvalue=0, checkbox_width=15, checkbox_height=15)
income_tax_expense_box = ctk.CTkCheckBox(master=currency_frame, text="Income Tax Expense",
                                         variable=income_tax_expense_var, onvalue=1, offvalue=0, checkbox_width=15,
                                         checkbox_height=15)
net_income_box = ctk.CTkCheckBox(master=currency_frame, text="Net Income", variable=net_income_var, onvalue=1,
                                 offvalue=0, checkbox_width=15, checkbox_height=15)
weighted_avg_shs_out_box = ctk.CTkCheckBox(master=currency_frame, text="Weighted Avg SHS Out",
                                           variable=weighted_avg_shs_out_var, onvalue=1, offvalue=0, checkbox_width=15,
                                           checkbox_height=15)
weighted_avg_shs_out_dil_box = ctk.CTkCheckBox(master=currency_frame, text="Weighted Avg SHS Out Diluted",
                                               variable=weighted_avg_shs_out_dil_var, onvalue=1, offvalue=0,
                                               checkbox_width=15, checkbox_height=15)

currency_label.grid(row=0, columnspan=2, pady=10)
revenue_box.grid(row=1, column=0)
cost_of_revenue_box.grid(row=2, column=0)
gross_profit_box.grid(row=3, column=0)
r_n_d_expenses_box.grid(row=4, column=0)
general_and_admin_expenses_box.grid(row=5, column=0)
marketing_expenses_box.grid(row=6, column=0)
other_expenses_box.grid(row=7, column=0)
operating_expenses_box.grid(row=8, column=0)
cost_and_expenses_box.grid(row=9, column=0)
depreciation_and_amortization_box.grid(row=10, column=0)
interest_income_box.grid(row=1, column=1)
interest_expense_box.grid(row=2, column=1)
gross_operating_margin_box.grid(row=3, column=1)
operating_income_box.grid(row=4, column=1)
income_before_tax_box.grid(row=5, column=1)
income_tax_expense_box.grid(row=6, column=1)
net_income_box.grid(row=7, column=1)
weighted_avg_shs_out_box.grid(row=8, column=1)
weighted_avg_shs_out_dil_box.grid(row=9, column=1)
create_currency_graph_button.grid(row=11, columnspan=2, pady=10)

# Graph options --> Ratios frame
ratio_frame = ctk.CTkFrame(master=options_frame)
ratio_frame.grid(row=2, column=0, sticky="nw", padx=25, pady=25, ipadx=25)

ratio_frame.columnconfigure(0, weight=1)
ratio_frame.rowconfigure(0, weight=1)
ratio_frame.rowconfigure(1, weight=1)
ratio_frame.rowconfigure(2, weight=1)
ratio_frame.rowconfigure(3, weight=1)
ratio_frame.rowconfigure(4, weight=1)
ratio_frame.rowconfigure(5, weight=1)

checked_ratio_box_list = set()
gross_profit_ratio_var = ctk.IntVar()
gross_operating_margin_ratio_var = ctk.IntVar()
operating_income_ratio_var = ctk.IntVar()
net_income_ratio_var = ctk.IntVar()

ratio_label = ctk.CTkLabel(master=ratio_frame, text="Ratio", font=("Roboto", 24))
create_ratio_graph_button = ctk.CTkButton(master=ratio_frame, text="Create Graph", width=20, command=make_ratio_graph)
gross_profit_ratio_box = ctk.CTkCheckBox(master=ratio_frame, text="Gross Profit Ratio", variable=gross_profit_ratio_var,
                                         onvalue=1, offvalue=0, checkbox_width=15, checkbox_height=15)
gross_operating_margin_ratio_box = ctk.CTkCheckBox(master=ratio_frame, text="Gross Operating Margin Ratio",
                                                   variable=gross_operating_margin_ratio_var, onvalue=1, offvalue=0,
                                                   checkbox_width=15, checkbox_height=15)
operating_income_ratio_box = ctk.CTkCheckBox(master=ratio_frame, text="Operating Income Ratio",
                                             variable=operating_income_ratio_var, onvalue=1, offvalue=0,
                                             checkbox_width=15, checkbox_height=15)
net_income_ratio_box = ctk.CTkCheckBox(master=ratio_frame, text="Net Income Ratio", variable=net_income_ratio_var,
                                       onvalue=1, offvalue=0, checkbox_width=15, checkbox_height=15)

ratio_label.grid(row=0, column=0, pady=10)
gross_profit_ratio_box.grid(row=1, column=0)
gross_operating_margin_ratio_box.grid(row=2, column=0)
operating_income_ratio_box.grid(row=3, column=0)
net_income_ratio_box.grid(row=4, column=0)
create_ratio_graph_button.grid(row=5, column=0, pady=10)

# Graph options --> Numbers frame
numbers_frame = ctk.CTkFrame(master=options_frame)
numbers_frame.grid(row=2, column=1, sticky="nw", padx=(0, 25), pady=25, ipadx=25)

numbers_frame.columnconfigure(0, weight=1)
numbers_frame.rowconfigure(0, weight=1)
numbers_frame.rowconfigure(1, weight=1)
numbers_frame.rowconfigure(2, weight=1)
numbers_frame.rowconfigure(3, weight=1)

checked_number_box_list = set()
eps_var = ctk.IntVar()
eps_diluted_var = ctk.IntVar()

number_label = ctk.CTkLabel(master=numbers_frame, text="Number", font=("Roboto", 24))
create_number_graph_button = ctk.CTkButton(master=numbers_frame, text="Create Graph", width=20,
                                           command=make_number_graph)
eps_box = ctk.CTkCheckBox(master=numbers_frame, text="EPS", variable=eps_var, onvalue=1, offvalue=0, checkbox_width=15,
                          checkbox_height=15)
eps_diluted_box = ctk.CTkCheckBox(master=numbers_frame, text="EPS Diluted", variable=eps_diluted_var, onvalue=1,
                                  offvalue=0, checkbox_width=15, checkbox_height=15)

number_label.grid(row=0, column=0, pady=10)
eps_box.grid(row=1, column=0)
eps_diluted_box.grid(row=2, column=0)
create_number_graph_button.grid(row=3, column=0, pady=10)

data = None
manage_display()
