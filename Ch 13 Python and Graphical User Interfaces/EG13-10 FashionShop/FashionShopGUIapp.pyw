'''
Starts a fashion Shop running with a Python Command Shell user interface

Only runs if it is started as the main program
 '''

if __name__ == '__main__':
    # Loads a user interface class and a storage manager class
    # and then uses these to create an application

    # Get the module containing the user interface class
    # from the ShellUI package
    from GUI import FashionShopGUI
    # Get the user interface manager class from this module
    ui = FashionShopGUI.FashionShopGUI

    # Get the module containing the data storage class
    # from the Storage package
    from Storage import FashionShop
    # Get the data manager class from the storage module
    shop = FashionShop.FashionShop

    # Now create an app from the user interface object
    # Give it the filename and the data manager class as
    # parameters
    app = ui(filename='fashionshop.pickle', storage_class=shop)

    # Now call the main_menu function on the app
    app.main_menu()

