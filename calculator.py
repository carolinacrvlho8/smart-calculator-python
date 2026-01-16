# calculator.py - Smart Calculator
import json
from datetime import datetime
from colorama import init, Fore, Back, Style

class SmartCalculator:
    def __init__(self):
        self.history = []
        init(autoreset=True)  # Inicializa Colorama
        
    def add(self, a, b):
        result = a + b
        self.save_to_history(f"{a} + {b} = {result}")
        return result
        
    def save_to_history(self, operation):
        entry = {
            "operation": operation,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.history.append(entry)
        self.save_to_file()
        
    def save_to_file(self):
        with open("calculator_history.json", "w") as f:
            json.dump(self.history, f, indent=2)
            
    def show_history(self):
        print(Fore.CYAN + "\n📜 Histórico de Operações:")
        for entry in self.history[-5:]:  # Últimas 5
            print(Fore.YELLOW + f"{entry['timestamp']}: {entry['operation']}")

# Menu principal
def main():
    calc = SmartCalculator()
    print(Fore.GREEN + "🧮 SMART CALCULATOR")
    
    while True:
        print(Fore.WHITE + "\n1. Adição")
        print("2. Ver histórico")
        print("3. Sair")
        
        choice = input(Fore.CYAN + "\nOpção: ")
        
        if choice == "1":
            try:
                a = float(input("Número 1: "))
                b = float(input("Número 2: "))
                result = calc.add(a, b)
                print(Fore.GREEN + f"✅ Resultado: {result}")
            except:
                print(Fore.RED + "❌ Erro: Digite números válidos!")
                
        elif choice == "2":
            calc.show_history()
            
        elif choice == "3":
            print(Fore.MAGENTA + "👋 Até breve!")
            break

if __name__ == "__main__":
    main()
