from pathlib import Path
import faceRecognition

# from tkinter import *
# Explicit imports to satisfy Flake8
import customtkinter, tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from button_data import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
faceRecognition.encodeFaces()

# window.geometry("1920x1080")
window.wm_attributes("-fullscreen", True)
window.configure(bg="#FFFFFF")

backgroundColor1 = "#262525"
backgroundColor2 = "#1D1D1D"

userIndex = 0
userNames = [("User " + chr(0)), "Amr Mahmoud", "Feras Alghammas", "Rakan Adnan", "Dr.Morshed Derbali"]
userXY = ["1687_225 0_0", "1688_215 1656_244", "1682_215 1648_244", "1677_215 1677_244", "1646_215 1675_244"]
userPhoto = ["image_User.png", "image_Amr.png", "image_Feras.png", "image_Rakan.png", "image_Derbali.png"]

selectedLangButton = ""
selectedComplexityButton = ""
selectedDomainButton = ""

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    1080.0,
    fill="#262525",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    80.0,
    102.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1690.0,
    106.0,
    image=image_image_2
)


def updateProfile():
    canvas.delete("userFirstName")
    canvas.delete("userLastName")
    canvas.delete("userPhoto")

    canvas.create_text(
        int(userXY[userIndex].split()[0].split('_')[0]),
        int(userXY[userIndex].split()[0].split('_')[1]),
        anchor="nw",
        text=userNames[userIndex].split()[0],
        fill="#FFFFFF",
        font=("Inter", 24 * -1, "bold"),
        tags="userFirstName"
    )

    canvas.create_text(
        int(userXY[userIndex].split()[1].split('_')[0]),
        int(userXY[userIndex].split()[1].split('_')[1]),
        anchor="nw",
        text=userNames[userIndex].split()[1],
        fill="#FFFFFF",
        font=("Inter", 24 * -1, "bold"),
        tags="userLastName"
    )

    image_image_profile = PhotoImage(
        file=relative_to_assets(userPhoto[userIndex]))
    canvas.image_profile = image_image_profile
    canvas.create_image(
        1714.0,
        142.0,
        image=image_image_profile,
        tags="userPhoto"
    )

    canvas.tag_bind("userPhoto", "<Button-1>", lambda event: faceRecognition.runRecognition())
    canvas.tag_bind("userPhoto", "<Enter>", lambda event: canvas.config(cursor="hand2"))
    canvas.tag_bind("userPhoto", "<Leave>", lambda event: canvas.config(cursor=""))


updateProfile()

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    277.0,
    41.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    87.0,
    642.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    626.0,
    536.0,
    image=image_image_7
)

image_image_totalF = PhotoImage(
    file=relative_to_assets("image_totalF.png"))
image_totalF = canvas.create_image(
    1069.0,
    307.0,
    image=image_image_totalF
)

sliderObjects = []


def getTotalF():
    total = 0
    for i in sliderObjects:
        total += i.get()

    sliderTotal.set(int(total)),
    canvas.itemconfigure(sliderLabelTotal, text=int(total))


def createSlider(y1, y2):
    slider = customtkinter.CTkSlider(
        master=window,
        from_=0,
        to=5,
        width=168,
        height=17,
        fg_color=backgroundColor1,
        progress_color="white",
        bg_color="#585656",
        button_hover_color=backgroundColor2,
        button_color="white",
        number_of_steps=5,
        hover=False,
        command=lambda value: [
            sliderLabel.configure(text=int(value)),
            getTotalF()
        ],
    )
    slider.place(
        x=985,
        y=y1 #332
    )
    slider.set(0)

    sliderLabel = customtkinter.CTkLabel(
        window,
        text=str(int(slider.get())),
        font=("Poppins Bold", 20 * -1),
        bg_color=backgroundColor2
    )
    sliderLabel.place(
        x=960,
        y=y2 #327
    )
    sliderObjects.append(slider)


y = 0
for i in range(14):
    createSlider((332 + y), (327 + y))
    y += 30


sliderTotal = customtkinter.CTkSlider(
        master=window,
        from_=0,
        to=70,
        width=166,
        height=17,
        fg_color=backgroundColor1,
        progress_color="white",
        bg_color=backgroundColor2,
        button_hover_color=backgroundColor2,
        button_color="white",
        hover=False,
        state="disabled",
        command=lambda value: canvas.itemconfigure(sliderLabelTotal, text=int(value)),
    )
sliderTotal.place(
    x=984,
    y=305
)
sliderTotal.set(0)

sliderLabelTotal = canvas.create_text(
        1132,
        286,
        anchor="nw",
        text=sliderTotal.get(),
        fill="#FFFFFF",
        font=("Inter", 15 * -1, "bold"),
)


