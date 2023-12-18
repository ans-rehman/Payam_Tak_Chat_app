import customtkinter
import os
from PIL import Image
import socket
import threading
from tkinter import filedialog, messagebox
from datetime import datetime
# customtkinter.set_default_color_theme("yellow")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("PAYAM TAK")
        self.geometry("800x450")


#==============Initializing communication==============

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.host = socket.gethostname()
        # self.host = '0.0.0.0'
        self.host = socket.gethostname()
        self.port = 12345
        self.client = (self.host, self.port)

        self.filename = None
        self.image_exe = ['jpg','png','svg', 'webp', 'jpeg','gif']
# ///////////////////////////gui interface///////////////////////////////
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        # try:
        #     dp_file = filedialog.askopenfilename()
        #     self.dp_image = customtkinter.CTkImage(Image.open(dp_file), size=(28, 28))
        # except:
        self.dp_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "dp.png")), size=(28, 28))

        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "chat1.png")), size=(40, 40))
        self.send_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "snd1.png")),
                                                size=(30, 30))
        self.file_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "file11.png")), size=(30, 30))
        self.mic_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "mic1.png")), size=(30, 30))
        self.camera_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "cm.png")), size=(30, 30))
        # users images
        self.user_1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user1.png")), size=(30, 30))
        self.user_2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user_2.jpg")), size=(30, 30))
        self.user_3 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user3.png")), size=(30, 30))
        self.user_4 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user4.png")), size=(30, 30))
        self.user_5 = self.dp_image
        self.user_6= customtkinter.CTkImage(Image.open(os.path.join(image_path, "user_6.jpg")), size=(30, 30))
        self.user_7 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user_7.jpg")), size=(30, 30))
        self.user_8 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user_8.jpg")), size=(30, 30))

        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew",)
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  PAYAM TAK", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Active users",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Dark","Light" ],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)



# //////////////////////////////////////////////home page content/////////////////////////////////

        # title bar frame
        self.title_bar = customtkinter.CTkFrame(self.home_frame)
        self.title_bar.grid(row=0, column=0, sticky='ew', padx=20, pady=10)

        # dp
        # for dp and profile name direction n position
        # self.title_bar.columnconfigure(0, weight=1)
        # self.title_bar.columnconfigure(1, weight=1)
        # self.title_bar.rowconfigure(0, weight=1)

        self.dp = customtkinter.CTkLabel(self.title_bar, text="", image=self.dp_image)
        self.dp.grid(row=0, column=0, padx=20, pady=10)
        # user name
        self.prf_name = customtkinter.CTkLabel(self.title_bar, text="ANS REHMAN")
        self.prf_name.grid(row=0, column=1, padx=20, pady=10,sticky='w')

        # chat area
        self.home_frame.grid_rowconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.chat_area = customtkinter.CTkScrollableFrame(self.home_frame,scrollbar_button_hover_color='#006ca5')
        self.chat_area.grid(row=1, column=0, sticky='nsew', padx=20, pady=10 )

        # typing area
        self.low_bar = customtkinter.CTkFrame(self.home_frame, fg_color='transparent')
        self.low_bar.grid(row=2, column=0, sticky='ew', padx=20, pady=10)
        # entry for typing
        self.low_bar.columnconfigure(0, weight=1)
        self.type_area = customtkinter.CTkEntry(self.low_bar)
        self.type_area.bind("<Return>", command = self.send_msg)
        self.type_area.grid(row=0, column=0, sticky='ew')

        # send button
        self.send_btn = customtkinter.CTkButton(self.low_bar,text="",width=10,height=34, image=self.send_image,
                                                 anchor='ns', command = self.send_msg)
        self.send_btn.grid(row=0, column=1 ,padx=10)
        # file button
        self.file_btn = customtkinter.CTkButton(self.low_bar,text="", image=self.file_image, width=10,
                                                command=self.select_file)
        self.file_btn.grid(row=0, column=2 ,padx=10)
        # camera
        self.mic_btn = customtkinter.CTkButton(self.low_bar,text="", image=self.mic_image, width=10,
                                                command=self.select_file)
        self.mic_btn.grid(row=0, column=3 ,padx=10)
        # audio
        self.camera_btn = customtkinter.CTkButton(self.low_bar,text="", image=self.camera_image, width=10,
                                                command=self.select_file)
        self.camera_btn.grid(row=0, column=4 ,padx=10)
