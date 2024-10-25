from typing import List

product_map = {
    1: "LIFX Original 1000",
    3: "LIFX Color 650",
    10: "LIFX White 800 (Low Voltage)",
    11: "LIFX White 800 (High Voltage)",
    15: "LIFX Color 1000",
    18: "LIFX White 900 BR30 (Low Voltage)",
    19: "LIFX White 900 BR30 (High Voltage)",
    20: "LIFX Color 1000 BR30",
    22: "LIFX Color 1000",
    27: "LIFX A19",
    28: "LIFX BR30",
    29: "LIFX A19 Night Vision",
    30: "LIFX BR30 Night Vision",
    31: "LIFX Z",
    32: "LIFX Z",
    36: "LIFX Downlight",
    37: "LIFX Downlight",
    38: "LIFX Beam",
    39: "LIFX Downlight White to Warm",
    40: "LIFX Downlight",
    43: "LIFX A19",
    44: "LIFX BR30",
    45: "LIFX A19 Night Vision",
    46: "LIFX BR30 Night Vision",
    49: "LIFX Mini Color",
    50: "LIFX Mini White to Warm",
    51: "LIFX Mini White",
    52: "LIFX GU10",
    53: "LIFX GU10",
    55: "LIFX Tile",
    57: "LIFX Candle",
    59: "LIFX Mini Color",
    60: "LIFX Mini White to Warm",
    61: "LIFX Mini White",
    62: "LIFX A19",
    63: "LIFX BR30",
    64: "LIFX A19 Night Vision",
    65: "LIFX BR30 Night Vision",
    66: "LIFX Mini White",
    68: "LIFX Candle",
    70: "LIFX Switch",
    71: "LIFX Switch",
    81: "LIFX Candle White to Warm",
    82: "LIFX Filament Clear",
    85: "LIFX Filament Amber",
    87: "LIFX Mini White",
    88: "LIFX Mini White",
    89: "LIFX Switch",
    90: "LIFX Clean",
    91: "LIFX Color",
    92: "LIFX Color",
    93: "LIFX A19 US",
    94: "LIFX BR30",
    96: "LIFX Candle White to Warm",
    97: "LIFX A19",
    98: "LIFX BR30",
    99: "LIFX Clean",
    100: "LIFX Filament Clear",
    101: "LIFX Filament Amber",
    109: "LIFX A19 Night Vision",
    110: "LIFX BR30 Night Vision",
    111: "LIFX A19 Night Vision",
    112: "LIFX BR30 Night Vision Intl",
    113: "LIFX Mini WW US",
    114: "LIFX Mini WW Intl",
    115: "LIFX Switch",
    116: "LIFX Switch",
    117: "LIFX Z US",
    118: "LIFX Z Intl",
    119: "LIFX Beam US",
    120: "LIFX Beam Intl",
    121: "LIFX Downlight Intl",
    122: "LIFX Downlight US",
    123: "LIFX Color US",
    124: "LIFX Color Intl",
    125: "LIFX White to Warm US",
    126: "LIFX White to Warm Intl",
    127: "LIFX White US",
    128: "LIFX White Intl",
    129: "LIFX Color US",
    130: "LIFX Color Intl",
    131: "LIFX White To Warm US",
    132: "LIFX White To Warm Intl",
    133: "LIFX White US",
    134: "LIFX White Intl",
    135: "LIFX GU10 Color US",
    136: "LIFX GU10 Color Intl",
    137: "LIFX Candle Color US",
    138: "LIFX Candle Color Intl",
}

