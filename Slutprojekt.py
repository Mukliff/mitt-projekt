import json

class Uppgift:
    """Representerar en uppgift i uppgiftshanteraren."""

    def __init__(self, uppgift, klar=False):
        """Initierar en ny uppgift."""
        self.uppgift = uppgift
        self.klar = klar

    def __str__(self):
        """Returnerar en strängrepresentation av uppgiften."""
        return f"{self.uppgift} (Klar: {self.klar})"
    
class Uppgiftshanterare:
    """Hanterar en lista med uppgifter."""

    def __init__(self, filnamn="uppgifter.json"):
        """Initierar en ny uppgiftshanterare."""
        self.filnamn = filnamn
        self.uppgifter = self.ladda_uppgifter()

    def ladda_uppgifter(self):
        """Laddar uppgifter från en JSON-fil."""
        try:
            with open(self.filnamn, "r") as f:
                data = json.load(f)
                return [Uppgift(uppgift["uppgift"], uppgift["klar"]) for uppgift in data]
        except FileNotFoundError:
            return []
        
    def spara_uppgifter(self):
        """Sparar uppgifter till en JSON-fil."""
        with open(self.filnamn, "w") as f:
            json.dump([{"uppgift": uppgift.uppgift, "klar": uppgift.klar} for uppgift in self.uppgifter], f)

    def lägg_till_uppgift(self):
        """Lägger till en ny uppgift."""
        uppgift = input("Ange uppgift: ")
        self.uppgifter.append(Uppgift(uppgift))
        print("Uppgift tillagd!")

    def ta_bort_uppgift(self):
        """Tar bort en uppgift."""
        if not self.uppgifter:
            print("Ingen uppgift att ta bort.")
            return
        
        for index, uppgift in enumerate(self.uppgifter):
            print(f"{index + 1}. {uppgift}")

        val = int(input("Ange numret på uppgiften att ta bort: ")) - 1

        if 0 <= val < len(self.uppgifter):
            del self.uppgifter[val]
            print("Uppgift borttagen!")
        else:
            print("Ogiltigt nummer.")

    def markera_klar(self):
        """Markerar en uppgift som klar."""
        if not self.uppgifter:
            print("Ingen uppgift att markera som klar.")
            return
        
        for index, uppgift in enumerate(self.uppgifter):
            print(f"{index + 1}. {uppgift}")

        val = int(input("Ange numret på uppgiften att markera som klar: ")) - 1

        if 0 <= val < len(self.uppgifter):
            self.uppgifter[val].klar = True
            print("Uppgift markerad som klar!")
        else:
            print("Ogiltigt nummer.")

    def visa_uppgifter(self):
        """Visar alla kvarstående uppgifter."""
        if not self.uppgifter:
            print("Inga kvarstående uppgifter.")
        else:
            print("Kvarstående uppgifter:")
            for index, uppgift in enumerate(self.uppgifter):
                if not uppgift.klar:
                    print(f"{index + 1}. {uppgift}")

def huvudprogram():
    """Kör huvudprogrammet."""
    hanterare = Uppgiftshanterare()

    while True:
        print("\nVälj en åtgärd:")
        print("1. Lägg till uppgift")
        print("2. Ta bort uppgift")
        print("3. Markera klar")
        print("4. Visa uppgifter")
        print("5. Avsluta")

        val = input("Ange val: ")

        if val == "1":
            hanterare.lägg_till_uppgift()
        elif val == "2":
            hanterare.ta_bort_uppgift()
        elif val == "3":
            hanterare.markera_klar()
        elif val == "4":
            hanterare.visa_uppgifter()
        elif val == "5":
            break
        else:
            print("Ogiltigt val.")

        hanterare.spara_uppgifter()
        
if __name__ == "__main__":
    huvudprogram()