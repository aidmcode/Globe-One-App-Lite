from customtkinter import *
from systemclass import System, show_error
from PIL import Image
from datetime import *
import json
import os


root = CTk()
root.after(0, lambda:root.resizable(0,0)) #disables resizing of the window
root.geometry("1200x675")
root.title("Globe One App Lite")

        
#Frames1
register_frame = CTkFrame(root, fg_color = "#c850c0", width = 500, height = 500)
log_in_frame = CTkFrame(root, fg_color = "#c850c0", width = 500, height = 500)

user_frame = CTkFrame(root, fg_color = "#144db2", width = 1200, height = 245)
menu_frame = CTkFrame(root, fg_color = "#4158d0", width = 1200, height = 430)

buy_load_frame = CTkFrame(menu_frame, fg_color = "#9764d7", width = 800, height = 430)
buy_promo_frame = CTkFrame(menu_frame, fg_color = "#9764d7", width = 800, height = 430)
promo1_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)
promo2_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)
promo3_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)
promo4_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)
promo5_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)
promo6_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)
promo7_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)
promo8_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)
promo9_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)
promo10_frame = CTkFrame(buy_promo_frame, fg_color="white", width=400, height=430)

send_load_frame = CTkFrame(menu_frame, fg_color = "#9764d7", width = 800, height = 430)
view_subs_frame= CTkFrame(menu_frame, fg_color = "white", width = 780, height = 430)
view_subs_frameSB= CTkScrollableFrame(view_subs_frame, fg_color="#9764d7", width = 780, height = 420)
transaction_frame = CTkFrame(menu_frame, fg_color = "white", width = 780, height = 430)
transaction_frameSB = CTkScrollableFrame(transaction_frame, fg_color = "#9764d7", width = 780, height = 420)

#Images
login_img = CTkImage(Image.open("images/login_ui.png"), size = (1200, 675))
user_img = CTkImage(Image.open("images/user.png"), size = (1200, 245))
menu_img = CTkImage(Image.open("images/frames.png"), size = (800, 430))
promo_img = CTkImage(Image.open("images/frames.png"), size = (400, 430))
user_bg = CTkLabel(user_frame, image=user_img, text = "")
user_bg.pack()

promo1_bg = CTkLabel(promo1_frame, image=promo_img, text="")
promo2_bg = CTkLabel(promo2_frame, image=promo_img, text="")
promo3_bg = CTkLabel(promo3_frame, image=promo_img, text="")
promo4_bg = CTkLabel(promo4_frame, image=promo_img, text="")
promo5_bg = CTkLabel(promo5_frame, image=promo_img, text="")
promo6_bg = CTkLabel(promo6_frame, image=promo_img, text="")
promo7_bg = CTkLabel(promo7_frame, image=promo_img, text="")
promo8_bg = CTkLabel(promo8_frame, image=promo_img, text="")
promo9_bg = CTkLabel(promo9_frame, image=promo_img, text="")
promo10_bg = CTkLabel(promo10_frame, image=promo_img, text="")

promo1_bg.pack()
promo2_bg.pack()
promo3_bg.pack()
promo4_bg.pack()
promo5_bg.pack()
promo6_bg.pack()
promo7_bg.pack()
promo8_bg.pack()
promo9_bg.pack()
promo10_bg.pack()

globe_img = CTkImage(Image.open("images/globe logo.jpg"), size = (55, 30))

#Function/command for switching from register frame to login frame
def switch_to_login():
    log_in_frame.pack(expand = 1, fill = BOTH)
    register_frame.pack_forget()
    user_frame.pack_forget()
    input_num_text = CTkLabel(forms_frame2, text = "Mobile Number", 
                              text_color = "Black", font = ("Arial", 20)) 
    input_num_text.place(x = 50, y = 80)

    input_pin_text = CTkLabel(forms_frame2, text = "PIN", 
                              text_color = "Black", font = ("Arial", 20)) 
    input_pin_text.place(x = 50, y = 180)
    
