import os

def contact_developer():
    print("Contact Developer:")
    print("[1] Facebook")
    print("[2] GitHub")
    print("[3] Telegram")
    print("[4] YouTube")
    print("[0] Back")
    opt = input("\nSelect: ")
    if opt == '1':
        os.system("xdg-open https://facebook.com/forhadhasan995")
    elif opt == '2':
        os.system("xdg-open https://github.com/Forhadj")
    elif opt == '3':
        os.system("xdg-open https://t.me/f_forhad")
    elif opt == '4':
        os.system("xdg-open https://youtube.com/@forhad2.00?si=vmV-oUKHLF3ZCTnu")
