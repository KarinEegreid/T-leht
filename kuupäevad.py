#Karl Paju IS22

kuupäev = input("Sisesta kuupäev järgmises formaadis (dd.mm.yyyy): ")

try:
    päev, kuu, aasta = map(int, kuupäev.split("."))
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni",
              "juuli", "august", "september", "oktoober", "november", "detsember"]
    if kuu < 1 or kuu > 12:
        raise ValueError
    print("{}. {} {}".format(päev, kuud[kuu-1], aasta))
except ValueError:
    print("vale kuupäev")
