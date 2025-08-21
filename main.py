import time
import random

from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.properties import (StringProperty, ObjectProperty, NumericProperty, ListProperty, DictProperty)
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatIconButton
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivymd.uix.snackbar import Snackbar
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
import webbrowser

from lakabaza import Artikli, Podesavanja, Instructions, Tutorial, QuickTips

SCREEN_HIGHT = Window.height
SCREEN_WIDTH = Window.width
LAKABAZA='lakabaza.db' #SPEEDBASE
WHITE="#ffffff"
WHITE_GREY="#e8e8e8"
LIGTH_GREY="#bcbcbc"
DARK_GREY="#5a5a5a"
RED = "#ff0000"
DARK_RED= "#7f0000"
ORANGE = "#ffa500"
BLACK="#000000"
BLUE="#0000ff"
GREEN="#008000"
PURPLE="#800080"

DEFAULT_SETTINGS = {
    'Imagine':
        {'vreme_prikaza': [2,'Imagine for {vrednost} sec', [.1, None, .1]],
         'font_family': [0, 'Font style {vrednost}', [0,5,1]],
         'velicina_fonta': [17,'Font size {vrednost}', [5, None, 1]]},
    'Accumulation':
        {'line_size': [4,'{vrednost} words/line', [2, None, 1]],
         'vreme_prikaza': [.4,'Show for {vrednost} sec', [.1, None, .1]],
         'vreme_akumulacije': [1,'Keyboard unavailable {vrednost} sec', [.1, None, .1]],
         'broj_zrna': [6,'{vrednost} test buttons', [3, 12, 1]],
         'font_family': [0, 'Font style {vrednost}', [0,5,1]],
         'velicina_fonta': [17,'Font size {vrednost}', [5, None, 1]]},
    'DeSync':
        {'vreme_prikaza': [.7,'Red word focus {vrednost} sec', [.1, None, .1]],
         'vreme_akumulacije': [.7,'Black chunk focus {vrednost} sec', [.05, None, .05]],
         'line_size': [3,'{vrednost} words/line', [2, None, 1]],
         'font_family': [0, 'Font style {vrednost}', [0,5,1]],
         'velicina_fonta': [17,'Font size {vrednost}', [5, None, 1]]},
    'Telegraphy':
        {'letter_mode': [0,'Mode: {vrednost}', [0, 4, 1]],
         'left_right': [0,'Left {vrednost} Right', [0, 1, 1]],
         'cilj_brzina': [150, 'Aim for {vrednost} words/min', [25, None, 25]], #[min_val,max_val,increment]
         'line_size': [4,'{vrednost} words/line', [1, None, 1]],
         'slova_ulevo': [2, 'Move by {vrednost} letters to left', [1, None, 1]],
         'font_family': [0, 'Font style {vrednost}', [0,5,1]],
         'velicina_fonta': [17,'Font size {vrednost}', [5, None, 1]]},
    'SpinSpanner':
        {'vreme_prikaza': [.2, 'Contrast the word for {vrednost} sec', [.05, None, .05]],
         'line_size': [5,'{vrednost} words/line', [3, None, 1]],
         'font_family': [0, 'Font style {vrednost}', [0,5,1]],
         'velicina_fonta': [17,'Font size {vrednost}', [5, None, 1]]},
    'Semtitles':
        {'line_size': [4,'{vrednost} words/line', [3, None, 1]],
         'letter_mode': [0,'Mode: {vrednost}', [0, 4, 1]],
         'vreme_prikaza': [.5,'Show for {vrednost} sec', [.1, None, .1]],
         'vreme_akumulacije': [.1,'Hide for {vrednost} sec', [.1, None, .1]],
         'pokazivac_span': [.3,'Underline {vrednost} % of the line', [0, 1, .1]],
         'font_family': [0, 'Font style {vrednost}', [0,5,1]],
         'velicina_fonta': [17,'Font size {vrednost}', [5, None, 1]]},
    'ZigZags':
        {'line_size': [3,'{vrednost} words/jump', [2, None, 1]],
         'vreme_prikaza': [.5,'Chunk time {vrednost} sec', [.1, None, .1]],
         'linija_po_strani': [15,'{vrednost} lines/page', [3, None, 1]],
         'font_family': [0, 'Font style {vrednost}', [0,5,1]],
         'velicina_fonta': [17,'Font size {vrednost}', [5, None, 1]]},
    'iSlider':
        {'line_size': [3,'{vrednost} words/line', [2, None, 1]],
         'vreme_prikaza': [.5,'Focus for {vrednost} sec', [.1, None, .1]],
         'linija_po_strani': [15,'{vrednost} total lines per page', [3, None, 1]],
         'font_family': [0, 'Font style {vrednost}', [0,5,1]],
         'velicina_fonta': [17,'Font size {vrednost}', [5, None, 1]]},
    }

FONT_names = ['Serif', 'Serif italic', 'Arial', 'Calibri', 'Times New Roman', 'Ubuntu']
FONTS = ['data/fonts/serif.otf', 'data/fonts/serif-italic.otf', 'data/fonts/arial.ttf', 'data/fonts/calibri.ttf', 'data/fonts/times-new-roman.ttf', 'data/fonts/ubuntu.ttf']

