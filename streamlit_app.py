import streamlit as st
import random

# 設定頁面寬度
st.set_page_config(layout="wide")

# 模擬科室筆記
departments = ["入院紀錄【臆斷】", "出院病摘【出院診斷】", "手術紀錄【術後診斷】", "病程紀錄【PAP之Problem】", "最近一次weekly summary diagnosis", 
                "入院紀錄【主訴、病史、醫療需求與治療計畫】", "病程紀錄類(progress note)", "病程紀錄類(on service note)",
                "病程紀錄類(off service note)", "病程紀錄類(free note)", "手術紀錄【手術日期、Operative Method】",
                "會診單【醫師訪視時間、會診科部、診斷、建議】", "最近一次weekly summary Brief Summary of this week",
                "醫師原本撰寫的diagnosis", "醫師原本撰寫的brief summary of this week"]

department_notes = {
"入院紀錄【臆斷】": """PED: # B-lineage acute lymphoblastic leukemia, DNA index = 1, fusion genes negative, CNS1 status, NUDT15 *1/*1, provisional SR 
- status post TPOG 2021 ALL induction I(D1=2022/4/21), Day15 BM MRD=0%
- status post TPOG 2021 ALL induction II-A(D1=2022/5/18), post-induction BM MRD 0%
- status post TPOG 2021 ALL consolidation week 7 (W7D1=2022/8/8)
- status post TPOG 2021 ALL reinduction week 1 (D1=2022/09/09)
- status post TPOG 2021 ALL reinduction week 7 (D1=2022/11/09)""",
"出院病摘【出院診斷】": """""", 
"手術紀錄【術後診斷】": """PAOD, left lower extremity, Fontaine stage IV""", 
"病程紀錄【PAP之Problem】": """""", 
"最近一次weekly summary diagnosis": """[Active]
- Coronary arterial disease 3 vessel disease

[Underlying]
- Left below knee peripheral arterial occlusive disease and left DM foot s/p amputation left 1st/2nd toe
- Chronic left foot ulcer 0.6cm
- Hypertension under medication
- Type 2 Diabetes mellitus under OHA and insulin
- Chronic kidney disease""", 
"入院紀錄【主訴、病史、醫療需求與治療計畫】": """[主訴]
SURG: Informant:patient and past medical history
Intermittent chest tightness since 2021/12
[病史]
SURG: [Present illness]

This is a 61-year-old patient with underlying disease of 

- Coronary arterial disease, 3 vessel disease
- Left below knee peripheral arterial occlusive disease and left DM foot, s/p amputation left 1st/2nd toe
- Chronic left foot ulcer, 0.6cm
- Hypertension, under medication
- Type 2 Diabetes mellitus, under OHA and insulin
- Chronic kidney disease

This patient was regularly followed up at 雙和 Hospital for diabetes mellitus and hypertension for about 20 years. Left foot gangrene was found about 2 years ago. DM foot and PAOD was then diagnosed and left 1st/2nd toe amputation was performed at the same year. 

He developed intermittent chest pain since about 2021/12, and the pain would relieve spontaneously after resting. He denied exersional dypnea, claudication, palpitation and could still tolerate gentle exercise. He went to 北護 Dr. Tsai's OPD on 2022/01/14 for help. Vascular duplex on 2022/01/26 reported diffuse mild atherosclerosis, left below knee ATA no flow, PTA decreased blood flow. Compatiable with left below knee PAOD. Dipyridamole stress test on 2022/04/01 showed mixed ischemia with non-transmural scar at basal inferoseptal, apical lateral, mid to basal inferolateral, and mid to basal inferior walls. Catheterization was then arranged. 

He was admitted to CV ward on 2022/05/02. Coronary angiography on 2022/05/03 reported Coronary artery disease, 3-vessel-disease (LAD: ostial stenosis 70%, LCX: distal stenosis 90%, RCA: distal stenosis 90% and PDA stenosis 70%). After discharge, he was referred to CVS Dr. Chen's OPD for CABG evaluation on 2022/05/06. 

This time, he was admitted for CABG.

Family History: Mother and father: DM, HTN, CAD(-), AMI(-), CVA(-)
Medication Allergy:No 病人自述 2022/06/15
Medication ADR:unknown
Allergy to Medical Device and Materials:No 病人自述 2022/06/15
Current Medication:
台大醫院:160 Diovan FC 160 mg/tab 0.5 tab QD PO 28 days
Herbesser 30 mg/tab 1 tab QD PO 28 days
Bokey EM cap 100 mg/cap 1 cap QD PO 28 days
Betame Eye Drops 0.1% 5 mL/btl 1 gtt QID OD 3 days
Fluitran 2 mg/tab 0.5 tab QDPC PO 28 days
Pletaal 100 mg/tab 0.5 tab QDAC30 PO 28 days
Methycobal 500 mcg/cap 1 cap BID PO 28 days
警 Ryzodeg FlexTouch 300 U/3 mL /pen 20 U BID SC 28 days
Trajenta F.C. 5 mg/tab 1 tab QD PO 28 days
Other: denied
中草藥: denied
保健食品: denied

Past Medical History: as above
Hospitalization:入院日期:2022_05_02 出院日期:2022_05_04 診斷:Coronary arterial disease
Past Surgical History: Left below knee peripheral arterial occlusive disease and left DM foot, s/p amputation left 1st/2nd toe
Travel History: denied
[醫療需求與治療計畫]
SURG: S
Intermittent chest tightness since 2021/12

O
[Lab]
Hb 14.7/PLT 236
PT 10.8/INR 1.0/PTT 30.8
UN 37/Cre 1.8
HbA1C 6.4

A
- Coronary arterial disease, 3 vessel disease

P
1. Arrange CT
2. Arrange carotid echo and cardiac echo
3. Arrange PFT
4. Pre CABG preparation


Treatment Goal: Complete CABG without major complication""", 
"病程紀錄類(progress note)": """""", 
"病程紀錄類(on service note)": """""",
"病程紀錄類(off service note)": """""", 
"病程紀錄類(free note)": """2022-06-24
2022-06-24 09:25:00
2022-06-24
VS Note/nCAD 3VD previous NSTEMI. s/p OPCAB (LAD OM2 PLA PDA)
CKD Cre 1.8
PAOD bilateral leg below knee lesion left ATA monophasic flow

2022/06/24 08:34 T:36.6 P:84 R:18
2022/06/24 08:34 BP:108/67
2022/06/24 10:09 Pain score:0

2022/06/24 06:51 體重:76.9kg
2022/06/23 07:01 體重:76kg
2022/06/22 06:45 體重:76.7kg
2022/06/20 01:00 體重:78.6kg

2022/06/23 CRE:1.4mg/dL
2022/06/23 hsCRP:6.20mg/dL
2022/06/23 HB:11.4g/dL
2022/06/23 PLT:211k/μL
Triflow 3 balls
Oral intake ok

bokey MgO Lasix 0.5 tab QD Trajenta for DM Concor 0.5 tab QD
Pletaal 0.5 tab BID for PAOD
Add Glyximib for sugar control
Arrange left leg PAOD angiography on 06/25 W6
Progress/weekly/n61M

[Today]
Leg pain stable
fair spirit

[Active]
# Coronary arterial disease 3-vessel disease with previous NSTEMI status post OPCAB on 2022/06/18
# Left below knee peripheral arterial occlusive disease

[Underlying]
# Left diabetic foot syndrome status post amputation of left 1st/2nd toe
# Chronic left foot ulcer 0.6cm
# Hypertension under medication
# Type 2 Diabetes mellitus under OHA and insulin
# Chronic kidney disease

[Course]
2021/12 intermittent chest pain

0401 Stress test: mixed ischemia with multiple 
         non-transmural scars
0503 CAG: CAD 3VD LAD ostial stenosis 70% LCX distal 
     stenosis 90% RCA distal stenosis 90% and PDA 
     stenosis 70%
0616 Echo: EF 75.9 No RWMA imaired LV relaxation
0618 OPCAB

 The patient was admitted due to CAD and he underwent OPCAB on 2022/06/18. He was transferred to 5CVI for close surveillance after the operation. 

 The patient underwent extubation uneventfully on 2022/06/18. In a stable condition the patient was transferred to general ward on 2022/06/21. Rehabilitation program was then consulted. PAOD angiography was scheduled on 2022/06/25.

[CV]
Bokey 1# QD
Concor 0.625mg QD

[Renal]
Lasix 0.5# QD

[Meta]
Glyxambi 1# QD
Ryzodeg 16U BID

[P]
. monitor blood sugar 
. Rehabilitation
. 6/25 PAOD angioplasty
VS Comment
I agree with the assessment of the resident.
共同照護紀錄/n[Active]
# Coronary arterial disease 3-vessel disease with previous NSTEMI status post OPCAB on 2022/06/18
# Left below knee peripheral arterial occlusive disease

[Underlying]
# Left diabetic foot syndrome status post amputation of left 1st/2nd toe
# Chronic left foot ulcer 0.6cm
# Hypertension under medication
# Type 2 Diabetes mellitus under OHA and insulin
# Chronic kidney disease

[Plan]
1. Encourage rehabilitation
2. control blood sugar
3. PAOD angiography tomorrow
VS Comment
I agree with the assessment of the resident.
2022-06-25
VS Note/nCAD 3VD previous NSTEMI. s/p OPCAB (LAD OM2 PLA PDA)
CKD Cre 1.8
PAOD bilateral leg below knee lesion left ATA CTO s/p PTA

2022/06/25 20:55 T:36.6 P:73 R:18
2022/06/25 20:55 BP:106/69
2022/06/25 17:09 Pain score:0

2022/06/25 07:06 體重:77.5kg
2022/06/24 06:51 體重:76.9kg
2022/06/23 07:01 體重:76kg
2022/06/22 06:45 體重:76.7kg
2022/06/20 01:00 體重:78.6kg

2022/06/23 CRE:1.4mg/dL
2022/06/23 hsCRP:6.20mg/dL
2022/06/23 HB:11.4g/dL
2022/06/23 PLT:211k/μL
Triflow 3 balls
Oral intake ok

bokey MgO Lasix 0.5 tab QD Trajenta for DM Concor 0.5 tab QD
Pletaal 0.5 tab BID for PAOD
Glyximib for sugar control
Keep PGE1 for one day
F/U Lab and CXR on 6/27 W1
2022-06-26
VS Note/nCAD 3VD previous NSTEMI. s/p OPCAB (LAD OM2 PLA PDA)
CKD Cre 1.8
PAOD bilateral leg below knee lesion left ATA CTO s/p PTA

2022/06/26 09:05 T:36.0 P:76 R:18
2022/06/26 09:05 BP:110/68

2022/06/26 06:58 體重:77.2kg
2022/06/25 07:06 體重:77.5kg
2022/06/24 06:51 體重:76.9kg
2022/06/23 07:01 體重:76kg
2022/06/22 06:45 體重:76.7kg
2022/06/20 01:00 體重:78.6kg

2022/06/23 CRE:1.4mg/dL
2022/06/23 hsCRP:6.20mg/dL
2022/06/23 HB:11.4g/dL
2022/06/23 PLT:211k/μL
Triflow 3 balls
Oral intake ok

bokey MgO Lasix 0.5 tab QD Trajenta for DM Concor 0.5 tab QD
Pletaal 0.5 tab BID for PAOD
Glyximib for sugar control
F/U Lab and CXR on 6/27 W1
2022-06-27
VS Note/nCAD 3VD previous NSTEMI. s/p OPCAB (LAD OM2 PLA PDA)
CKD Cre 1.8
PAOD bilateral leg below knee lesion left ATA CTO s/p PTA

2022/06/27 05:39 T:36.3 P:75 R:18
2022/06/27 05:39 BP:101/60
2022/06/27 01:16 Pain score:0

2022/06/27 07:03 體重:76.9kg
2022/06/26 06:58 體重:77.2kg
2022/06/25 07:06 體重:77.5kg
2022/06/24 06:51 體重:76.9kg
2022/06/23 07:01 體重:76kg
2022/06/22 06:45 體重:76.7kg
2022/06/20 01:00 體重:78.6kg

2022/06/27 CRE:1.6mg/dL
2022/06/27 hsCRP:2.67mg/dL
2022/06/27 HB:10.8g/dL
2022/06/27 PLT:308k/μL
Triflow 3 balls
Oral intake ok

bokey MgO Lasix 0.5 tab QD Trajenta for DM Concor 0.5 tab QD
Pletaal 0.5 tab BID for PAOD
Glyximib for sugar control
F/U Lab and CXR on 06/30 W4
Progress/n61M

[Today]
Complain back pain -> encourage more exercise less lying bed
AKI(Cre 1.3->1.4->1.6) -> encourage more water intake(originally about 500-800ml per day)

[Active]
# Coronary arterial disease 3-vessel disease with previous NSTEMI status post OPCAB on 2022/06/18
# Left below knee peripheral arterial occlusive disease status post PTA of left P3 to ATA on 2022/06/25

[Underlying]
# Left diabetic foot syndrome status post amputation of left 1st/2nd toe
# Chronic left foot ulcer 0.6cm
# Hypertension under medication
# Type 2 Diabetes mellitus under OHA and insulin
# Chronic kidney disease


[CV]
Bokey 1# QD
Concor 0.625mg QD
Pleetal 0.5# BID

[Renal]
Lasix 0.5# QD

[Meta]
Glyxambi 1# QD
Ryzodeg 16U BID

[P]
. monitor blood sugar 
. Rehabilitation
. Encourage more water intake
VS Comment
Water should be control ~1500/days
2022-06-28
VS Note/nCAD 3VD previous NSTEMI. s/p OPCAB (LAD OM2 PLA PDA)
CKD Cre 1.8
PAOD bilateral leg below knee lesion left ATA CTO s/p PTA

2022/06/28 08:58 T:37.1 P:80 R:18
2022/06/28 08:58 BP:109/68
2022/06/27 17:11 Pain score:0

2022/06/28 06:38 體重:76.4kg
2022/06/27 07:03 體重:76.9kg
2022/06/26 06:58 體重:77.2kg
2022/06/25 07:06 體重:77.5kg
2022/06/24 06:51 體重:76.9kg
2022/06/23 07:01 體重:76kg
2022/06/22 06:45 體重:76.7kg
2022/06/20 01:00 體重:78.6kg

2022/06/27 CRE:1.6mg/dL
2022/06/27 hsCRP:2.67mg/dL
2022/06/27 HB:10.8g/dL
2022/06/27 PLT:308k/μL
Triflow 3 balls
Oral intake ok

bokey MgO Lasix 0.5 tab QD Trajenta for DM Concor 0.5 tab QD
Pletaal 0.5 tab BID for PAOD
Glyximib for sugar control
F/U Lab and CXR on 06/30 W4
Left foot wound healing gradually
Progress/n61M

[Today]
Leg pain improve could tolerate gentle exercise
Encourage more water intake

[Active]
# Coronary arterial disease 3-vessel disease with previous NSTEMI status post OPCAB on 2022/06/18
# Left below knee peripheral arterial occlusive disease status post PTA of left P3 to ATA on 2022/06/25

[Underlying]
# Left diabetic foot syndrome status post amputation of left 1st/2nd toe
# Chronic left foot ulcer 0.6cm
# Hypertension under medication
# Type 2 Diabetes mellitus under OHA and insulin
# Chronic kidney disease


[CV]
Bokey 1# QD
Concor 0.625mg QD
Pleetal 0.5# BID

[Renal]
Lasix 0.5# QD

[Meta]
Glyxambi 1# QD
Ryzodeg 16U BID

[P]
. monitor blood sugar f/u lab and CXR W4
. Rehabilitation
. Encourage more water intake to 1500ml
2022-06-29
Progress/n61M

[Today]
improve leg pain could slowly go upstairs and exercise
Good spirit

[Active]
# Coronary arterial disease 3-vessel disease with previous NSTEMI status post OPCAB on 2022/06/18
# Left below knee peripheral arterial occlusive disease status post PTA of left P3 to ATA on 2022/06/25

[Underlying]
# Left diabetic foot syndrome status post amputation of left 1st/2nd toe
# Chronic left foot ulcer 0.6cm
# Hypertension under medication
# Type 2 Diabetes mellitus under OHA and insulin
# Chronic kidney disease


[CV]
Bokey 1# QD
Concor 0.625mg QD
Pleetal 0.5# BID

[Renal]
Lasix 0.5# QD

[Meta]
Glyxambi 1# QD
Ryzodeg 16U BID

[P]
. monitor blood sugar f/u lab and CXR W4
. Rehabilitation
. Encourage more water intake to 1500ml
VS Comment
I agree with the assessment of the resident.
VS Note/nCAD 3VD previous NSTEMI. s/p OPCAB (LAD OM2 PLA PDA)
CKD Cre 1.8
PAOD bilateral leg below knee lesion left ATA CTO s/p PTA

2022/06/29 14:32 T:36.1 P:75 R:18
2022/06/29 14:32 BP:114/70
2022/06/29 10:13 Pain score:0

2022/06/29 08:07 體重:75.3kg
2022/06/28 06:38 體重:76.4kg
2022/06/27 07:03 體重:76.9kg
2022/06/26 06:58 體重:77.2kg
2022/06/25 07:06 體重:77.5kg
2022/06/24 06:51 體重:76.9kg
2022/06/23 07:01 體重:76kg
2022/06/22 06:45 體重:76.7kg
2022/06/20 01:00 體重:78.6kg

2022/06/27 CRE:1.6mg/dL
2022/06/27 hsCRP:2.67mg/dL
2022/06/27 HB:10.8g/dL
2022/06/27 PLT:308k/μL
Triflow 3 balls
Oral intake ok

bokey MgO Lasix 0.5 tab QD Trajenta for DM Concor 0.5 tab QD
Pletaal 0.5 tab BID for PAOD
Glyximib for sugar control
F/U Lab and CXR on 06/30 W4
Left foot wound healing gradually
2022-06-30
VS Note/nCAD 3VD previous NSTEMI. s/p OPCAB (LAD OM2 PLA PDA)
CKD Cre 1.8
PAOD bilateral leg below knee lesion left ATA CTO s/p PTA

2022/06/30 08:28 T:36.3 P:83 R:18
2022/06/30 08:28 BP:107/68

2022/06/30 08:08 體重:75.4kg
2022/06/29 08:07 體重:75.3kg
2022/06/28 06:38 體重:76.4kg
2022/06/27 07:03 體重:76.9kg
2022/06/26 06:58 體重:77.2kg
2022/06/25 07:06 體重:77.5kg
2022/06/24 06:51 體重:76.9kg
2022/06/23 07:01 體重:76kg
2022/06/22 06:45 體重:76.7kg
2022/06/20 01:00 體重:78.6kg

2022/06/27 CRE:1.6mg/dL
2022/06/27 hsCRP:2.67mg/dL
2022/06/27 HB:10.8g/dL
2022/06/27 PLT:308k/μL
Triflow 3 balls
Oral intake ok

bokey MgO Lasix 0.5 tab QD Trajenta for DM Concor 0.5 tab QD
Pletaal 0.5 tab BID for PAOD
Glyximib for sugar control
F/U Lab and CXR on 06/30 W4
Left foot wound healing gradually
VS Comment
I agree with the assessment of the resident.
Progress/off service/n61M

[Today]
Good spirit
fair urine output no leg edema


[Active]
# Coronary arterial disease 3-vessel disease with previous NSTEMI status post OPCAB on 2022/06/18
# Left below knee peripheral arterial occlusive disease status post PTA of left P3 to ATA on 2022/06/25
# Acute on chronic kidney disease etiology unknown

[Underlying]
# Left diabetic foot syndrome status post amputation of left 1st/2nd toe
# Chronic left foot ulcer 0.6cm
# Hypertension under medication
# Type 2 Diabetes mellitus under OHA and insulin

[Course]
 After admission the patient underwent OPCAB on 2022/06/18. He was transferred to 5CVI for close surveillance after the operation. 

 The patient underwent extubation uneventfully on 2022/06/18. In a stable condition the patient was transferred to general ward on 2022/06/21. Rehabilitation program was then consulted. PAOD angiography was performed smoothly on 2022/06/25. After the operation leg pain improved and the patient could tolerate walking upstairs and gentle exercise.

 Followed lab data revealed elevated serum creatinine. More water intake was encouraged. He denied decreased urine output pitting edema. He may be dicharged next week and keep OPD follow-up.


[CV]
Bokey 1# QD
Concor 0.625mg QD
Pleetal 0.5# BID

[Renal]
Lasix 0.5# QD

[Meta]
Glyxambi 1# QD
Ryzodeg 16U BID

[P]
. Rehabilitation
. Encourage more water intake to 1500ml Consider hydration?
. MBD next week
VS Comment
I agree with the assessment of the resident.
2022-07-01
Progress/On service/n[Active]
# Coronary arterial disease 3-vessel disease with previous NSTEMI status post OPCAB on 2022/06/18
# Left below knee peripheral arterial occlusive disease status post PTA of left P3 to ATA on 2022/06/25
# Acute on chronic kidney disease etiology unknown

[Underlying]
# Left diabetic foot syndrome status post amputation of left 1st/2nd toe
# Chronic left foot ulcer 0.6cm
# Hypertension under medication
# Type 2 Diabetes mellitus under Glyxambi and Ryzodeg

[PE]

[Lab]
Anemia
Elevated Creatinine BUN level 
[Pain]
Utraphen 1# QIDPRN mostly not requiring any
[Medication]
Bokey 1# QD
Concor 0.625mg QD
Pleetal 0.5# BID
Lasix 0.5# QD
Concor 1# QD

[Plan]
. Rehabilitation
. Encourage more water intake to 1500ml Consider hydration?
. MBD next week
VS Comment
No hydration keep CKD care
VS Note/nCAD 3VD previous NSTEMI. s/p OPCAB (LAD OM2 PLA PDA)
CKD Cre 1.8
PAOD bilateral leg below knee lesion left ATA CTO s/p PTA

2022/07/01 08:07 T:36.1 P:83 R:18
2022/07/01 08:07 BP:102/65
2022/07/01 09:19 Pain score:0

2022/07/01 07:09 體重:75.3kg
2022/06/30 08:08 體重:75.4kg
2022/06/29 08:07 體重:75.3kg
2022/06/28 06:38 體重:76.4kg
2022/06/27 07:03 體重:76.9kg
2022/06/26 06:58 體重:77.2kg
2022/06/25 07:06 體重:77.5kg
2022/06/24 06:51 體重:76.9kg
2022/06/23 07:01 體重:76kg
2022/06/22 06:45 體重:76.7kg
2022/06/20 01:00 體重:78.6kg

2022/06/27 CRE:1.6mg/dL
2022/06/27 hsCRP:2.67mg/dL
2022/06/27 HB:10.8g/dL
2022/06/27 PLT:308k/μL
Triflow 3 balls
Oral intake ok
CXR: clear

bokey MgO Lasix 0.5 tab QD Trajenta for DM Concor 0.5 tab QD
Pletaal 0.5 tab BID for PAOD
Glyximib for sugar control
Left foot wound healing gradually
Remove half stitches today and all stitches on 7/4 W1
共同照護紀錄/n[Active]
# Coronary arterial disease 3-vessel disease with previous NSTEMI status post OPCAB on 2022/06/18
# Left below knee peripheral arterial occlusive disease status post PTA of left P3 to ATA on 2022/06/25
# Acute on chronic kidney disease etiology to be determined

[Underlying]
# Left diabetic foot syndrome status post amputation of left 1st/2nd toe
# Chronic left foot ulcer 0.6cm
# Hypertension under medication
# Type 2 Diabetes mellitus under Glyxambi and Ryzodeg

[Plan]
1. Keep current rehabilitation plan QW12345
2. Remove all stitches on 7/4 
3. Monitor clinical condition closely

VS Comment
I agree with the assessment of the resident.""", 
"手術紀錄【手術日期、Operative Method】": """2022-06-18 00:00:00
2022-06-18
OPCAB
2022-06-25
PTA of left P3 to ATA """,
"會診單【醫師訪視時間、會診科部、診斷、建議】": """2022-06-21 00:00:00
2022-06-21
PMR
DIAGNOSIS: # Coronary arterial disease, 3-vessel disease, with previous NSTEMI, status post OPCAB on 2022/6/18
SUGGESTION: 1.Keep intensive care and control CV risk factor for secondary prevention
2.We will arrange physical therapy, including 
物理治療評估, therapeutic exercise, cardiorespiratory exercise training
3.Encourage increase of physical activity level or entry of outpatient cardiac rehabilitation program after discharge.
-此病人有門診心臟復健適應症，若主治醫師同意，請於出院兩周後約回復健部陳思遠/陳冠誠/莊泓叡醫師之門診, 若預約門診有困難請聯絡照會醫師協助安排

[Special notice]
1. Type of exercise:
a.ICU stay: Routine ICU activities, sitting warm-ups, bedside commode as tolerated.
b.General ward stay: Out of bed as tolerated, sitting warm-ups, standing warm-ups, walking in-room, walking 5-10 min in hall, walking up one flight of stairs, etc
2. Exercise intensity: 
a.To tolerance if asymptomatic
b.RPE ≦ 13 on a scale of 6–20
c.HRrest + 30 bpm and HR ≦ 120 bpm as the arbitrary upper limit
3. Exercise duration:
a.Begin with intermittent bouts lasting 3 to 5 minutes as tolerated
b.Rest period may be a slower walk (or complete rest, at the patient’s discretion) that is shorter than the duration of the exercise bout. Attempt to achieve a 2:1 exercise/rest ratio
4. Stop exercise training if occurrence of the following adverse responses:
a.Diastolic blood pressure (DBP)≧110 mm Hg
b.Decrease in systolic blood pressure (SBP)≧10 mm Hg during exercise
c.Significant ventricular or atrial dysrhythmias with or without associated signs/symptoms
d.Second- or third-degree heart block
e.Signs/symptoms of exercise intolerance, including angina, marked dyspnea, and electrocardiogram (ECG) changes suggestive of ischemia
5.If the operation involved sternotomy, upper extremity resistance exercise should be avoided for 5 weeks after the surgery. 

[Rehabilitation Goals]
1.Limit the deleterious physiological and psychological effects of bed rest and CVD.
2.Improved lung hygienes and cardiopulmonary functions
3.Enable the patient to safely return to activities of daily living within limits imposed by his/her CVD. 
4.Encourage gradual increase of physical activity level or entry of outpatient cardiac rehabilitation program after discharge.

回覆醫師:R2黃薇臻(GSM:53659)/ VS陳冠誠(114521) 成本中心:13620""", 
"最近一次weekly summary Brief Summary of this week": """After admission evaluation for scheduled coronary artery bypass grafting was arranged. Vascular duplex showed moderate stenosis at right femoral artery left femoral artery and left popleteal artery. Carotid echo showed mild to moderate atherosclerosis in bilateral CCAs carotid bulbs and left ICA. Non-contrast CT showed no definite structural abnormalities. Cardiac echo reported preserved LV systolic function. Pulmonary function test showed adequated lung function. He would received scheduled CABG this weekend and may transferred to ICU for post-OP care.""",
"醫師原本撰寫的diagnosis": """""",
"醫師原本撰寫的brief summary of this week": """"""
}

