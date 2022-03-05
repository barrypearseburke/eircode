import os

LOG_LOCATION = '/var/log/eircode/eircode.log' if os.getenv('TEST_ENV') != 'True' else '/var/log/eircode/test_eircode.log'

IDENTITY_URL_PATH = 'https://api-finder.eircode.ie/Latest/findergetidentity'
EIRCODE_FINDER_URL_PATH = 'https://api-finder.eircode.ie/Latest/finderfindaddress'

ROUTING_KEYS_TOWNS_MAP = {
    'A41': ['Ballyboughal'],
    'A42': ['Garristown'],
    'A45': ['Oldtown'],
    'A63': ['Greystones'],
    'A67': ['Wicklow'],
    'A75': ['Castleblayney'],
    'A81': ['Carrickmacross'],
    'A82': ['Kells', 'Kingscourt', 'Virginia'],
    'A83': ['Enfield', 'Summerhill', 'Rathmoylon'],
    'A84': ['Ashbourne'],
    'A85': ['Dunshaughlin'],
    'A86': ['Dunboyne'],
    'A91': ['Dundalk'],
    'A92': ['Drogheda', 'Ardee', 'Dunleer'],
    'A94': ['Blackrock', 'Monkstown', 'Booterstown', 'Stillorgan'],
    'A96': ['Dun Laoghaire', 'Dalkey', 'Sallynoggin', 'Glenageary'],
    'A98': ['Bray', 'Kilmacanogue', 'Roundwood'],
    'C15': ['Trim', 'Navan', 'Athboy'],
    'D01': ['Dublin 1'],
    'D02': ['Dublin 2'],
    'D03': ['Dublin 3'],
    'D04': ['Dublin 4'],
    'D05': ['Dublin 5'],
    'D06': ['Dublin 6'],
    'D6W': ['Dublin 6W'],
    'D07': ['Dublin 7'],
    'D08': ['Dublin 8'],
    'D09': ['Dublin 9'],
    'D10': ['Dublin 10'],
    'D11': ['Dublin 11'],
    'D12': ['Dublin 12'],
    'D13': ['Dublin 13'],
    'D14': ['Dublin 14'],
    'D15': ['Dublin 15'],
    'D16': ['Dublin 16'],
    'D17': ['Dublin 17'],
    'D18': ['Dublin 18'],
    'D20': ['Dublin 20'],
    'D22': ['Dublin 22'],
    'D24': ['Dublin 24'],
    'E21': ['Cahir'],
    'E25': ['Cashel'],
    'E32': ['Carrick on Suir'],
    'E34': ['Tipperary'],
    'E41': ['Thurles', 'Templemore'],
    'E45': ['Nenagh'],
    'E53': ['Roscrea'],
    'E91': ['Clonmel', 'Fethard'],
    'F12': ['Knock', 'Swinford', 'Claremorris'],
    'F23': ['Castlebar'],
    'F26': ['Ballina', 'Bangor'],
    'F28': ['Westport', 'Achill'],
    'F31': ['Ballinrobe'],
    'F35': ['Ballyhaunis'],
    'F42': ['Roscommon'],
    'F45': ['Castlerea', 'Glenamaddy'],
    'F52': ['Boyle'],
    'F56': ['Ballymote'],
    'F91': ['Sligo', 'Manorhamilton', 'Tubbercurry'],
    'F92': ['Letterkenny'],
    'F93': ['Lifford', 'Carndonagh'],
    'F94': ['Bundoran', 'Donegal'],
    'H12': ['Cavan'],
    'H14': ['Belturbet'],
    'H16': ['Cootehill'],
    'H18': ['Monaghan'],
    'H23': ['Clones'],
    'H53': ['Ballinasloe', 'Portumna'],
    'H54': ['Tuam'],
    'H62': ['Loughrea'],
    'H65': ['Athenry'],
    'H71': ['Clifden'],
    'H91': ['Galway', 'Spiddal', 'Headford', 'Ballyvaughan'],
    'K32': ['Balbriggan'],
    'K34': ['Skerries'],
    'K36': ['Malahide', 'Donabate'],
    'K45': ['Lusk'],
    'K56': ['Rush'],
    'K67': ['Swords'],
    'K78': ['Lucan'],
    'N37': ['Athlone', 'Moate'],
    'N39': ['Longford', 'Ballymahon', 'Granard', 'Lanesborough'],
    'N41': ['Carrick On Shannon'],
    'N91': ['Mullingar', 'Kinnegad'],
    'P12': ['Macroom'],
    'P14': ['Crookstown'],
    'P17': ['Kinsale'],
    'P24': ['Cobh'],
    'P25': ['Midleton'],
    'P31': ['Ballincollig'],
    'P32': ['Rylane'],
    'P36': ['Youghal'],
    'P43': ['Carrigaline'],
    'P47': ['Dunmanway'],
    'P51': ['Mallow', 'Rathmore', 'Cappoquin'],
    'P56': ['Charleville'],
    'P61': ['Fermoy', 'Rathcormac'],
    'P67': ['Mitchelstown'],
    'P72': ['Bandon'],
    'P75': ['Bantry', 'Glengarriff'],
    'P81': ['Skibbereen', 'Baltimore'],
    'P85': ['Clonakilty', 'Rosscarbery'],
    'R14': ['Athy'],
    'R21': ['Bagenalstown'],
    'R32': ['Portlaoise', 'Abbeyleix', 'Portarlington'],
    'R35': ['Tullamore', 'Walsh Island, Offaly'],
    'R42': ['Birr', 'Banagher'],
    'R45': ['Edenderry'],
    'R51': ['Kildare'],
    'R56': ['Curragh'],
    'R93': ['Carlow', 'Tullow'],
    'R95': ['Kilkenny', 'Graiguenamanagh', 'Thomastown'],
    'T12': ['Cork city southside', 'Mahon', 'Passage West'],
    'T23': ['Cork city northside', 'Hollyhill'],
    'T34': ['Carrignavar'],
    'T45': ['Glanmire', 'Carrigtwohill'],
    'T56': ['Watergrasshill'],
    'V14': ['Shannon'],
    'V15': ['Kilrush', 'Kilkee'],
    'V23': ['Caherciveen'],
    'V31': ['Listowel'],
    'V35': ['Kilmallock'],
    'V42': ['Newcastle West'],
    'V92': ['Tralee', 'Dingle'],
    'V93': ['Kenmare', 'Killarney'],
    'V94': ['Limerick', 'Abbeyfeale', 'Newport', 'Killaloe-Ballina'],
    'V95': ['Miltown Malbay', 'Ennis', 'Kildysart'],
    'W12': ['Newbridge'],
    'W23': ['Maynooth', 'Celbridge', 'Leixlip'],
    'W34': ['Monasterevin'],
    'W91': ['Naas', 'Blessington'],
    'X35': ['Dungarvan'],
    'X42': ['Kilmacthomas', 'Bunmahon'],
    'X91': ['Waterford', 'Dunmore East', 'Tramore'],
    'Y14': ['Arklow'],
    'Y21': ['Enniscorthy', 'Bunclody'],
    'Y25': ['Gorey'],
    'Y34': ['New Ross', 'Fethard On Sea'],
    'Y35': ['Wexford', 'Rosslare'],
}