#Function/command for switching from login frame to register frame
def switch_to_reg():
    register_frame.pack(expand = 1, fill = BOTH)
    user_frame.pack_forget()
    log_in_frame.pack_forget()
    

account_number = ""
def register():
    global account_number
    global system
    user_number = reg_num_entry.get().strip()
    user_pin = reg_pin_entry.get().strip()
    system = System(user_number, user_pin)
    
    #checks user input, if invalid, will show an error messagebox or window
    if user_number == "":
        show_error("ERROR", "PLEASE INPUT YOUR NUMBER")
    elif len(user_number) != 11:
        show_error("ERROR", "INVALID NUMBER")
    elif user_pin == "":
        show_error("ERROR", "PLEASE INPUT YOUR PIN")
    elif len(user_pin) != 4:
        show_error("ERROR", "INVALID PIN")
    else:
        #check if the account number file exists
        if os.path.exists(f"{user_number}.json"):
            show_error("ERROR", "THIS ACCOUNT ALREADY EXISTS")
        else:
            system.register()
            account_number = user_number
            to_menu()

def login():
    global account_number
    global system
    user_number = login_num_entry.get().strip()
    user_pin = login_pin_entry.get().strip()
    system = System(user_number, user_pin)
    validation = system.login()

    #checks user input, if invalid, will show an error messagebox or window
    if user_number == "":
            show_error("ERROR", "PLEASE INPUT YOUR NUMBER")
    elif len(user_number) != 11:
            show_error("ERROR", "INVALID NUMBER")
    elif os.path.exists(f"{user_number}.json"):
        if user_pin == "":
            show_error("ERROR", "PLEASE INPUT YOUR PIN")
        elif len(user_pin) != 4:
            show_error("ERROR", "INVALID PIN")
        elif validation == -1:
            show_error("ERROR", "THIS ACCOUNT NUMBER DOESN'T EXIST")
        elif validation == -2:
            show_error("ERROR", "WRONG PIN")
        elif validation == -3:
            show_error("ERROR", "THIS ACCOUNT NUMBER DOESN'T EXIST")
        elif validation == 1:
            account_number = user_number
            to_menu()
        else:
            show_error("ERROR", "LOG IN ERROR, PLEASE TRY AGAIN")
    else:
        show_error("ERROR", "THIS ACCOUNT NUMBER DOESN'T EXIST")


#shows the user frame(yung frame sa taas) that contains user details(account number and load balance)
def user_details():
    global num_frame
    user_frame.pack(side = TOP)
    with open(f"{account_number}.json", mode = "r+") as f:
            acc_data = json.load(f)
    #Displays account number
    num_frame = CTkFrame(user_frame, fg_color="white", width = 650, height = 200, corner_radius=10)
    num_frame.place(x = 50, y = 80)
    user_num_lb = CTkLabel(num_frame, text = f'Account Number', text_color = "black", 
                           font = ("Arial", 30, "bold"), fg_color="white", corner_radius=10)
    user_num_lb.place(x = 5, y = 50)
    user_num_text = CTkLabel(num_frame, text = f'{account_number}', text_color = "black", 
                             font = ("Arial", 25), fg_color="white", corner_radius=10)
    user_num_text.place(x = 5, y = 100)

    CTkLabel(num_frame, fg_color="#cee1fd", text="Registered", 
             text_color="#1f4b88", 
             font=("Arial", 20),
             corner_radius=20, height = 30).place(x=180,y=100) #registered text
    CTkLabel(num_frame, image = globe_img, text = "").place(x=10,y=10) #globe logo
    CTkLabel(num_frame, text = "Globe Prepaid", font=("Arial", 15, "bold"), 
             text_color="dark blue").place(x = 80, y=10) #globe prepaid text

    #Displays load balance
    acc_balance_text = CTkLabel(num_frame, text = "P" + str(acc_data["balance"]) + ".00", 
                                text_color = "black", font = ("Arial", 25, "bold"))
    acc_balance_text.place(x = 500, y = 60)
    acc_balance_lb = CTkLabel(num_frame, text = "Load Balance", text_color = "black", font = ("Arial", 20))
    acc_balance_lb.place(x = 500, y = 100)

    #Log out button 
    log_out_btn =  CTkButton(user_frame, text = "Log out", text_color = "Black", 
                             font = ("Arial", 12), width = 25, fg_color = "lightblue", 
                             corner_radius=20, command = log_out)
    log_out_btn.place(x = 20, y = 10)