#///////////////////////////////////// create second frame/////////////////////////////////////////
        self.second_frame = customtkinter.CTkScrollableFrame(self, corner_radius=20,scrollbar_button_hover_color='#006ca5')
        # self.second_frame.columnconfigure(0, weight=1)
        self.user1 = customtkinter.CTkLabel(self.second_frame,text_color='black', width=300, text='  ANS REHMAN', image=self.user_5, compound='left',
                                            anchor='w' , font=('helvetica', 15) , corner_radius=20, fg_color='#006ca5')
        self.user1.grid(row=0,column=0,padx=10, pady=20, ipadx=10, ipady=10,)

        self.user2 = customtkinter.CTkLabel(self.second_frame,text_color='black', width=300, text='  MARYAM NADEEM', image=self.user_1, compound='left',
                                            anchor='w' , font=('helvetica', 15) , corner_radius=20, fg_color='#006ca5')
        self.user2.grid(row=1,column=0,padx=100, pady=20, ipadx=10, ipady=10)

        self.user3 = customtkinter.CTkLabel(self.second_frame,text_color='black', width=300, text='  SAQIB JAVED', image=self.user_3, compound='left',
                                            anchor='w' , font=('helvetica', 15) , corner_radius=20, fg_color='#006ca5')
        self.user3.grid(row=2,column=0,padx=10, pady=20, ipadx=10, ipady=10)

        self.user4 = customtkinter.CTkLabel(self.second_frame,text_color='black', width=300, text='  FATIMA HASSAN', image=self.user_4, compound='left',
                                            anchor='w' , font=('helvetica', 15) , corner_radius=20, fg_color='#006ca5')
        self.user4.grid(row=3,column=0,padx=10, pady=20, ipadx=10, ipady=10)

        self.user5 = customtkinter.CTkLabel(self.second_frame,text_color='black', width=300, text='  M. ZUBAIR', image=self.user_6, compound='left',
                                            anchor='w' , font=('helvetica', 15) , corner_radius=20, fg_color='#006ca5')
        self.user5.grid(row=4,column=0, padx=10, pady=20, ipadx=10, ipady=10)

        self.user6 = customtkinter.CTkLabel(self.second_frame,text_color='black', width=300, text='  SAIF UR REHMAN', image=self.user_7, compound='left',
                                            anchor='w' , font=('helvetica', 15) , corner_radius=20, fg_color='#006ca5')
        self.user6.grid(row=5,column=0,padx=10, pady=20, ipadx=10, ipady=10)

        self.user7 = customtkinter.CTkLabel(self.second_frame,text_color='black', width=300, text='  UMAR FAROOQ', image=self.user_8, compound='left',
                                            anchor='w' , font=('helvetica', 15) , corner_radius=20, fg_color='#006ca5')
        self.user7.grid(row=6,column=0,padx=10, pady=20, ipadx=10, ipady=10)

        self.user8 = customtkinter.CTkLabel(self.second_frame,text_color='black', width=300, text='  ALI HASSAN', image=self.user_2, compound='left',
                                            anchor='w' , font=('helvetica', 15) , corner_radius=20, fg_color='#006ca5')
        self.user8.grid(row=7,column=0,padx=10, pady=20, ipadx=10, ipady=10)

        self.user1.bind('<Button-1>', command=lambda event: self.profile(self.user1))
        self.user2.bind('<Button-1>', command=lambda event: self.profile(self.user2))
        self.user3.bind('<Button-1>', command=lambda event: self.profile(self.user3))
        self.user4.bind('<Button-1>', command=lambda event: self.profile(self.user4))
        self.user5.bind('<Button-1>', command=lambda event: self.profile(self.user5))
        self.user6.bind('<Button-1>', command=lambda event: self.profile(self.user6))
        self.user7.bind('<Button-1>', command=lambda event: self.profile(self.user7))
        self.user8.bind('<Button-1>', command=lambda event: self.profile(self.user8))

