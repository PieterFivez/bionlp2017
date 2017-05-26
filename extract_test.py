from tokenise import tokenize
import re
import json

valid_checker = re.compile(r'(^[^\d\W])[^\d\W]*(-[^\d\W]*)*([^\d\W]$)')

def prepreproc(infile, outfile):

    with open(infile, 'r') as f:
        text = f.read()
        with open(outfile, 'w') as g:
            text = re.sub(r'(?<!\n)\n(?!\n)', "\t", text)
            text = re.sub("\n\n", "\n", text)
            g.write(text)

def preproc(infile, outfile):

    with open(infile, 'r') as f:
        with open(outfile, 'w') as g:
            for i, line in enumerate(f):
                if line:
                    sentences = tokenize(line)
                    preproc_lines = []
                    for sentence in sentences:
                        preproc_line = " ".join([t for t in sentence.lower().split() if valid_checker.match(t)])
                        preproc_lines.append(preproc_line)
                        preproc_lines.append("\t")
                    g.write(" ".join(preproc_lines) + "\n")
                if i % 10000 == 0:
                    print(i)

if __name__ == "__main__":
    
    print 'First stage of preprocessing'
    prepreproc('../data/NOTEEVENTS.csv', '../data/mimic_raw_preprocessed.txt')
    print 'Finished'
    
    print('Second stage of preprocessing')
    preproc('../data/mimic_raw_preprocessed.txt', '../data/mimic_preprocessed.txt')
    print('Finished')

    line_idxs = [1910947, 3286751, 5335498, 6727613, 6821132, 8218411, 452118, 984680, 3794421, 3101507, 6429854, 9365464, 187111, 3089964, 3120205, 3112562, 3095223, 1244167, 7119012, 6680650, 7430799, 7825169, 8355022, 8984581, 6166348, 3149740, 5961871, 4200482, 5015011, 6365822, 9021496, 9021503, 60169, 7309860, 3688720, 4494908, 5546589, 6384121, 6442465, 6603702, 8241393, 9321154, 8929093, 5023090, 9276931, 1190696, 2763137, 909474, 949943, 949946, 949980, 7437427, 7036386, 5358751, 5394797, 5973104, 8026801, 9290034, 3103749, 3152875, 1453197, 6842718, 8282493, 8673863, 8939481, 2076494, 2015852, 6378076, 6600692, 7342564, 3135471, 5777450, 963403, 1468035, 6751522, 6877505, 6904372, 8391049, 914353, 914408, 1978647, 3122592, 3142045, 3162660, 8361687, 8923, 3091150, 3114664, 3151455, 6484397, 7634804, 7776086, 3107116, 3091605, 3121599, 3359919, 3552890, 4850107, 3279837, 6915020, 1693562, 7117469, 7705893, 8645080, 5531124, 1040298, 6429891, 6437674, 7220351, 8473179, 9487387, 3131546, 3092280, 7443438, 7678721, 9284588, 4898840, 4203399, 5124216, 3122087, 3363748, 3887610, 385138, 4323872, 6204818, 6204828, 5722112, 6334563, 131459, 229207, 1860806, 3108236, 8825271, 3110682, 3119691, 8745238, 767820, 1187751, 1903550, 19249, 41146, 1710911, 2102723, 6595625, 6836147, 7167597, 8676202, 9342711, 3088595, 1749056, 1121363, 3083451, 3120185, 3122675, 4975087, 6233657, 850935, 3105742, 3366567, 3373211, 3376672, 4654017, 3125408, 6513164, 6587743, 7135014, 8411808, 3108300, 8838013, 1318538, 8966430, 9308053, 3297258, 325234, 4556868, 5386943, 6566821, 8002504, 8593042, 9436618, 328060, 818252, 9099568, 3136616, 6498088, 6705538, 6952290, 7768457, 180453, 3114512, 3121599, 2065242, 3101546, 3126131, 5189655, 6155552, 7599683, 8626524, 6936368, 8056126, 1229940, 8052887, 3109218, 3109726, 3109922, 6922251, 7191209, 7719042, 7902428, 8268254, 3096729, 3111008, 9029047, 3125949, 8815466, 8841438, 9033301, 9227726, 4754324, 3145159, 3088595, 563353, 563354, 8097979, 8140355, 1190098, 3090962, 8775609, 61729, 6574182, 1378941, 3095525, 3122167, 3142933, 3091492, 7109354, 651986, 1727602, 5125493, 5786787, 6341085, 929061, 3090668, 3119945, 3120635, 3154313, 5102555, 3112465, 3133604, 7414865, 8707952, 8914704, 6934099, 7002332, 1078260, 1510904, 1613790, 6551070, 7692740, 166961, 3128592, 5087538, 3091344, 457326, 1377857, 1490055, 1541031, 6466388, 3594425, 1702419, 3108923, 3120819, 3091053, 1067001, 1565153, 3102302, 3102421, 3769599, 1801231, 4394435, 3225793, 3229134, 3244531, 8416917, 3094767, 1669112, 2200877, 3107095, 3092959, 1517552, 3097317, 1344722, 3124226, 6494264, 3090028, 3092959, 3109176, 3141648, 3158077, 5203067, 3134406, 5269196, 7619930, 8361443, 8491663, 6471238, 2348640, 3135311, 3314314, 3392149, 8776427, 2688379, 7818488, 8771202, 3125927, 234665, 3103359, 7839585, 2028516, 844328, 3122715, 3129670, 5489681, 8597873, 8781093, 9354446, 814816, 334046, 3109667, 6428134, 7710873, 8105715, 291590, 389762, 3315330, 5155064, 3117722, 7069146, 8866166, 8929299, 9257654, 1364059, 6554492, 6968321, 9404953, 947295, 2140965, 2476859, 7246764, 7727202, 8337459, 8577011, 3087124, 1796945, 3091767, 3153470, 2922016, 3140639, 3352153, 7178286, 8189835, 1878030, 2099649, 3080740, 8326178, 9270030, 3120963, 4684260, 4829207, 5395984, 5677951, 5997900, 6056067, 6386680, 1716233, 5331969, 1822400, 3626002, 5635798, 156462, 317401, 844829, 7592016, 9114508, 477295, 3415607, 3658224, 5932077, 7075501, 6509396, 7354222, 7368150, 7751005, 8872108, 2044655, 6686056, 7662180, 8555873, 8588882, 321791, 3207538, 3634233, 4950270, 5079196, 2009889, 9537376, 3119610, 1769576, 3107192, 6897090, 7636681, 9198206, 3096410, 3113566, 3153591, 4880930, 6636785, 4186715, 4634914, 4734135, 1732502, 3309359, 5758719, 124161, 3121685, 3806561, 6415339, 7183158, 7202707, 7848981, 8082177, 791768, 796177, 940313, 1433834, 7875279, 1486390, 3114872, 3410833, 7612894, 979581, 1754912, 8680455, 9542334, 8431332, 1433046, 6937839, 7304277, 7529836, 8748092, 421874, 948026, 6671589, 7823445, 8625101, 5736427, 3103282, 7615860, 641065, 6566860, 7535173, 7634370, 8365716, 286964, 1333629, 2072768, 3154203, 3152343, 3097881, 3110105, 3110498, 3121488, 3142242, 1547468, 1829702, 3148395, 1370740, 1059561, 7355096, 4894466, 3152079, 7859942, 7973558, 3103790, 3107116, 8949986, 3445732, 6476047, 6552919, 7065565, 8914833, 1918615, 3132498, 5630069, 8418944, 1587323, 7903504, 859236, 851526, 1499954, 3139148, 7170640, 8277010, 3152304, 83113, 1861494, 3122167, 7418709, 8369463, 8890062, 9431795, 868356, 3083451, 7608857, 8559111, 8795666, 3113075, 1710015, 7554614, 3090050, 1860722, 3224167, 4087890, 4483899, 1392681, 5419200, 969642, 4984708, 3095301, 1588511, 6736615, 6854134, 7089000, 9461124, 836763, 7337325, 7761503, 8119506, 9239358, 1306737, 2248384, 3092059, 3092261, 3096588, 213671, 213673, 966945, 531437, 8368186, 3091384, 3091442, 674679, 3514310, 778697, 1681422, 3141040, 8252869, 9099453, 271258, 1369583, 7448095, 7286190, 7722790, 8867447, 6457238, 7505651, 7854412, 8170929, 9059962, 3105563, 3141809, 7299408, 528215, 3498253, 4001025, 6557951, 9223247, 7727620, 3111435, 3112880, 3147740, 3105938, 3120076, 3151286, 3153231, 1581895, 6470012, 7114938, 7400863, 9207635, 9251645, 1195185, 551264, 3474204, 6531426, 7519161, 9380859, 3090611, 3122592, 8026852, 8411047, 1765731, 3151132, 7220381, 7311082, 7549954, 7838406, 3108198, 3120177, 6503166, 8391558, 3083405, 3100920, 3112608, 3132909, 7403472, 3100441, 7568163, 8504257, 8742233, 8819274, 8924880, 866089, 674607, 966665, 3125231, 8925678, 3096771, 3107484, 3140305, 6417853, 3788316, 5783623, 7248573, 8525828, 8532904, 890082, 6549102, 6627754, 6685618, 8752929, 8961557, 714173, 7599994, 6444825, 3146642, 5651179, 8843456, 7263612, 7438595, 5781224, 5577286, 6293086, 6313866, 6313872, 1745423, 762576, 905871, 937881, 7452614, 8217727, 3095223, 3093641, 3268585, 3268586, 385796, 1868907, 6530187, 6820932, 6997676, 7685243, 8543501, 2157149, 3107016, 5650780, 3087045, 3088613, 3139424, 3140209, 8794005, 1342992, 3113261, 8075076, 8346591, 8346593, 130456, 3146994, 5668929, 5854585, 6446280, 1589007, 3154280, 6213434, 8021655, 8844759, 3096239, 1404796, 4032051, 7256036, 7837083, 7859049, 8393989, 150862, 4244920, 4743106, 5133119, 5998831, 970431, 6806348, 8576126, 3102037, 3110338, 6564890, 1707720, 3768978, 7391885, 7344096, 9202946, 1067465, 1943588, 3132281, 3152679, 6416965, 3093796, 3127277, 3221840, 7225378, 9369516, 3154280, 4254093, 9432740, 765916, 3594001, 3714002, 1671025, 3623099, 3685976, 3705910, 1443830, 5643545, 8862014, 1513533, 989147, 1810697, 1944022, 3112445, 1095047, 3123512, 39710, 3118285, 8618484, 3120941, 3099287, 3231405, 3632703, 5604146, 9444220, 3094956, 4766961, 4813539, 4813546, 4836090, 7455035, 7467377, 7467593, 8256757, 9104226, 6388898, 8001363, 8056376, 8560013, 1686377, 7574698, 3091344, 3867347, 8429795, 3107335, 3120736, 8604434, 9193043, 8538120, 8574244, 281564, 901298, 3090028, 1395320, 3110931, 3133419, 54733, 96125, 347300, 3696362, 7186785, 1436981, 733688, 9128449, 1911543, 6546547, 155941, 1925886, 7139841, 9181502, 404229, 1488577, 3418405, 4074434, 6099128, 1414895, 7775341, 2304160, 3091344, 5232334, 5818529, 7185617, 182525, 742907, 1287208, 3143010, 9433778, 825786, 145041, 1129580, 1229696, 3149683, 9226747, 59798, 828852, 3095543, 6403066, 7246933, 3080645, 3083405, 3120025, 3120840, 3120941, 1491651, 1878820, 5773, 1165967, 5562772, 6490302, 7172930, 9396595, 7771593, 8915748, 3095372, 3121820, 3122167, 3152426, 6597213, 442495, 2448779, 2560783, 3117704, 3358287, 8365143, 3090744, 203888, 2329680, 851834, 851836, 1178912, 1949357, 3138526, 3140621, 3140727, 2060695, 3150980, 3241520, 4247409, 8838982, 7013731, 8157282]
    set_line_idxs = set(line_idxs)
    misspellings = ['carediolgy', 'lugns', 'lugns', 'lugns', 'lugns', 'lugns', 'ecchinocytes', 'procuedure', 'procuedure', 'avening', 'avening', 'avening', 'enteracept', 'enteracept', 'enteracept', 'hepaotology', 'precipirtouskly', 'trachiotomy', 'trachiotomy', 'responsvie', 'responsvie', 'responsvie', 'responsvie', 'responsvie', 'intubwted', 'sunglottic', 'laternatively', 'pylenonephritis', 'pylenonephritis', 'pylenonephritis', 'pylenonephritis', 'pylenonephritis', 'increaseds', 'increaseds', 'qudrant', 'qudrant', 'qudrant', 'noteed', 'noteed', 'noteed', 'noteed', 'noteed', 'specil', 'distince', 'distince', 'hypokiinesis', 'hypokiinesis', 'hypercholesteromia', 'hypercholesteromia', 'hypercholesteromia', 'hypercholesteromia', 'hypercholesteromia', 'supportvie', 'spenomegaly', 'spenomegaly', 'spenomegaly', 'spenomegaly', 'spenomegaly', 'antiarrrhythmics', 'antiarrrhythmics', 'reporteldy', 'reporteldy', 'reporteldy', 'reporteldy', 'reporteldy', 'myalgais', 'imapenem', 'imapenem', 'imapenem', 'placemedt', 'transducion', 'supralilar', 'neoptlams', 'umcomplicated', 'umcomplicated', 'umcomplicated', 'umcomplicated', 'umcomplicated', 'arimdex', 'arimdex', 'arimdex', 'arimdex', 'arimdex', 'acrss', 'acetazolamind', 'roccuronium', 'sless', 'aroound', 'aroound', 'aroound', 'aroound', 'aroound', 'concerntrate', 'demarginization', 'demarginization', 'hpatic', 'hpatic', 'hpatic', 'retroobital', 'ferinosl', 'systoilic', 'systoilic', 'systoilic', 'systoilic', 'hyyaline', 'ferriecit', 'claoric', 'claoric', 'claoric', 'claoric', 'claoric', 'ankld', 'desature', 'cyclorsporin', 'cyclorsporin', 'cyclorsporin', 'rgoins', 'bacteremis', 'bacteremis', 'sympots', 'comminted', 'comminted', 'signl', 'signl', 'signl', 'signl', 'extcretion', 'ssigns', 'incontinenece', 'incontinenece', 'incontinenece', 'incontinenece', 'incontinenece', 'vaspopressin', 'vaspopressin', 'vaspopressin', 'regurtitation', 'regurtitation', 'regurtitation', 'thalasemmia', 'thalasemmia', 'thalasemmia', 'thalasemmia', 'incrrease', 'incrrease', 'incrrease', 'incrrease', 'incrrease', 'rtotated', 'accordnace', 'backgroun', 'backgroun', 'backgroun', 'constusions', 'constusions', 'constusions', 'iatrogentic', 'iatrogentic', 'iatrogentic', 'iatrogentic', 'iatrogentic', 'hmeithorax', 'requirs', 'requirs', 'requirs', 'requirs', 'requirs', 'chheks', 'chheks', 'confuson', 'confuson', 'confuson', 'peunothorax', 'fibros', 'fibros', 'fibros', 'mininutes', 'mininutes', 'mininutes', 'mininutes', 'dehiscnece', 'hydorcele', 'hydorcele', 'aprropriately', 'aprropriately', 'aprropriately', 'aprropriately', 'aprropriately', 'psteroids', 'prosatectomy', 'prosatectomy', 'popletial', 'popletial', 'popletial', 'popletial', 'popletial', 'intuabte', 'intuabte', 'femerals', 'femerals', 'popletieal', 'sensarion', 'thryohyoid', 'thryohyoid', 'thryohyoid', 'dicarded', 'dicarded', 'dicarded', 'dicarded', 'dicarded', 'palitave', 'mucoiud', 'drianable', 'respoding', 'respoding', 'respoding', 'respoding', 'respoding', 'invadses', 'resutlts', 'exctration', 'agglutin', 'agglutin', 'agglutin', 'vasoleine', 'eosoniphils', 'eosoniphils', 'eosoniphils', 'hopitilization', 'nygstamus', 'diurises', 'diurises', 'diurises', 'diurises', 'nutritio', 'nutritio', 'pevlic', 'pevlic', 'pevlic', 'pevlic', 'pevlic', 'syndomre', 'syndomre', 'syndomre', 'syndomre', 'syndomre', 'tomorrowpt', 'respiraoty', 'respiraoty', 'respiraoty', 'respiraoty', 'respiraoty', 'pupilarry', 'pupilarry', 'desceased', 'desceased', 'desceased', 'rflex', 'rflex', 'miacalicin', 'sliglhtly', 'sliglhtly', 'fionger', 'prblm', 'prblm', 'prblm', 'glarigine', 'glarigine', 'strcture', 'atazanzvir', 'readins', 'readins', 'ureteteral', 'pleurodeses', 'pleurodeses', 'pleurodeses', 'pleurodeses', 'pleurodeses', 'hematc', 'adenapathy', 'drainags', 'drainags', 'drainags', 'drainags', 'partcipate', 'cortonary', 'cortonary', 'cortonary', 'cerruloplasm', 'adiitionally', 'induartion', 'beccame', 'beccame', 'beccame', 'resuem', 'resuem', 'resuem', 'resuem', 'resuem', 'entends', 'inferolater', 'inferolater', 'addeed', 'addeed', 'addeed', 'tachcypnea', 'procecure', 'procecure', 'procecure', 'procecure', 'procecure', 'milfdly', 'placewd', 'placewd', 'controntation', 'persistenting', 'persistenting', 'persistenting', 'extingushes', 'perhaphs', 'opern', 'opern', 'opern', 'opern', 'opern', 'huggger', 'anxioltics', 'inclusing', 'inclusing', 'inclusing', 'inclusing', 'inclusing', 'sphyncterotomies', 'sphyncterotomies', 'paracoloic', 'paracoloic', 'liquds', 'liquds', 'liquds', 'liquds', 'liquds', 'levimere', 'sleeo', 'sleeo', 'sleeo', 'phelyephrine', 'phelyephrine', 'phelyephrine', 'quiclkly', 'quiclkly', 'quiclkly', 'quiclkly', 'hypoxemnia', 'polymycin', 'propfolo', 'propfolo', 'noited', 'noited', 'noited', 'noited', 'noited', 'hiting', 'hiting', 'hiting', 'hiting', 'hiting', 'conytinue', 'enahncing', 'enahncing', 'enahncing', 'enahncing', 'enahncing', 'trasnformation', 'exstravation', 'stablitized', 'entrappment', 'creartinine', 'creartinine', 'isoechic', 'prosthese', 'apsects', 'apsects', 'apsects', 'apsects', 'receipient', 'receipient', 'receipient', 'receipient', 'receipient', 'hypercarbnea', 'hypercarbnea', 'hypercarbnea', 'hypercarbnea', 'hypercarbnea', 'breakfst', 'breakfst', 'breakfst', 'breakfst', 'breakfst', 'hypolucency', 'hypolucency', 'hypolucency', 'hypolucency', 'hypolucency', 'riskk', 'riskk', 'opitate', 'acidoic', 'acidoic', 'acidoic', 'acidoic', 'acidoic', 'nchanged', 'nchanged', 'nchanged', 'nchanged', 'nchanged', 'stomah', 'stomah', 'stomah', 'hypodenities', 'hypodenities', 'hypodenities', 'otator', 'otator', 'initiationg', 'usally', 'usally', 'usally', 'usally', 'usally', 'perfored', 'perfored', 'perfored', 'perfored', 'perfored', 'nondiagnositic', 'nondiagnositic', 'nondiagnositic', 'interparachymal', 'couselor', 'couselor', 'couselor', 'couselor', 'consustently', 'jypokinesis', 'coomfortable', 'coomfortable', 'coomfortable', 'coomfortable', 'eythromycin', 'eythromycin', 'eythromycin', 'eythromycin', 'eythromycin', 'verrtex', 'recreationl', 'iompared', 'aggitating', 'aggitating', 'aggitating', 'aggitating', 'aggitating', 'symmptoms', 'symmptoms', 'symmptoms', 'symmptoms', 'intrgrillin', 'cathotomy', 'eneteroscopy', 'eneteroscopy', 'eneteroscopy', 'eneteroscopy', 'tropnins', 'tropnins', 'tropnins', 'celcoxib', 'retsriction', 'retsriction', 'thickineng', 'addedndum', 'addedndum', 'addedndum', 'imprves', 'imprves', 'imprves', 'goint', 'goint', 'goint', 'goint', 'goint', 'lichanified', 'ilnconsistently', 'fragmeny', 'veerapamil', 'radaiation', 'radaiation', 'trancortical', 'ruputure', 'ruputure', 'ruputure', 'ruputure', 'ruputure', 'antiarrhymatic', 'hyperphosphtemia', 'dwait', 'respositions', 'respositions', 'respositions', 'respositions', 'respositions', 'interpet', 'interpet', 'interpet', 'interpet', 'interpet', 'unlely', 'supoprtive', 'supoprtive', 'heptacellular', 'ecsherichia', 'peratracheal', 'peratracheal', 'peratracheal', 'subcaspsular', 'subcaspsular', 'dlateral', 'dlateral', 'colisitina', 'criciod', 'containemnt', 'containemnt', 'containemnt', 'containemnt', 'immunosuppresents', 'immunosuppresents', 'immunosuppresents', 'immunosuppresents', 'immunosuppresents', 'brance', 'brance', 'expirqtory', 'expirqtory', 'haematochezia', 'bronhcial', 'bronhcial', 'bronhcial', 'cnadidate', 'cnadidate', 'assistsance', 'assistsance', 'pedestrin', 'pedestrin', 'erythromyocin', 'erythromyocin', 'erythromyocin', 'erythromyocin', 'erythromyocin', 'gentteal', 'heterogebous', 'cardiognitc', 'antipyschotic', 'antipyschotic', 'antipyschotic', 'justs', 'justs', 'justs', 'justs', 'justs', 'distendes', 'distendes', 'distendes', 'nectotic', 'nectotic', 'nectotic', 'nectotic', 'nectotic', 'ythick', 'senstivites', 'senstivites', 'senstivites', 'downgoin', 'tranpsort', 'tranpsort', 'tranpsort', 'cefotaxmin', 'sennekot', 'sennekot', 'sennekot', 'sennekot', 'sennekot', 'secontary', 'secon', 'secon', 'secon', 'secon', 'secon', 'tinglin', 'tinglin', 'tinglin', 'tinglin', 'arrythmmia', 'contonese', 'contonese', 'contonese', 'contonese', 'contonese', 'pregant', 'pregant', 'pregant', 'pregant', 'neuropatic', 'neuropatic', 'neuropatic', 'neuropatic', 'neuropatic', 'meteprolol', 'meteprolol', 'meteprolol', 'meteprolol', 'meteprolol', 'calmmed', 'deniesd', 'denises', 'denises', 'denises', 'denises', 'remining', 'remining', 'remining', 'remining', 'thrach', 'thrach', 'thrach', 'thrach', 'thrach', 'zyprexax', 'bvery', 'bvery', 'bvery', 'bvery', 'bvery', 'holosstolic', 'deveopling', 'resuults', 'brochodilations', 'abnormalityin', 'coolaborate', 'isordril', 'isordril', 'parafaulcine', 'consoliodation', 'cholangiis', 'cholangiis', 'cholangiis', 'atributes', 'alond', 'alond', 'alond', 'alond', 'alond', 'satruation', 'incrwase', 'patecheal', 'patecheal', 'tramodal', 'tramodal', 'evenin', 'evenin', 'evenin', 'evenin', 'evenin', 'infeoseptal', 'resusitaton', 'dehiscene', 'alverolar', 'alverolar', 'alverolar', 'barrieer', 'barrieer', 'preciptitously', 'preciptitously', 'fluctuatio', 'dyamics', 'dyamics', 'autocoidal', 'doubel', 'doubel', 'doubel', 'doubel', 'mimick', 'mimick', 'mimick', 'mimick', 'mimick', 'phebilitis', 'difinitely', 'exteme', 'exteme', 'exteme', 'exteme', 'exteme', 'limite', 'limite', 'limite', 'limite', 'limite', 'proporanolol', 'proporanolol', 'requiriemnts', 'splemectomy', 'splemectomy', 'splemectomy', 'psitacci', 'untin', 'untin', 'transprot', 'transprot', 'chesp', 'chesp', 'chesp', 'chesp', 'chesp', 'temporaty', 'temporaty', 'temporaty', 'temporaty', 'temporaty', 'uperr', 'uperr', 'uperr', 'imaginig', 'arteriogrphy', 'arteriogrphy', 'stabilizind', 'intubabation', 'intubabation', 'intubabation', 'rehospialization', 'generenerative', 'strpng', 'electrocradiogram', 'dicsontinued', 'dicsontinued', 'dicsontinued', 'dicsontinued', 'lukocytosis', 'lukocytosis', 'divertculi', 'sduring', 'sduring', 'erythemay', 'identifie', 'identifie', 'identifie', 'identifie', 'identifie', 'caucasaian', 'sclerosin', 'sclerosin', 'sclerosin', 'sclerosin', 'brinsg', 'brinsg', 'brinsg', 'brinsg', 'brinsg', 'coxycx', 'coxycx', 'coxycx', 'coxycx', 'spubsided', 'tthey', 'attempst', 'attempst', 'attempst', 'ventriculostmy', 'ventriculostmy', 'ventriculostmy', 'ventriculostmy', 'activiety', 'activiety', 'ankes', 'ankes', 'ankes', 'cconjunctival', 'cconjunctival', 'abrrogate', 'ellicited', 'ellicited', 'ellicited', 'ellicited', 'ellicited', 'levatiracetem', 'resulatant', 'anitiboitc', 'smade', 'smade', 'baselilne', 'baselilne', 'baselilne', 'baselilne', 'gastroesophgeal', 'gastroesophgeal', 'gastroesophgeal', 'gastroesophgeal', 'gastroesophgeal', 'nictine', 'nictine', 'partiallly', 'partiallly', 'partiallly', 'partiallly', 'partiallly', 'diplocci', 'diplocci', 'diplocci', 'diplocci', 'diplocci', 'sensatations', 'indiependence', 'chracteristics', 'chracteristics', 'underdampened', 'underdampened', 'robatussin', 'robatussin', 'robatussin', 'robatussin', 'robatussin', 'adrtenergic', 'adrtenergic', 'adrtenergic', 'adrtenergic', 'adrtenergic', 'purpuses', 'purpuses', 'eppiplocae', 'cisplatinin', 'studues', 'studues', 'studues', 'studues', 'sofeners', 'sofeners', 'creatinnine', 'creatinnine', 'creatinnine', 'creatinnine', 'creatinnine', 'stneosis', 'stneosis', 'stneosis', 'stneosis', 'stneosis', 'oharmacy', 'espiodes', 'successufl', 'orificice', 'aassociated', 'aassociated', 'onocology', 'onocology', 'onocology', 'onocology', 'onocology', 'apasia', 'apasia', 'apasia', 'apasia', 'apasia', 'ppulse', 'ppulse']
    corrected = ['cardiology', 'lungs', 'lungs', 'lungs', 'lungs', 'lungs', 'echinocytes', 'procedure', 'procedure', 'evening', 'evening', 'evening', 'etanercept', 'etanercept', 'etanercept', 'hepatology', 'precipitously', 'tracheotomy', 'tracheotomy', 'responsive', 'responsive', 'responsive', 'responsive', 'responsive', 'intubed', 'subglottic', 'alternatively', 'pyelonephritis', 'pyelonephritis', 'pyelonephritis', 'pyelonephritis', 'pyelonephritis', 'increases', 'increases', 'quadrant', 'quadrant', 'quadrant', 'noted', 'noted', 'noted', 'noted', 'noted', 'special', 'distinct', 'distinct', 'hypokinesis', 'hypokinesis', 'hypercholesteremia', 'hypercholesteremia', 'hypercholesteremia', 'hypercholesteremia', 'hypercholesteremia', 'supportive', 'splenomegaly', 'splenomegaly', 'splenomegaly', 'splenomegaly', 'splenomegaly', 'antiarrhythmics', 'antiarrhythmics', 'reportedly', 'reportedly', 'reportedly', 'reportedly', 'reportedly', 'myalgias', 'imipenem', 'imipenem', 'imipenem', 'placement', 'transduction', 'suprahilar', 'neoplasm', 'uncomplicated', 'uncomplicated', 'uncomplicated', 'uncomplicated', 'uncomplicated', 'arimidex', 'arimidex', 'arimidex', 'arimidex', 'arimidex', 'across', 'acetazolamide', 'rocuronium', 'less', 'around', 'around', 'around', 'around', 'around', 'concentrate', 'demargination', 'demargination', 'hepatic', 'hepatic', 'hepatic', 'retroorbital', 'fer-in-sol', 'systolic', 'systolic', 'systolic', 'systolic', 'hyaline', 'ferrlecit', 'caloric', 'caloric', 'caloric', 'caloric', 'caloric', 'ankle', 'desaturate', 'cyclosporin', 'cyclosporin', 'cyclosporin', 'groins', 'bacteremia', 'bacteremia', 'symptoms', 'comminuted', 'comminuted', 'signal', 'signal', 'signal', 'signal', 'excretion', 'signs', 'incontinence', 'incontinence', 'incontinence', 'incontinence', 'incontinence', 'vasopressin', 'vasopressin', 'vasopressin', 'regurgitation', 'regurgitation', 'regurgitation', 'thalassemia', 'thalassemia', 'thalassemia', 'thalassemia', 'increase', 'increase', 'increase', 'increase', 'increase', 'rotated', 'accordance', 'background', 'background', 'background', 'contusions', 'contusions', 'contusions', 'iatrogenic', 'iatrogenic', 'iatrogenic', 'iatrogenic', 'iatrogenic', 'hemithorax', 'requires', 'requires', 'requires', 'requires', 'requires', 'cheeks', 'cheeks', 'confusion', 'confusion', 'confusion', 'pneumothorax', 'fibrosis', 'fibrosis', 'fibrosis', 'minutes', 'minutes', 'minutes', 'minutes', 'dehiscence', 'hydrocele', 'hydrocele', 'appropriately', 'appropriately', 'appropriately', 'appropriately', 'appropriately', 'steroids', 'prostatectomy', 'prostatectomy', 'popliteal', 'popliteal', 'popliteal', 'popliteal', 'popliteal', 'intubate', 'intubate', 'femoralis', 'femoralis', 'popliteal', 'sensation', 'thyrohyoid', 'thyrohyoid', 'thyrohyoid', 'discarded', 'discarded', 'discarded', 'discarded', 'discarded', 'palliative', 'mucoid', 'drainable', 'responding', 'responding', 'responding', 'responding', 'responding', 'invades', 'results', 'extraction', 'agglutinin', 'agglutinin', 'agglutinin', 'vaseline', 'eosinophils', 'eosinophils', 'eosinophils', 'hospitalization', 'nystagmus', 'diuresis', 'diuresis', 'diuresis', 'diuresis', 'nutrition', 'nutrition', 'pelvic', 'pelvic', 'pelvic', 'pelvic', 'pelvic', 'syndrome', 'syndrome', 'syndrome', 'syndrome', 'syndrome', 'tomorrow', 'respiratory', 'respiratory', 'respiratory', 'respiratory', 'respiratory', 'pupilary', 'pupilary', 'deceased', 'deceased', 'deceased', 'reflex', 'reflex', 'miacalcic', 'slightly', 'slightly', 'finger', 'problem', 'problem', 'problem', 'glargine', 'glargine', 'stricture', 'atazanavir', 'reading', 'reading', 'ureteral', 'pleurodesis', 'pleurodesis', 'pleurodesis', 'pleurodesis', 'pleurodesis', 'hematic', 'adenopathy', 'drainages', 'drainages', 'drainages', 'drainages', 'participated', 'coronary', 'coronary', 'coronary', 'ceruloplasmin', 'additionally', 'induration', 'became', 'became', 'became', 'resume', 'resume', 'resume', 'resume', 'resume', 'extends', 'inferolateral', 'inferolateral', 'added', 'added', 'added', 'tachypnea', 'procedure', 'procedure', 'procedure', 'procedure', 'procedure', 'mildly', 'placed', 'placed', 'confrontation', 'persisting', 'persisting', 'persisting', 'extinguishes', 'perhaps', 'open', 'open', 'open', 'open', 'open', 'hugger', 'anxiolytics', 'including', 'including', 'including', 'including', 'including', 'sphincterotomies', 'sphincterotomies', 'paracolic', 'paracolic', 'liquids', 'liquids', 'liquids', 'liquids', 'liquids', 'levemir', 'sleep', 'sleep', 'sleep', 'phenylephrine', 'phenylephrine', 'phenylephrine', 'quickly', 'quickly', 'quickly', 'quickly', 'hypoxemia', 'polymyxin', 'propofol', 'propofol', 'noted', 'noted', 'noted', 'noted', 'noted', 'hitting', 'hitting', 'hitting', 'hitting', 'hitting', 'continue', 'enhancing', 'enhancing', 'enhancing', 'enhancing', 'enhancing', 'transformation', 'extravasation', 'stabilized', 'entrapment', 'creatinine', 'creatinine', 'isoechoic', 'prostheses', 'aspects', 'aspects', 'aspects', 'aspects', 'recipient', 'recipient', 'recipient', 'recipient', 'recipient', 'hypercarbia', 'hypercarbia', 'hypercarbia', 'hypercarbia', 'hypercarbia', 'breakfast', 'breakfast', 'breakfast', 'breakfast', 'breakfast', 'hyperlucency', 'hyperlucency', 'hyperlucency', 'hyperlucency', 'hyperlucency', 'risk', 'risk', 'opiate', 'acidotic', 'acidotic', 'acidotic', 'acidotic', 'acidotic', 'unchanged', 'unchanged', 'unchanged', 'unchanged', 'unchanged', 'stomach', 'stomach', 'stomach', 'hypodensities', 'hypodensities', 'hypodensities', 'rotator', 'rotator', 'initiating', 'usually', 'usually', 'usually', 'usually', 'usually', 'performed', 'performed', 'performed', 'performed', 'performed', 'nondiagnostic', 'nondiagnostic', 'nondiagnostic', 'interparenchymal', 'counselor', 'counselor', 'counselor', 'counselor', 'consistently', 'hypokinesis', 'comfortable', 'comfortable', 'comfortable', 'comfortable', 'erythromycin', 'erythromycin', 'erythromycin', 'erythromycin', 'erythromycin', 'vertex', 'recreational', 'compared', 'agitating', 'agitating', 'agitating', 'agitating', 'agitating', 'symptoms', 'symptoms', 'symptoms', 'symptoms', 'integrilin', 'canthotomy', 'enteroscopy', 'enteroscopy', 'enteroscopy', 'enteroscopy', 'troponins', 'troponins', 'troponins', 'celecoxib', 'restriction', 'restriction', 'thickening', 'addendum', 'addendum', 'addendum', 'improves', 'improves', 'improves', 'going', 'going', 'going', 'going', 'going', 'lichenified', 'inconsistently', 'fragment', 'verapamil', 'radiation', 'radiation', 'transcortical', 'rupture', 'rupture', 'rupture', 'rupture', 'rupture', 'antiarrhythmic', 'hyperphosphatemia', 'wait', 'repositions', 'repositions', 'repositions', 'repositions', 'repositions', 'interpret', 'interpret', 'interpret', 'interpret', 'interpret', 'unlikely', 'supportive', 'supportive', 'hepatocellular', 'escherichia', 'paratracheal', 'paratracheal', 'paratracheal', 'subcapsular', 'subcapsular', 'lateral', 'lateral', 'colistin', 'cricoid', 'containment', 'containment', 'containment', 'containment', 'immunosuppressants', 'immunosuppressants', 'immunosuppressants', 'immunosuppressants', 'immunosuppressants', 'branch', 'branch', 'expiratory', 'expiratory', 'hematochezia', 'bronchial', 'bronchial', 'bronchial', 'candidate', 'candidate', 'assistance', 'assistance', 'pedestrian', 'pedestrian', 'erythromycin', 'erythromycin', 'erythromycin', 'erythromycin', 'erythromycin', 'genteal', 'heterogenous', 'cardiogenic', 'antipsychotic', 'antipsychotic', 'antipsychotic', 'just', 'just', 'just', 'just', 'just', 'distended', 'distended', 'distended', 'necrotic', 'necrotic', 'necrotic', 'necrotic', 'necrotic', 'thick', 'sensitivities', 'sensitivities', 'sensitivities', 'downgoing', 'transport', 'transport', 'transport', 'cefotaxime', 'senekot', 'senekot', 'senekot', 'senekot', 'senekot', 'secondary', 'second', 'second', 'second', 'second', 'second', 'tingling', 'tingling', 'tingling', 'tingling', 'arrythmia', 'cantonese', 'cantonese', 'cantonese', 'cantonese', 'cantonese', 'pregnant', 'pregnant', 'pregnant', 'pregnant', 'neuropathic', 'neuropathic', 'neuropathic', 'neuropathic', 'neuropathic', 'metoprolol', 'metoprolol', 'metoprolol', 'metoprolol', 'metoprolol', 'calmed', 'denied', 'denies', 'denies', 'denies', 'denies', 'remaining', 'remaining', 'remaining', 'remaining', 'trach', 'trach', 'trach', 'trach', 'trach', 'zyprexa', 'very', 'very', 'very', 'very', 'very', 'holosystolic', 'developing', 'results', 'bronchodilations', 'abnormality', 'collaborate', 'isordil', 'isordil', 'parafalcine', 'consolidation', 'cholangitis', 'cholangitis', 'cholangitis', 'attributes', 'along', 'along', 'along', 'along', 'along', 'saturation', 'increase', 'petechial', 'petechial', 'tramadol', 'tramadol', 'evening', 'evening', 'evening', 'evening', 'evening', 'inferoseptal', 'resuscitation', 'dehiscence', 'alveolar', 'alveolar', 'alveolar', 'barrier', 'barrier', 'precipitously', 'precipitously', 'fluctuation', 'dynamics', 'dynamics', 'autacoidal', 'double', 'double', 'double', 'double', 'mimic', 'mimic', 'mimic', 'mimic', 'mimic', 'phlebitis', 'definitely', 'extreme', 'extreme', 'extreme', 'extreme', 'extreme', 'limited', 'limited', 'limited', 'limited', 'limited', 'propranolol', 'propranolol', 'requirements', 'splenectomy', 'splenectomy', 'splenectomy', 'psittaci', 'until', 'until', 'transport', 'transport', 'chest', 'chest', 'chest', 'chest', 'chest', 'temporary', 'temporary', 'temporary', 'temporary', 'temporary', 'upper', 'upper', 'upper', 'imaging', 'arteriography', 'arteriography', 'stabilizing', 'intubation', 'intubation', 'intubation', 'rehospitalization', 'generative', 'strong', 'electrocardiogram', 'discontinued', 'discontinued', 'discontinued', 'discontinued', 'leukocytosis', 'leukocytosis', 'diverticuli', 'during', 'during', 'erythema', 'identified', 'identified', 'identified', 'identified', 'identified', 'caucasian', 'sclerosing', 'sclerosing', 'sclerosing', 'sclerosing', 'brings', 'brings', 'brings', 'brings', 'brings', 'coccyx', 'coccyx', 'coccyx', 'coccyx', 'subsided', 'they', 'attempts', 'attempts', 'attempts', 'ventriculostomy', 'ventriculostomy', 'ventriculostomy', 'ventriculostomy', 'activity', 'activity', 'ankles', 'ankles', 'ankles', 'conjunctival', 'conjunctival', 'abrogate', 'elicited', 'elicited', 'elicited', 'elicited', 'elicited', 'levetiracetam', 'resultant', 'antibiotic', 'made', 'made', 'baseline', 'baseline', 'baseline', 'baseline', 'gastroesophageal', 'gastroesophageal', 'gastroesophageal', 'gastroesophageal', 'gastroesophageal', 'nicotine', 'nicotine', 'partially', 'partially', 'partially', 'partially', 'partially', 'diplococci', 'diplococci', 'diplococci', 'diplococci', 'diplococci', 'sensations', 'independence', 'characteristics', 'characteristics', 'underdamped', 'underdamped', 'robitussin', 'robitussin', 'robitussin', 'robitussin', 'robitussin', 'adrenergic', 'adrenergic', 'adrenergic', 'adrenergic', 'adrenergic', 'purposes', 'purposes', 'epiploicae', 'cisplatin', 'studies', 'studies', 'studies', 'studies', 'softeners', 'softeners', 'creatinine', 'creatinine', 'creatinine', 'creatinine', 'creatinine', 'stenosis', 'stenosis', 'stenosis', 'stenosis', 'stenosis', 'pharmacy', 'episodes', 'successful', 'orifice', 'associated', 'associated', 'oncology', 'oncology', 'oncology', 'oncology', 'oncology', 'aphasia', 'aphasia', 'aphasia', 'aphasia', 'aphasia', 'pulse', 'pulse']

    detection_contexts = []
    final_misspellings = []
    final_line_idxs = []
    final_corrected = []

    assert len(line_idxs) == len(misspellings)

    print('Extracting test set from MIMIC-III')
    found_line_idxs = []
    with open('../data/mimic_preprocessed.txt', 'r') as f:
        for i, line in enumerate(f):
            if i in set_line_idxs:
                tokenlist = line.split()
                ides = [x for x, line in enumerate(line_idxs) if line == i]
                for ide in ides:
                    misspelling = misspellings[ide]
                    assert misspelling in tokenlist
                    j = tokenlist.index(misspelling)
                    left_context = " ".join(tokenlist[:j])
                    right_context = " ".join(tokenlist[j+1:])
                    detection_contexts.append((" ".join(left_context.split()[-10:]), " ".join(right_context.split()[:10])))
                    
                    final_misspellings.append(misspelling)
                    final_corrected.append(corrected[ide])
                    final_line_idxs.append(i)

    assert len(detection_contexts) == len(misspellings)

    print('Finished')

    with open('../data/testcorpus.json', 'w') as f:
        json.dump((final_corrected, final_misspellings, detection_contexts, final_line_idxs), f)