disabled_buyload_btn = CTkLabel(menu_frame, text = "Buy Load", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)
disabled_buypromo_btn = CTkLabel(menu_frame, text = "Buy Promo", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)
disabled_sendload_btn = CTkLabel(menu_frame, text = "Send Load", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)
disabled_viewsubs_btn = CTkLabel(menu_frame, text = "View Subscriptions", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)
disabled_transaction_btn = CTkLabel(menu_frame, text = "Transaction History", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)

#shows the main menu
def to_menu():
    user_details()
    menu_frame.pack(side = BOTTOM)
    log_in_frame.pack_forget()
    register_frame.pack_forget()
    to_buy_promo()
    #Main buttons
    buy_load_btn = CTkButton(menu_frame, text = "Buy Load", text_color = "white", font = ("Arial", 20), width = 250, height = 35, fg_color = "#9764d7", corner_radius=20, command = to_buy_load)
    buy_load_btn.place(x = 80, y = 50)

    buy_promo_btn = CTkButton(menu_frame, text = "Buy Promo", text_color = "white", font = ("Arial", 20), width = 250, height = 35, fg_color = "#9764d7", corner_radius=20, command = to_buy_promo)
    buy_promo_btn.place(x = 80, y = 120)

    send_load_btn = CTkButton(menu_frame, text = "Send Load", text_color = "white", font = ("Arial", 20), width = 250, height = 35, fg_color = "#9764d7", corner_radius=20, command = to_send_load)
    send_load_btn.place(x = 80, y = 190)
 
    view_subs_btn = CTkButton(menu_frame, text = "View Subscriptions", text_color = "white", font = ("Arial", 20), width = 250, height = 35, fg_color = "#9764d7", corner_radius=20, command = to_view_subs)
    view_subs_btn.place(x = 80, y = 260)

    transaction_btn = CTkButton(menu_frame, text = "Transaction History", text_color = "white", font = ("Arial", 20), width = 250, height = 35, fg_color = "#9764d7", corner_radius=20, command = to_transaction_history)
    transaction_btn.place(x = 80, y = 330)

#Used to restrict user from typing inputs other than numbers/digits
#Also restricts the user from typing more characters after the required length of input is exceeded
def validate(P):
        if len(P) == 0:
            return True
        elif len(P) < 12 and P.isdigit():
            return True
        else:
            return False
        
def validate_pin(P):
        if len(P) == 0:
            return True
        elif len(P) < 5 and P.isdigit():
            return True
        else:
            return False
        
def validate_load_amount(P):
    if len(P) == 0:
        return True
    elif len(P) < 5 and P.isdigit():
        return True
    else:
        return False
vcmd = (root.register(validate), '%P')
vcmd_pin = (root.register(validate_pin), '%P')
vcmd_load = (root.register(validate_load_amount), '%P')


