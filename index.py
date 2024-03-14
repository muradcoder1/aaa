class TeleviziyaRemote:
    def _init_(self,power_on,power_off,value_down,channel):
        self.power_on = False
        self.power_off=True
        self.value_down = 31
        self.channel=54

    def power_on(self):
        if not self.power_on:
            self.power_on = True
            print("power_on")
            self.televiziya_durumu()

    def power_off(self):
        if self.power_off:
            self.power_off = False
            print("power_off.")
            self.televiziya_vaziyeti()

    def channel(self, new_channel):
        self.channel = new_channel
        print(f"Kanal deyişdirildi: {self.channel}")
        self.televiziya_vaziyeti()

    def value_down(self, new_value):
        self.value_down = new_value
        print(f"Ses səviyyəsi ayarlandı: {self.value_down}")
        self.televiziya_vaziyeti()

    def televiziya_vaziyeti(self):
        if self.power_on:
            print("Televiziya açıq.")
            print(f"Kanal: {self.channel}")
            print(f"Ses səviyyəsi: {self.value_down}")
        else:
            print("Televiziya söndürülmüşdur.")


kumanda = TeleviziyaRemote()
kumanda.power_on()
kumanda.channel(5)
kumanda.value_down(70)
kumanda.channel()