class Pocetna(Screen):

    def go_web(self, where):
        if where == "blog":
            webbrowser.open(str("https://wizardry-of-science.blogspot.com"))
        elif where == "speed_reading_blog":
            webbrowser.open(str("https://wizardry-of-science.blogspot.com/p/reading-speedster.html"))
        elif where == "googleplay_profile":
            webbrowser.open(str("https://play.google.com/store/apps/developer?id=Miroslav+Stojic"))

    def pop_info(self):
        pop_welcome = MyPopup("Welcome to Read Speeding!")
        pop_welcome.size_hint = (1,1)
        pop_welcome.title_color = DARK_RED
        pop_welcome.separator_color = DARK_RED
        layout = GridLayout(cols=1, padding=5, spacing=2, size_hint_y=None)
        label_text = "\n    [b]Thank You for downloading the Reading Speedster app![/b][size=5sp]\n\n[/size]    Let's improve our reading capabilities! This can be used on its own, but it goes well with the blog: [b]wizardry-of-science.blogspot.com[/b] (blue link below). On the blog, I describe in detail the science, theory and ideas behind this app, my experiance with speed reading and how I think I improved it significantly.[size=5sp]\n\n[/size]    Anyhow, if you've just downloaded this app, and reading this for the first time, I recommend that you go through 'tutorial', familiarize yourself with each game and try to 'learn' as much as you can about the reading.[size=5sp]\n\n[/size]    Like this popup, you can see in the right upper corner of the screen instructions, make sure to understand it, because without understanding those instructions, the exercises might be pointless.[size=5sp]\n\n[/size]    I hope you enjoy this app, and I wish you a happy training! :)"
        intro_label=pop_welcome.make_label(label_text, BLACK, height_hint=None)
        intro_label.height=self.height*.75
        intro_label.valign='top'
        layout.add_widget(intro_label)
        #scroll_content
        pop_welcome.content_box.add_widget(pop_welcome.make_scroll(layout, height_hint=.82))
        #Link
        go_blog_btn = Button(text="[u]Wizardry-of-Science[/u]", markup=True, color=BLUE, background_normal='', background_color=WHITE, border=(1,1,2,2))
        go_blog_btn.bind(on_press = lambda link_copy: self.go_web("speed_reading_blog"))
        #Done
        done_btn = pop_welcome.make_done(height_hint=1)
        done_btn.text = "Let's GO!"
        done_btn.background_color = DARK_RED
        done_btn.bind(on_press=pop_welcome.dismiss)
        bottom_box = BoxLayout(orientation='horizontal', size_hint_y = .08, spacing=10, padding=5)
        bottom_box.add_widget(go_blog_btn)
        bottom_box.add_widget(done_btn)

        pop_welcome.content_box.add_widget(bottom_box)
        #OpenMe
        pop_welcome.open()

    def pop_donate(self):
        pop_sup = MyPopup("Toss a coin to your...")
        pop_sup.size_hint = (1,1)
        pop_sup.separator_color = GREEN
        #Make_scroll
        layout = GridLayout(cols=1, padding=5, spacing=2, size_hint_y=None)
        #Wallets:
        #PayPal
        pp = pop_sup.make_label("PayPal & Coinbase", BLUE, height_hint=None)
        pp.height='25sp'
        layout.add_widget(pp)
        pp_address = pop_sup.make_linkbox("oneclevercoin@gmail.com", height_hint=None)
        pp_address.height='45sp'
        layout.add_widget(pp_address)
        #advCache
        advc = pop_sup.make_label("advCash", GREEN, height_hint=None)
        advc.font_size='18sp'
        advc.height='25sp'
        layout.add_widget(advc)
        advc_address = pop_sup.make_linkbox("E 7385 3381 0334", height_hint=None)
        advc_address.font_size='18sp'
        advc_address.height='45sp'
        layout.add_widget(advc_address)
        #Binance
        binace = pop_sup.make_label("BinanceID", PURPLE, height_hint=None)
        binace.font_size='18sp'
        binace.height='25sp'
        layout.add_widget(binace)
        binace_address = pop_sup.make_linkbox("64018851", height_hint=None)
        binace_address.font_size='18sp'
        binace_address.height='45sp'
        layout.add_widget(binace_address)
        #BTC
        btc = pop_sup.make_label("Bitcoin (BTC)", ORANGE, height_hint=None)
        btc.font_size='18sp'
        btc.height='25sp'
        btc.halign = 'center'
        layout.add_widget(btc)
        btc_address = pop_sup.make_linkbox("bc1qpplgam8wu4ltrhftg5a3wfynmdkn8neswzkc75", height_hint=None)
        btc_address.font_size='18sp'
        btc_address.height='45sp'
        layout.add_widget(btc_address)
        #ETH
        eth_label = pop_sup.make_label("Etherium (ETH & ERC20)", DARK_GREY, height_hint=None) #height_hint=.15
        eth_label.font_size='18sp'
        eth_label.height='25sp'
        eth_label.halign = 'center'
        layout.add_widget(eth_label)
        eth_address = pop_sup.make_linkbox("0xe807ac3ad4eFD09043d66205DA55C3D3EAB3112B", height_hint=None)
        eth_address.font_size='18sp'
        eth_address.height='45sp'
        layout.add_widget(eth_address)
        #XMR
        xmr_label = pop_sup.make_label("Monero (XMR)", DARK_RED, height_hint=None) #height_hint=.15
        xmr_label.font_size='18sp'
        xmr_label.height='25sp'
        xmr_label.halign = 'center'
        layout.add_widget(xmr_label)
        xmr_address = pop_sup.make_linkbox("46J6yBc1aj3P3r33KVR93UcGZcxNWLbEZ5eBD8Cgap2g8F6vc6Eh4hB8AqqUtWKoovDhZtE574cwf4M4mzJoHAE7QGifcTB", height_hint=None)
        xmr_address.font_size='18sp'
        xmr_address.height='45sp'
        layout.add_widget(xmr_address)
        #DOGE
        doge_label = pop_sup.make_label("Dogecoin (DOGE)", ORANGE, height_hint=None) #height_hint=.15
        doge_label.font_size='18sp'
        doge_label.height='25sp'
        doge_label.halign = 'center'
        layout.add_widget(doge_label)
        doge_address = pop_sup.make_linkbox("DTg6HdnDRU8LniUZekXD1UHDN4isPUvdjB", height_hint=None)
        doge_address.font_size='18sp'
        doge_address.height='45sp'
        layout.add_widget(doge_address)
        #TRX and USDT
        trc_label = pop_sup.make_label("TRC-20 (USDT or TRX)", RED, height_hint=None) #height_hint=.15
        trc_label.font_size='18sp'
        trc_label.height='25sp'
        trc_label.halign = 'center'
        layout.add_widget(trc_label)
        trc_address = pop_sup.make_linkbox("TA2aVaktnTQ8guMdxSaTshMJHzxsrVUZMW", height_hint=None)
        trc_address.font_size='18sp'
        trc_address.height='45sp'
        layout.add_widget(trc_address)
        #content
        pop_sup.content_box.add_widget(pop_sup.make_scroll(layout, height_hint=.92))
        #Done
        # done_btn = pop_sup.make_done(height_hint=.07)
        done_btn = MDRaisedButton(text="Please and thank You!", md_bg_color = "green", pos_hint={"center_x": .5, "center_y": 0})
        # done_btn.text = "Please and thank You"
        done_btn.bind(on_press=pop_sup.dismiss)
        pop_sup.content_box.add_widget(done_btn)
        #OpenMe
        pop_sup.open()

    def pop_contribute(self):
        pop_sup = MyPopup("Would you like to contribute?")
        pop_sup.size_hint = (1,1)
        pop_sup.separator_color = GREEN
        #Label
        intro_grid = GridLayout(cols=1, padding=5, spacing=5, size_hint_y=None)
        label_text = "Hey, you! Do you like my app? Well I hope so. It took me around a year to make it possible. First part was the research and trying out different speed reading courses, and the second part was programing the whole thing (which I had to learn).[size=8sp]\n\n[/size]There are a lot of speed reading courses. But, they are not considering neuroscience, just some experiance in teaching speed reading where [i]'for some works, for some doesn°t'[/i]. Also, they are needlessly expensive - even the cheapest ones are at least 30€/$, up to 70$ (beats me). I made this app mainly for the purpose of appying my knowledge in neuroscience and make it FREE for everyone. Nevertheless, it would be nice if you can contribute so that others can enjoy this app too. Few easy ways to contribute: sharing it, rate it and read my blog. Also, maybe send me some feedback via email. Donations are also welcomed: [b]PayPal[/b], [b]advCash[/b] or crypto.\n\nHappy speeding!"
        intro_label=pop_sup.make_label(label_text, BLACK, height_hint=None)
        intro_label.height=self.height#'800sp'
        intro_label.valign='top'
        intro_grid.add_widget(intro_label)
        intro_scroll=pop_sup.make_scroll(intro_grid, height_hint=.92)
        intro_scroll.padding=3
        pop_sup.content_box.add_widget(intro_scroll)
        #Done
        bot_box = BoxLayout(orientation='horizontal', size_hint_y=.08, spacing=5)
        dona_btn = Button(text='Donate', size_hint_x=1, background_normal='', background_color=GREEN)
        dona_btn.bind(on_press=lambda dona_btn: self.pop_donate())
        bot_box.add_widget(dona_btn)
        done_btn = pop_sup.make_done(height_hint=1)
        done_btn.text = "Sure!"
        done_btn.background_color=BLUE
        done_btn.bind(on_press=pop_sup.dismiss)
        bot_box.add_widget(done_btn)
        pop_sup.content_box.add_widget(bot_box)
        #OpenMe
        pop_sup.open()

    def pop_author(self):
        pop_auth = MyPopup("Author")
        pop_auth.title_color = BLUE
        pop_auth.size_hint = (1,1)
        pop_auth.separator_color = BLUE
        #Label Hello
        label_text = "Hello! My name is [b]Miroslav Stojić[/b], [i]but you can call me[/i] [size=19sp][b]Magic Miro[/b][/size]"
        pop_auth.content_box.add_widget(pop_auth.make_label(label_text, BLACK, height_hint=.2))
        #Banner
        img = pop_auth.make_banner('data/MagicM.png', height_hint=.3)
        img.pos_hint={'center_x': .4, 'center_y':.3}
        pop_auth.content_box.add_widget(img)
        #Label Info
        money = "\n  [b]Edu: [/b][i]M.Sc.Biology and M.Sc.Neuroscience[/i]\n  [b]E-mail: [/b]miroslavstojic91@gmail.com\n  [b]Blogs:[/b] wizardry-of-science.blogspot.com (eng) and nagija-mauke.rs (serb)"
        pop_auth.content_box.add_widget(pop_auth.make_label(money, BLACK, height_hint=.37))
        #Done
        done_btn = pop_auth.make_done(height_hint=.08)
        done_btn.background_color=BLUE
        done_btn.text = "Nice to meet you!"
        done_btn.bind(on_press=pop_auth.dismiss)
        pop_auth.content_box.add_widget(done_btn)
        #OpenMe
        pop_auth.open()

    def pop_tips(self):
        r = random.randint(0,100)
        pop_tip = MyPopup("Quick Tip")
        pop_tip.size_hint = (.8, .9)
        tips = QuickTips(LAKABAZA)
        label_text = tips.pick_tip()
        inst_label = pop_tip.make_label(label_text, BLACK, height_hint=.88)
        pop_tip.content_box.add_widget(inst_label)
        done_btn = pop_tip.make_done(height_hint=.1)
        done_btn.text = "Got it!"
        done_btn.bind(on_press=pop_tip.dismiss)
        pop_tip.content_box.add_widget(done_btn)
        #OpenMe
        pop_tip.open()

