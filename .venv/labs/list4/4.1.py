class Pacjent:
    BEZPIECZNY_ZAKRES_BMI = (18.5, 24.9)

    def __init__(self, *dane):

        if len(dane) == 1:
            dane = dane[0]
        self.pesel = dane[0]
        self.imie = dane[1]
        self.nazwisko = dane[2]
        self.waga = float(dane[3])
        self.wzrost = float(dane[4])

    def wiek(self):
        pesel = self.pesel
        if int(pesel[2]) >= 2 and int(pesel[2]) <= 3:
            rok = 2000 + int(pesel[0:2])
        else:
            rok = 1900 + int(pesel[0:2])
        wiek = 2024 - rok
        if wiek % 10 == 1 and wiek < 10:
            return str(wiek) + " rok"
        elif wiek % 10 in (1, 5, 6, 7, 8, 9, 0):
            return str(wiek) + " lat"
        else:
            return str(wiek) + " lata"

    def bmi(self):
        return self.waga / ((self.wzrost / 100) ** 2)

    def ryzyko(self):
        bmi_value = self.bmi()
        if not (self.BEZPIECZNY_ZAKRES_BMI[0] <= bmi_value):
            return "Niedowaga!!!"
        if not (bmi_value <= self.BEZPIECZNY_ZAKRES_BMI[1]):
            return "Nadwaga!!!"
        else:
            return "Norma"

    def norm_waga(self):
        waga_min = ((self.wzrost / 100) ** 2) * self.BEZPIECZNY_ZAKRES_BMI[0]
        waga_max = ((self.wzrost / 100) ** 2) * self.BEZPIECZNY_ZAKRES_BMI[1]
        return {"BMI ": round(self.bmi(), 2), "Waga normalna minimalna": round(waga_min, 2),
                "Waga normalna maksymalna": round(waga_max, 2)}


pac = '11111111111 Tom Deff 24 180'.split()
pac2 = ['28013548619', 'John', 'Smith', 22, 220]
dane1 = Pacjent(pac)
print(dane1.ryzyko())
print(dane1.wiek())
print(dane1.norm_waga())
dane2 = Pacjent(pac2)
print(dane2.ryzyko())
print(dane2.wiek())
print(dane2.norm_waga())