#//////////////////////////////create third frame////////////////////////////////////////////////
        self.third_frame = customtkinter.CTkScrollableFrame(self, corner_radius=0, fg_color="transparent", scrollbar_button_hover_color='#006ca5')
        # about section
        self.about = customtkinter.CTkFrame(self.third_frame, fg_color="transparent")
        self.about.pack(side='top', pady=10, ipady=10)
        self.head_abt = customtkinter.CTkLabel(self.about,text_color='black',corner_radius=10, text='About "Payam Tak"', font=('helvetica', 20), fg_color='#006ca5')
        self.head_abt.pack(side='top',pady=10, ipadx=10, ipady=10,)
        about = 'Welcome to Payam Tak, a collaborative effort between Ans Rehman and Maryam Nadeem.'+ '\n'+' Payam Tak is an intuitive, user-friendly chat application crafted with '+ '\n'+'the fusion of Ans`s expertise in web development and Maryam`s proficiency in'+ '\n'+' creating captivating graphical interfaces using Python`s Socket and Tkinter libraries.'
        self.about_txt = customtkinter.CTkLabel(self.about,text_color='black', corner_radius=10, text = about,font=('helvetica', 14), fg_color='#006ca5')
        self.about_txt.pack(side='top',  ipady=20, ipadx=10)

        # Our Vision

        vision = 'At Payam Tak, our vision is to redefine communication by providing'+'\n' + 'a seamless, secure, and engaging platform. We strive to create an innovative space'+'\n' + ' where users can effortlessly connect and exchange messages, fostering efficient'+'\n'+' and meaningful interactions.'
        self.vision_frame = customtkinter.CTkFrame(self.third_frame, fg_color="transparent")
        self.vision_frame.pack(side='top', padx=10, pady=10)
        self.vision = customtkinter.CTkLabel(self.vision_frame,corner_radius=10, text='Our Vision',text_color='black', font=('helvetica', 20), fg_color='#006ca5')
        self.vision.pack(side='top', pady=10, ipady=10, ipadx=10)

        self.vision_txt = customtkinter.CTkLabel(self.vision_frame,corner_radius=10, text=vision,text_color='black', font=('helvetica', 14), fg_color='#006ca5')
        self.vision_txt.pack(side='top', ipadx=10, ipady=20)

        # Features
        features = 'Real-time Messaging: Enjoy instant and reliable messaging with minimal latency.'+'\n' + 'Sleek User Interface: Experience a visually appealing interface'+'\n' + ' designed to enhance user interaction and navigation.'+'\n' + 'Secure Communication: Prioritize your privacy with secure end-to-end encrypted messaging.'+'\n' + 'Customization: Personalize your messaging experience with a range of customizable options.'
        self.features_frame = customtkinter.CTkFrame(self.third_frame, fg_color="transparent")
        self.features_frame.pack(side='top', padx=10, pady=10)
        self.features = customtkinter.CTkLabel(self.features_frame,corner_radius=10, text='Features',text_color='black', font=('helvetica', 20), fg_color='#006ca5')
        self.features.pack(side='top', pady=10, ipady=10, ipadx=10)

        self.features_txt = customtkinter.CTkLabel(self.features_frame,corner_radius=10, text=features,text_color='black', font=('helvetica', 14), fg_color='#006ca5')
        self.features_txt.pack(side='top', ipadx=10, ipady=20)

        # Our Collaboration
        collab = 'Combining Ans Rehman`s technical prowess in programming and web development'+'\n' + 'with Maryam Nadeem`s artistic expertise in crafting appealing graphical user '+'\n' + 'interfaces, Payam Tak amalgamates functionality with aesthetics.'
        self.collab_frame = customtkinter.CTkFrame(self.third_frame, fg_color="transparent")
        self.collab_frame.pack(side='top', padx=10, pady=10)
        self.collab = customtkinter.CTkLabel(self.collab_frame,corner_radius=10, text='Our Collaboration',text_color='black', font=('helvetica', 20), fg_color='#006ca5')
        self.collab.pack(side='top', pady=10, ipady=10, ipadx=10)

        self.collab_txt = customtkinter.CTkLabel(self.collab_frame,corner_radius=10, text=collab,text_color='black', font=('helvetica', 14), fg_color='#006ca5')
        self.collab_txt.pack(side='top', ipadx=10, ipady=20)
        # Get in Touch
        get_intouch = 'For any queries, feedback, or support requests, reach out to us at'+'\n'+ 'payamtak.contact@enterprise.com'+'\n'+'Thank you for choosing Payam Tak - where communication meets innovation.'
        self.get_intouch_frame = customtkinter.CTkFrame(self.third_frame, fg_color="transparent")
        self.get_intouch_frame.pack(side='top', padx=10, pady=10)
        self.get_intouch = customtkinter.CTkLabel(self.get_intouch_frame,corner_radius=10, text='Get In Touch',text_color='black', font=('helvetica', 20), fg_color='#006ca5')
        self.get_intouch.pack(side='top', pady=10, ipady=10, ipadx=10)

        self.get_intouch_txt = customtkinter.CTkLabel(self.get_intouch_frame,corner_radius=10, text=get_intouch,text_color='black', font=('helvetica', 14), fg_color='#006ca5')
        self.get_intouch_txt.pack(side='top', ipadx=10, ipady=20)