class MyPopup(Popup):
    def __init__(self, title, **kwargs):
        super(MyPopup,self).__init__(**kwargs)
        self.auto_dismiss= False
        self.orientation= "vertical"
        self.size_hint= (None,None)
        self.padding= 3
        self.title = title
        self.title_color= GREEN
        self.title_size= '18sp'
        self.separator_color= GREEN
        self.background= ''
        self.background_color=WHITE
        self.content_box = BoxLayout(orientation='vertical', padding=3)
        self.content=self.content_box

    def make_label(self, text, color, height_hint):
        pop_label = Label(text=text, size_hint_y=height_hint, markup=True, halign='left', valign='middle', color=color) #font_size=font_size,
        pop_label.bind(size=pop_label.setter('text_size'))
        return pop_label

    def make_banner(self, image_source, height_hint):
        img = Image(source=image_source, size_hint_y=height_hint)#, allow_stretch=False)
        return img

    def make_linkbox(self, link, height_hint, multiline=False):
        link_box = BoxLayout(orientation='horizontal', size_hint_y=height_hint, padding=(2,5), spacing=2)
        link_input = TextInput(text=link, size_hint_x=.85, halign='center', font_size='18sp', readonly=True, background_color=LIGTH_GREY, multiline=multiline)
        link_copy = Button(text="copy", size_hint_x=.15, on_release=lambda link_copy: Clipboard.copy(str(link)))
        link_box.add_widget(link_input)
        link_box.add_widget(link_copy)
        return link_box

    def make_done(self, height_hint):
        done_btn = Button(text="Nice", size_hint_y=height_hint, background_normal='', background_color=GREEN)
        return done_btn

    def make_scroll(self, grid_layout, height_hint=1):
        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        scroll_view=ScrollView(size_hint=(.98,height_hint), pos_hint={"center_x": .5, "center_y": .5}, bar_color=BLUE, opacity=.9)
        scroll_view.add_widget(grid_layout)
        return scroll_view


