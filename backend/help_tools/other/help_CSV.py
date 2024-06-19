import csv
import os

####################################
# Functions to help with csv files #
####################################

# Function to split a CSV file into smaller files
def split_csv(input_file, output_dir, batch_size):
    with open(input_file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Get the header

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        file_count = 1
        current_batch = []

        for row in csv_reader:
            current_batch.append(row)

            if len(current_batch) >= batch_size:
                output_file = os.path.join(output_dir, f'o_{file_count}.csv')
                write_csv(output_file, header, current_batch)
                current_batch = []
                file_count += 1

        # Write the last batch if it's not empty
        if current_batch:
            output_file = os.path.join(output_dir, f'o_{file_count}.csv')
            write_csv(output_file, header, current_batch)

# Function to write CSV file
def write_csv(output_file, header, rows):
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)
        csv_writer.writerows(rows)

# Example usage
#input_file = 'D:/neo4j/import/BIOGRID.txt'
#input_file = 'C:/Users/pc/Desktop/Masterarbeit/code-masterarbeit/backend/neo4j/ProCan-DepMapSanger_protein_matrix_8498_averaged.csv'
#input_file = 'C:/Users/PC/Desktop/Masterarbeit/code-masterarbeit/backend/neo4j/ProCan-DepMapSanger_protein_matrix_6692_averaged.csv'
input_file = 'C:/Users/PC/Desktop/code-masterarbeit/backend/neo4j/ProCan-DepMapSanger_protein_matrix_6692_averaged.txt.csv'
#input_file = 'C:/Users/PC/Desktop/code-masterarbeit/backend/neo4j/ProCan-DepMapSanger_protein_matrix_8498_averaged.txt.csv'
output_directory = 'C:/Users/PC/neo4j/import/Cell_Line_Protein/6692'
batch_size = 500000  # Adjust the batch size as needed

split_csv(input_file, output_directory, batch_size)