#shows the buy load frame
def to_buy_load():
    global disabled_buyload_btn
    buy_load_frame.place(x = 400, y = 0)
    buy_load_frame.tkraise()

    CTkLabel(buy_load_frame, text = "Buy Load", font=("Arial", 20, "bold"), 
             fg_color="#36c1bc",corner_radius=10, text_color="white", width = 600, height = 40).place(x=100, y= 20)
    load_amount_text = CTkLabel(buy_load_frame, text = "Enter load amount (P10 to P2,000)",
                                text_color = "white", font = ("Arial", 30, "bold"))
    load_amount_text.place(x = 170, y = 140)
    load_amount_input = CTkEntry(buy_load_frame, validate = "key", validatecommand=vcmd_load, width = 400, 
                                 font = ("Arial", 30), text_color="black", fg_color = "white", 
                                 border_width=5, border_color="#3a50ca", corner_radius=20)
    load_amount_input.place(x = 200, y = 190)

    #Takes the user input in the load amount entry
    def get_load():
        load_amount = load_amount_input.get().strip()
        if load_amount == "":
            show_error("ERROR", "PLEASE INPUT LOAD AMOUNT")
        elif int(load_amount) > 2000:
            show_error("ERROR", "MAXIMUM OF P2000 ONLY! PLEASE TRY AGAIN.")
        elif int(load_amount) < 10:
            show_error("ERROR", "MINIMUM OF P10 ONLY! PLEASE TRY AGAIN.")
        else:
            system.buyload(load_amount)
            user_details() #displays the updated user frame

    buyload_btn = CTkButton(buy_load_frame, text = "BUY", text_color = "white", font = ("Arial", 20, "bold"), 
                            width = 300, height = 35, fg_color = "#4158d0", corner_radius=20, command = get_load)
    buyload_btn.place(x = 230, y = 300)
    disabled_buyload_btn = CTkLabel(menu_frame, text = "Buy Load", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)
    disabled_buyload_btn.place(x=80,y=50)
    
    disabled_buypromo_btn.destroy()
    disabled_sendload_btn.destroy()
    disabled_viewsubs_btn.destroy()
    repack_transactions()
    

#displays the selected promo's details(promo name, price, duration)
def show_promo_details(promo_frame, promo_price, description, selected_promo, duration):
    promo_frame.place(x=400, y=0)
    promo_frame.tkraise()

    promo_name_lb = CTkLabel(promo_frame, text=selected_promo, font = ("Arial", 20), text_color="black")
    promo_name_lb.place(x = 60, y = 70)

    promo_duration_lb = CTkLabel(promo_frame, text=f'Valid for {duration} days', font = ("Arial", 15), text_color="black")
    promo_duration_lb.place(x = 60, y = 100)

    promo_price_lb = CTkLabel(promo_frame, text = f'P{promo_price}', font = ("Arial", 20), fg_color="#c850c0", text_color="white", width = 100, corner_radius=10)
    promo_price_lb.place(x = 250, y = 80)

    description_lb = CTkLabel(promo_frame, text = description, text_color="Black", font=("Arial", 15), justify="left")
    description_lb.place(x = 60, y = 200)
    
    subscribe_btn = CTkButton(promo_frame, text = "Subscribe", fg_color="blue", text_color="white", font=("Arial", 15, "bold"), command=lambda: [system.buypromo(selected_promo, promo_price, duration), user_details()])
    subscribe_btn.place(x = 100, y = 300)