class TextPrep(Screen):
    igram_igru=StringProperty("")
    odakle="Iz početne"
    podesavanja_grid=ObjectProperty()
    podesavanja_prikazana=False
    izabrani_text=ObjectProperty()
    current_settings=DictProperty()
    brzina_vezbanja=ObjectProperty()
    velicina_fonta=NumericProperty(20)
    letter_modes=ListProperty(['Normal', 'No spaces', 'Space each 2nd', 'Space each 3rd', 'Space each 4th'])
    lista_naslova=ObjectProperty()
    ceo_tekst = ""

    def on_enter(self):
        if self.odakle == "Iz početne":
            while len(self.ids.lista_naslova.children):
                self.ids.lista_naslova.remove_widget(self.ids.lista_naslova.children[0])
            self.take_articles()
            self.load_settings()
            self.izracunaj_brzinu()

    def on_pre_leave(self):
        self.save_settings()

    def on_leave(self):
        if self.odakle == "Iz početne":
            self.pod_grid("del")

    def pop_instrukcije(self):
        pop_inst = MyPopup("How to setup > " + self.igram_igru)
        pop_inst.size_hint = (1,1)
        pop_inst.title_color = DARK_RED
        pop_inst.separator_color = DARK_RED

        label_text = Instructions(LAKABAZA, self.igram_igru, version="prep").text
        inst_label = pop_inst.make_label(label_text, BLACK, height_hint=.92)
        inst_label.valign = 'top'
        pop_inst.content_box.add_widget(inst_label)
        #Done
        done_btn = pop_inst.make_done(height_hint=.08)
        done_btn.background_color = DARK_RED
        done_btn.text = "Let's GO!"
        done_btn.bind(on_press=pop_inst.dismiss)
        pop_inst.content_box.add_widget(done_btn)
        #OpenMe
        pop_inst.open()

    def label_page(self):
        text_split = self.ceo_tekst.split()
        i_beg = self.RECI_PO_STRANI * self.i_page
        i_end = min(i_beg+self.RECI_PO_STRANI-1, len(text_split)-1)
        return ' '.join(text_split[i_beg:i_end])

    def list_pages(self, direction):
        if direction == "Next":
            self.i_page += 1
        elif direction == "Prev":
            self.i_page -= 1
        if self.i_page == -1:
            self.i_page = round(len(self.ceo_tekst.split())/self.RECI_PO_STRANI)
        elif self.i_page == round(len(self.ceo_tekst.split())/self.RECI_PO_STRANI):
            self.i_page = 0

        self.pages=str(self.i_page)+"/"+str(round(len(self.ceo_tekst.split())/self.RECI_PO_STRANI))
        self.pop_lbl.text = self.label_page()

    def popuni_polja(self, odabran_naslov): #selektovanim_tekstom
        baza_artikla = Artikli(LAKABAZA)
        self.izabrani_text.text = odabran_naslov
        artikl = baza_artikla.izdvoji_artikl(odabran_naslov)
        odabran_naslov = artikl[0]
        self.make_settings_interface(self.igram_igru)
        self.izracunaj_brzinu()
        self.ceo_tekst = odabran_naslov[1]

    def izracunaj_brzinu(self):
        if self.igram_igru == "Accumulation" or self.igram_igru == "Imagine":
            self.brzina_vezbanja.text = "-"
        elif self.igram_igru == "SpinSpanner":
            show_time = self.current_settings["vreme_prikaza"][0]
            brzina = int(round(60/show_time,0))
            self.brzina_vezbanja.text = "@" + str(brzina) + "\nw/min"
        elif self.igram_igru == "DeSync":
            line_size = self.current_settings["line_size"][0]
            show_time = self.current_settings["vreme_prikaza"][0]
            accu_time = self.current_settings["vreme_akumulacije"][0]
            brzina = 60*(line_size)/(show_time+accu_time)
            self.brzina_vezbanja.text = "@" + str(round(brzina,0)) + "\nw/min"
        elif self.igram_igru == "ZigZags":
            line_size = self.current_settings["line_size"][0]
            show_time = self.current_settings["vreme_prikaza"][0]
            brzina = 60*line_size/show_time
            self.brzina_vezbanja.text = "@" + str(round(brzina,0)) + "\nw/min"
        elif self.igram_igru == "Semtitles":
            accu_time = self.current_settings["vreme_akumulacije"][0]
            show_time = self.current_settings["vreme_prikaza"][0]
            line_size = self.current_settings["line_size"][0]
            brzina = round(60/(accu_time + show_time),0)
            brzina_reci = brzina * line_size
            self.brzina_vezbanja.text = "@" + str(round(brzina_reci,0)) + "\nw/min"
        elif self.igram_igru == "iSlider":
            show_time = self.current_settings["vreme_prikaza"][0]
            line_size = self.current_settings["line_size"][0]
            brzina = round(60/show_time,0)
            brzina_reci = brzina * line_size
            self.brzina_vezbanja.text = "@" + str(round(brzina_reci,0)) + "\nw/min"

    def take_articles(self):
        baza_artikla = Artikli(LAKABAZA)
        artikli = baza_artikla.uzmi_artikle()
        for artikl in artikli:
            two_liner = TwoLineListItem(text=artikl[0], secondary_text=artikl[1][0:100], bg_color = WHITE_GREY)
            two_liner.bind(on_release=lambda two_liner: self.popuni_polja(two_liner.text))
            self.lista_naslova.add_widget(two_liner)

    def pod_grid(self, load_del):
        if load_del == "del" or self.podesavanja_prikazana == True:
            self.podesavanja_grid.canvas.after.clear()
            while len(self.ids.podesavanja_grid.children):
                self.ids.podesavanja_grid.remove_widget(self.ids.podesavanja_grid.children[0])
            self.podesavanja_prikazana = False
        elif load_del == "load" or self.podesavanja_prikazana == False:
            self.make_settings_interface(self.igram_igru)

    def pop_preread(self):
        if self.izabrani_text.text == "" or self.ceo_tekst == "": return
        pop_reader = PopReader(title=self.izabrani_text.text, article=self.ceo_tekst)
        pop_reader.open()
        pop_reader.list_pages("")

    def load_settings(self):
        default_settings = DEFAULT_SETTINGS[self.igram_igru]
        settings_table = Podesavanja(LAKABAZA)
        self.current_settings.clear()
        for setting in default_settings: #'setting': [val, 'format',[min_val,max_val,increment]]
            set_row = settings_table.game_setting(self.igram_igru, setting)
            if not set_row: #if no, take default
                set_row = [self.igram_igru, setting, default_settings[setting][1], default_settings[setting][0]]
            reg = default_settings[setting][2]
            self.current_settings[setting] = [set_row[3], set_row[2], reg]

    def make_settings_interface(self, game): #make_settings_interface
        s = 0 #index of settings
        self.pod_grid("del")
        #add titile
        grd_lyt_set = GridLayout(cols=1,rows=1)
        title = Button(background_normal='',background_color="#64148c", background_down='', halign='center', valign='center', text = "Settings:")
        grd_lyt_set.add_widget(title)
        self.podesavanja_grid.add_widget(grd_lyt_set)
        self.podesavanja_grid.size_hint_y = s*.09

        for setting in self.current_settings: #'setting': [val, 'format',[min_val,max_val,increment]]
            set_row = self.current_settings[setting] #[val, 'format',[min_val,max_val,increment]

            grd_lyt = GridLayout(cols=3,rows=1,spacing=2,padding=1)
            text_za_btn = str(set_row[1]).format(vrednost = set_row[0])
            btn_text = Button(background_normal='', background_down='', background_color="#17497b", halign='center', valign='center', size_hint_x=.7, text=text_za_btn, text_language = setting, font_family=set_row[1])
            grd_lyt.add_widget(btn_text)

            btn_plus = Button(text="+", text_language = setting, font_size='20sp', size_hint_x=.15, background_normal=GREEN, background_color=GREEN)
            btn_plus.bind(on_press=lambda btn_plus: self.ajdust_setting(btn_plus.text_language,"up"))
            btn_plus.bind(on_release=lambda btn_plus: self.izracunaj_brzinu())
            grd_lyt.add_widget(btn_plus)

            btn_minus = Button(text="-", text_language = setting, font_size='20sp', size_hint_x=.15, background_normal='#ff0000', background_color='#ff0000')
            btn_minus.bind(on_press=lambda btn_minus: self.ajdust_setting(btn_minus.text_language,"down"))
            btn_minus.bind(on_release=lambda btn_plus: self.izracunaj_brzinu())
            grd_lyt.add_widget(btn_minus)

            self.podesavanja_grid.add_widget(grd_lyt)
            self.podesavanja_grid.size_hint_y = s*.07
            s += 1

        grid_lay_pre = GridLayout(cols=1,rows=1)
        btn_preread = Button(text="> Click me to preread the article <", background_normal='', background_down='', background_color="#b27400", halign='center', valign='center', size_hint_x=.8)
        btn_preread.bind(on_press=lambda btn_preread: self.pop_preread())
        grid_lay_pre.add_widget(btn_preread)
        self.podesavanja_grid.add_widget(grid_lay_pre)
        self.podesavanja_grid.size_hint_y = s*.09

        self.podesavanja_prikazana = True
        self.reload_settings = False
        self.update_settings_grid()

    def ajdust_setting(self, setting, updw_regulate): #upregulate/downregulate
        min_val, max_val, increment = self.current_settings[setting][2]
        if updw_regulate == 'up':
            if max_val:
                if self.current_settings[setting][0] + increment <= max_val:
                    self.current_settings[setting][0] += increment
            else:
                self.current_settings[setting][0] += increment
        elif updw_regulate == 'down':
            if min_val or min_val == 0:
                if self.current_settings[setting][0] - increment >= min_val:
                    self.current_settings[setting][0] -= increment
            else:
                self.current_settings[setting][0] -= increment

        self.update_settings_grid()

    def update_settings_grid(self):
        for set_grid in self.podesavanja_grid.children:
            for i in range(len(set_grid.children)):
                txt = set_grid.children[i].text
                if txt == "+" or txt == "-" or txt == "Settings:" or txt.startswith("> Click me"): continue
                setting = set_grid.children[i].text_language #text_language čuva podešavanje_variablu
                fornat = set_grid.children[i].font_family #font_family čuva format
                decimals = 2 #to odredi od increments
                split_inc = str(self.current_settings[setting][2][2]).split('.')
                if len(split_inc) == 1:
                    dec = 1
                else:
                    dec = len(split_inc[1])

                if setting == "letter_mode":
                    val = self.letter_modes[self.current_settings[setting][0]]
                else:
                    val = round(self.current_settings[setting][0], dec)


                novi_text = str(fornat).format(vrednost = val)

                if setting == "font_family":
                    novi_text = "Font: " + FONT_names[self.current_settings[setting][0]]

                if setting == "left_right":
                    if self.current_settings[setting][0] == 0:
                        novi_text = "Left>>Right"
                    else:
                        novi_text = "Left<<Right"

                if setting == "pokazivac_span":
                    if val == 0:
                        novi_text = "W/o pointer"
                    else:
                        novi_text = str(fornat).format(vrednost = round(val*100,0))

                set_grid.children[i].text = novi_text

    def save_settings(self):
        settings_table = Podesavanja(LAKABAZA)
        game_settings = DEFAULT_SETTINGS[self.igram_igru]
        for setting in game_settings:
            setting_row = settings_table.game_setting(self.igram_igru,setting)
            if setting_row: #update
                settings_table.setting_update(self.igram_igru, setting, self.current_settings[setting][0])
            else: #insert [game, setting, format, value]
                settings_table.setting_insert(self.igram_igru, setting, game_settings[setting][1], game_settings[setting][0])


class PopReader(Popup):
    def __init__(self, title, article, **kwargs):
        super(PopReader,self).__init__(**kwargs)
        self.title = title
        self.size_hint = (.9,.9)
        self.RECI_PO_STRANI = 130
        self.ceo_tekst = article
        self.separator_color = [.15,.4,.75,.99]
        self.title_color = [.15,.4,.75,.99]
        self.title_size = '20sp'
        self.background = ''
        self.background_color = [0.8,0.8,0.8,1]
        self.i_page=0
        self.display = Label(halign='left', size_hint=(1,1),valign='middle', markup=True, color="#000000")
        self.display.bind(size=self.display.setter('text_size'))
        self.body = BoxLayout(orientation='vertical', padding=2, spacing=2) #size_hint_y=1,
        self.bottom_navigation=BoxLayout(orientation='horizontal', size_hint_y=.1, padding=2, spacing=2)
        btn_prev = Button(text="<<", size_hint_x = .3, background_normal='', background_color=[.15,.4,.75,.99])
        btn_next = Button(text=">>", size_hint_x = .3, background_normal='', background_color=[.15,.4,.75,.99])
        btn_prev.bind(on_press=lambda btn_next: self.list_pages("Prev"))
        btn_next.bind(on_press=lambda btn_next: self.list_pages("Next"))
        btn_ok = Button(text="Done", background_normal='', background_color=[.15,.4,.75,.99], on_press=lambda p: self.dismiss())
        self.pages_label = Label(size_hint_x = .3, color=DARK_GREY)
        self.body.add_widget(self.display)
        self.bottom_navigation.add_widget(btn_prev)
        self.bottom_navigation.add_widget(btn_next)
        self.bottom_navigation.add_widget(self.pages_label)
        self.bottom_navigation.add_widget(btn_ok)
        self.body.add_widget(self.bottom_navigation)
        self.content=self.body

    def print_page(self):
        text_split = self.ceo_tekst.split()
        i_beg = self.RECI_PO_STRANI * self.i_page
        i_end = min(i_beg + self.RECI_PO_STRANI - 1, len(text_split))
        return ' '.join(text_split[i_beg:i_end+1])

    def list_pages(self, direction):
        if direction == "Next":
            self.i_page += 1
        elif direction == "Prev":
            self.i_page -= 1
        if self.i_page == -1:
            self.i_page = round(len(self.ceo_tekst.split())/self.RECI_PO_STRANI)
        elif self.i_page > round(len(self.ceo_tekst.split())/self.RECI_PO_STRANI):
            self.i_page = 0

        self.pages_label.text = str(self.i_page+1)+"/"+str(round(len(self.ceo_tekst.split())/self.RECI_PO_STRANI)+1)
        self.display.text_size = (self.size[0]*.9, self.size[1]*.8)
        self.display.text = self.print_page()