def find_unqiue_values():
    with open("D:/neo4j/import/Drug_Protein/lm_sklearn_degr_drug_annotated_diann_051021.csv", 'r', newline='') as csvfile:
        different_columns_set = set()
        csv_reader = csv.DictReader(csvfile, delimiter=",")
        for row in csv_reader:
            news = [row['y_id'].split(";")[0]]
            different_columns_set.update(news)
    print(len(different_columns_set))
    print(different_columns_set)
    b = {'EPZ004777', 'Vinblastine', 'KIT_6754', 'NPK76-II-72-1', 'CCT-018159', 'A-770041', 'RO-3306', 'Erlotinib', 'Dactolisib', 'Lestaurtinib', 'Elesclomol', 'VER-155008', 'AST-1306', 'Torin 2', 'Methotrexate', 'RAF_9304', 'PLK4_0066', 'IAP_7638', 'S-crizotinib', 'STAT3_2372', 'GSK1070916', 'IAP_5620', 'WYE-125132', 'Gemcitabine', 'Dacinostat', 'CGP-082996', 'CCT007093', 'Alpelisib', 'CDK12_8969', 'Imatinib', 'GSK1904529A', 'GNF-2', 'S63845', 'DMOG', 'IC-87114', 'TAK-715', 'EPZ020411', 'Y-39983', 'Telomerase Inhibitor IX', 'Mcl1_6386', 'PDGFR_5313', 'NU7441', 'Capivasertib', 'Flavopiridol', 'SU11274', 'Genentech Cpd 10', 'Afuresertib', 'PLX7904', 'QL-XII-47', 'I-BRD9', 'RGFP966', 'AZD1152-HQPA', 'GSK690693', 'Topotecan', 'LGK974', 'Tubacin', 'UNC1215', 'WZ3105', 'Palbociclib', 'NSC-207895', 'FH535', 'Sorafenib', 'CP724714', 'ERK_5051', 'UMI-77', 'Entospletinib', 'AZD8835', 'MZ1', 'Panobinostat', 'eEF2K Inhibitor, A-484954', 'CP-724714', 'Enzastaurin', 'Navitoclax', 'AZD5438', 'UNC0379', 'Fenretinide', 'WEHI-539', 'GNF-5', 'YM201636', 'PDD00017273', 'Sphingosine Kinase 1 Inhibitor II', 'CPI-360', 'PHA-793887', 'Barasertib', 'NVP-ADW742', 'LCL161', 'SB590885', 'THZ-2-102-1', 'THZ-2-49', 'AC220', 'Deltarasin', 'Bicalutamide', 'Lasalocid', 'Vinorelbine', 'PLX-4720', 'PARP_0108', 'FEN1_3940', 'C-75', 'Luminespib', 'Veliparib', 'FGFR_3831', 'FR-180204', 'AZ20', 'Latamoxef', 'Dabrafenib', 'Sepantronium bromide', 'G-5555', 'Bortezomib', 'AMG-319', 'Tivozanib', 'Dyrk1b_0191', 'MIM1', 'OSI-027', 'FTI-277', 'Midostaurin', 'Docetaxel', 'RU-SKI 43', 'BCL6_7224', 'Brivanib, BMS-540215', 'Cisplatin', 'Lapatinib', 'AS605240', 'ABT737', 'Merestinib', 'Axitinib', 'PAC-1', 'EHT-1864', 'AZD1775', 'PF-3644022', 'EI1', 'Prexasertib', 'Rucaparib', 'ZM447439', 'GSK2578215A', 'VX-11e', 'Mitomycin-C', 'EphB4_9721', 'XMD8-85', 'GSK429286A', 'Linsitinib', 'EGFR_7518', 'IRAK4_8366', 'Epirubicin', 'JNJ38877605', 'WIKI4', 'SYK_1543', 'CGI1746', 'Irinotecan', 'PARP_9482', 'Wee1 Inhibitor', 'TGX221', 'Paclitaxel (0.005)', 'VX-745', 'MPS-1-IN-1', 'AZD3514', 'CDK12_2242', 'NVP-TAE684', 'Vorinostat', 'Pictilisib', 'Pemetrexed', 'A-443654', 'UNC0638', 'BPTES', 'SL0101', 'Cediranib', 'GSK1059615', 'FGFR_0939', 'QL-VIII-58', 'XL413', 'Sonolisib', 'UNC0642', 'Staurosporine', 'I-BET-762', 'TW 37', 'Temsirolimus', 'Mcl1_7350', 'Serdemetan', 'PFI-1', 'Tenovin-6', 'Dasatinib', 'AZD5363', 'GW441756', 'AT-7519', 'Tepotinib', 'Ponatinib', 'EPZ011989', 'AT7867', 'Buparlisib', 'ICL1100013', 'Fulvestrant', 'OSU-03012', 'AZD4205', 'AZD1480', 'AZD8931', 'Menin_MLL_8690', 'AZD8055', 'PF-3758309', 'GSK591', 'EAI045', 'Pyridostatin', 'ZSTK474', 'Wnt-C59', 'Rociletinib', 'Regorafenib', 'BVD523', 'Taselisib', 'Picrotin', 'TTK_3146', 'HG-9-91-01', 'Bleomycin', 'Rapamycin', 'Obatoclax Mesylate', 'BCLXL_3202', 'FTY-720', 'GW843682X', 'Dabrafenib (1373) + Trametinib (1372)', 'Ara-G', 'MK-5108', 'Tanespimycin', 'WH-4-023', 'Poziotinib', 'JW-7-24-1', 'AZD6482', 'Motesanib', 'Alisertib', 'AZD5582', 'Osimertinib', 'AMG900', 'Serabelisib', 'RAF_7242', 'Brigatinib', 'KIN001-270', 'MIK-665 / S-64315', 'LDN-193189', 'Gefitinib', 'KU-55933', 'Filgotinib', 'NSC319726', 'Quizartinib', 'PD173074', 'BMS-754807', 'BMS-509744', 'GSK269962A', 'Kobe2602', 'Cetuximab', 'Tozasertib', 'CAY10603', 'Cytarabine', 'EPZ5676', 'CI-1033', 'EGFR_0300', 'Sapatinib', 'A-196', 'IPA-3', 'Masitinib', 'ACY-738', 'AICA Ribonucleotide', 'Vismodegib', 'NVP-BHG712', 'Nazartinib', 'Kobe0065', 'NSC-624206', 'MS023', 'Bleomycin (10 uM)', 'Uprosertib', 'VE821', 'AZ960', 'Phenformin', 'PF-00299804', '5-Fluorouracil', 'JQ1', 'LIMK1 inhibitor BMS4', 'Sapanisertib', 'EGF816', 'BIX-02188', 'Afatinib', 'ERK_5330', 'Ribociclib', 'Tretinoin', 'JAK3_7406', 'HG-5-113-01', 'NVS-PAK1-1', 'MCT1_6447', 'Doramapimod', 'AZD8186', 'AZD7969', 'ML216', 'Ruxolitinib', 'AZD3759', 'QL-X-138', 'SN-38', '(5Z)-7-Oxozeaenol', 'BAM7', 'Cyclopamine', 'PIM447', 'P5091', 'ETP-45835', 'AZD1332', 'Pyrimethamine', 'Mirin', 'Venetoclax', 'QL-XI-92', 'Refametinib', 'Senexin B', 'CA3', 'ERK_6197', 'GDC-0879', 'HG6-64-1', 'BLU9931', 'CD532', 'Ulixertinib', 'Bleomycin (50 uM)', 'Olaparib(1495) + Temozolomide(1375)', 'Venotoclax', 'PARP_9495', 'ASLAN002', 'CDK7_8454', 'Crizotinib', 'GSK650394', 'CDK12_1992', 'TL-2-105', 'Foretinib', 'GSK2830371A', 'Avagacestat', 'Z-LLNle-CHO', 'Daporinad', 'Volasertib', 'JNK Inhibitor VIII', 'BX-912', 'Bosutinib', 'Linifanib', 'MK-1775', 'Bexarotene', 'XAV939', 'PD0166285', 'Cabozantinib', 'EGFR_5383', 'Doxorubicin', 'LY2584702', 'CI-1040', 'MK-8776', 'AZD4877', 'CAP-232, TT-232, TLN-232', 'KIT_5808', 'PI-103', 'Tipifarnib', 'EGFR_8897', 'PHA-665752', 'ACY-1215', 'IOX2', 'R428', 'CB-839', 'UNC-2025', 'Picolinici-acid', 'Camptothecin', 'GSK126', 'Menin_MLL_8687', 'Amuvatinib', 'CAY10566', 'Trametinib', 'MK-2206', 'GNE-317', 'Seliciclib', 'IMD-0354', 'GDC0810', 'Idelalisib', 'A-83-01', 'Capmatinib', 'XMD13-2', 'AZD7762', 'Pilaralisib', 'Savolitinib', 'PLK_6522', 'AZ6102', 'BX795', 'AS601245', 'A-366', 'Ravoxertinib', 'Sunitinib', 'KIN001-236', 'BMS-536924', 'BIBF-1120', 'AZD2014', 'BAY-87-2243', 'Piperlongumine', 'Romidepsin', 'CX-5461', 'JW-7-52-1', 'BIX02189', 'Temozolomide', 'BAY-598', 'Alectinib', 'IGFR_3801', 'Rigosertib', 'Paclitaxel', 'AZD6738', 'Etoposide', 'Everolimus', 'Olaparib', 'TWS119', 'AZD0156', 'Embelin', 'CPI-169', 'Cyclophosphamide', 'kb NB 142-70', 'YK-4-279', 'Cymarine', 'AT13148', 'Nutlin-3a (-)', 'IRAK4_7891', 'WZ-1-84', 'Pevonedistat', 'SCH772984', 'AKT inhibitor VIII', 'MG-132', 'CHIR-99021', 'TANK_1366', 'RK-33', 'Ipatasertib', 'PI3Ka_4409', 'Trichostatin A', 'KIT_7208', 'MCL1_8070', 'AZD5991', 'Talazoparib', 'Ceritinib', 'JNK-IN-8', 'LTT462', 'Oxaliplatin', 'AGI-5198', 'eCF309', 'P22077', 'LFM-A13', 'ARRY-520', 'CCT244747', 'AZD6094', 'MIRA-1', 'Nilotinib', 'KU-60019', 'AZ628', 'Epothilone B', 'Shikonin', 'Danusertib', 'Pazopanib', 'WHI-P97', 'PDGFR_0615', 'KRASi', 'Abemaciclib', 'Thapsigargin', 'Saracatinib', 'TL-1-85', 'Tubastatin A', 'AGI-6780', 'Entinostat', 'GNE7915', 'CCT251545', 'BI-2536', 'CGP-60474', 'LJI308', 'rTRAIL', 'Selisistat', 'PF-06747775', 'MCL1_1284', 'IRAK4_1495', 'SYK_9721', 'AZD4547', 'Dactinomycin', 'BIBR-1532', 'KIN001-260', 'A-1155463', 'Pelitinib', 'PD0325901', 'BMX-IN-1', 'Fedratinib', 'Ibrutinib', 'Selumetinib', 'Carboplatin', 'SB505124', 'SB52334', 'LLY-283'}
    
    a = {'Ulixertinib', 'EAI045', 'Talazoparib', 'AZD8931', 'Sepantronium bromide', 'Vorinostat', 'AZD6094', 'Prexasertib', 'KIN001-270', 'TL-1-85', 'Dyrk1b_0191', 'Tretinoin', 'Seliciclib', 'Ceritinib', 'BI-2536', 'ASLAN002', 'CI-1040', 'A-443654', 'Telomerase Inhibitor IX', 'Alisertib', 'Barasertib', 'WH-4-023', 'Enzastaurin', 'FGFR_0939', 'ARRY-520', 'PD0166285', 'Latamoxef', 'Savolitinib', 'CGP-082996', 'AKT inhibitor VIII', 'FH535', 'AT-7519', 'BMX-IN-1', '(5Z)-7-Oxozeaenol', 'Menin_MLL_8687', 'LY2584702', 'Ravoxertinib', 'I-BET-762', 'QL-XII-47', 'LDN-193189', 'WZ-1-84', 'Regorafenib', 'Venetoclax', 'Selumetinib', 'AGI-5198', 'Uprosertib', 'Quizartinib', 'Refametinib', 'ETP-45835', 'Torin 2', 'Lasalocid', 'Taselisib', 'Idelalisib', 'XMD13-2', 'Temozolomide', 'THZ-2-102-1', 'PDGFR_5313', 'Ipatasertib', 'AZ20', 'Olaparib(1495) + Temozolomide(1375)', 'AZD6738', 'SB52334', 'BMS-509744', 'Ruxolitinib', 'Sorafenib', 'GSK2578215A', 'YK-4-279', 'NVP-ADW742', 'Vinblastine', 'Z-LLNle-CHO', 'BIBF-1120', 'PARP_9495', 'Entospletinib', 'GSK429286A', 'Merestinib', 'Danusertib', 'EPZ004777', 'UNC0642', 'BIX02189', 'Afuresertib', 'LTT462', 'PAC-1', 'CI-1033', 'BAY-598', 'IRAK4_1495', 'Doramapimod', 'EGFR_0300', 'eEF2K Inhibitor, A-484954', 'AMG900', 'Filgotinib', 'Carboplatin', 'IAP_5620', 'SL0101', 'GSK126', 'QL-XI-92', 'Cyclophosphamide', 'EGF816', 'TWS119', 'AZD3759', 'KIT_5808', 'SCH772984', 'PHA-793887', 'LCL161', 'HG-9-91-01', 'GSK2830371A', 'BLU9931', 'WYE-125132', 'GSK690693', 'PD173074', 'BIBR-1532', 'CDK12_1992', 'CCT-018159', 'Saracatinib', 'I-BRD9', 'Venotoclax', 'Temsirolimus', 'Sonolisib', 'EphB4_9721', 'SN-38', 'Menin_MLL_8690', 'CAP-232, TT-232, TLN-232', 'Paclitaxel (0.005)', 'NVS-PAK1-1', 'Kobe2602', 'Tubastatin A', 'AZD5582', 'P5091', 'AZD5438', 'VE821', 'IRAK4_8366', 'Sphingosine Kinase 1 Inhibitor II', 'TGX221', 'Phenformin', 'Cediranib', 'GSK1059615', 'GDC0810', 'TAK-715', 'AZD4547', 'AZD4205', 'XL413', 'Foretinib', 'WHI-P97', 'AS605240', 'EHT-1864', 'PLK4_0066', 'BCLXL_3202', 'AZD4877', 'Wee1 Inhibitor', 'Cymarine', 'AZD3514', 'Picolinici-acid', 'PF-00299804', 'PF-06747775', 'Bicalutamide', 'Pictilisib', 'Dacinostat', 'BX-912', 'Crizotinib', 'IMD-0354', 'THZ-2-49', 'Tubacin', 'Bortezomib', 'MK-1775', 'UNC1215', 'NVP-BHG712', 'eCF309', 'MCL1_8070', 'LIMK1 inhibitor BMS4', 'FGFR_3831', 'PF-3644022', 'Deltarasin', 'LLY-283', 'Thapsigargin', 'Cabozantinib', 'MS023', 'JW-7-24-1', 'PLX7904', 'Ibrutinib', 'A-1155463', 'Midostaurin', 'CDK12_2242', 'IAP_7638', 'PI-103', 'Entinostat', 'AT13148', 'BPTES', 'CAY10566', 'RO-3306', 'EPZ5676', 'AZ960', 'KRASi', 'S-crizotinib', 'XMD8-85', 'DMOG', 'AST-1306', 'LGK974', 'Cetuximab', 'PLK_6522', 'JW-7-52-1', 'CHIR-99021', 'Dasatinib', 'Tozasertib', 'AC220', 'EGFR_7518', 'Mcl1_6386', 'RAF_9304', 'AZD5991', 'Wnt-C59', 'RK-33', 'MPS-1-IN-1', 'CX-5461', 'GW441756', 'CD532', 'Bosutinib', 'Pazopanib', 'PLX-4720', 'AZD0156', 'Nazartinib', 'XAV939', 'Alectinib', 'AZD8186', 'Mcl1_7350', 'Sunitinib', 'Serabelisib', 'Shikonin', 'KIN001-236', 'Capmatinib', 'PFI-1', 'PD0325901', 'MCL1_1284', 'Fedratinib', 'CDK12_8969', 'A-366', 'UNC0379', 'Pemetrexed', 'Elesclomol', 'Palbociclib', 'IRAK4_7891', 'MK-5108', 'Buparlisib', 'kb NB 142-70', 'Erlotinib', 'Linifanib', 'VER-155008', 'Imatinib', 'SU11274', 'Pevonedistat', 'AZD8835', 'EGFR_8897', 'ABT737', 'Pyrimethamine', 'CPI-169', 'ICL1100013', 'Cyclopamine', 'IOX2', 'JAK3_7406', 'UMI-77', 'PF-3758309', 'GNF-5', 'Staurosporine', 'QL-X-138', 'BIX-02188', 'Mirin', 'ERK_5330', 'RU-SKI 43', 'KIN001-260', 'AT7867', 'Lapatinib', 'PARP_0108', 'Dabrafenib', 'AMG-319', 'Masitinib', 'HG-5-113-01', 'JNK Inhibitor VIII', 'Avagacestat', 'Luminespib', 'ACY-1215', 'GNF-2', 'ZSTK474', 'BMS-536924', 'Gemcitabine', 'LJI308', 'Amuvatinib', 'Dactolisib', 'MIK-665 / S-64315', 'CP-724714', 'Trichostatin A', 'C-75', 'Mitomycin-C', 'ERK_6197', 'Trametinib', 'A-770041', 'ACY-738', 'CGP-60474', 'VX-745', 'Brivanib, BMS-540215', 'NSC-624206', '5-Fluorouracil', 'P22077', 'Ponatinib', 'Volasertib', 'NVP-TAE684', 'AZ6102', 'IGFR_3801', 'Rapamycin', 'TW 37', 'BX795', 'Veliparib', 'AICA Ribonucleotide', 'PARP_9482', 'Navitoclax', 'rTRAIL', 'Abemaciclib', 'BVD523', 'Vismodegib', 'AZD1332', 'Tepotinib', 'GSK650394', 'Genentech Cpd 10', 'drug_name', 'JNK-IN-8', 'CCT007093', 'AZD1152-HQPA', 'CDK7_8454', 'Capivasertib', 'Lestaurtinib', 'Irinotecan', 'Bleomycin (50 uM)', 'Cytarabine', 'AZD1480', 'Ara-G', 'Tenovin-6', 'EGFR_5383', 'GNE-317', 'KU-55933', 'CP724714', 'VX-11e', 'CCT244747', 'WZ3105', 'Gefitinib', 'GSK1070916', 'Sapanisertib', 'Romidepsin', 'STAT3_2372', 'KU-60019', 'S63845', 'PHA-665752', 'A-196', 'Nilotinib', 'GSK591', 'Axitinib', 'Bexarotene', 'EPZ020411', 'CPI-360', 'Docetaxel', 'AGI-6780', 'OSI-027', 'MK-8776', 'Tivozanib', 'MIRA-1', 'R428', 'AZ628', 'Fulvestrant', 'FTY-720', 'Etoposide', 'PIM447', 'Epirubicin', 'MG-132', 'Methotrexate', 'Bleomycin (10 uM)', 'Alpelisib', 'QL-VIII-58', 'Rucaparib', 'JQ1', 'WEHI-539', 'CGI1746', 'GSK1904529A', 'MK-2206', 'CCT251545', 'Pelitinib', 'Everolimus', 'Doxorubicin', 'Dactinomycin', 'Fenretinide', 'Ribociclib', 'JNJ38877605', 'Sapatinib', 'Selisistat', 'NSC319726', 'G-5555', 'IC-87114', 'CAY10603', 'Tipifarnib', 'Cisplatin', 'TTK_3146', 'Dabrafenib (1373) + Trametinib (1372)', 'HG6-64-1', 'PDGFR_0615', 'Poziotinib', 'Picrotin', 'Bleomycin', 'Senexin B', 'Epothilone B', 'EI1', 'Kobe0065', 'Pilaralisib', 'SB505124', 'MCT1_6447', 'SYK_1543', 'PDD00017273', 'LFM-A13', 'TL-2-105', 'AZD6482', 'EPZ011989', 'Rigosertib', 'RAF_7242', 'AZD2014', 'SB590885', 'GDC-0879', 'Camptothecin', 'Y-39983', 'MIM1', 'MZ1', 'Motesanib', 'CB-839', 'Embelin', 'KIT_7208', 'KIT_6754', 'BMS-754807', 'FTI-277', 'Afatinib', 'BAM7', 'OSU-03012', 'FR-180204', 'YM201636', 'SYK_9721', 'Oxaliplatin', 'GNE7915', 'GSK269962A', 'NU7441', 'UNC-2025', 'AZD7762', 'ZM447439', 'Panobinostat', 'Piperlongumine', 'CA3', 'Serdemetan', 'Rociletinib', 'Paclitaxel', 'Nutlin-3a (-)', 'FEN1_3940', 'ML216', 'Tanespimycin', 'AZD5363', 'BCL6_7224', 'RGFP966', 'Vinorelbine', 'Olaparib', 'GW843682X', 'UNC0638', 'PI3Ka_4409', 'NSC-207895', 'WIKI4', 'Osimertinib', 'AZD8055', 'IPA-3', 'Flavopiridol', 'Obatoclax Mesylate', 'BAY-87-2243', 'TANK_1366', 'Brigatinib', 'Topotecan', 'Pyridostatin', 'AZD7969', 'NPK76-II-72-1', 'Daporinad', 'Linsitinib', 'AS601245', 'A-83-01', 'ERK_5051', 'AZD1775'}
    print(a-b)

#find_unqiue_values()