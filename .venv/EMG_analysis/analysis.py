import time
import csv

import matplotlib.pyplot as plt
import serial  # Dodano brakujący import serial

class SerialReader:
    def __init__(self, comport, baudrate, timestamp=False, output_file='output.csv'):
        """
        Initializes the SerialReader class.
        Args:
        comport(str): Serial port
        baudrate(int): Czestotliwosc pobierania danych
        timestamp: Whether to include timestamps in the output
        :param output_file: Path to the output CSV file
        """
        self.comport = comport
        self.baudrate = baudrate
        self.timestamp = timestamp
        self.plik = output_file
        self.serial_connection = None
        self.start_time = None

    def setup_serial_connection(self):
        """Initializes the serial connection."""
        self.serial_connection = serial.Serial(self.comport, self.baudrate, timeout=0.1)
        self.start_time = time.perf_counter()  # Record the start time using perf_counter for accurate elapsed time

    def read_and_write(self):
        """
        Reads data from the serial port and writes it to a CSV file.
        """
        if not self.serial_connection:
            raise ValueError("Serial connection is not initialized. Call setup_serial_connection first.")

        with open(self.output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write header row
            if self.timestamp:
                csv_writer.writerow(['Elapsed Time (s)', 'Data'])
            else:
                csv_writer.writerow(['Data'])

            print(f"Writing data to {self.output_file}...")

            while True:
                try:
                    data = self.serial_connection.readline().decode().strip()  # Read and decode serial data

                    if data:
                        if self.timestamp:
                            elapsed_time = round(time.perf_counter() - self.start_time, 1)  # Add 0.1 to start time
                            print(f'{elapsed_time}s > {data}')
                            csv_writer.writerow([elapsed_time, data])
                        else:
                            print(data)
                            csv_writer.writerow([data])

                        csvfile.flush()  # Ensure data is written to the file immediately

                except KeyboardInterrupt:
                    print("\nStopped by user.")
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    break

    def close_connection(self):
        """Closes the serial connection."""
        if self.serial_connection:
            self.serial_connection.close()
            print("Serial connection closed.")

class Analiz:
    import matplotlib.pyplot as plt
    def __init__(self, plik):
        self.plik = plik
        self.nap = range(800, 1024)  # miesien napiety
        self.roz = range(0, 350)  # miesien rozluzniony
        self.sr_nap = range(350, 800)  # miesien srednio napiety

        with open('output.csv', 'r', newline='') as csv_plik:
            plik = csv.reader(csv_plik)
            czas, sygnal = list(), list()
            for wiersz in plik:
                try:
                    czas.append(float(wiersz[0]))
                    sygnal.append(int(wiersz[1]))
                except Exception:
                    continue
        self.sygnal = sygnal
        self.czas = czas

    def wykres(self, nazwa):
        plt.plot(self.czas, self.sygnal,label = "f(x)", color = "blue",marker='o', linestyle='-', markersize=2)
        plt.savefig(str(nazwa)+'.png')
        plt.show()

    def czas_trwania(self):

        sygnal = self.sygnal
        czas_nap, czas_luz, czas_sred = 0,0,0
        for i in range(len(sygnal)+1):
            if i in self.nap:
                czas_nap += 0.1
            elif i in self.sr_nap:
                czas_sred += 0.1
            elif i in self.roz:
                czas_luz += 0.1
        return {'rozluznione': round(czas_luz,2),'srednionapiete':round(czas_sred,2),'napiete':round(czas_nap,2)}
    def maximum(self):
        czas = self.czas
        sygnal = self.sygnal
        max_nap, max_luz, max_sred = 0, 0, 0
        napiety, rozluzniony, srednio_napiety = self.nap, self.roz, self.sr_nap
        for i in range(len(sygnal)):
            if sygnal[i] in napiety:
                for j in range(i, len(sygnal)):
                    if sygnal[j] not in napiety:
                        break
                    if max_nap < czas[j] - czas[i]:
                        max_nap = czas[j] - czas[i]
            if i in rozluzniony:
                for j in range(i, len(sygnal)):
                    if sygnal[j] not in rozluzniony:
                        break
                    if max_luz < czas[j] - czas[i]:
                        max_luz = czas[j] - czas[i]
            if i in srednio_napiety:
                for j in range(i, len(sygnal)):
                    if sygnal[j] not in srednio_napiety:
                        break
                    if max_sred < czas[j] - czas[i]:
                        max_sred = czas[j] - czas[i]
        return {'rozluznione': round(max_luz,2), 'srednionapiete': round(max_sred,2), 'napiete': round(max_nap,2)}

if __name__ == '__main__':
    reader = SerialReader('COM4', 9600, timestamp=True)
    try:
        reader.setup_serial_connection()
        reader.read_and_write()
    finally:
        reader.close_connection()
    analiz = Analiz('output.csv')
    analiz.wykres('popa')
    print(analiz.czas_trwania())
    print(analiz.maximum())
