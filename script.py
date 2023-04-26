import customtkinter
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import os.path


url = "https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
filename = "data.csv"

if not os.path.isfile(filename):
    urllib.request.urlretrieve(url, filename)
else:
    print("File already exists, skipping download.")


#------------------------ GUI Code ------------------------#
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1280}x{720}")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 1280) // 2
        y = (screen_height - 720) // 2
        self.geometry("+{}+{}".format(x, y))

        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        #Create sidebar frame with Buttons
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(9, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Project Python", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Profit per Month", height=(40), width=(300), font=customtkinter.CTkFont(size=18, weight="bold"), command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Profit per Country", height=(40), width=(300), font=customtkinter.CTkFont(size=18, weight="bold"), command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Profit per Transport", height=(40), width=(300), font=customtkinter.CTkFont(size=18, weight="bold"), command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Profit per Day of Week", height=(40), width=(300), font=customtkinter.CTkFont(size=18, weight="bold"), command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Profit per Products", height=(40), width=(300), font=customtkinter.CTkFont(size=18, weight="bold"), command=self.sidebar_button_event)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, text="5 Most Profitable Months", height=(40), width=(300), font=customtkinter.CTkFont(size=18, weight="bold"), command=self.sidebar_button_event)
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, text="5 Most Profitable Products", height=(40), width=(300), font=customtkinter.CTkFont(size=18, weight="bold"), command=self.sidebar_button_event)
        self.sidebar_button_7.grid(row=7, column=0, padx=20, pady=10)
        self.sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame, text="Most Profitable Day per Product", height=(40), width=(300), font=customtkinter.CTkFont(size=18, weight="bold"), command=self.sidebar_button_event)
        self.sidebar_button_8.grid(row=8, column=0, padx=20, pady=10)
        self.sidebar_button_9 = customtkinter.CTkButton(self.sidebar_frame, text="Exit", height=(40), width=(300), font=customtkinter.CTkFont(size=18, weight="bold"), command=lambda: [self.destroy(), plt.close('all')], fg_color="Red")
        self.sidebar_button_9.grid(row=9, column=0, padx=20, pady=10)

    def sidebar_button_event(self):
        usecols = ["Direction", "Date", "Measure", "Value", "Year"]
        data = pd.read_csv('data.csv', usecols=usecols)
        data = data[data['Direction'] == 'Exports'] # filter in the 'Exports' Direction
        data.to_csv("test.csv")
        data['Month'] = pd.to_datetime(data['Date'], format='%d/%m/%Y').dt.strftime('%b') # create a new column for short month names
        monthly_data = data.groupby(['Year', 'Month', 'Measure'])['Value'].sum().reset_index() # group the data by year and month, and sum the Value column for $ and Tonnes measures separately
        
        month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_data['Month'] = pd.Categorical(monthly_data['Month'], categories=month_order, ordered=True)
        monthly_data.to_csv("test.csv")
        dollars_data = monthly_data[monthly_data['Measure'] == '$'].pivot_table(index='Month', columns='Year', values='Value', aggfunc='sum') # create pivot tables with years as columns, months as rows, and the sum of values as values for $ and Tonnes measures separately
        tonnes_data = monthly_data[monthly_data['Measure'] == 'Tonnes'].pivot_table(index='Month', columns='Year', values='Value', aggfunc='sum')
        
        fig, axs = plt.subplots(nrows=2, figsize=(9.39, 6.48)) # create the bar charts as subplots
         
        dollars_data.plot(kind='bar', ax=axs[0], legend=False)
        axs[0].set_title('Monthly Value by Year ($)')
        axs[0].set_xlabel('Month')
        axs[0].set_ylabel('Value ($)')

        fig.legend(loc="upper right", ncol=len(month_order))
        tonnes_data.plot(kind='bar', ax=axs[1], legend=False)
        axs[1].set_title('Monthly Value by Year (Tonnes)')
        axs[1].set_xlabel('Month')
        axs[1].set_ylabel('Value (Tonnes)')

        fig.tight_layout(pad=3.0) # adjust the subplots layout and spacing
        mngr=plt.get_current_fig_manager()
        mngr.window.geometry("+661+210")
        plt.show()

if __name__ == "__main__":
    app = App()
    app.mainloop()