#show buy promo
def to_buy_promo():
    global disabled_buypromo_btn
    buy_promo_frame.place(x = 400, y = 0)
    buy_promo_frame.tkraise() 
    
    promo_list = {0:["Go50",50, 3], 1:["UnliCalls", 20, 2], 2:["Go99", 99, 7], 3:["UnliGo50", 50, 1], 
                  4:["SuperXclusive199", 199, 15], 5:["UnliGo299", 299, 7], 6:["Go199", 199, 7], 
                  7:["ML10", 10, 3], 8:["GoUNLI350", 350, 15], 9:["Go129", 129, 7]}
    
    CTkLabel(buy_promo_frame, text = "Choose your Promo", font = ("Arial", 25), fg_color="#36c1bc", text_color="white", width = 300, height = 40, corner_radius=15).place(x=50, y=20)

    promo1_des = "5GB data for all sites + 1GB GoWiFi." #Go50
    promo2_des = "Unli calls to all networks." #UnliCalls
    promo3_des = "8GB data for all sites + Unli texts to \nall networks." #Go99
    promo4_des = "Unlimited data for all sites + Unli texts \nto all networks.\nValid for 1 day" #UnliGo50
    promo5_des = "15GB data for all sites + 8GB data \nfor your app of choice + Unli texts \nto all networks." #SuperXclusive199
    promo6_des = "Unlimited data for all sites + Unli texts \nto all networks.\nValid for 7 days" #UnliGo299
    promo7_des = "15GB data for all sites + Unli texts \nto all networks" #Go199
    promo8_des = "1GB data for Mobile Legends.\nValid for 3 days" #ML10
    promo9_des = "Unlimited data for all sites + Unli texts \nto all networks.\nValid for 15 days" #GoUNLI350
    promo10_des = "10GB data for all sites + Unli texts \nto all networks" #Go129

    promo1 = CTkButton(buy_promo_frame, text = promo_list[0][0], text_color = "white", font = ("Arial", 20), fg_color="#3e53bc", width = 130, height = 35, command=lambda: show_promo_details(promo1_frame, promo_list[0][1], promo1_des, promo_list[0][0], promo_list[0][2]))
    promo2 = CTkButton(buy_promo_frame, text = promo_list[1][0], text_color = "white", font = ("Arial", 20), fg_color="#3e53bc", width = 130, height = 35, command=lambda: show_promo_details(promo2_frame, promo_list[1][1], promo2_des, promo_list[1][0], promo_list[1][2]))
    promo3 = CTkButton(buy_promo_frame, text = promo_list[2][0], text_color = "white", font = ("Arial", 20), fg_color="#3e53bc", width = 130, height = 35, command=lambda: show_promo_details(promo3_frame, promo_list[2][1], promo3_des, promo_list[2][0], promo_list[2][2]))
    promo4 = CTkButton(buy_promo_frame, text = promo_list[3][0], text_color = "white", font = ("Arial", 20), fg_color="#3e53bc", width = 130, height = 35, command=lambda: show_promo_details(promo4_frame, promo_list[3][1], promo4_des, promo_list[3][0], promo_list[3][2]))
    promo5 = CTkButton(buy_promo_frame, text = promo_list[4][0], text_color = "white", font = ("Arial", 15), fg_color="#3e53bc", width = 80, height = 35, command=lambda: show_promo_details(promo5_frame, promo_list[4][1], promo5_des, promo_list[4][0], promo_list[4][2]))
    promo6 = CTkButton(buy_promo_frame, text = promo_list[5][0], text_color = "white", font = ("Arial", 20), fg_color="#3e53bc", width = 130, height = 35, command=lambda: show_promo_details(promo6_frame, promo_list[5][1], promo6_des, promo_list[5][0], promo_list[5][2]))
    promo7 = CTkButton(buy_promo_frame, text = promo_list[6][0], text_color = "white", font = ("Arial", 20), fg_color="#3e53bc", width = 130, height = 35, command=lambda: show_promo_details(promo7_frame, promo_list[6][1], promo7_des, promo_list[6][0], promo_list[6][2]))
    promo8 = CTkButton(buy_promo_frame, text = promo_list[7][0], text_color = "white", font = ("Arial", 20), fg_color="#3e53bc", width = 130, height = 35, command=lambda: show_promo_details(promo8_frame, promo_list[7][1], promo8_des, promo_list[7][0], promo_list[7][2]))
    promo9 = CTkButton(buy_promo_frame, text = promo_list[8][0], text_color = "white", font = ("Arial", 20), fg_color="#3e53bc", width = 130, height = 35, command=lambda: show_promo_details(promo9_frame, promo_list[8][1], promo9_des, promo_list[8][0], promo_list[8][2]))
    promo10 = CTkButton(buy_promo_frame, text = promo_list[9][0], text_color = "white", font = ("Arial", 20), fg_color="#3e53bc", width = 130, height = 35, command=lambda: show_promo_details(promo10_frame, promo_list[9][1], promo10_des, promo_list[9][0], promo_list[9][2]))

    promo1.place(x = 50, y = 100)
    promo2.place(x = 50, y = 160)
    promo3.place(x = 50, y = 220)
    promo4.place(x = 50, y = 280)
    promo5.place(x = 50, y = 340)
    promo6.place(x = 200, y = 100)
    promo7.place(x = 200, y = 160)
    promo8.place(x = 200, y = 220)
    promo9.place(x = 200, y = 280)
    promo10.place(x = 200, y = 340)

    disabled_buypromo_btn = CTkLabel(menu_frame, text = "Buy Promo", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)
    disabled_buypromo_btn.place(x=80,y=120)

    disabled_buyload_btn.destroy()
    disabled_sendload_btn.destroy()
    disabled_viewsubs_btn.destroy()
    repack_transactions()
    show_promo_details(promo4_frame, promo_list[4][1], promo4_des, promo_list[4][0], promo_list[4][2])

