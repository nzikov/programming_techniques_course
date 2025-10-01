class Wielomian:
    """
    Klasa reprezentująca wielomian o współczynnikach rzeczywistych lub całkowitych.

    Atrybuty:
        _wsp (tuple): krotka przechowująca współczynniki wielomianu.
                      współczynniki są uporządkowane od najniższego do najwyższego stopnia.

    Komentarze wygenerowane przez ChatGPT w odpowiedzi na prompt: 'Hei, dodaj docstringi w stylu Google do kodu:',
    z niewielkimi korektami autorskimi.
    """

    def __init__(self, *wsp):
        """
        Inicjalizuje wielomian na podstawie podanych współczynników.

        Args:
            *wsp (int, float): współczynniki wielomianu podane jako argumenty pozycyjne.

        Raises:
            TypeError: Jeśli którykolwiek z współczynników nie jest liczbą całkowitą ani zmiennoprzecinkową.
        """
        for w in wsp:
            if not isinstance(w, (int, float)):
                raise TypeError('Współczynniki wielomianu powinny być liczbami!')

        wsp = list(wsp)
        while len(wsp) > 1 and wsp[-1] == 0:
            del wsp[-1]

        self._wsp = tuple(wsp)

    def __str__(self):
        """
        Zwraca reprezentację tekstową wielomianu.

        Returns:
            str: reprezentacja wielomianu w postaci wyrażenia algebraicznego.
        """
        if self.deg() == 0 and self._wsp[0] == 0:
            return '0'

        zapis = ''
        for i in range(len(self._wsp)):
            if self._wsp[i] != 0:
                zapis += (str(self._wsp[i]) +
                         ('x^' + str(i) if i > 0 else '') +
                         (' + ' if i < len(self._wsp) - 1 else ''))
        return zapis

    def __call__(self, x):
        """
        Oblicza wartość wielomianu dla podanej wartości argumentu x.

        Args:
            x (int, float): wartość argumentu, dla której należy obliczyć wielomian.

        Returns:
            float: wartość wielomianu w punkcie x.
        """
        wynik = 0
        for i in range(len(self._wsp)):
            wynik += self._wsp[i] * x**i
        return wynik

    def __add__(self, drugi):
        """
        Dodaje dwa wielomiany.

        Args:
            drugi (wielomian): wielomian, który ma zostać dodany.

        Returns:
            wielomian: nowy wielomian będący sumą dwóch wielomianów.
        """
        if len(self._wsp) >= len(drugi._wsp):
            wsp = list(self._wsp)
            for i in range(len(drugi._wsp)):
                wsp[i] += drugi._wsp[i]
            return Wielomian(*wsp)
        else:
            return drugi + self

    def deg(self):
        """
        Zwraca stopień wielomianu.

        Returns:
            int: stopień wielomianu (najwyższy indeks z niezerowym współczynnikiem).
        """
        return len(self._wsp) - 1

w = Wielomian(1, 2, 3, 4, 5)
print('w(x) =', w)
print('deg(w(x)) =', w.deg())

w5 = Wielomian(1, 2, 5, 10, 20)
print('w5(x) =', w5)
print('deg(w5(x)) =', w5.deg())

w1 = Wielomian(-1)
print('w1(x) =', w1)
print('deg(w1(x)) =', w1.deg())

v = w + w5 + w1
print('v(x) =', v)
print('deg(v(x)) =', v.deg())