class Olaksaonica(Screen):
    igram_igru=""
    #params
    ceo_tekst=StringProperty("")
    tekst_split=[]
    grozd_box=ObjectProperty()
    bot_nav_box=ObjectProperty()
    rsvp_display=ObjectProperty()
    display_ugao=NumericProperty(0)
    pokazivac_ugao=NumericProperty(0)
    running=False

    nav_grid=ObjectProperty()
    nav_play=ObjectProperty()
    nav_show=ObjectProperty()
    nav_game=ObjectProperty()
    pokazivac=ObjectProperty()

    vreme_prikaza=.1
    vreme_akumulacije=.4
    line_size=4
    linija_po_strani=15 #0-9
    pokazivac_span=.5
    min_letters=5
    x_korak=.01
    broj_zrna=8 #<------------- /broj dugmenta u grzodovanju
    #variables
    pauza=0
    imagine_clock=Clock
    telegraf_clock=Clock
    klatno_clock=Clock
    titlovi_clock=Clock
    utisaj_clock=Clock
    grozda_clock=Clock
    slajder_clock=Clock
    kolonar_clock=Clock
    ### from right to left
    left_right=0
    sve_linije=[] #sve_linije[i_linije]
    i_linije=0 #index_linije
    i_reci=0
    i_linija_strana=0
    i_linije_sve=0
    cilj_brzina=100
    tele_korak="Display"
    t=0
    t_do=0
    slova_ulevo=0
    tele_text = ""
    letter_mode=0
    letter_modes=['Normal', 'No spaces', 'Space each 2nd', 'Space each 3rd', 'Space each 4th']
    utisaj_stat="Kaži"
    i_crvene=0
    i_sledece_crvene=1
    slova_po_redu=30
    grozd_korak="Display"
    zrna_postavljena=False
    zrna_otkrivena=True
    titl_korak="Display"
    tacan_grozd=[]
    nagadjam_grozd=[]
    klizeca_strana=[]

#Ne igrice (pripreme)
    def on_enter(self):
        self.podesi_podesavanja()
        self.prep_text(self.igram_igru)

    def podesi_podesavanja(self):
        PodesavanjaDB = Podesavanja(LAKABAZA)
        podesavanja_igre = PodesavanjaDB.ocitaj_podesavanja(self.igram_igru)
        for podesavanje in podesavanja_igre: #podešavanje[0-igra, 1-podešavanje, 2-format, 3-vrednosti]
            if podesavanje[1] == "vreme_prikaza":
                self.vreme_prikaza = podesavanje[3]
            elif podesavanje[1] == "vreme_akumulacije":
                self.vreme_akumulacije = podesavanje[3]
            elif podesavanje[1] == "min_letters":
                self.min_letters = podesavanje[3]
            elif podesavanje[1] == "cilj_brzina":
                self.cilj_brzina = podesavanje[3]
            elif podesavanje[1] == "line_size":
                self.line_size = podesavanje[3]
            elif podesavanje[1] == "velicina_fonta":
                self.rsvp_display.font_size = str(podesavanje[3]) + 'sp'
            elif podesavanje[1] == "font_family":
                self.rsvp_display.font_name = FONTS[podesavanje[3]]
            elif podesavanje[1] == "broj_zrna":
                self.broj_zrna = podesavanje[3]
            elif podesavanje[1] == "linija_po_strani":
                self.linija_po_strani = podesavanje[3]
            elif podesavanje[1] == "pokazivac_span":
                self.pokazivac_span = podesavanje[3]
            elif podesavanje[1] == "slova_ulevo":
                self.slova_ulevo = podesavanje[3]
            elif podesavanje[1] == "letter_mode":
                self.letter_mode = podesavanje[3]
            elif podesavanje[1] == "left_right":
                self.left_right = podesavanje[3]

    def prep_text(self, igra):
        self.i_reci = 0
        self.i_linije_sve = 0
        self.t=0
        self.sve_linije=[]
        self.tekst_split=self.ceo_tekst.split()
        r=len(self.tekst_split)//self.line_size #može l_linije_rec kao length_linije_(u jedinici)rec)
        linija = ""
        for i in range(r):
            red = self.tekst_split[i*self.line_size : (i+1)*self.line_size] #array od reči
            self.sve_linije.append(' '.join(red)) #Zašto novi red? .append(' '.join(red)+"\n")

        for _ in range(len(self.ids.nav_grid.children)):
            child = self.ids.nav_grid.children[0]
            if isinstance(child, StackButton):
                self.ids.nav_grid.remove_widget(child)

        self.rsvp_display.halign='center'
        if igra=="Imagine":
            self.rsvp_display.pos_hint={'center_x': .5, 'center_y': .5}
            text_set = [word for n, word in enumerate(self.tekst_split) if word not in self.tekst_split[:n]]
            counts = [self.tekst_split.count(word) for word in text_set]
            dikt = dict(zip(text_set, counts))
            srted = sorted(dikt.items(), key=lambda x: x[1])
            self.tekst_split = []
            sum_val = 0
            for key, val in srted:
                self.tekst_split.append("".join([ch for ch in key if ch.isalpha()]))
                sum_val += val
                if sum_val > len(counts) *.3: break
        elif igra=="Accumulation":
            self.rsvp_display.pos_hint={"center_x": .5, "center_y": .7} #+1 +
            self.rsvp_display.size_hint_y=.5
            self.add_nav_widget('keyboard')
            self.add_nav_widget('eye')
        elif igra=="Telegraphy":
            self.rsvp_display.pos_hint={'center_x': .5, 'center_y': .5}
            self.rsvp_display.size_hint_y=.7
            mode = self.letter_modes[self.letter_mode]
            if mode == 'Normal':
                self.tele_text = self.ceo_tekst
                return
            else:
                self.tele_text = "".join([ch for ch in self.ceo_tekst if ch!=" "]) # if ch.isalpha()

            if mode == 'Space each 2nd':
                self.tele_text = " ".join(self.tele_text)
            elif mode == 'Space each 3rd':
                self.tele_text = " ".join([self.tele_text[i:i+2] for i in range(0, len(self.tele_text), 2)])
            elif mode == 'Space each 4th':
                self.tele_text = " ".join([self.tele_text[i:i+3] for i in range(0, len(self.tele_text), 3)])

        elif igra=="Semtitles":
            self.rsvp_display.pos_hint={'center_x': .5, 'center_y': .5}
            self.zrna("obriši")
            self.rsvp_display.size_hint_y=.8
            self.grozd_box.size_y=.1

        else: #if igra!= "Accumulation": ili :"SpinSpanner":"DeSync":"Semtitles":"iSlider":
            self.rsvp_display.pos_hint={'center_x': .5, 'center_y': .5}
            if igra == "DeSync":
                self.rsvp_display.halign='left'
                self.rsvp_display.pos_hint={'x': .1, 'center_y': .5}
            self.zrna("obriši")
            self.rsvp_display.size_hint_y=.8
            self.grozd_box.size_y=.1

    def meri_vreme(self, meri, igra=""):
        if meri=="kreni":
            if not self.running:
                if igra=="Imagine":
                    self.imagine_clock=Clock.schedule_interval(self.imagine, 0.01)
                elif igra=="Telegraphy":
                    slova_po_reci = len(self.ceo_tekst)/len(self.ceo_tekst.split())
                    self.t_do=int(round(self.line_size * slova_po_reci,0))
                    to_tick= 60/(self.cilj_brzina * 1/self.slova_ulevo * slova_po_reci)
                    self.telegraf_clock=Clock.schedule_interval(self.telegrafi, to_tick)
                elif igra=="SpinSpanner":
                    self.klatno_clock=Clock.schedule_interval(self.klati, 0.01)
                elif igra=="DeSync":
                    self.utisaj_stat="Kaži"
                    self.utisaj_clock=Clock.schedule_interval(self.utisaj, 0.01)
                elif igra=="Accumulation":
                    self.zrna("obriši")
                    self.grozda_clock=Clock.schedule_interval(self.grozdaj, 0.01)
                elif igra=="Semtitles":
                    self.titlovi_clock=Clock.schedule_interval(self.titluj, 0.01)
                elif igra=="ZigZags":
                    self.kolonar_clock=Clock.schedule_interval(self.kolonari, 0.01)
                elif igra=="iSlider":
                    self.slajder_clock=Clock.schedule_interval(self.slajduj, 0.01)
                if self.pokazivac_span >= 0.1:
                    if igra=="Semtitles":# or igra=="DeSync":
                        self.pokazivac.text = "[b][u]A[/u]\n|!|\n|i|"
                        self.podvuci_red("start")
                else:
                    self.pokazivac.text = ""
                self.running = True
        elif meri=="završi":
            if self.running:
                if igra=="Imagine":
                    self.imagine_clock.cancel()
                elif igra=="Telegraphy":
                    self.telegraf_clock.cancel()
                elif igra=="SpinSpanner":
                    self.klatno_clock.cancel()
                elif igra=="DeSync":
                    self.utisaj_clock.cancel()
                elif igra=="Accumulation":
                    self.grozda_clock.cancel()
                elif igra=="Semtitles":
                    self.titlovi_clock.cancel()
                elif igra=="ZigZags":
                    self.kolonar_clock.cancel()
                elif igra=="iSlider":
                    self.slajder_clock.cancel()
                if self.pokazivac_span >= 0.1:
                    self.podvuci_red("stop")
                self.nav_play.icon = 'play'
                self.running = False

    def pop_instrukcije(self, igra):
        pop_inst = MyPopup("How to play > " + self.igram_igru)
        pop_inst.size_hint = (1,1)
        pop_inst.title_color = BLUE
        pop_inst.separator_color = BLUE
        layout = GridLayout(cols=1, padding=5, spacing=2, size_hint_y=None)
        label_text = Instructions(LAKABAZA, self.igram_igru, version="aims").text
        inst_label=pop_inst.make_label(label_text, BLACK, height_hint=.92)
        inst_label.valign='top'
        pop_inst.content_box.add_widget(inst_label)
        #Done
        done_btn = pop_inst.make_done(height_hint=.08)
        done_btn.background_color = BLUE
        done_btn.text = "Let's GO!"
        done_btn.bind(on_press=pop_inst.dismiss)
        pop_inst.content_box.add_widget(done_btn)
        #OpenMe
        pop_inst.open()

    def nav_kontrola(self, funkcija, igra):
        if funkcija == "Kreni/Stani":
            if self.running == False:
                self.meri_vreme("kreni", igra)
                self.nav_play.icon = 'pause'
            elif self.running == True:
                self.meri_vreme("završi", igra)
                self.nav_play.icon = 'play'
        elif funkcija == "Dugmeta":
            if self.zrna_postavljena:
                if self.zrna_otkrivena:
                    self.zrna("sakrij")
                else:
                    self.zrna("otkrij")
            else:
                if self.grozd_korak == "Display":
                    if len(self.ids.grozd_box.children) == 0 and len(self.tacan_grozd):
                        self.zrna("postavi")

        elif funkcija == "Povratak":
            if igra=="Accumulation":
                for _ in range(len(self.ids.nav_grid.children)):
                    child = self.ids.nav_grid.children[0]
                    if isinstance(child, StackButton):
                        self.ids.nav_grid.remove_widget(child)

    def add_nav_widget(self, nav_button):
        stack_button = StackButton()
        image_source = ''
        label_text = ""
        if nav_button == 'keyboard':
            stack_button.bind(on_press=lambda stb: self.nav_kontrola("Dugmeta","Accumulation"))
            #ideja: dodaj stack_buttun attribut oba image source i onda on press da Image menja između ta 2
            image_source = 'icons/keyboard_outline_grey_48dp.png'
            label_text = "Test"
        elif nav_button == 'eye':
            stack_button.bind(on_press=lambda stb: self.uporedjujem_grozdove())
            image_source = 'icons/eye_grey_48dp.png'
            label_text = "Show/Hide"
        img = Image(source=image_source, size_hint_y=.7)
        lbl = Label(text=label_text, color='#5a5a5a', size_hint_y=.3)
        stack_button.add_widget(img)
        stack_button.add_widget(lbl)
        self.ids.nav_grid.add_widget(stack_button)

