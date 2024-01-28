from tkinter import *
import sys
import requests
import qbittorrentapi

def authenticate():
    username = entry_U.get()
    password = entry_P.get()
    server = entry_S.get()
    conn_info = dict(
        host=server,
        port=8080,
        username=username,
        password=password,
    )
    qbt_client = qbittorrentapi.Client(**conn_info)

    # the Client will automatically acquire/maintain a logged-in state
    # in line with any request. therefore, this is not strictly necessary;
    # however, you may want to test the provided login credentials.
    try:
        qbt_client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)

        return qbt_client


    headers = {'Referer': f'http://{server}:8080'}
    data = {'username': username, 'password': password}
    response = requests.post(f'http://{server}:8080/api/v2/auth/login', headers=headers, data=data)
    print(response.cookies.get_dict())
    if response.status_code == 200:
        login_label.config(text = "Login Successful", bg='white')




root = Tk()
root.title('Model Definition')
root.geometry('{}x{}'.format(600, 600))
root.configure(bg='#c6cca5')
root.minsize(600,600)


# create all of the main containers
top_frame = Frame(root, bg='#c6cca5', width=450, height=50, pady=3)
center_frame = Frame(root, bg='#c6cca5', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='#c6cca5', width=450, height=45, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center_frame.grid(row=1, sticky="ew")
btm_frame.grid(row=3, sticky="ew")

# create the widgets for the top frame
login_label = Label(top_frame, text='Login Information:', background="#c6cca5")
server_label = Label(top_frame, text='Server:', background="#c6cca5")
User_label = Label(top_frame, text='User:', background="#c6cca5")
Password_label = Label(top_frame, text='Password:', background="#c6cca5")
Login_button = Button(top_frame, text='Login', command=authenticate)
entry_S = Entry(top_frame, background="white")
entry_U = Entry(top_frame, background="white")
entry_P = Entry(top_frame, background="white", show='*')

# layout the widgets in the top frame
login_label.grid(row=0, columnspan=4,padx=5, pady=5)
server_label.grid(row=1, column=0, pady=5)
User_label.grid(row=1, column=2, pady=5)
Password_label.grid(row=1, column=4,padx=5, pady=5)
Login_button.grid(row=1, column=6)
entry_S.grid(row=1, column=1,padx=5, pady=5)
entry_U.grid(row=1, column=3,padx=5, pady=5)
entry_P.grid(row=1, column=5,padx=5, pady=5)

# create the center widgets
center_frame.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(1, weight=1)


root.mainloop()


