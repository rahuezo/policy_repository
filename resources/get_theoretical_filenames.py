import csv

def set_policy_type(s):
    s = int(s)

    if s == 1:
        return 'law'
    elif s == 2:
        return 'other'
    elif s == 3:
        return 'resolution'
    elif s == 4:
        return 'resolution as law'

def set_policy_subtype(s):
    s = int(s)

    if s == 1:
        return 'ban/prohib'
    elif s == 2:
        return 'mor'
    elif s == 3:
        return 'mor ext'
    elif s == 4:
        return 'NA'
    elif s == 5:
        return 'other'
    elif s == 7:
        return 'road'
    elif s == 8:
        return 'zoning'
    elif s == 9:
        return 'zoning rev'

def build_name(row):
    # muni_name, muni_type, policy_stance, policy_stance, policy_type, policy_subtype

    muni_name = row[0]
    muni_type = row[3]
    policy_year = row[244]

    try:
        policy_type = set_policy_type(row[245])
    except:
        policy_type = row[245]
    try:
        policy_subtype = set_policy_subtype(row[246])
    except:
        policy_subtype = row[246]

    policy_stance = row[247]

    file_name = ' '.join(' '.join([muni_name, muni_type, policy_year, policy_type, policy_subtype, policy_stance]).split())  + '.pdf'

    return file_name


with open('policy_reference_sheet.csv', 'rb') as cf:
    rows = [row for row in csv.reader(cf, delimiter=',')][1:]

with open('ideal_file_names.csv', 'wb') as cf:
    writer = csv.writer(cf, delimiter=',')

    writer.writerow(['File Name'])

    for row in rows:
        fn = build_name(row)

        writer.writerow([fn])