#Igrice
    def imagine(self, tick):
        self.pauza+=tick
        if self.pauza > self.vreme_prikaza:
            self.rsvp_display.text = self.tekst_split[self.i_reci]
            self.i_reci += 1
            if self.i_reci > len(self.tekst_split) - 1: self.i_reci = 0
            self.pauza = 0
## Accumulation
    def grozdaj(self, tick):
        self.pauza += tick
        if self.grozd_korak == "Display":
            if self.zrna_postavljena: self.zrna("obriši")
            if self.rsvp_display.text != "": self.rsvp_display.text = ""
            if self.pauza > 1: #da prođe mala pauza pa na display
                self.nagadjam_grozd = []
                self.rsvp_display.text = self.sve_linije[self.i_linije]
                self.tacan_grozd = self.sve_linije[self.i_linije].split()
                self.i_linije += 1
                if self.i_linije > len(self.sve_linije)-1: self.i_linije=0
                self.pauza = 0
                self.grozd_korak="Sakrij"
        elif self.grozd_korak=="Sakrij":
            if self.pauza > self.vreme_prikaza:
                self.rsvp_display.text = ""
                self.pauza = 0
                self.grozd_korak="Buttons"
        elif self.grozd_korak=="Buttons":
            if self.pauza > self.vreme_akumulacije:
                # self.zrna("postavi")
                self.grozd_korak = "Display"
                self.meri_vreme("završi","Accumulation")
                self.pauza = 0

    def zrna(self, uradi):
        if uradi == "postavi":
            fs=self.rsvp_display.font_size
            r = random.sample(range(0,len(self.tekst_split)-1), self.broj_zrna)
            random_reci = [self.tekst_split[i] for i in r]
            for i in range(self.broj_zrna):
                btn = Button(text=random_reci[i], font_size=fs, size_hint=(.15,.1), background_normal='', color=BLACK, on_press=lambda btn: self.nagadjam_grozd.append(btn.text))
                self.grozd_box.add_widget(btn)
            rnd_sample = random.sample(range(0,self.broj_zrna-1), self.line_size)
            for i in range(self.line_size):
                self.ids.grozd_box.children[rnd_sample[i]].text = self.tacan_grozd[i]
            self.zrna_postavljena = True
        elif uradi == "obriši":
            while len(self.ids.grozd_box.children):
                self.ids.grozd_box.remove_widget(self.ids.grozd_box.children[0])
            self.zrna_postavljena = False
        elif uradi == "sakrij":
            for child in self.ids.grozd_box.children: child.color = WHITE
            self.zrna_otkrivena=False
        elif uradi == "otkrij":
            for child in self.ids.grozd_box.children: child.color = BLACK
            self.zrna_otkrivena=True

    def uporedjujem_grozdove(self):
        if self.rsvp_display.text == "" and self.grozd_korak == "Display":
            self.rsvp_display.text = ' '.join(self.tacan_grozd) + "\n"
            self.rsvp_display.text += ' '.join(self.nagadjam_grozd)
        else:
            self.rsvp_display.text = ""
