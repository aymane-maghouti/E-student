def check_postal_code(code):
    if len(code) != 5:
        return False
    for char in code:
        if not char.isdigit():
            return False
    return True

def check_CNE(CNE):
    if len(CNE) != 10:
        return False
    if not CNE[0].isupper():
        return False
    for char in CNE[1:]:
        if not char.isdigit():
            return False
    return True

def check_phone_number(phone):
    if len(phone) != 10:
        return False
    if phone[0] != '0':
        return False
    for char in phone[1:]:
        if not char.isdigit():
            return False
    return True

def check_CIN(CIN):
    if len(CIN) != 6:
        return False
    if CIN[0].isupper() and CIN[1:].isdigit():
        return True
    if CIN[:2].isupper() and CIN[2:].isdigit():
        return True
    return False