# 中間欄整理的病歷資訊
diagnosis_text = """# Coronary arterial disease, 3 vessel disease, is being managed.
# Left below knee peripheral arterial occlusive disease and left DM foot, status post amputation of left 1st/2nd toe, are underlying conditions.
# A chronic left foot ulcer, measuring 0.6cm, is present.
# Hypertension is being controlled with medication.
# Type 2 Diabetes mellitus is being managed with oral hypoglycemic agents and insulin.
# Chronic kidney disease is a comorbid condition.
# The patient has peripheral arterial occlusive disease, left lower extremity, classified as Fontaine stage IV.
"""
summary_text = """This week, the patient underwent OPCAB on 06/18 and was transferred to the general ward on 06/21. PAOD angiography was performed on 06/25, which showed bilateral leg below knee lesion left ATA CTO, and PTA was done. The patient's leg pain improved, and he could tolerate walking upstairs and gentle exercise by 06/29. Laboratory data revealed elevated serum creatinine, and more water intake was encouraged. The patient denied decreased urine output and pitting edema. On 06/27, his creatinine level was 1.6mg/dL, and hsCRP was 2.67mg/dL. The patient's left foot wound was healing gradually, and half of the stitches were removed on 07/01, with the remaining stitches to be removed on 07/04. The patient's current medications include Bokey, Concor, Pletaal, Lasix, Glyxambi, and Ryzodeg. The plan is to continue rehabilitation, encourage more water intake to 1500ml, and consider hydration."""