ROUTING_KEYS_COUNTY_MAP = {
    'A41': 'Dublin',
    'A42': 'Dublin',
    'A45': 'Dublin',
    'A63': 'Wicklow',
    'A67': 'Wicklow',
    'A75': 'Monaghan',
    'A81': 'Monaghan',
    'A82': 'Meath',
    'A83': 'Meath',
    'A84': 'Meath',
    'A85': 'Meath',
    'A86': 'Meath',
    'A91': 'Louth',
    'A92': 'Louth',
    'A94': 'Dublin',
    'A96': 'Dublin',
    'A98': 'Wicklow',
    'C15': 'Meath',
    'D01': 'Dublin',
    'D02': 'Dublin',
    'D03': 'Dublin',
    'D04': 'Dublin',
    'D05': 'Dublin',
    'D06': 'Dublin',
    'D6W': 'Dublin',
    'D07': 'Dublin',
    'D08': 'Dublin',
    'D09': 'Dublin',
    'D10': 'Dublin',
    'D11': 'Dublin',
    'D12': 'Dublin',
    'D13': 'Dublin',
    'D14': 'Dublin',
    'D15': 'Dublin',
    'D16': 'Dublin',
    'D17': 'Dublin',
    'D18': 'Dublin',
    'D20': 'Dublin',
    'D22': 'Dublin',
    'D24': 'Dublin',
    'E21': 'Tipperary',
    'E25': 'Tipperary',
    'E32': 'Tipperary',
    'E34': 'Tipperary',
    'E41': 'Tipperary',
    'E45': 'Tipperary',
    'E53': 'Tipperary',
    'E91': 'Tipperary',
    'F12': 'Mayo',
    'F23': 'Mayo',
    'F26': 'Down',
    'F28': 'Mayo',
    'F31': 'Mayo',
    'F35': 'Mayo',
    'F42': 'Roscommon',
    'F45': 'Roscommon',
    'F52': 'Roscommon',
    'F56': 'Sligo',
    'F91': 'Sligo',
    'F92': 'Donegal',
    'F93': 'Donegal',
    'F94': 'Donegal',
    'H12': 'Cavan',
    'H14': 'Cavan',
    'H16': 'Cavan',
    'H18': 'Monaghan',
    'H23': 'Monaghan',
    'H53': 'Galway',
    'H54': 'Galway',
    'H62': 'Galway',
    'H65': 'Galway',
    'H71': 'Galway',
    'H91': 'Galway',
    'K32': 'Dublin',
    'K34': 'Dublin',
    'K36': 'Dublin',
    'K45': 'Dublin',
    'K56': 'Dublin',
    'K67': 'Dublin',
    'K78': 'Dublin',
    'N37': 'Westmeath',
    'N39': 'Longford',
    'N41': 'Leitrim',
    'N91': 'Westmeath',
    'P12': 'Cork',
    'P14': 'Cork',
    'P17': 'Cork',
    'P24': 'Cork',
    'P25': 'Cork',
    'P31': 'Cork',
    'P32': 'Cork',
    'P36': 'Cork',
    'P43': 'Cork',
    'P47': 'Cork',
    'P51': 'Cork',
    'P56': 'Cork',
    'P61': 'Cork',
    'P67': 'Cork',
    'P72': 'Cork',
    'P75': 'Cork',
    'P81': 'Cork',
    'P85': 'Cork',
    'R14': 'Kildare',
    'R21': 'Carlow',
    'R32': 'Laois',
    'R35': 'Offaly',
    'R42': 'Offaly',
    'R45': 'Offaly',
    'R51': 'Kildare',
    'R56': 'Kildare',
    'R93': 'Carlow',
    'R95': 'Kilkenny',
    'T12': 'Cork',
    'T23': 'Cork',
    'T34': 'Cork',
    'T45': 'Cork',
    'T56': 'Cork',
    'V14': 'Clare',
    'V15': 'Clare',
    'V23': 'Kerry',
    'V31': 'Kerry',
    'V35': 'Limerick',
    'V42': 'Limerick',
    'V92': 'Kerry',
    'V93': 'Kerry',
    'V94': 'Limerick',
    'V95': 'Clare',
    'W12': 'Kildare',
    'W23': 'Kildare',
    'W34': 'Kildare',
    'W91': 'Kildare',
    'X35': 'Dungarvan',
    'X42': 'Waterford',
    'X91': 'Waterford',
    'Y14': 'Wicklow',
    'Y21': 'Wexford',
    'Y25': 'Wexford',
    'Y34': 'Wexford',
    'Y35': 'Wexford',
}