#show send load frame
def to_send_load():
    global disabled_sendload_btn
    send_load_frame.place(x = 400, y = 0)
    send_load_frame.tkraise()

    CTkLabel(send_load_frame, text = "Send Load", font=("Arial", 20, "bold"), 
             fg_color="#36c1bc",corner_radius=10, text_color="white", width = 600, height = 40).place(x=100, y= 20)
    receiver_num_text = CTkLabel(send_load_frame, text = "Recipient's Number", text_color = "white", font = ("Arial", 25))
    receiver_num_text.place(x = 100, y = 150)
    receiver_num = CTkEntry(send_load_frame, validate="key",validatecommand=vcmd, 
                            width = 270, font = ("Arial", 25), text_color="black", 
                            fg_color = "white", border_width=5, 
                            border_color = "#3a50ca", corner_radius=20)
    receiver_num.place(x = 100, y = 190)

    load_amount_text = CTkLabel(send_load_frame, text = "Amount (P10 to P2,000)", text_color = "white", font = ("Arial", 25))
    load_amount_text.place(x = 480, y = 150)
    load_amount_ent = CTkEntry(send_load_frame, validate = "key", validatecommand=vcmd_load, 
                               width = 230, font = ("Arial", 25), 
                               text_color="black", fg_color = "white", 
                               border_width=5 , border_color = "#3a50ca", corner_radius=20)
    load_amount_ent.place(x = 480, y = 190)

    #takes user input from the load amount and recipient entry
    def get_input():
        load_amount = load_amount_ent.get().strip()
        recipient = receiver_num.get().strip()
        
        if recipient == "":
            show_error("ERROR", "PLEASE INPUT RECIPIENT NUMBER")
        elif len(recipient) != 11:
                show_error("ERROR", "INVALID NUMBER")
        elif os.path.exists(f"{recipient}.json"):         
            if recipient == account_number:
                show_error("ERROR", "YOU CANNOT SEND LOAD TO YOUR OWN NUMBER")
            elif load_amount == "":
                show_error("ERROR", "PLEASE INPUT LOAD AMOUNT")
            else:    
                system.sendload(recipient, load_amount)
                user_details() #displays the updated user frame
        else:
             show_error("ERROR", "THIS ACCOUNT DOESN'T EXIST")

    sendload_btn = CTkButton(send_load_frame, 
                             text = "SEND", 
                             text_color = "white", 
                             font = ("Arial", 22), 
                             width = 300, 
                             fg_color = "#4158d0", 
                             corner_radius=20,
                             command = get_input)
    sendload_btn.place(x = 250, y = 330)
    disabled_sendload_btn = CTkLabel(menu_frame, text = "Send Load", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)
    disabled_sendload_btn.place(x=80,y=190)

    disabled_buyload_btn.destroy()
    disabled_buypromo_btn.destroy()
    disabled_viewsubs_btn.destroy()
    repack_transactions()