# 側邊欄輸入
st.sidebar.title("工作區")

# 輸入員編
user_id = st.sidebar.text_input("請輸入您的員編")

# 選科室
dept_choice = st.sidebar.selectbox("請選擇科室", ["內科部", "外科部"])

# 選範例
example_choice = st.sidebar.selectbox("請選擇範例", ["範例1", "範例2", "範例3"])

# 主區域顯示
st.markdown(f"**員編**：{user_id} &nbsp;&nbsp; **科室**：{dept_choice}&nbsp;—&nbsp;{example_choice}", unsafe_allow_html=True)

# 左、中、右三欄
left_column, middle_column, right_column = st.columns([1.5, 2.5, 2])

# 左欄：科室筆記
with left_column:
    st.header("參考資料")
    for dept in departments:
        with st.expander(dept):
            st.text(department_notes[dept])

# 中間欄：整理後資訊
with middle_column:
    st.header("weekly summary")
    st.subheader("Diagnosis")
    st.text(diagnosis_text)
    st.subheader("Brief Summary of This Week")
    st.text(summary_text)

# 右欄：問卷調查
with right_column:
    st.header("問卷調查")
    st.markdown(
        """
        <style>
        /* 調整 radio 控件的問句字體大小 */
        div[data-testid="stRadio"] > label:first-child {
            font-size: 18px;  /* 問句大小 */
            font-weight: bold;
            margin-bottom: -5px;
            margin-top: -5px;  /* 上方空白清除 */
            padding-top: 0px; /* 內部 padding 清除 */
        }
        
        /* st.text_area 標題 */
        div[data-testid="stTextArea"] > label {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: -5px;
        }

        /* 調整 radio 選項文字大小 */
        div[data-testid="stRadio"] label[for^="radio"] {
            font-size: 18px;  /* 選項大小 */
        }
        
        /* 統一問句樣式 */
        .question-text {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        
        </style>
        """,
        unsafe_allow_html=True
    )

    ##### Diagnosis 問卷 #####
    with st.expander("Diagnosis 問卷"):
        #Q1
        st.write('<p class="question-text" style="margin-bottom:-30px;">1. 是否包含重要診斷？</p>', unsafe_allow_html=True)
        Q1 = st.radio(
            "",
            [
                "完全包含，資訊完整且清楚",
                "幾乎完整包含，資訊足夠理解診斷重點，可接受",
                "大部分包含，仍有少量缺失",
                "部分包含，但不足以理解全貌",
                "幾乎完全未包含（幾乎沒有提供相關診斷資訊）"
            ], key="Q1"
        )
        
        #Q2
        st.write('<p class="question-text" style="margin-bottom:-30px;">2. 如果有缺少診斷，請簡述缺少的內容：</p>', unsafe_allow_html=True)
        Q2 = st.text_area("", key="Q2_textarea")
        
        #Q3
        st.write('<p class="question-text" style="margin-bottom:-30px;">3. 正確性評估（請選最符合）</p>', unsafe_allow_html=True)
        Q3 = st.radio(
            "",
            [
                "無明顯錯誤",
                "僅有少量不影響理解的小錯",
                "有部分錯誤，但整體仍可參考",
                "多處錯誤，可信度低",
                "完全錯誤，有明顯事實性錯誤或誤導"
            ], key="Q3"
        )
        
        #Q4
        st.write('<p class="question-text" style="margin-bottom:-30px;">4. 長度評估（請選最符合）</p>', unsafe_allow_html=True)
        Q4 = st.radio(
            "",
            [
                "明顯太長，資訊過多冗贅",
                "稍微太長，但可以接受",
                "恰到好處",
                "稍微太短，有些內容缺失",
                "明顯太短，資訊不足"
            ], key="Q4"
        )
        
        #Q5
        st.write('<p class="question-text" style="margin-bottom:-30px;">5. 如果您覺得正確性或長度有問題，請簡述原因：</p>', unsafe_allow_html=True)
        Q5 = st.text_area("", key="Q5_textarea")
        
        #Q6
        st.write('<p class="question-text" style="margin-bottom:-30px;">6. 您對這段Diagnosis的整體滿意程度？</p>', unsafe_allow_html=True)
        Q6 = st.radio("", ["非常不滿意", "不滿意", "普通", "滿意", "非常滿意"], horizontal=True, key="Q6")

    ##### brief summary of this week 問卷 #####
    with st.expander("Brief Summary of this week 問卷"):        
        # Q1
        st.write('<p class="question-text">1. 本週摘要是否有需包含但未包含的資訊？（可複選）</p>', unsafe_allow_html=True)
        
        ### 勾選選項
        missing_info_options = [
            "病情變化",
            "重要處置、手術或檢查",
            "呼吸護理調整（如呼吸機模式、撤機試驗）",
            "藥物開始或停用（如抗生素、類固醇等）",
            "藥物治療方案變化（如調整劑量、更換藥物種類）",
            "臨床不良副作用及相關檢查（如肝腎功能異常、藥物過敏反應檢驗）",
            "合併症或突發狀況（如感染、出血、急性器官衰竭）",
            "目前狀態簡述（如意識狀態、生命徵象穩定度、飲食狀況）",
            "臨床決策和管理變化（如加強監測、改變治療計畫）",
            "實驗室檢查資料（如血液、尿液、培養結果等）",
            "轉診或轉院計畫（如安排專科轉診、轉至加護病房）"
        ]
        
        ### 用字典收集勾選結果
        Q7_dict = {}
        for option in missing_info_options:
            Q7_dict[option] = st.checkbox(option)
        Q7_selected = [k for k, v in Q7_dict.items() if v]
        
        #Q2
        st.write('<p class="question-text" style="margin-bottom:-30px;">2. 除了上述類別外，請簡述您發現缺少的資訊：</p>', unsafe_allow_html=True)
        Q8 = st.text_area("", key="Q8_textarea")
        
        #Q3
        st.write('<p class="question-text" style="margin-bottom:-30px;">3. 您所在科別是否偏重某部分資訊紀錄？請說明需求：</p>', unsafe_allow_html=True)
        Q9 = st.text_area("", key="Q9_textarea")
        
        #Q4
        st.write('<p class="question-text" style="margin-bottom:-30px;">4. 您對這段Brief Summary of this week的整體滿意程度？</p>', unsafe_allow_html=True)
        Q10 = st.radio("", ["非常不滿意", "不滿意", "普通", "滿意", "非常滿意"], horizontal=True, key="Q10")

    # 提交按鈕
    if st.button("提交問卷"):
        st.success("問卷已提交！")
        st.write("### Diagnosis 評估結果")
        st.write(f"1. 是否包含重要診斷：{Q1}")
        st.write(f"2. 缺少的診斷內容：{Q2}")
        st.write(f"3. 診斷正確性：{Q3}")
        st.write(f"4. 診斷長度：{Q4}")
        st.write(f"5. 診斷正確性以及長度的問題：{Q5}")
        st.write(f"6. diagnosis整滿意度：{Q6}")

        st.write("### Brief Summary 評估結果")
        st.write(f"7. 缺少資訊：{'、'.join(Q7_selected)}")
        st.write(f"8. 其他缺少資訊：{Q8}")
        st.write(f"9. 科別需求說明：{Q9}")
        st.write(f"10. brief summary整體滿意度：{Q10}")
