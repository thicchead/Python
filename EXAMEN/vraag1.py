# Karakoruk Metehan - 1TINE

def main():
    jeugdbewegingen = ["Scouts", "KSA", "Chiro", "KSJ"]
    leden_jeugdbewegingen = ["An:V:15jaar Elly:V:13jaar Jef:M:13jaar Mia:V:17jaar Frans:M:5jaar Els:V:10jaar",
                             "Daan:M:12jaar Eva:V:8jaar Luk:M:13jaar Noor:V:17jaar Jos:M:5jaar Sara:V:10jaar Storm:M:11jaar",
                             "Tess:V:15jaar Evy:V:13jaar Sezn:M:16jaar",
                             "Liv:V:15jaar Roos:V:13jaar Jack:M:16jaar Gijs:M:17jaar Jan:M:5jaar Joep:M:10jaar Isa:V:16jaar"]

    activiteiten = ["voetbal", "dropping", "potteke-stamp", "trefbal"]
    voorwaarden_activiteiten = ["M,10,14", "X,14,25", "X,5,9", "V,10,14"]

    scoutsleden = [leden_jeugdbewegingen[0]]
    # jongens_s = str(scoutsleden).count(":M:")

    ksaleden = [leden_jeugdbewegingen[1]]

    chiroleden = [leden_jeugdbewegingen[2]]

    ksjleden = [leden_jeugdbewegingen[3]]

    # deelnemers_voetbal = []
    # deelnemers_voetbal.append(jongens_s)

    voetbal_voorwaarden = voorwaarden_activiteiten[0].split(",")
    voetbal_geslacht = voetbal_voorwaarden[0]
    minimum_leeftijd_voetbal = voetbal_voorwaarden[1]
    maximum_leeftijd_voetbal = voetbal_voorwaarden[2]

    dropping_voorwaarden = voorwaarden_activiteiten[1].split(",")
    minimum_leeftijd_dropping = dropping_voorwaarden[1]
    maximum_leeftijd_dropping = dropping_voorwaarden[2]

    potteke_stamp_voorwaarden = voorwaarden_activiteiten[2].split(",")
    minimum_leeftijd_potteke = potteke_stamp_voorwaarden[1]
    maximum_leeftijd_potteke = potteke_stamp_voorwaarden[2]

    trefbal_voorwaarden = voorwaarden_activiteiten[3].split(",")
    trefbal_geslacht = trefbal_voorwaarden[0]
    minimum_leeftijd_trefbal = trefbal_voorwaarden[1]
    maximum_leeftijd_trefbal = trefbal_voorwaarden[2]

    print("Jeugdbeweging KSJ met 4 inschrijving(en) voor dropping")


if __name__ == '__main__':
    main()