#show active promos frame
def to_view_subs():
    global disabled_viewsubs_btn
    view_subs_frame.place(x = 400, y = 0)
    view_subs_frame.tkraise()
    view_subs_frameSB.pack()

    #destroy pre-existing labels to avoid repeated display of labels
    for widgets in view_subs_frameSB.winfo_children():
        widgets.destroy()

    #displays all the active promos in the account
    with open(f"{account_number}.json", mode = "r+") as f:
        acc_data = json.load(f)
        active_promos = acc_data["promos"]
        CTkLabel(view_subs_frameSB, text = f'{" "*10}Active Promos{" "*10}', 
                 text_color = "white", font = ("Arial", 20, "bold"), width = 200, height = 40, 
                 fg_color="#4158d0", corner_radius=5).pack(pady = 10)
        if len(active_promos) == 0:
            CTkLabel(view_subs_frameSB, text = "NO ACTIVE PROMOS", 
                 text_color = "black", font = ("Arial", 20, "bold"), width = 400, height = 80, 
                 fg_color="lightblue", corner_radius=5).pack(anchor = "center", pady = 40)
        else:
            for p in active_promos:
                act_promos_txt = CTkLabel(view_subs_frameSB, 
                                        text = f'{p}\n\nwill expire on {acc_data["promos"][p][1]}', 
                                        text_color = "black", fg_color="lightblue", 
                                        corner_radius=10, font = ("Arial", 20), 
                                        width = 200, 
                                        height = 80,
                                        justify ="left")
                act_promos_txt.pack(anchor = "w", padx = 20, pady = 10)
    disabled_viewsubs_btn = CTkLabel(menu_frame, text = "View Subscriptions", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)
    disabled_viewsubs_btn.place(x=80,y=260)
    
    disabled_buyload_btn.destroy()
    disabled_buypromo_btn.destroy()
    disabled_sendload_btn.destroy()
    repack_transactions()

def repack_transactions():
    disabled_transaction_btn.destroy()
    #destroy pre-existing labels to avoid repeated display of labels
    for widgets in transaction_frameSB.winfo_children():
        widgets.destroy()
#show transaction history
def to_transaction_history():
    global disabled_transaction_btn
    transaction_frame.place(x = 400, y = 0)
    transaction_frame.tkraise()
    transaction_frameSB.pack()

    #displays all transactions
    with open(f"{account_number}.json", mode = "r+") as f:
        acc_data = json.load(f)
        transactions = acc_data["transac_history"]
        CTkLabel(transaction_frameSB, text = f'{" "*10}Transaction History{" "*10}', 
                 text_color="white", font = ("Arial", 20, "bold"), width = 200, height=40, fg_color="#4158d0").pack(pady = 10)
        if len(transactions) == 0:
            CTkLabel(transaction_frameSB, text = "NO RECENT TRANSACTIONS", 
                 text_color = "black", font = ("Arial", 20, "bold"), width = 400, height = 80, 
                 fg_color="#ffcc70", corner_radius=5).pack(anchor = "center", pady = 40)
        else:
            for t in transactions:
                purchasetime = acc_data["transac_history"][t]
                transac_history_txt = CTkLabel(transaction_frameSB, 
                                            text = f'{t}{" "*30}\n\n{purchasetime}', 
                                            text_color = "black", 
                                            font = ("Arial", 20), 
                                            width = 200,
                                            height = 80,
                                            corner_radius=10,
                                            fg_color="#ffcc70",
                                            justify="left")
                transac_history_txt.pack(anchor = "w", padx = 20, pady = 10)
    disabled_transaction_btn = CTkLabel(menu_frame, text = "Transaction History", text_color = "white", font = ("Arial", 20), 
             width = 250, height = 35, fg_color = "#7e30df", corner_radius=20)
    disabled_transaction_btn.place(x=80,y=330)

    disabled_buyload_btn.destroy()
    disabled_buypromo_btn.destroy()
    disabled_sendload_btn.destroy()
    disabled_viewsubs_btn.destroy()

