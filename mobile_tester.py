'''
Week 11 Challenge Activities
Draw the UML Diagram for the mobile phone class.

********************************************************
*     Class:     MobilePhone                           *
********************************************************
*     Attribute 1:     __manufact: str                 *
*     Attribute 2:     __model: str                    *
*     Attribute 3:     __retail_price: float           *
********************************************************
*     Methods:                                         *
*     __init__(manufacturer, model, retail_price)      *
*     #Accepts arguments for the manufacturer,         *
*     model number, and retail price.#                 *
*                                                      *
*     set_manufact(manufacturer)                       *
*     #Accepts an argument for the manufacturer.#      *
*                                                      *
*     set_model(model)                                 *
*     #Accepts an argument for the model.#             *
*                                                      *
*     set_retail_price(retail_price)                   *
*     #Accepts an argument for the retail price.#      *
*                                                      *
*     get_manufact() -> str                            *
*     #Returns the phone’s manufacturer.#              *
*                                                      *
*     get_model() -> str                               *
*     #Returns the phone’s model.#                     *
*                                                      *
*     get_retail_price() -> float                      *
*     #Returns the phone’s retail price.#              *
*                                                      *
********************************************************

'''

import mobile
from mobile import Phone


def main():
    # Create a MobilePhone object
    manufact = input('Enter the manufacturer: ')
    model = input('Enter the model number: ')
    price = input('Enter the retail price: ')
    phone = Phone(manufact, model, price)

    # Display initial phone information
    print("Here is the data that you entered: ")
    print("Manufacturer:", phone.get_manufact())
    print("Model:", phone.get_model())
    print("Retail Price: $", phone.get_retail_price())


if __name__ == "__main__":
    main()
