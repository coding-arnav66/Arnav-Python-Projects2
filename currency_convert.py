from forex_python.converter import CurrencyRates

c = CurrencyRates()
currency_dict = {
    "american dollar": "USD",
    "euro": "EUR",
    "british pound": "GBP",
    "indian rupee": "INR",
    "japanese yen": "JPY",
    "chinese yuan": "CNY",
    "australian dollar": "AUD",
    "canadian dollar": "CAD",
    "swiss franc": "CHF",
    "russian ruble": "RUB",
    "brazilian real": "BRL",
    "south african rand": "ZAR",
    "singapore dollar": "SGD",
    "hong kong dollar": "HKD",
    "new zealand dollar": "NZD",
    "thai baht": "THB",
    "mexican peso": "MXN",
    "turkish lira": "TRY",
    "south korean won": "KRW",
    "swedish krona": "SEK",
    "norwegian krone": "NOK",
    "danish krone": "DKK",
    "polish zloty": "PLN",
    "czech koruna": "CZK",
    "hungarian forint": "HUF",
    "israeli shekel": "ILS",
    "philippine peso": "PHP",
    "indonesian rupiah": "IDR",
    "malaysian ringgit": "MYR",
    "pakistani rupee": "PKR",
    "bangladeshi taka": "BDT",
    "sri lankan rupee": "LKR",
    "nepalese rupee": "NPR",
    "bitcoin": "BTC"
}
while True:
    currencies = list(currency_dict.keys())
    try:
        current_currency = input("Enter the country whos currency you want to convert (in the form of demonyms. eg - indian, american) in case of rupee or dollar. Else, enter the currency directly(eg - yen, euro): ")



        for currency in currencies:
            if current_currency in currency:
                
                short_form1 = currency_dict[currency]
        currency_convert = input("Enter the country whos currency you want to get converted from previous one (in the form of demonyms. eg - indian, american) in case of rupee or dollar. Else, enter the currency directly(eg - yen, euro): ")
        for currency2 in currencies:
            if currency_convert in currency2:
                short_form2 = currency_dict[currency2]
        amt = int(input("Enter the amount in currency, which is to be converted: "))
        converted = c.convert(short_form1, short_form2, amt)
        print(f"Converted currency from {amt} {short_form1} to {short_form2} is {converted} {short_form2}.\n\n")
    except Exception as e:
        print("Error:", str(e).lower(), "Try entering the spelling correct and follow the instructions correctly...\n\n")        