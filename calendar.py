import PySimpleGUI as sg
import datetime

sg.theme("DarkBlue12")

date = datetime.date.today()
year = int(str(date)[0:4])
day = int(str(date)[8::])
month = int(str(date)[5:7])

layout = [  [sg.CalendarButton("Calendar",format = "%m-%d",default_date_m_d_y= (month,day,year),begin_at_sunday_plus=1)],
            [sg.Button("Go to date")],
            [sg.Button("Exit")]]
window = sg.Window('Calendar', layout, no_titlebar=False)
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Go to date":
        layout = [  [sg.Text('Choose the date:', justification='center', size=(15, 1))],
                    [sg.Text("DAY:"), sg.Spin(values=[i for i in range(1, 32)], initial_value=day, key = "Day")],
                    [sg.Text("MONTH:"), sg.Spin(values=[i for i in range(1, 13)], initial_value= month, key = "Month")],
                    [sg.Text("YEAR:"), sg.Spin(values=[i for i in range(1900, 2051)], initial_value= year, key = "Year")],
                    [sg.Button("Apply"), sg.Button('Cancel')]]

        window = sg.Window('Calendar', layout)
        while True: 
            event, values = window.read()
            if event == 'Cancel' or event == sg.WIN_CLOSED:
                window.close()
                break
            if event == "Apply":
                layout = [  [sg.CalendarButton("Calendar",format = "%m-%d",default_date_m_d_y= (values["Month"],values["Day"],values["Year"]),begin_at_sunday_plus=1)],
                            [sg.Button('Exit')]]
                window = sg.Window('Go to date', layout, no_titlebar=False)
                while True:
                    event, values = window.read()
                    if event == 'Exit' or event == sg.WIN_CLOSED:
                        break
                window.close()
            

        
    
        











