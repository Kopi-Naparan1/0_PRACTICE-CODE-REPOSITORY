from abc import ABC, abstractmethod



# Assignment 7 Failed
def assignment7():
    class Exporter(ABC):

        @abstractmethod
        def export(self,data):
            pass

    class PDF_Exporter(Exporter):
        def export(self, data):
            print(f'Exporting [{data}] to [{data}.pdf] file. ')


    class CSV_Exporter(Exporter):
        def export(self,data):
            print(f'Exporting [{data}] to [{data}.csv] file. ')

    class TXT_Exporter(Exporter):
        def export(self,data):
            print(f'Exporting [{data}] to [{data}.txt] file. ')

    def alert_user(file_type_export, data):
        file_type_export.export(data)

    def file_type_to_variable():
        pdf = PDF_Exporter()
        csv = CSV_Exporter()
        txt = TXT_Exporter()


        alert_user(pdf,"Kopi Interview")
        alert_user(txt,"Love letter")
        alert_user(csv, "Income 2025")
    file_type_to_variable()

def assignment7_1():
    class Item(ABC):

        @abstractmethod
        def dispense(self):
            pass


    class Snack(Item):
        def dispense(self):
            print('[Toy Machine Activated]')
            print('Dropping snack with a thud!')


    class Drink(Item):
        def dispense(self):
            print("[Drink Machine Activated]")
            print('Pouring drink into a magic cup!')


    class Toy(Item):

        def dispense(self):
            print("[Snack Machine Activated]")
            print('Activating the toy chute!')

    class Book(Item):

        def dispense(self):
            print("[Book Machine Activated]")
            print('Flipping the smart book')


    def vending_machine(items_to_get):
        items_to_get.dispense()


    S = Snack()
    D = Drink()
    T = Toy()
    B = Book()

    vending_machine(S)
    vending_machine(D)
    vending_machine(T)
    vending_machine(B)
















def main():
    print("=" * 30)
    print('STARTING THE #6 Abstract')
    print("=" * 30)
    print('\n' * 5)

    # assignment7()
    # assignment7_1()



if __name__ == "__main__":
    main()