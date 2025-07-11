def temperature_converter():
    print("\n🌡️ Temperature Converter")
    print("----------------------")
    print("Supported scales: Celsius (C), Fahrenheit (F), Kelvin (K)")
    
    while True:
        try:
            # Get input temperature
            temp = float(input("\nEnter temperature value: "))
            original_scale = input("Enter original scale (C/F/K): ").upper()
            
            if original_scale not in ['C', 'F', 'K']:
                print("⚠️ Invalid scale! Please enter C, F, or K")
                continue
            
            # Perform conversions
            if original_scale == 'C':
                f = (temp * 9/5) + 32
                k = temp + 273.15
                print(f"\n{temp}°C is equal to:")
                print(f"{f:.2f}°F")
                print(f"{k:.2f} K")
            elif original_scale == 'F':
                c = (temp - 32) * 5/9
                k = c + 273.15
                print(f"\n{temp}°F is equal to:")
                print(f"{c:.2f}°C")
                print(f"{k:.2f} K")
            elif original_scale == 'K':
                c = temp - 273.15
                f = (c * 9/5) + 32
                print(f"\n{temp} K is equal to:")
                print(f"{c:.2f}°C")
                print(f"{f:.2f}°F")
            
            # Ask to continue
            another = input("\nConvert another temperature? (y/n): ").lower()
            if another != 'y':
                print("\nThank you for using the Temperature Converter! Goodbye!")
                break
                
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

# ASCII art and program start
print("""
   _______                       __                __
  / ___/ /  ___ ____ ____ ___   / /  ____  ___ ___/ /__ ____
 / /__/ _ \/ _ `/ _ `/ -_) _ \ / /__/ __/ (_-</ _  / -_) __/
 \___/_//_/\_,_/\_, /\__/_//_/____/_/    \___/\_,_/\__/_/   
                /___/                                        
""")
temperature_converter()