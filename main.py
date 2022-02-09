import ht_zone
import c_nofesh

# while True:
#     code = input("Enter code: ")
#     if code == 'E':
#         break
#     elif len(code) == 10:
#         c_nofesh.main(code)
#     elif len(code) == 12:
#         ht_zone.main(code)
#     else:
#         print("Invalid code")


def get_ticket(code):
    if len(code) == 10:
        c_nofesh.main(code)
    elif len(code) == 12:
        ht_zone.main(code)
    elif code == '':
        return "הכנס קוד"
    else:
        return "קוד לא תקין - נסה שוב או גש לשומר"
    return '1'
