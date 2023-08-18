# A project that automatically converts Celsius to Fahrenheit 
# And Fahrenheit to Celsius 
def main():
    print("Hello! Here's the forecast for today:")
    answer = input("Do you need Fahrenheit or Celsius?")
    originalTemperature = input("What is the temperature currently?")
    match answer:
        case "Fahrenheit":
            CelsiusToFahrenheit(int(originalTemperature))
        case "Celsius":
            FahrenheitToCelsius(int(originalTemperature))
        case "fahrenehit":
            CelsiusToFahrenheit(int(originalTemperature))
        case "celsius":
            FahrenheitToCelsius(int(originalTemperature))

def CelsiusToFahrenheit(celsius):
    Fahrenheit = int((celsius * 9/5) + 32)
    print("The temperature today is", Fahrenheit, "Fahrenheit")
    return Fahrenheit
          

def FahrenheitToCelsius(fahrenheit):
    Celsius = int((fahrenheit - 32) * 5/9)
    print("the temperature today is", Celsius, "Celsius")
    return Celsius

if __name__ == "__main__":
    main()