#log out 
def log_out():
    user_frame.pack_forget()
    menu_frame.pack_forget()
    for widgets in num_frame.winfo_children():
         widgets.destroy()
    repack_transactions()
    switch_to_login()


#Register Account Number
reg_bg = CTkLabel(register_frame, image = login_img, text = "")
reg_bg.pack()

forms_frame = CTkFrame(register_frame, fg_color="#4158d0", width = 480, height = 450)
forms_frame.place(x = 700, y = 150)

input_num_text = CTkLabel(forms_frame, text = "Mobile Number", text_color = "Black", font = ("Arial", 20)) 
input_num_text.place(x = 50, y = 80)
input_pin_text = CTkLabel(forms_frame, text = "PIN", text_color = "Black", font = ("Arial", 20)) 
input_pin_text.place(x = 50, y = 180)


reg_num_entry = CTkEntry(forms_frame, validate="key",validatecommand=vcmd, text_color="black", width = 370, height = 35, border_width=1, fg_color = "white", font = ("Arial", 20))
reg_num_entry.place(x = 50, y = 120)
reg_pin_entry = CTkEntry(forms_frame, validate="key",validatecommand=vcmd_pin, text_color="black", width = 210, height = 35, border_width=1, fg_color = "white", font = ("Arial", 20))
reg_pin_entry.place(x = 50, y = 220)

register_btn = CTkButton(forms_frame, text = "Register", text_color="white", font=("Arial", 20, "bold"), width = 370, height = 35, fg_color="#ffcc70", corner_radius=20, command = register)
register_btn.place(x = 50, y = 330)

#Log in Account 
login_bg = CTkLabel(log_in_frame, image = login_img, text = "")
login_bg.pack()

forms_frame2 = CTkFrame(log_in_frame, fg_color="#4158d0", width = 480, height = 450)
forms_frame2.place(x = 700, y = 150)

login_num_entry = CTkEntry(forms_frame2, validate="key",validatecommand=vcmd, text_color="black", width = 370, height = 35, border_width=1, fg_color = "white", font =("Arial", 20))
login_num_entry.place(x = 50, y = 120)
login_pin_entry = CTkEntry(forms_frame2, validate="key",validatecommand=vcmd_pin, text_color="black", width = 210, height = 35, border_width=1, fg_color = "white", font = ("Arial", 20))
login_pin_entry.place(x = 50, y = 220)

login_btn = CTkButton(forms_frame2, text = "Log In", text_color="white", font=("Arial", 20, "bold"), width = 370, height = 35, fg_color="#ffcc70", corner_radius=20, command = login)
login_btn.place(x = 50, y = 330)

clicked_reg_btn = CTkLabel(register_frame, text = "REGISTER", corner_radius=5, fg_color="#4158d0", font=("Arial", 20), width=250, height=40)
clicked_reg_btn.place(x = 700, y = 130)

to_reg_btn = CTkButton(log_in_frame, text = "REGISTER", text_color="Black", 
                       hover_color="#2f4ead", fg_color="lightblue", font=("Arial", 20), 
                       width = 250, height=40, command = switch_to_reg)
to_reg_btn.place(x = 700, y = 130)

clicked_login_btn = CTkLabel(log_in_frame, text = "LOG IN", corner_radius=5, fg_color="#4158d0", font=("Arial", 20), width=250, height=40)
clicked_login_btn.place(x = 930, y = 130)

to_login_btn = CTkButton(register_frame, text = "LOG IN", text_color="Black", 
                         hover_color="#2f4ead", fg_color="lightblue", 
                         font=("Arial", 20), width = 250, height=40, 
                         command = switch_to_login)
to_login_btn.place(x = 930, y = 130)


register_frame.pack(expand = 1, fill = BOTH)

root.mainloop()