features_map = {
    1: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 2500,
        "multizone": False,
        "relays": False,
    },
    3: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 2500,
        "multizone": False,
        "relays": False,
    },
    10: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 6500,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    11: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 6500,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    15: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 2500,
        "multizone": False,
        "relays": False,
    },
    18: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 2500,
        "multizone": False,
        "relays": False,
    },
    19: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 2500,
        "multizone": False,
        "relays": False,
    },
    20: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 2500,
        "multizone": False,
        "relays": False,
    },
    22: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 2500,
        "multizone": False,
        "relays": False,
    },
    27: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    28: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    29: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    30: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    31: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 2500,
        "multizone": True,
        "relays": False,
    },
    32: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": True,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_ext_mz_firmware": 1532997580,
        "min_ext_mz_firmware_components": [2, 77],
        "min_kelvin": 1500,
        "multizone": True,
        "relays": False,
    },
    36: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    37: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    38: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": True,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_ext_mz_firmware": 1532997580,
        "min_ext_mz_firmware_components": [2, 77],
        "min_kelvin": 1500,
        "multizone": True,
        "relays": False,
    },
    39: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    40: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    43: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    44: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    45: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    46: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    49: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    50: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    51: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2700,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    52: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    53: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    55: {
        "buttons": False,
        "chain": True,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": True,
        "max_kelvin": 9000,
        "min_kelvin": 2500,
        "multizone": False,
        "relays": False,
    },
    57: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": True,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    59: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    60: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    61: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2700,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    62: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    63: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    64: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    65: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    66: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2700,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    68: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": True,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    70: {
        "buttons": True,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "multizone": False,
        "relays": True,
        "temperature_range": None,
    },
    71: {
        "buttons": True,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "multizone": False,
        "relays": True,
        "temperature_range": None,
    },
    81: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 6500,
        "min_kelvin": 2200,
        "multizone": False,
        "relays": False,
    },
    82: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2100,
        "min_kelvin": 2100,
        "multizone": False,
        "relays": False,
    },
    85: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2000,
        "min_kelvin": 2000,
        "multizone": False,
        "relays": False,
    },
    87: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2700,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    88: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2700,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    89: {
        "buttons": True,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "multizone": False,
        "relays": True,
        "temperature_range": None,
    },
    90: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": True,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    91: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    92: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    93: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    94: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    96: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 6500,
        "min_kelvin": 2200,
        "multizone": False,
        "relays": False,
    },
    97: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    98: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    99: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": True,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    100: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2100,
        "min_kelvin": 2100,
        "multizone": False,
        "relays": False,
    },
    101: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2000,
        "min_kelvin": 2000,
        "multizone": False,
        "relays": False,
    },
    109: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    110: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    111: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    112: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": True,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    113: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    114: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    115: {
        "buttons": True,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "multizone": False,
        "relays": True,
        "temperature_range": None,
    },
    116: {
        "buttons": True,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "multizone": False,
        "relays": True,
        "temperature_range": None,
    },
    117: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": True,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": True,
        "relays": False,
    },
    118: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": True,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": True,
        "relays": False,
    },
    119: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": True,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": True,
        "relays": False,
    },
    120: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": True,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": True,
        "relays": False,
    },
    121: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    122: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    123: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    124: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    125: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    126: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    127: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2700,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    128: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2700,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    129: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    130: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    131: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    132: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    133: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2700,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    134: {
        "buttons": False,
        "chain": False,
        "color": False,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 2700,
        "min_kelvin": 2700,
        "multizone": False,
        "relays": False,
    },
    135: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    136: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": False,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    137: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": True,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
    138: {
        "buttons": False,
        "chain": False,
        "color": True,
        "extended_multizone": False,
        "hev": False,
        "infrared": False,
        "matrix": True,
        "max_kelvin": 9000,
        "min_kelvin": 1500,
        "multizone": False,
        "relays": False,
    },
}


class Product:
    def __init__(
        self,
        id: int,
        name: str,
        buttons: bool,
        chain: bool,
        color: bool,
        extended_multizone: bool,
        hev: bool,
        infrared: bool,
        matrix: bool,
        multizone: bool,
        relays: bool,
        max_kelvin: int,
        min_kelvin: int,
        min_ext_mz_firmware: int,
        min_ext_mz_firmware_components: List[int],
        temperature_range: None,
    ):
        self.id = id
        self.name = name
        self.buttons = buttons
        self.chain = chain
        self.color = color
        self.extended_multizone = extended_multizone
        self.hev = hev
        self.infrared = infrared
        self.matrix = matrix
        self.multizone = multizone
        self.relays = relays
        self.max_kelvin = max_kelvin
        self.min_kelvin = min_kelvin
        self.min_ext_mz_firmware = min_ext_mz_firmware
        self.min_ext_mz_firmware_components = min_ext_mz_firmware_components
        self.temperature_range = temperature_range

    def __str__(self):
        return (
            f"Product(id={self.id}, "
            f"name='{self.name}', "
            f"buttons={self.buttons}, "
            f"chain={self.chain}, "
            f"color={self.color}, "
            f"extended_multizone={self.extended_multizone}, "
            f"hev={self.hev}, "
            f"infrared={self.infrared}, "
            f"matrix={self.matrix}, "
            f"multizone={self.multizone}, "
            f"relays={self.relays}, "
            f"max_kelvin={self.max_kelvin}, "
            f"min_kelvin={self.min_kelvin}, "
            f"min_ext_mz_firmware={self.min_ext_mz_firmware}, "
            f"min_ext_mz_firmware_components={self.min_ext_mz_firmware_components}, "
            f"temperature_range={self.temperature_range})"
        )


def create_product_dict(product_map, features_map):
    products_dict = {}
    for product_id, product_name in product_map.items():
        features = features_map[product_id]
        products_dict[product_id] = Product(
            id=product_id,
            name=product_name,
            buttons=features.get("buttons"),
            chain=features.get("chain"),
            color=features.get("color"),
            extended_multizone=features.get("extended_multizone"),
            hev=features.get("hev"),
            infrared=features.get("infrared"),
            matrix=features.get("matrix"),
            multizone=features.get("multizone"),
            relays=features.get("relays"),
            max_kelvin=features.get("max_kelvin"),
            min_kelvin=features.get("min_kelvin"),
            min_ext_mz_firmware=features.get("min_ext_mz_firmware"),
            min_ext_mz_firmware_components=features.get(
                "min_ext_mz_firmware_components"
            ),
            temperature_range=features.get("temperature_range"),
        )
    return products_dict


products_dict = create_product_dict(product_map, features_map)