##
    def utisaj(self, tick):
        self.pauza += tick
        if self.utisaj_stat == "Kaži":
            if self.pauza > self.vreme_prikaza:
                self.pauza = 0
                red = self.sve_linije[self.i_linije].split()
                za_display = "[color="+RED+"]"+red[0]+"[/color] " + "[color="+LIGTH_GREY+"]" + ' '.join(red[1:]) + "[/color]"
                self.utisaj_stat = "Prepoznaj"
                self.rsvp_display.text = za_display
        elif self.utisaj_stat == "Prepoznaj":
            if self.pauza > self.vreme_akumulacije:
                self.pauza = 0
                red = self.sve_linije[self.i_linije].split()
                za_display = "[color="+RED+"]"+red[0]+"[/color] " + ' '.join(red[1:])
                self.utisaj_stat = "Kaži"
                self.i_linije += 1
                if self.i_linije > len(self.sve_linije)-1: self.i_linije = 0
                self.rsvp_display.text = za_display

    def telegrafi(self,tick):
        text = ""
        if self.left_right == 0: #"Left>>Right"
            if self.t+self.t_do <= len(self.tele_text):
                self.t+=self.slova_ulevo
            else:
                self.t=0
            text = self.tele_text[self.t:self.t+self.t_do]
        elif self.left_right == 1: #"Left<<Right"
            if self.t-self.t_do >= 0:
                self.t-=self.slova_ulevo
            else:
                self.t=len(self.tele_text)-1
            text = self.tele_text[self.t-self.t_do:self.t]

        self.rsvp_display.text = text#[::-1]

    def klati(self, tick):
        self.pauza+=tick
        if self.pauza > self.vreme_prikaza:
            self.pauza = 0
            if self.i_reci +1 < self.line_size:
                self.i_reci += 1
            else:
                self.i_reci = 0
                if self.i_linije +1 < len(self.sve_linije):
                    self.i_linije +=1
                else:
                    self.i_linije = 0

            red = self.sve_linije[self.i_linije].split()
            list_red=["[color="+LIGTH_GREY+"]"+rec+"[/color]" for rec in red]
            glavna_rec=str(list_red[self.i_reci])
            list_red[self.i_reci] = glavna_rec[15:len(glavna_rec)-8]
            za_display = "[color="+LIGTH_GREY+"]|[/color]\n" + ' '.join(list_red) + "\n[color="+LIGTH_GREY+"]|[/color]"
            self.rsvp_display.text = za_display

    def titluj(self, tick):
        self.pauza+=tick
        if self.titl_korak == "Display":
            if self.pauza > self.vreme_akumulacije:
                self.pauza = 0
                if self.i_linije +1 < len(self.sve_linije):
                    self.i_linije +=1
                else:
                    self.i_linije = 0
                red = self.model_text(self.sve_linije[self.i_linije])
                za_display = "[color="+LIGTH_GREY+"]|[/color]\n" + red #+ "[color="+LIGTH_GREY+"]|[/color]"
                self.rsvp_display.text = za_display
                self.titl_korak = "Pauza"
                self.podvuci_red("start", tick)
        elif self.titl_korak == "Pauza":
            self.podvuci_red(tick=tick)
            if self.pauza > self.vreme_prikaza:
                self.rsvp_display.text = "[color="+LIGTH_GREY+"]|\n"#\n|[/color]"
                self.titl_korak = "Display"
                self.pauza = 0
                self.podvuci_red("stop")

    def kolonari(self, tick):
        self.pauza += tick
        if self.pauza > self.vreme_prikaza:
            #Proveri za novu stranu
            if self.i_linija_strana > self.linija_po_strani*2-1 or len(self.klizeca_strana) == 0: #ako završi stranu ili prazna
                self.klizeca_strana = []
                for i in range(self.linija_po_strani*2):
                    self.klizeca_strana.append(self.sve_linije[self.i_linije_sve]) #i_linije_sve
                    if self.i_linije_sve >= len(self.sve_linije) - 1:
                        self.i_linije_sve = 0
                    else:
                        self.i_linije_sve += 1
                self.i_linija_strana = 0
            #Pripremi tekst: obeleži sve_linije na strani
            za_display=""
            for i in range(self.linija_po_strani): #pređi stranu
                if i*2+1>len(self.klizeca_strana)-1:
                    continue

                if i*2==self.i_linija_strana: #ako je leva crna
                    za_display+=str(self.klizeca_strana[i*2]) + " [color="+LIGTH_GREY+"]" + self.klizeca_strana[i*2+1] + "[/color]\n "
                elif i*2+1==self.i_linija_strana: #ako je desna crna
                    za_display+="[color="+LIGTH_GREY+"]" + str(self.klizeca_strana[i*2]) + " [/color] " + self.klizeca_strana[i*2+1] + "\n"
                else: #ako su obe sive
                    za_display+="[color="+LIGTH_GREY+"]" + str(self.klizeca_strana[i*2]) + " " + self.klizeca_strana[i*2+1] + "[/color]\n"

            #Pošalji za print text
            self.rsvp_display.text = za_display
            self.i_linija_strana += 1
            self.pauza = 0

    def slajduj(self, tick):
        self.pauza += tick
        if self.pauza > self.vreme_prikaza:
            #Proveri za novu stranu
            if self.i_linija_strana > self.linija_po_strani-1 or len(self.klizeca_strana) == 0: #ako završi stranu ili prazna
                self.klizeca_strana = []
                for i in range(self.linija_po_strani):
                    self.klizeca_strana.append(self.sve_linije[self.i_linije_sve]) #i_linije_sve
                    if self.i_linije_sve >= len(self.sve_linije) - 1:
                        self.i_linije_sve = 0
                    else:
                        self.i_linije_sve += 1
                self.i_linija_strana = 0
            #Pripremi tekst: obeleži sve_linije na strani
            za_display=""
            for i in range(self.linija_po_strani): #pređi stranu
                if i>len(self.klizeca_strana)-1:
                    continue
                if i==self.i_linija_strana:
                    za_display+=" "+self.klizeca_strana[i]+" \n"
                    # za_display+=str(self.klizeca_strana[i]).replace(" ","")+" \n"
                else:
                    za_display+=" [color="+LIGTH_GREY+"]"+ self.klizeca_strana[i] +"[/color] \n"
            #Pošalji za print text
            self.rsvp_display.text = za_display
            self.i_linija_strana += 1
            self.pauza = 0

    def model_text(self, line):
        mode = self.letter_modes[self.letter_mode]
        new_line = "".join([ch for ch in line if ch!=" "]) # if ch.isalpha()
        if mode == 'No spaces':
            return new_line
        if mode == 'Space each 2nd':
            return " ".join(new_line)
        elif mode == 'Space each 3rd':
            return " ".join([self.line[i:i+2] for i in range(0, len(line), 2)])
        elif mode == 'Space each 4th':
            self.tele_text = " ".join([self.tele_text[i:i+3] for i in range(0, len(self.tele_text), 3)])
        else:
            return line

#Suplementery
    def podvuci_red(self, poz="cepaj", tick=0.01):
        if self.display_ugao != 0: return
        x = self.pokazivac.pos_hint['center_x'] + self.x_korak*tick/.01
        y = self.pokazivac.pos_hint['center_y']
        if poz == "start":
            self.x_korak = round(self.pokazivac_span/(self.vreme_prikaza/0.01),4)
            dis_y = self.rsvp_display.pos_hint['center_y']
            pok_height = self.pokazivac.texture_size[1]/self.height
            y = dis_y - pok_height
            x = .5 - self.pokazivac_span / 2
        elif poz == "stop" or x > .5 + self.pokazivac_span / 2:
            x = 1.1
        self.pokazivac.pos_hint = {'center_x': x, 'center_y': y}

    def rotiraj_display(self, ugao):
        self.display_ugao += ugao
        if abs(self.display_ugao) >= 360: self.display_ugao = 0
        if abs(self.display_ugao) == 90 or abs(self.display_ugao) == 270:
            self.rsvp_display.text_size = [Window.height, Window.width*.8]
        else:
            self.rsvp_display.text_size = [Window.width, Window.height]


class StackButton(ButtonBehavior, StackLayout):
    def __init__(self, **kwargs):
        super(StackButton,self).__init__(**kwargs)
        self.orientation='tb-lr'
        self.padding = (2,10)