#////////////////////////////////select default frame/////////////////////////////////////////////
        self.select_frame_by_name("home")


#/////////////////////////////////////////// functions for the page handling/////////////////////////////////

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def profile(self, user):
        self.prf_name.configure(text = user.cget('text'))
        self.dp.configure(image=user.cget('image'))
        self.select_frame_by_name("home")
# /////////////////////////////////functions for backend working ///////////////////////////////

    def extension_file(self, name, key):
        name_split = name.split('.')
        exe = name_split[-1]
        exe = exe.lower()
        dt = datetime.now()
        time = dt.strftime( "%d/%m/%Y, %I:%M %p")
        img_fnd=1
        for exet in self.image_exe:
            if exe in exet:
                img_fnd=0
                print(exe)
                if key:
                    f_name=self.file_path
                else:
                    f_name='./Recieved/'+ name
                self.rcvd_img = customtkinter.CTkImage(Image.open(f_name), size=(200,200) )
                self.msg_frm = customtkinter.CTkFrame(self.chat_area, corner_radius=10, fg_color='#006ca5', )
                if key:
                    self.msg_frm.pack(side='top', anchor='e', pady=5)
                else:
                    self.msg_frm.pack(side='top', anchor='w', pady=5)

                self.msg_write = customtkinter.CTkLabel(self.msg_frm,image=self.rcvd_img,text=time, compound='top')
                self.msg_write.pack(side='top', padx=10, pady=10)
                break
        if key and img_fnd:
            msg1=name + '\n'+'File sent'
            self.send_sms_txt(file_message=msg1)
        if key==0:
            msg1 = name + '\n'+'File recieved'
            self.send_sms_txt(file_message=msg1)

    def get_filename(self, folder):
        self.file_path = folder
        self.temp_filename = folder.split("/")
        self.temp_filename = self.temp_filename[-1]
        return self.temp_filename


    def select_file(self, event=None):
        self.select_file = filedialog.askopenfilename()
        self.filename = self.select_file
        self.temp_filename = self.get_filename(self.select_file)
        # self.file_label.config(text=self.temp_filename)
        # self.file_label.place(x=40, y=380)


    def receive_sms_txt(self, receive_txt=None):
        self.msg_frm = customtkinter.CTkFrame(self.chat_area, corner_radius=10, fg_color='#006ca5', )
        print("Receiving sms again")
        print(self.received_message)
        if receive_txt:
            self.sm = receive_txt
        else:
            self.sm = self.received_message
            self.type_area.delete(0, "end")
        if self.sm:
            dt = datetime.now()
            time = dt.strftime( "%d/%m/%Y, %I:%M %p")
            self.sm =self.sm+"\n\n"+ time
            self.msg_frm.pack(side='top', anchor='w', pady=5)
            self.dp_msg = customtkinter.CTkLabel(self.msg_frm,text='',image=self.user_1 ,)
            self.dp_msg.pack(side='left',padx=5, pady=5)
            self.msg_write = customtkinter.CTkLabel(self.msg_frm,text=self.sm, text_color='black',font=('hevetica',15),
                                                    wraplength=500, justify='left',)
            self.msg_write.pack(side='left',fill='both',expand=True, padx=10, pady=10)
            self.type_area.delete(0, 'end')
            self.received_message=None

    def receive_file(self, size, name):
        with open('./Recieved/'+name, "wb") as rec_file:
            print(size)
            print(name)
            while size>0:
                received_buffer = self.server.recv(1024)
                rec_file.write(received_buffer)
                size = size-len(received_buffer)
                print('receiving..', size)
                # print(size)
            self.server.send(("File_received").encode())
            self.received_message = None


    def try_sample1(self):
        self.receive_sms_thread= threading.Thread(target=self.receive_file, args=(self.received_size, self.received_name))
        self.receive_sms_thread.start()
        self.receive_sms_thread.join()
        self.extension_file(name=self.received_name, key=0)


    def receive_sms(self):
        while True:
            try:
                self.server.connect(self.client)
                while True:
                    try:
                        self.received_message = self.server.recv(1024).decode()
                        if "&&&" in self.received_message:
                            self.received_message = self.received_message.split("&&&")
                            self.received_size = self.received_message[0]
                            self.received_name = self.received_message[1]
                            self.received_size = int(self.received_size)
                            self.try_sample1()

                        else:
                            if self.received_message:
                                self.receive_sms_txt()
                    except:
                        continue
            except:
                continue

    def send_sms_txt(self, file_message=None):
        self.msg_frm = customtkinter.CTkFrame(self.chat_area, corner_radius=10, fg_color='#006ca5', )
        dt = datetime.now()
        time = dt.strftime( "%d/%m/%Y, %I:%M %p")
        if file_message:
            self.sms = file_message
        else:
            self.sms= self.type_area.get()
            if self.sms:
                self.server.send(self.sms.encode())
                self.type_area.delete(0, 'end')
        if self.sms:
            self.sms = self.sms+"\n\n"+time
            self.msg_frm.pack(side='top', anchor='e', pady=5)
            self.dp_msg = customtkinter.CTkLabel(self.msg_frm,text='',image=self.dp_image ,)
            self.dp_msg.pack(side='right',padx=5, pady=5)
            self.msg_write = customtkinter.CTkLabel(self.msg_frm,text=self.sms, text_color='black',font=('hevetica',15),
                                                     wraplength=500, justify='left')
            self.msg_write.pack(side='right',fill='both',expand=True, padx=10, pady=10)
            print("Message sent succefull")

    def send_file(self, size):
        print(size)
        with open(self.filename, "rb") as file:
            size = int(size)
            while size>0:
                buffer = file.read(1024)
                self.server.send(buffer)
                size =size - len(buffer)
                print('sending...',size)
                # buffer_size = len(buffer)
                # break
        print("File successful sent")


    def try_sample(self):
        sendfile_thread = threading.Thread(target=self.send_file, args=(self.filesize,), daemon=True)
        sendfile_thread.start()
        # print("thread on")
        sendfile_thread.join()
        self.extension_file(name=self.file_name, key=1)
        self.filename = None
        # self.file_label.place_forget()
        print("Thread stopped")


    def send_msg(self, event=None):
        try:
            if self.filename:
                self.ask_send = messagebox.askyesno("Confirm", "Do want to send message with file")
                print(self.ask_send)
                if self.ask_send:
                    # self.org_filename = self.filename
                    self.file_name = self.get_filename(self.filename)
                    self.filesize = str(os.stat(self.filename).st_size)
                    print("file size is : {}".format(self.filesize))
                    self.embedded_filename = self.filesize+"&&&"+self.file_name
                    self.send_sms_txt()
                    # print('khali message')
                    # self.send_sms_txt(file_message="File has been sent")
                    self.server.send(self.embedded_filename.encode())
                    self.try_sample()
                else:
                    self.filename = None
                    # self.file_label.place_forget()
                    self.send_sms_txt()

            else:
                self.send_sms_txt()
        except:
            self.show_error =messagebox.showerror("No connection", "Time out , no connection found")
            # print('errr')
if __name__ == "__main__":
    app = App()
    receive_thread = threading.Thread(target=app.receive_sms, daemon=True)
    receive_thread.start()
    app.mainloop()
    app.server.close()