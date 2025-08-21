import sqlite3

class Artikli:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.commit()

    def uzmi_artikle(self):
        self.cur.execute("SELECT * FROM Artikli ")
        rows = self.cur.fetchall()
        return rows

    def izdvoji_artikl(self, naslov):
        self.cur.execute("SELECT * FROM Artikli WHERE [naslov]=?", (naslov,))
        rows = self.cur.fetchall()
        return rows

    def sacuvaj_artikl(self, naslov, tekst):
        self.cur.execute("INSERT INTO Artikli VALUES (?, ?)", (naslov, tekst))
        self.conn.commit()

    def izbrisi_artikl(self, naslov):
        self.cur.execute("DELETE FROM Artikli WHERE [naslov]=?", (naslov,))
        self.conn.commit()

    def __del__(self): #destructor
        self.conn.close()


class Podesavanja:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.commit()

    def check_all(self):
        #SELECT where igra == svaka igra
        pass

    def ocitaj_podesavanja(self, igra):
        self.cur.execute("SELECT * FROM Podesavanja WHERE igra = ? ", (igra,)) #ako nije trailing , onda gleda kao len(igra) broja inputa
        rows = self.cur.fetchall()
        return rows

    def sacuvaj_podesavanja(self, igra, podesavanje, vrednost):
        self.cur.execute("UPDATE Podesavanja SET vrednost = ? WHERE igra = ? AND podešavanje = ?", (vrednost, igra, podesavanje))
        self.conn.commit()

    def __del__(self): #destructor
        self.conn.close()

    #eng
    def game_setting(self, game, setting):
        self.cur.execute("SELECT * FROM Podesavanja WHERE igra = ? AND podešavanje = ?", (game, setting))
        rows = self.cur.fetchall()
        if rows:
            return rows[0]

    def setting_update(self, game, setting, value):
        self.cur.execute("UPDATE Podesavanja SET vrednost = ? WHERE igra = ? AND podešavanje = ?", (value, game, setting))
        self.conn.commit()

    def setting_insert(self, game, setting, fornat, value):
        self.cur.execute("INSERT INTO Podesavanja VALUES (?, ?, ?, ?)", (game, setting, fornat, value))
        self.conn.commit()

class Instructions:
    def __init__(self, db, game, version):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.commit()
        self.text = ""
        if game == "Imagine": self.text = self.imagine(version)
        if game == "Telegraphy": self.text = self.telegrafy(version)
        if game == "SpinSpanner": self.text = self.spin_spanner(version)
        if game == "DeSync": self.text = self.desync(version)
        if game == "Accumulation": self.text = self.accumulation(version)
        if game == "Semtitles": self.text = self.semtitles(version)
        if game == "ZigZags": self.text = self.zig_zags(version)
        if game == "iSlider": self.text = self.islider(version)

    def imagine(self, version):
        self.cur.execute("SELECT * FROM Instructions WHERE [game]='Imagine'")
        instruction_row = self.cur.fetchall()
        if version == "prep":
            return str(instruction_row[0][1]) #returns plain text! so python's \n doesn't translate into new line
        elif version == "aims":
            return instruction_row[0][2]

    def telegrafy(self, version):
        self.cur.execute("SELECT * FROM Instructions WHERE [game]='Telegraphy'")
        instruction_row = self.cur.fetchall()
        if version == "prep":
            return str(instruction_row[0][1]) #returns plain text! so python's \n doesn't translate into new line
        elif version == "aims":
            return instruction_row[0][2]

    def spin_spanner(self, version):
        self.cur.execute("SELECT * FROM Instructions WHERE [game]='SpinSpanner'")
        instruction_row = self.cur.fetchall()
        if version == "prep":
            return instruction_row[0][1]
        elif version == "aims":
            return instruction_row[0][2]

    def desync(self, version):
        self.cur.execute("SELECT * FROM Instructions WHERE [game]='DeSync'")
        instruction_row = self.cur.fetchall()
        if version == "prep":
            return instruction_row[0][1]
        elif version == "aims":
            return instruction_row[0][2]

    def accumulation(self, version):
        self.cur.execute("SELECT * FROM Instructions WHERE [game]='Accumulation'")
        instruction_row = self.cur.fetchall()
        if version == "prep":
            return instruction_row[0][1]
        elif version == "aims":
            return instruction_row[0][2]


    def semtitles(self, version):
        self.cur.execute("SELECT * FROM Instructions WHERE [game]='Semtitles'")
        instruction_row = self.cur.fetchall()
        if version == "prep":
            return instruction_row[0][1]
        elif version == "aims":
            return instruction_row[0][2]

    def zig_zags(self, version):
        self.cur.execute("SELECT * FROM Instructions WHERE [game]='ZigZags'")
        instruction_row = self.cur.fetchall()
        if version == "prep":
            return instruction_row[0][1]
        elif version == "aims":
            return instruction_row[0][2]

    def islider(self, version):
        self.cur.execute("SELECT * FROM Instructions WHERE [game]='iSlider'")
        instruction_row = self.cur.fetchall()
        if version == "prep":
            return instruction_row[0][1]
        elif version == "aims":
            return instruction_row[0][2]


class QuickTips:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.commit()

    def pick_tip(self):
        self.cur.execute("SELECT * FROM Tips")
        tip_rows = self.cur.fetchall()
        import random
        i=random.randint(0,len(tip_rows)-1)
        return tip_rows[i][0]


class Tutorial:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.commit()
        self.steps = []
        self.instructions = []
        self.load_tutorial()

    def load_tutorial(self):
        self.cur.execute("SELECT * FROM Tutorial")
        tutorial_rows = self.cur.fetchall()
        self.steps = [step[0] for step in tutorial_rows]
        self.instructions = [instruction[1] for instruction in tutorial_rows]