class Tekstovi(Screen):
    lista_naslova=ObjectProperty()
    input_naslov=ObjectProperty()
    input_text=ObjectProperty()

    def popuni_polja(self, odabran_naslov): #selektovanim_tekstom
        baza_artikla = Artikli(LAKABAZA)
        artikl = baza_artikla.izdvoji_artikl(odabran_naslov)
        odabran_naslov = artikl[0]
        self.input_naslov.text = odabran_naslov[0]
        self.input_text.text = odabran_naslov[1]

    def uzmi_artikle(self):
        baza_artikla = Artikli(LAKABAZA)
        artikli = baza_artikla.uzmi_artikle()
        for artikl in artikli:
            one_liner = OneLineListItem(text=artikl[0], bg_color=WHITE)
            one_liner.bind(on_release=lambda one_liner: self.popuni_polja(one_liner.text))
            self.lista_naslova.add_widget(one_liner)


    def sacuvaj_artikl(self):
        if self.input_naslov.text == "" or self.input_text.text == "": return
        baza_artikla = Artikli(LAKABAZA)
        artikli = baza_artikla.uzmi_artikle()
        svi_naslovi = []
        for artikl in artikli:
            svi_naslovi.append(artikl[0])
        tekst = self.input_text.text
        cist_tekst = tekst.replace("\n"," ")
        while cist_tekst.find("  ") != -1:
            cist_tekst = cist_tekst.replace("  "," ")

        if self.input_naslov.text in svi_naslovi:
            baza_artikla.izbrisi_artikl(self.input_naslov.text)
        baza_artikla.sacuvaj_artikl(self.input_naslov.text, cist_tekst)
        self.on_enter()

    def izbrisi_artikl(self):
        baza_artikla = Artikli(LAKABAZA)
        naslov = self.input_naslov.text
        success = baza_artikla.izbrisi_artikl(naslov)
        self.on_enter()

    def on_enter(self):
        while len(self.ids.lista_naslova.children):
            self.ids.lista_naslova.remove_widget(self.lista_naslova.children[0])
        self.uzmi_artikle()


class Dynamic(Screen):
    miro_top_bar=ObjectProperty()
    bar_icon=ObjectProperty()
    content_box=ObjectProperty()
    tut_steps = []
    tut_instructions = []
    step = StringProperty("")
    title_but=ObjectProperty()
    body_text=ObjectProperty()


    def learning(self):
        self.clear_content()
        text = "What to learn about speed reading and why I constructed this app like this? Well, you're in luck because I'm writing a lot about reading on my blog. Basically, [b]this app is the practical part of the written course I made on my blog[/b].\n[i]Here is the link to dive deeper:[/i]"
        lbl = Label(text=text, size_hint_y=.22, markup=True, halign='center', valign='middle', color=BLACK)
        lbl.bind(size=lbl.setter('text_size'))
        self.content_box.add_widget(lbl)

        link_blog = "https://wizardry-of-science.blogspot.com/p/reading-speedster.html"
        blog_link = MDRectangleFlatIconButton(text = "[u]Wizardry-of-Science/p/reading-speedster.html[/u]", icon="link", line_color="purple", text_color="blue", pos_hint = {"center_x": .5, "center_y": .5})
        blog_link.bind(on_press=lambda blog_link: webbrowser.open(str(link_blog)))
        self.content_box.add_widget(blog_link)

        text = "[b]  I part: Anatomy and physiology of reading[/b] - first let's understand and dive deep into the whole theory of how we percive words and connect them into meaning. Then we'll try to understend how brain comprehends the text. That should be enough to build strategy for reading improvment. Here are the titles:"
        text += "\n     >> Gotta read fast\n     >> Word Perception\n     >> Word boxer\n     >> Subvocalization and reading\n     >> Horizons of reading comprehension\n     >> Semantic memory\n     >> Abstractive knowledge << "
        text += "\n\n[b]  II part: Planning and the Strategy of Exercising[/b]:\n     >> Practicing easy and speed reading\n     >> Numbers and not words\n     >> Movement control for improved reading \n           [i]...and probably more[/i]  <<"
        title_names = Label(text=text, size_hint_y=.6, markup=True, halign='left', valign='middle', color=BLACK)
        title_names.bind(size=title_names.setter('text_size'))
        self.content_box.add_widget(title_names)

    def next_step(self):
        i = self.tut_steps.index(self.step)
        if i >= len(self.tut_steps) - 1:
            i = 0
        else:
            i += 1
        self.step = self.tut_steps[i]
        self.title_but.text = self.tut_steps[i]
        self.body_text.text = self.tut_instructions[i]

    def prev_step(self):
        i = self.tut_steps.index(self.step)
        if i < 0:
            i = len(self.tut_steps)-1
        else:
            i -= 1
        self.step = self.tut_steps[i]
        self.title_but.text = self.tut_steps[i]
        self.body_text.text = self.tut_instructions[i]

    def load_tut(self):
        tut = Tutorial(LAKABAZA)
        self.tut_steps = tut.steps
        self.tut_instructions = tut.instructions

    def tutorial(self):
        self.load_tut()
        self.clear_content()
        menu_box = BoxLayout(orientation='horizontal', padding=2, spacing=2, size_hint_y=.07)
        left_but = Button(text="<<", size_hint_x=.12, background_normal='', background_color=DARK_RED)
        left_but.bind(on_press = lambda a: self.prev_step())
        self.step = self.tut_steps[0]
        self.title_but = MDLabel(text=self.tut_steps[0], font_style='Subtitle1', markup=True, size_hint_x=.7, color=BLUE, halign='center')
        right_but = Button(text=">>", size_hint_x=.12, background_normal='', background_color=GREEN)
        right_but.bind(on_press = lambda a: self.next_step())
        menu_box.add_widget(left_but)
        menu_box.add_widget(self.title_but)
        menu_box.add_widget(right_but)
        self.content_box.add_widget(menu_box)
        self.body_text = MDLabel(text=self.tut_instructions[0], font_style='Body1', color=BLACK, size_hint_y=.85, markup=True, halign='left', valign='top')
        self.body_text.bind(size=self.body_text.setter('text_size'))
        self.content_box.add_widget(self.body_text)

    def clear_content(self):
        while len(self.content_box.children):
            self.content_box.remove_widget(self.content_box.children[0])


#########################################
class WindowManager(ScreenManager):
    back_button_press_counter = NumericProperty(0)

    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.key_pressed)

    def key_pressed(self, window, key, *args):
        if key==27:
            if self.current_screen.name == "Pocetna":
                if self.back_button_press_counter == 1:
                    return False
                else:
                    snak = Snackbar(text="Press back again to exit Reading Speedster", duration = .5, snackbar_x="10dp", snackbar_y="10dp")
                    snak.size_hint_x = (Window.width - (snak.snackbar_x * 2)) / Window.width
                    snak.bg_color = "purple"
                    snak.open()
                    self.back_button_press_counter += 1
                    Clock.schedule_once(self.reset_back, 1)
                    return True
            elif self.current_screen.name == "TextPrep":
                self.screens[1].odakle = "Iz početne"
                self.transition = SlideTransition(direction='right')
                self.current = "Pocetna"
                return True
            elif self.current_screen.name == "Olaksaonica":
                self.screens[2].nav_kontrola("Povratak", self.screens[1].igram_igru)
                self.screens[2].meri_vreme("završi", self.screens[1].igram_igru)
                self.screens[1].odakle = "Iz olakšaonice"
                self.transition = SlideTransition(direction='right')
                self.current = "TextPrep"
                return True
            elif self.current_screen.name == "Tekstovi":
                self.transition = SlideTransition(direction='down')
                self.current = "Pocetna"
                return True
            elif self.current_screen.name == "Dynamic":
                self.transition = SlideTransition(duration=0)
                self.current = "Pocetna"
                return True
        else:
            self.back_button_press_counter = 0

    def reset_back(self,*args):
        self.back_button_press_counter = 0


class LakoCitanjeApp(MDApp):
    pass

        # LabelBase.register(name='Serif', fn_regular='data/fonts/serif.otf')
        # LabelBase.register(name='Serif italic', fn_regular='data/fonts/serif-italic.otf')
        # LabelBase.register(name='Arial', fn_regular='data/fonts/arial.ttf')
        # LabelBase.register(name='Calibri', fn_regular='data/fonts/calibri.ttf')
        # LabelBase.register(name='Times New Roman', fn_regular='data/fonts/times-new-roman.ttf')
        # LabelBase.register(name='Ubuntu', fn_regular='data/fonts/ubuntu.ttf')


if __name__=='__main__':
    LakoCitanjeApp().run()