def triggerLangButtons(buttonActive):
    global selectedLangButton

    placeButtonJava(buttonActive if buttonActive != selectedLangButton else "java")
    placeButtonSql(buttonActive if buttonActive != selectedLangButton else "sql")
    placeButtonCPlus(buttonActive if buttonActive != selectedLangButton else "cPlus")
    placeButtonPhp(buttonActive if buttonActive != selectedLangButton else "php")
    placeButtonC(buttonActive if buttonActive != selectedLangButton else "c")
    placeButtonHtml(buttonActive if buttonActive != selectedLangButton else "html")

    selectedLangButton = "" if buttonActive == selectedLangButton else buttonActive


def placeButtonJava(buttonActive="java"):
    buttonJava.place_forget()
    buttonJava_inactive.place_forget()
    if buttonActive == "java":
        buttonJava.place(
            x=837.0,
            y=785.0,
            width=325.0,
            height=125.0
        )
    else:
        buttonJava_inactive.place(
            x=837.0,
            y=785.0,
            width=325.0,
            height=125.0
        )


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
buttonJava_inactive = Button(
    image=button_image_1,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("java"),
    relief="flat"
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
buttonJava = Button(
    image=button_image_2,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("java"),
    relief="flat"
)
placeButtonJava()


def placeButtonSql(buttonActive="sql"):
    buttonSql.place_forget()
    buttonSql_inactive.place_forget()
    if buttonActive == "sql":
        buttonSql.place(
            x=837.0,
            y=927.0,
            width=325.0,
            height=125.0
        )
    else:
        buttonSql_inactive.place(
            x=837.0,
            y=927.0,
            width=325.0,
            height=125.0
        )


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
buttonSql_inactive = Button(
    image=button_image_3,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("sql"),
    relief="flat"
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
buttonSql = Button(
    image=button_image_4,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("sql"),
    relief="flat"
)
placeButtonSql()


def placeButtonCPlus(buttonActive="cPlus"):
    buttonCPlus.place_forget()
    buttonCPlus_inactive.place_forget()
    if buttonActive == "cPlus":
        buttonCPlus.place(
            x=1185.0,
            y=785.0,
            width=325.0,
            height=125.0
        )
    else:
        buttonCPlus_inactive.place(
            x=1185.0,
            y=785.0,
            width=325.0,
            height=125.0
        )


button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
buttonCPlus_inactive = Button(
    image=button_image_5,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("cPlus"),
    relief="flat"
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
buttonCPlus = Button(
    image=button_image_6,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("cPlus"),
    relief="flat"
)
placeButtonCPlus()


def placeButtonPhp(buttonActive="php"):
    buttonPhp.place_forget()
    buttonPhp_inactive.place_forget()
    if buttonActive == "php":
        buttonPhp.place(
            x=1187.0,
            y=927.0,
            width=325.0,
            height=125.0
        )
    else:
        buttonPhp_inactive.place(
            x=1187.0,
            y=927.0,
            width=325.0,
            height=125.0
        )


button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
buttonPhp_inactive = Button(
    image=button_image_7,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("php"),
    relief="flat"
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
buttonPhp = Button(
    image=button_image_8,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("php"),
    relief="flat"
)
placeButtonPhp()


def placeButtonC(buttonActive="c"):
    buttonC.place_forget()
    buttonC_inactive.place_forget()
    if buttonActive == "c":
        buttonC.place(
            x=1538.0,
            y=785.0,
            width=325.0,
            height=125.0
        )
    else:
        buttonC_inactive.place(
            x=1538.0,
            y=785.0,
            width=325.0,
            height=125.0
        )


button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
buttonC_inactive = Button(
    image=button_image_9,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("c"),
    relief="flat"
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
buttonC = Button(
    image=button_image_10,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("c"),
    relief="flat"
)
placeButtonC()


def placeButtonHtml(buttonActive="html"):
    buttonHtml.place_forget()
    buttonHtml_inactive.place_forget()
    if buttonActive == "html":
        buttonHtml.place(
            x=1538.0,
            y=927.0,
            width=325.0,
            height=125.0
        )
    else:
        buttonHtml_inactive.place(
            x=1538.0,
            y=927.0,
            width=325.0,
            height=125.0
        )


button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
buttonHtml_inactive = Button(
    image=button_image_11,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("html"),
    relief="flat"
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
buttonHtml = Button(
    image=button_image_12,
    background=backgroundColor1,
    activebackground=backgroundColor1,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerLangButtons("html"),
    relief="flat"
)
placeButtonHtml()

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    427.0,
    921.0,
    image=image_image_8
)


def triggerComplexityButtons(buttonActive):
    global selectedComplexityButton

    placeButtonOrganic(buttonActive if buttonActive != selectedComplexityButton else "organic")
    placeButtonSemi(buttonActive if buttonActive != selectedComplexityButton else "semi")
    placeButtonEmbedded(buttonActive if buttonActive != selectedComplexityButton else "embedded")

    selectedComplexityButton = "" if buttonActive == selectedComplexityButton else buttonActive


def placeButtonOrganic(buttonActive="organic"):
    buttonOrganic.place_forget()
    buttonOrganic_inactive.place_forget()
    if buttonActive == "organic":
        buttonOrganic.place(
            x=101.0,
            y=827.0,
            width=208.0,
            height=208.0
        )
    else:
        buttonOrganic_inactive.place(
            x=101.0,
            y=827.0,
            width=208.0,
            height=208.0
        )


button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
buttonOrganic_inactive = Button(
    image=button_image_13,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerComplexityButtons("organic"),
    relief="flat"
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
buttonOrganic = Button(
    image=button_image_14,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerComplexityButtons("organic"),
    relief="flat"
)
placeButtonOrganic()


def placeButtonSemi(buttonActive="semi"):
    buttonSemi.place_forget()
    buttonSemi_inactive.place_forget()
    if buttonActive == "semi":
        buttonSemi.place(
            x=340.0,
            y=827.0,
            width=208.0,
            height=208.0
        )
    else:
        buttonSemi_inactive.place(
            x=340.0,
            y=827.0,
            width=208.0,
            height=208.0
        )


button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
buttonSemi_inactive = Button(
    image=button_image_15,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerComplexityButtons("semi"),
    relief="flat"
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
buttonSemi = Button(
    image=button_image_16,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerComplexityButtons("semi"),
    relief="flat"
)
placeButtonSemi()


def placeButtonEmbedded(buttonActive="embedded"):
    buttonEmbedded.place_forget()
    buttonEmbedded_inactive.place_forget()
    if buttonActive == "embedded":
        buttonEmbedded.place(
            x=579.0,
            y=827.0,
            width=208.0,
            height=208.0
        )
    else:
        buttonEmbedded_inactive.place(
            x=579.0,
            y=827.0,
            width=208.0,
            height=208.0
        )


button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
buttonEmbedded_inactive = Button(
    image=button_image_17,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerComplexityButtons("embedded"),
    relief="flat"
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
buttonEmbedded = Button(
    image=button_image_18,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerComplexityButtons("embedded"),
    relief="flat"
)
placeButtonEmbedded()

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    245.0,
    181.0,
    image=image_image_9
)

canvas.create_text(
    100.0,
    141.0,
    anchor="nw",
    text="82.80 FP",
    fill="#FFFFFF",
    font=("Inter", 36 * -1, "bold")
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    626.0,
    180.0,
    image=image_image_10
)

canvas.create_text(
    481.0,
    141.0,
    anchor="nw",
    text="8694.00",
    fill="#5DFF91",
    font=("Inter", 40 * -1, "bold")
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1007.0,
    180.0,
    image=image_image_11
)

canvas.create_text(
    862.0,
    140.0,
    anchor="nw",
    text="33.81 PM",
    fill="#FC646C",
    font=("Inter", 36 * -1, "bold")
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    1388.0,
    179.0,
    image=image_image_12
)

canvas.create_text(
    1243.0,
    139.0,
    anchor="nw",
    text="8.57 M",
    fill="#F3F558",
    font=("Inter", 36 * -1, "bold")
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    1539.0,
    536.0,
    image=image_image_13
)


totalCountTexts = []


def updateTotalCountText(index, newText):
    canvas.itemconfigure(totalCountTexts[index], text=newText)

    total = 0
    for i in totalCountTexts:
        total += int(canvas.itemcget(i, "text"))
    canvas.itemconfigure(totalCount, text=str(total))


def createTotalCountText(y, text="0"):
    totalCounttext = canvas.create_text(
        1799.0,
        y,  # 425.0,
        anchor="center",
        text=text,
        fill="#FFFFFF",
        font=("Poppins", 20 * -1, "bold")
    )
    totalCountTexts.append(totalCounttext)


y = 0
for i in range(5):
    createTotalCountText(425 + y)
    y += 61


totalCount = canvas.create_text(
    1799.0,
    721.0,
    anchor="center",
    text="0",
    fill="#FFFFFF",
    font=("Poppins", 20 * -1, "bold")
)


def triggerDomainButtons(buttonActive):
    global selectedDomainButton

    placeButtonSimple(buttonActive if buttonActive != selectedDomainButton else "simple")
    placeButtonAverage(buttonActive if buttonActive != selectedDomainButton else "average")
    placeButtonComplex(buttonActive if buttonActive != selectedDomainButton else "complex")

    selectedDomainButton = "" if buttonActive == selectedDomainButton else buttonActive

    if selectedDomainButton != "":
        for i in buttonDomainData:
            if selectedDomainButton == i["name"]:
                for j in range(5):
                    updateTotalCountText(j, 0 if str(entries[j].get()) == "" else int(entries[j].get()) * i["data"][j])
    else:
        for i in range(5):
            updateTotalCountText(i, 0)


def placeButtonSimple(buttonActive="simple"):
    buttonSimple.place_forget()
    buttonSimple_inactive.place_forget()
    if buttonActive == "simple":
        buttonSimple.place(
            x=1475.0,
            y=338.0,
            width=85.0,
            height=360.0
        )
    else:
        buttonSimple_inactive.place(
            x=1475.0,
            y=338.0,
            width=85.0,
            height=360.0
        )


button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
buttonSimple_inactive = Button(
    image=button_image_19,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerDomainButtons("simple"),
    relief="flat"
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
buttonSimple = Button(
    image=button_image_20,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerDomainButtons("simple"),
    relief="flat"
)
placeButtonSimple()


def placeButtonAverage(buttonActive="average"):
    buttonAverage.place_forget()
    buttonAverage_inactive.place_forget()
    if buttonActive == "average":
        buttonAverage.place(
            x=1566.0,
            y=338.0,
            width=85.0,
            height=360.0
        )
    else:
        buttonAverage_inactive.place(
            x=1566.0,
            y=338.0,
            width=85.0,
            height=360.0
        )


button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
buttonAverage_inactive = Button(
    image=button_image_21,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerDomainButtons("average"),
    relief="flat"
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
buttonAverage = Button(
    image=button_image_22,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerDomainButtons("average"),
    relief="flat"
)
placeButtonAverage()


def placeButtonComplex(buttonActive="complex"):
    buttonComplex.place_forget()
    buttonComplex_inactive.place_forget()
    if buttonActive == "complex":
        buttonComplex.place(
            x=1657.0,
            y=338.0,
            width=85.0,
            height=360.0
        )
    else:
        buttonComplex_inactive.place(
            x=1657.0,
            y=338.0,
            width=85.0,
            height=360.0
        )


button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
buttonComplex_inactive = Button(
    image=button_image_23,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerDomainButtons("complex"),
    relief="flat"
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
buttonComplex = Button(
    image=button_image_24,
    background=backgroundColor2,
    activebackground=backgroundColor2,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: triggerDomainButtons("complex"),
    relief="flat"
)
placeButtonComplex()

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    1412.0,
    427.0,
    image=image_image_14
)


entries = []


def updateEntry(index, value):
    if selectedDomainButton != "":
        for i in buttonDomainData:
            if selectedDomainButton == i["name"]:
                updateTotalCountText(index, 0 if str(value) == "" else int(value) * i["data"][index])


def createEntry(y, index):
    entry_var = tkinter.StringVar()
    entries.append(entry_var)

    entry_image = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    canvas.image_entry = entry_image
    canvas.create_image(
        1412.5,
        427.5,
        image=entry_image
    )
    entry = Entry(
        bd=0,
        bg="#454545",
        fg="white",
        highlightthickness=0,
        font = ("Inter", 18 * -1, "bold"),
        insertbackground= "white",
        justify="center",
        textvariable=entry_var,
        validate="key",
        validatecommand=(window.register(lambda newValue: newValue.isdigit() and len(newValue) <= 2 or newValue == ""), "%P"),
    )
    entry.place(
        x=1402.0,
        y=y,  # 420.0 + 61
        width=21.0,
        height=13.0
    )
    entry_var.trace("w", lambda *args, index=index, entry_var=entry_var: updateEntry(index=index, value=entry_var.get()))


image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    1412.0,
    488.0,
    image=image_image_15
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1412.5,
    488.5,
    image=entry_image_2
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    1412.0,
    549.0,
    image=image_image_16
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1412.5,
    549.5,
    image=entry_image_3
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    1412.0,
    610.0,
    image=image_image_17
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1412.5,
    610.5,
    image=entry_image_4
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    1412.0,
    671.0,
    image=image_image_18
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    1412.5,
    671.5,
    image=entry_image_5
)

y = 0
for i in range(5):
    createEntry(420 + y, i)
    y += 61

window.resizable(False, False)
window.mainloop()
