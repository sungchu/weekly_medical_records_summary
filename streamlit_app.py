import streamlit as st
import random
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
#os.environ["STREAMLIT_SERVER_RUNONSAVE"] = "false"
base_dir = os.path.dirname(__file__)

sa_json = st.secrets["google_service_account"]
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']  # 可以同時存取 Drive
creds = ServiceAccountCredentials.from_json_keyfile_dict(sa_json, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1wM-Q11flPuvorbjbmUcKLVbbSJKAegTxRvI_f-xiL9E").sheet1

# 設定頁面寬度
st.set_page_config(layout="wide")

# 側邊欄輸入
#st.sidebar.title("工作區")
#user_id = st.sidebar.text_input("請輸入您的員工編號")
#dept_choice = st.sidebar.selectbox("請選擇科部", ["內科部"])
#example_choice = st.sidebar.selectbox("請選擇範例", ["範例1", "範例2", "範例3"])

#department_file = {"內科部": "filtered_MED.jsonl"}
#df = pd.read_json(department_file[dept_choice], lines=True)

#example_to_idx = {"範例1": 0, "範例2": 1, "範例3": 2}
#idx = example_to_idx[example_choice]

# 在主頁面輸入員工編號
col1, col2, col3, col4 = st.columns([1, 1, 1, 5])
with col1:
    user_id = st.text_input("請輸入您的員工編號")

if not user_id:
    st.warning("請先輸入員工編號")
else:
    # 在主頁面選擇科部
    with col2:
        dept_choice = st.selectbox("請選擇科部", ["外科部"])

    # 根據科部讀取對應檔案
    department_file = {"外科部": "SURG_10input_output.jsonl"}
    df = pd.read_json(department_file[dept_choice], lines = True)    

    # 在主頁面選擇範例
    with col3:
        example_choice = st.selectbox("請選擇範例", ["範例1", "範例2", "範例3", "範例4", "範例5", "範例6", "範例7", "範例8", "範例9", "範例10"])

    # 範例對應索引
    example_to_idx = {"範例1": 0, "範例2": 1, "範例3": 2, "範例4": 3, "範例5": 4, "範例6": 5, "範例7": 6, "範例8": 7, "範例9": 8, "範例10": 9}
    idx = example_to_idx[example_choice]
    st.write(df.iloc[idx])
    st.write(type(df.iloc[idx]['DIAGNOSIS']))
    # 模擬科室筆記
    departments = [
        "醫師原本撰寫的diagnosis",
        "醫師原本撰寫的brief summary of this week",
        "入院紀錄【臆斷】",
        "出院病摘【出院診斷】",
        "手術紀錄【術後診斷】",
        "病程紀錄【PAP之Problem】",
        "最近一次weekly summary Diagnosis",
        "入院紀錄【主訴、病史、醫療需求與治療計畫】",
        "病程紀錄類(progress note)",
        "病程紀錄類(on service note)",
        "病程紀錄類(off service note)",
        "病程紀錄類(free note)",
        "手術紀錄【手術日期、Operative Method】",
        "會診單【醫師訪視時間、會診科部、診斷、建議】",
        "最近一次weekly summary Brief Summary of this week",
    ]

    department_notes = {
    "醫師原本撰寫的diagnosis": df.iloc[idx]['DIAGNOSIS'], 
    "醫師原本撰寫的brief summary of this week": df.iloc[idx]['BRIEFSUMMARY'], 
    "入院紀錄【臆斷】": df.iloc[idx]['DEPT_CONTENT'],
    "出院病摘【出院診斷】": df.iloc[idx]['CD'],
    "手術紀錄【術後診斷】": df.iloc[idx]['OPNOTEVALUETEXT_x'],
    "病程紀錄【PAP之Problem】": {"progress_note": df.iloc[idx]['progress_history'],
                            "on_service_note": df.iloc[idx]['onservice_history'],
                            "off_service_note": df.iloc[idx]['offservice_history']},
    "最近一次weekly summary Diagnosis": df.iloc[idx]['last_week_diagnosis'],
    "入院紀錄【主訴、病史、醫療需求與治療計畫】": {"主訴": df.iloc[idx]['CC_CONTENT'],
                                        "病史": df.iloc[idx]['PH_CONTENT'],
                                        "醫療需求與治療計畫": df.iloc[idx]['PT_CONTENT']},
    "病程紀錄類(progress note)": {"insert_datetime": df.iloc[idx]['PROGRESSNOTE_INSERTDATETIME'],
                                "subjective": df.iloc[idx]['PROGRESSNOTE_SUBJECTIVE'],
                                "objective": df.iloc[idx]['PROGRESSNOTE_OBJECTIVE'],
                                "yesterday_summary": df.iloc[idx]['PROGRESSNOTE_YESTERDAYSUMMARY'],
                                "bsibundle_reason": df.iloc[idx]['PROGRESSNOTE_BSIBUNDLE'],
                                "PAP": df.iloc[idx]['PROGRESSNOTE_PAP']}, 
    "病程紀錄類(on service note)": {"insert_datetime": df.iloc[idx]['ONSERVICENOTE_INSERTDATETIME'],
                                "diagnosis_and_history": df.iloc[idx]['ONSERVICENOTE_DIAGNOSISANDHISTORY'],
                                "physical_exam_and_assessment": df.iloc[idx]['ONSERVICENOTE_PHYSICALEXAMANDASSESSMENT'],
                                "current_medication": df.iloc[idx]['ONSERVICENOTE_CURRENTMEDICATION'],
                                "pap": df.iloc[idx]['ONSERVICENOTE_PAP']}, 
    "病程紀錄類(off service note)": {"insert_datetime": df.iloc[idx]['OFFSERVICENOTE_INSERTDATETIME'],
                                "diagnosis": df.iloc[idx]['OFFSERVICENOTE_DIAGNOSIS'],
                                "brief_summary": df.iloc[idx]['OFFSERVICENOTE_BRIEFSUMMARY'],
                                "current_medication": df.iloc[idx]['OFFSERVICENOTE_CURRENTMEDICATION'],
                                "pap": df.iloc[idx]['OFFSERVICENOTE_PAP']}, 
    "病程紀錄類(free note)": {"insert_datetime": df.iloc[idx]['BLANKNOTE_INSERTDATETIME'],
                            "note_content": df.iloc[idx]['NOTE_CONTENT']},
    "手術紀錄【手術日期、Operative Method】": {"operation_date": df.iloc[idx]['OPERATIONDATE'],
                                        "op_note_text": df.iloc[idx]['OPNOTEVALUETEXT_y']}, 
    "會診單【醫師訪視時間、會診科部、診斷、建議】": {"event_date": df.iloc[idx]['EVENTDATE'],
                                        "assessment_note": df.iloc[idx]['ASSESSMENTNOTE']}, 
    "最近一次weekly summary Brief Summary of this week": df.iloc[idx]['last_weekly_brief_summary'],}

    # 中間欄整理的病歷資訊
    diagnosis_text = df.iloc[idx]['LLM_DIAGNOSIS']
    summary_text = df.iloc[idx]['LLM_BRIEFSUMMARY']

    # 主區域顯示
    #st.markdown(f"**員編**：{user_id} &nbsp;&nbsp; **科室**：{dept_choice}&nbsp;—&nbsp;{example_choice}", unsafe_allow_html=True)

    # 左、中、右三欄
    left_column, middle_column, right_column = st.columns([2.5, 2.5, 2])

    # 左欄：科室筆記
    with left_column:
        st.header("參考資料")
        
        # 依序顯示各科室筆記
        for dept in departments:
            with st.expander(dept):
                content = department_notes.get(dept, "")
                
                if isinstance(content, dict):
                    # dictionary 內容整理成文字
                    display_text = ""
                    for key, value in content.items():
                        if value:  # 避免空值
                            # 這裡確保換行符號正確
                            display_text += f"【{key}】\n{value}\n\n"
                    # 用 text 顯示多行文字，最後加一個空格避免壓縮
                    st.text(display_text + " ")
                else:
                    if content:
                        st.text(content + " ")  # 加一個空格讓 text 框高度自動調整
        
        with st.expander("預測Diagnosis的prompt", expanded=False):
            st.text(department_notes.get("預測Diagnosis的prompt", """
            Given the following information from the current hospitalization:
            - The most recent weekly summary written during this admission.
            - The admission note for this admission.
            - All inter-ward discharge summaries (if any).
            - All operative records available up to the time of writing.
            - Progress notes, on-service notes, and off-service notes from the 7 days prior to the note-writing date.

            Generate a medically concise weekly inpatient summary.

            Requirements:
            - Present the summary in bullet point format, each starting with #.
            - Each bullet must be a short, self-contained clinical statement.
            - Focus only on: diagnosis, significant clinical events, procedures performed, response to treatment, and current condition.
            - Omit any statements that simply indicate 'no events', 'nil', or 'no changes'.
            - Do not use labels such as 'Main diagnosis' or 'Procedures performed'.
            - Keep the wording concise and factual."""))
            
        with st.expander("預測Brief summary of this week的prompt", expanded=False):
            st.text(department_notes.get("預測Brief summary of this week的prompt", """
            Given the following input data:
            - Weekly summary
            - Current admission note
            - Progress notes from the past up to 7 days (may be fewer)
            - All operative records up to the weekly note
            - All consultation notes up to the weekly note
            - The diagnosis summary predicted by the language model

            Generate a weekly inpatient summary written as a concise narrative paragraph.
            Focus ONLY on the events from THIS WEEK, not the entire hospitalization.
            Do not include admission history or events from previous weeks unless directly relevant to this week's status.

            Instructions:
            - Write the weekly summary as a short narrative paragraph (3-5 sentences).
            - Avoid date-by-date recounting; instead, summarize this week¡¦s clinical course in natural flow.
            - Clearly mention the date of each clinical event within the sentence using the MM/DD format (e.g., \"on 09/21\", \"by 09/23\").
            - Present the information in chronological order, combining daily clinical events into a readable, natural-flow paragraph.
            - Include key clinical events such as: changes in condition, procedures, treatments, labs, imaging, cultures, decision-making, and transfers.
            - Be concise, medically accurate, and avoid unnecessary repetition.
            - Do not expand into full discharge summaries or unrelated comorbidities.
            - If multiple events happen on the same day, combine them into the same sentence or paragraph segment.
            - If a date has no meaningful clinical event, omit it from the narrative.
            - Style should resemble a physician¡¦s weekly progress summary like examples below.

            Example output 1:
            After admission to intensive care unit, fluid supplementation, inhalation therapy, and symptomatic medications were initiated. FilmArray respiratory panel was positive for parainfluenza virus type 2; thus, antibiotics were not administered. The patient was kept NPO on 2025/04/29 due to respiratory distress, but feeding was resumed that night and was well tolerated. Subcostal retractions improved with HFNC support (17L/min, FiO 0.21), and he could tolerate room air without HFNC support since 2025/04/30. Under a relatively stable clinical condition, the patient was transferred to the general ward on 2025/05/01. After transferral to general ward, we kept routine bronchodilator, mucolytic agent and the usage of nebulizer. 

            Example output 2:
            This week, the patient kept receiving physical therapy. On 5/2, the lab data revealed no elevation on Ca2+, the TSH was still pending. The CXR revealed no obvious opacity. In light of suspected subclinical hypothyroidism, the amiodarone was switched to dronedarone. Next week, the lab data will be rechecked again to follow up previous hypercalemia or hypothyroidism. 

            Example output 3:
            After admission, we adjusted her medication into lamotrigine 100mg, abilify 5mg, fluoxetine 40mg and seroquel XR 50mg. The patient had close but tensed relationship with her mother, and her mother's anxiety triggers the patient's guilt as well. We suggested long-term personal and parent-child psychotherapy in the future. Currently, we'll close monitor her mood symptoms and adjust the medication accordingly.

            Only output the final narrative. Do not explain your reasoning."""))

    # 中間欄：整理後資訊
    with middle_column:
        st.header("weekly summary")
        st.subheader("Diagnosis")
        st.text(diagnosis_text)
        st.subheader("Brief Summary of This Week")
        st.text(summary_text)

    # 右欄：問卷調查
    with right_column:
        st.header("醫師評審")
        st.markdown(
            """
            <style>
            /* === Radio 問句樣式 === */
            div[data-testid="stRadio"] > label:first-child {
                font-size: 18px;      /* 問句大小 */
                font-weight: bold;
                margin-bottom: 10px;  /* 下方行距增加 */
                margin-top: -5px;     /* 上方空白清除 */
                padding-top: 0px;     /* 內部 padding 清除 */
            }

            /* === TextArea 標題樣式 === */
            div[data-testid="stTextArea"] > label {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: -4px;
            }

            /* === Radio 選項樣式 === */
            div[data-testid="stRadio"] label[for^="radio"] {
                font-size: 18px;      /* 選項文字大小 */
                line-height: 1.2;     /* 行距 */
                margin-bottom: -4px;  /* 減少選項間距 */
            }

            /* === Checkbox 選項樣式 === */
            div[data-testid="stCheckbox"] {
                margin-bottom: -4px;  /* 減少勾選框間距 */
            }

            div[data-testid="stCheckbox"] label {
                font-size: 16px;      /* 選項文字大小 */
                line-height: 1.2;     /* 行距 */
            }

            /* === 統一問句樣式 === */
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
        st.subheader("Diagnosis 問卷")
        #Q1
        st.write('<p class="question-text" style="margin-bottom:-30px;">1. 是否包含重要診斷？</p>', unsafe_allow_html=True)
        Q1 = st.radio(
            "Q1_label",  # 真實 label
            [
                "完整，資訊清楚",
                "幾乎完整，可理解診斷重點",
                "大部分包含，少量缺失",
                "部分包含，不足以理解全貌",
                "幾乎未包含"
            ], key="Q1", label_visibility="collapsed"
        )

        #Q2
        st.write('<p class="question-text" style="margin-bottom:-10px;">2. 如果有缺少診斷，請簡述缺少的內容：</p>', unsafe_allow_html=True)
        Q2 = st.text_area("Q2_label", key="Q2_textarea", label_visibility="collapsed")

        #Q3
        st.write('<p class="question-text" style="margin-bottom:-30px;">3. 正確性評估（請選最符合）</p>', unsafe_allow_html=True)
        Q3 = st.radio(
            "Q3_label",
            [
                "無明顯錯誤",
                "小錯，不影響理解",
                "部分錯誤，仍可參考",
                "多處錯誤，可信度低",
                "完全錯誤或誤導"
            ], key="Q3", label_visibility="collapsed"
        )

        #Q4
        st.write('<p class="question-text" style="margin-bottom:-30px;">4. 長度評估（請選最符合）</p>', unsafe_allow_html=True)
        Q4 = st.radio(
            "Q4_label",
            [
                "太長，資訊冗贅",
                "稍長，可接受",
                "剛好",
                "稍短，有些內容缺失",
                "太短，資訊不足"
            ], key="Q4", label_visibility="collapsed"
        )

        #Q5
        st.write('<p class="question-text" style="margin-bottom:-10px;">5. 如果您覺得正確性或長度有問題，請簡述原因：</p>', unsafe_allow_html=True)
        Q5 = st.text_area("Q5_label", key="Q5_textarea", label_visibility="collapsed")

        #Q6
        st.write('<p class="question-text" style="margin-bottom:-30px;">6. 您對這段Diagnosis的整體滿意程度？</p>', unsafe_allow_html=True)
        Q6 = st.radio("Q6_label", ["非常不滿意", "不滿意", "普通", "滿意", "非常滿意"], horizontal=True, key="Q6", label_visibility="collapsed")


        ##### brief summary of this week 問卷 #####
        st.subheader("Brief Summary of this week 問卷")
        # Q1
        st.write('<p class="question-text">1. 本週摘要是否有需包含但未包含的資訊？（可複選）</p>', unsafe_allow_html=True)

        # 勾選選項
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

        # 用字典收集勾選結果
        Q7_dict = {}
        for option in missing_info_options:
            Q7_dict[option] = st.checkbox(option, key=f"Q7_{option}")
        Q7_selected = [k for k, v in Q7_dict.items() if v]

        #Q2
        st.write('<p class="question-text" style="margin-bottom:-10px;">2. 除了上述類別外，請簡述您發現缺少的資訊：</p>', unsafe_allow_html=True)
        Q8 = st.text_area("Q8_label", key="Q8_textarea", label_visibility="collapsed")

        #Q3
        st.write('<p class="question-text" style="margin-bottom:-30px;">3. 長度評估（請選最符合）</p>', unsafe_allow_html=True)
        Q9 = st.radio("Q9_label",
            [
                "太長，資訊冗贅",
                "稍長，可接受",
                "剛好",
                "稍短，有些內容缺失",
                "太短，資訊不足"
            ], key="Q9", label_visibility="collapsed"
        )

        #Q4
        st.write('<p class="question-text" style="margin-bottom:-10px;">4. 您所在科別是否偏重某部分資訊紀錄？請說明需求：</p>', unsafe_allow_html=True)
        Q10 = st.text_area("Q10_label", key="Q10_textarea", label_visibility="collapsed")

        #Q5
        st.write('<p class="question-text" style="margin-bottom:-30px;">5. 您對這段Brief Summary of this week的整體滿意程度？</p>', unsafe_allow_html=True)
        Q11 = st.radio("Q11_label", ["非常不滿意", "不滿意", "普通", "滿意", "非常滿意"], horizontal=True, key="Q11", label_visibility="collapsed")

        # 提交按鈕
        if st.button("提交問卷"):
            
            # 存入 google sheet
            Q7_str = "\n".join(Q7_selected) # 多選題，原為list，轉為字串
            submission_data = [user_id, dept_choice, example_choice, Q1, Q2, Q3, Q4, Q5, Q6, Q7_str, Q8, Q9, Q10, Q11]
            sheet.append_row(submission_data, value_input_option='RAW')
            
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
            st.write(f"9. 其他缺少資訊：{Q9}")
            st.write(f"10. 科別需求說明：{Q10}")
            st.write(f"11. brief summary整體滿意度：{Q11}")
