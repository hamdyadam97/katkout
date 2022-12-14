import re



def validation_phone(phone):
    regx = '^01[0125][0-9]{8}$'
    if re.match(regx, phone):
        return phone
    else:
        return ("من فضلك رقم مناسب ")

print(validation_phone('01092263234'))