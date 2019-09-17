# This program given                            |
#   1. A file containing multiple '.PRG' files  |
#   named [unique Identifier].prg               |
#   2. A dictionary of [unique Identifiers]     |
#   3. A parallel dicitonary of watch names     |
# Will rename all files with watch name         |
#-----------------------------------------------|

import os
import glob
import shutil
import zipfile

watchModel = {"006-B1907-00": "vivoactive(1)",
"006-B2160-00": "vivoactive(2)",
"006-B2337-00": "vivoactivehr(1)",
"006-B2497-00": "vivoactivehr(2)",
"006-B2700-00": "vivoactive3(1)",
"006-B2976-00": "vivoactive3(2)",
"006-B3163-00": "vivoactive3(3)",
"006-B3473-00": "vivoactive3(4)",
"006-B3446-00": "vivoactive3(5)",
"006-B2988-00": "vivoavtive3(6)",
"006-B3066-00": "vivoactive3MLTE(1)",
"006-B3477-00": "vivoactive3d(1)",
"006-B3225-00": "vivoactive4(1)",
"006-B3388-00": "vivoactive4(2)",
"006-B3387-00": "vivoactive4s(1)",
"006-B3224-00": "vivoactive4s(2)",
"006-B2130-00": "fr920xt(1)",
"006-B2131-00": "fr920xt(2)",
"006-B2132-00": "fr920xt(3)",
"006-B1765-00": "fr920xt(4)",
"006-B2156-00": "fr630(1)",
"006-B2157-00": "fr230(1)",
"006-B2313-00": "fr230(2)",
"006-B2396-00": "fr230(3)",
"006-B2397-00": "fr230(4)",
"006-B2653-00": "fr235(1)",
"006-B2733-00": "fr235(2)",
"006-B2431-00": "fr235(3)",
"006-B3076-00": "fr245(1)",
"006-B3145-00": "fr245(2)",
"006-B3077-00": "fr245m(1)",
"006-B3321-00": "fr245m(2)",
"006-B2886-00": "fr645(1)",
"006-B3003-00": "fr645(2)",
"006-B3004-00": "fr645m(1)",
"006-B2888-00": "fr645m(2)",
"006-B2533-00": "fr735xt(1)",
"006-B2534-00": "fr735xt(2)",
"006-B2158-00": "fr735xt(3)",
"006-B2691-00": "fr935(1)",
"006-B2833-00": "fr935(2)",
"006-B3441-00": "fr945(1)",
"006-B3113-00": "fr945(2)",
"006-B2188-00": "fenix3(1)",
"006-B2189-00": "fenix3(2)",
"006-B2050-00": "fenix3(3)",
"006-B2293-00": "fenix3(4)",
"006-B2407-00": "fenix3(5)",
"006-B2408-00": "fenix3(6)",
"006-B2413-00": "fenix3hr(1)",
"006-B2473-00": "fenix3hr(2)",
"006-B2432-00": "fenixchronos(1)",
"006-B2675-00": "fenixchronos(2)",
"006-B2467-00": "d2bravo(1)",
"006-B2262-00": "d2bravo(2)",
"006-B2547-00": "d2bravotitanium(1)",
"006-B2819-00": "d2charlie(1)",
"006-B2994-00": "d2charlie(2)",
"006-B2859-00": "descentmk1(1)",
"006-B2991-00": "descentmk1(2)",
"006-B2697-00": "fenix5-quatix5(1)",
"006-B2796-00": "fenix5-quatix5(2)",
"006-B2798-00": "fenix5-quatix5(3)",
"006-B3089-00": "fenix5plus(1)",
"006-B2544-00": "fenix5s(1)",
"006-B2797-00": "fenix5s(2)",
"006-B3134-00": "fenix5splus(1)",
"006-B2900-00": "fenix5splus(2)",
"006-B3110-00": "fenix5xplus(1)",
"006-B3111-00": "fenix5xplus(2)",
"006-B3135-00": "fenix5xplus(2)",
"006-B3196-00": "d2delta(1)",
"006-B3197-00": "d2delta(2)",
"006-B3198-00": "d2deltapx(1)",
"006-B3324-00": "d2deltapx(2)",
"006-B3246-00": "marqdriver(1)",
"006-B3420-00": "marqdriver(2)",
"006-B3247-00": "marqaviator(1)",
"006-B3421-00": "marqaviator(2)",
"006-B3248-00": "marqcaptain(1)",
"006-B3448-00": "marqcaptain(2)",
"006-B3450-00": "marqexpedition(1)",
"006-B3250-00": "marqexpedition(2)",
"006-B3251-00": "marqathlete(1)",
"006-B3451-00": "marqathlete(2)",
"006-B3287-00": "fenix6s(1)",
"006-B3512-00": "fenix6s(2)",
"006-B3289-00": "fenix6(1)",
"006-B3514-00": "fenix6(2)",
"006-B3288-00": "feniz6spro-6ssapphire(1)",
"006-B3513-00": "fenix6spro-6ssapphire(2)",
"006-B3290-00": "fenix6pro-6sapphire(1)",
"006-B3515-00": "fenix6pro-6sapphire(2)",
"006-B3291-00": "fenix6xpro-6xsapphire(1)",
"006-B3516-00": "fenix6xpro-6xsapphire(2)",
"006-B2604-00": "fenix5x-tactixcharlie(1)",   
"006-B2310-00": "--",
"006-B2311-00": "--"

}


#input filename of the program ids you want to rename
#filename = input()
filename = "stryd_data_field_two.zip"

#destination to "filename" in this case the local folder
path = './'

#unzip all contents of your folder into beta-progs folder
with zipfile.ZipFile(path + filename, 'r') as zip_ref:
    zip_ref.extractall('./beta-progs')

#copy all device ids that are present in folder 'beta-progs into devIds array
path = './beta-progs'
devIds = os.listdir(path)

#rename all Ids to corresponding names
for x in range(len(devIds)):
    try:
        os.rename(path +"/"+ devIds[x],path +"/"+ watchModel[devIds[x]])
        print(devIds[x] + " >>> " +watchModel[devIds[x]] )
    except:
        print("pop")








