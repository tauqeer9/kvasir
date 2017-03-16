import pandas as pd
import re
from settings import *

def all_groups(groups_file):
    allsp = ["Thermus_thermophilus_HB8","Mycobacterium_vaccae_CIP_105934","Corynebacterium_variabile_DSM_44702","Corynebacterium_flavescens_Mu128","Corynebacterium_casei_UCMA_3821","Corynebacterium_casei_JB4","Corynebacterium_stationis_CRBM6","Corynebacterium_ammoniagenes_ws2211","Propionibacterium_acidipropinicii_LSPAc1","Propionibacterium_thoenii_LSPTH1","Propionibacterium_freudenreichii_subsp_shermanii_CIRM_BIA1","Luteococcus_japonicus_LSP_Lj1","Brevibacterium_linens_ATCC_9172","Brevibacterium_iodinum_ATCC_49514","Brevibacterium_casei_S18","Brevibacterium_casei_CIP_102111","Brevibacterium_antiquum_CNRZ918","Brevibacterium_linens_341_13","Brevibacterium_linens_JB5","Brevibacterium_linens_BL2","Brevibacterium_linens_900_6","Brevibacterium_linens_908_7","Brevibacterium_linens_947_7","Brevibacterium_linens_862_7","Brevibacterium_linens_962_8","Brevibacterium_linens_876_7","Brevibacterium_linens_738_8","Rothia_mucilaginosa_M1710","Kocuria_varians_Mu208","Kocuria_carniphila_CRBM38","Weissella_cibaria_3386","Citrococcus_sp__ws2216","Pediococcus_parvulus_CIRM750","Micrococcus_luteus_Mu201","Glutamicibacter_sp__BW78","Glutamicibacter_sp__BW80","Glutamicibacter_bergerei_BW77","Glutamicibacter_arilaitensis_JB182","Glutamicibacter_arilaitensis_Re117","Glutamicibacter_arilaitensis_GMPA29","Glutamicibacter_arilaitensis_Ca106","Glutamicibacter_arilaitensis_3M03","Leucobacter_komagatae_1L36","Leucobacter_sp__ER15_166_BHI15","Agrococcus_casei_LMG22410","Microbacterium_oxydans_PCA1","Microbacterium_gubbeenense_DSM_15944","Microbacterium_sp__JB110","Corynebacterium_variabile","Brachybacterium_alimentarium_CNRZ925","Brachybacterium_alimentarium_862_8","Brachybacterium_alimentarium_738_10","Brachybacterium_alimentarium_341_9","Brachybacterium_alimentarium_900_8","Brachybacterium_alimentarium_908_11","Brachybacterium_alimentarium_947_11","Brachybacterium_alimentarium_JB7","Brachybacterium_alimentarium_962_10","Brachybacterium_alimentarium_876_9","Ornithinibacillus_bavariensis_CIP_109287","Exiguobacterium_sibiricum_NL255","Exiguobacterium_acetylicum_180","Bacillus_pumilus_M21","Bacillus_altitudinis_263","Jeotgalicoccus_psychrophilus_CRBMD21","Macrococcus_caseolyticus_ATCC_13458","Staphylococcus_fleuretti_CIP106114","Staphylococcus_vitulinus_Ma1","Staphylococcus_lentus_Ca2","Staphylococcus_xylosus","Staphylococcus_equorum_BC9","Staphylococcus_equorum_BC15","Staphylococcus_caprae_DSM_20608","Staphylococcus_warneri_1445","Enterococcus_malodoratus_FAM208_55","Enterococcus_saccharominimus_M17_423","Enterococcus_durans_LMG10746","Enterococcus_hirae_SB10","Vagococcus_fluvialis_bH819","Vagococcus_lutrae_FAM208","Facklamia_tabacinasalis_FAM208_56","Leuconostoc_mesenteroides_CNRZ1283","Leuconostoc_citreum_MSE2","Leuconostoc_pseudomesenteroides_MSE7","Lactococcus_garvieae_N201","Lactococcus_plantarum_NCDO_1869","Lactococcus_raffinolactis_NCDO617","Streptococcus_macedonicus_679","Streptococcus_infantarius_11FA","Streptococcus_salivarius_CJ181","Streptococcus_infantarius_subsp__infantarius_3AG","Bavariicoccus_seileri_ws4188","Alkalibacterium_kapii_FAM208_38","Carnobacterium_maltaromaticum_38b","Lactobacillus_casei_BD_II","Lactobacillus_casei_ATCC_334","Lactobacillus_crustorum_FH4","Lactobacillus_brevis_ATCC_367","Lactobacillus_brevis_KB290","Brochothrix_thermosphacta_cH814","Listeria_fleischmannii_subsp_fleischmannii_LU2006_1","Listeria_monocytogenes_str__Scott_A","Listeria_monocytogenes_serotype_4bV_str__LS542","Bacillus_galactosidilyticus_CIP_108417","Bacillus_fordii_CIP_108821","Brevibacillus_parabrevis_CIP_110335","Paenibacillus_sp__3M17","Paenibacillus_lactis_CIP_108827","Brevundimonas_diminuta_3F5N","Stenotrophomonas_rhizophila_PCA13","Stenotrophomonas_indologenes_PCAi2_2","Stenotrophomonas_maltophilia_Pi1","Comamonas_testosteroni_NL2512","Delftia_acidovorans_PCA12","Advenella_kashmirensis_3T5F","Weissella_cibaria_3385","Alcaligenes_faecalis_2L10","Alcaligenes_sp__2L29","Psychrobacter_sp_JB193","Psychrobacter_namhaensis_1439","Psychrobacter_immobilis_PG1","Psychrobacter_aquimaris_ER15_174_BHI7","Psychrobacter_celer_91","Psychrobacter_faecalis_H5","Acinetobacter_johnsonii_3M05","Acinetobacter_genospecies_3_PCAiE610","Pseudomonas_fluorescens_PCAiD62","Pseudomonas_pseudojaponica_PCAi6_5","Pseudomonas_lundensis_PCAiD2_2","Pseudomonas_psychrophila_1E44","Pseudomonas_fragi_1E26","Halomonas_venusta_3D7M","Halomonas_venusta_3A7M","Halomonas_venusta_3F2F","Halomonas_sp__1M45","Halomonas_sp_JB37","Pseudoalteromonas_sp_JB197","Vibrio_litoralis_B4","Vibrio_casei_JB196","Vibrio_casei_ws4539","Morganella_morganii_subsp__siboni_3A5A","Morganella_psychrotolerans_925","Providencia_heimbachae_GR4","Providencia_alcalifaciens_GM3","Providencia_rettgeri_947","Proteus_vulgaris_1M25","Proteus_hauseri_1M10","Pantoea_agglomerans_PCAiQ63","Klebsiella_oxytoca_Pi20","Citrobacter_freundii_Pi15","Enterobacter_amnigenus_CV9","Kluyvera_intermedia_TL336A","Raoultella_planticola_3M45","Raoultella_ornithinolytica_TL332","Serratia_marescens_448","Serratia_rubidaea_TA_26","Serratia_proteamaculans_1C2F","Sphingobacterium_sp_JB170","Sphingobacterium_faecium_PCAiF2_5","Chryseobacterium_bovis_Pi18","Chryseobacterium_shigense_PCAiB2_3","Chryseobacterium_joostei_PCAiD6_3","Chryseobacterium_vrystaatense_PCAIF2_7","Chryseobacterium_ginsengisoli_M17",]
    name_dict = {re.sub(r"[. \-]+(?=\w)", "_", re.sub(r"\(.+?\)","",x)) for x in MONGODB["genes"].distinct("species")}

    df = pd.read_csv(groups_file)
