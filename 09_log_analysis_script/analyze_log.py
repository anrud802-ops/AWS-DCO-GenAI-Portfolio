import os

# ---------------------------------------------------------
# 초보자를 위한 파이썬 로그 분석 스크립트
# - 외부 패키지(Pandas 등) 없이 파이썬 기본 기능만 사용합니다.
# - 파일 읽기, 리스트(List), 딕셔너리(Dictionary) 등의 기초 문법을 활용합니다.
# ---------------------------------------------------------

def analyze_dco_log(input_file, output_file):
    """
    주어진 로그 파일을 분석하여 요약 보고서를 생성하는 함수입니다.
    """
    
    # 1. 분석할 데이터를 담을 공간(변수) 준비하기
    total_lines = 0
    severity_counts = {}       # 심각도별 개수를 저장할 딕셔너리
    event_counts = {}          # 이벤트별 개수를 저장할 딕셔너리
    warning_critical_list = [] # 주의/위험 로그 원문을 모아둘 리스트
    major_event_list = []      # 주요 이벤트(CRC, LINK DOWN 등)를 모아둘 리스트

    # 찾고자 하는 주요 키워드 (대소문자 상관없이 찾기 위해 모두 소문자로 작성했습니다)
    key_terms = ["crc error", "link down", "ticket escalated"]

    print("로그 분석을 시작합니다...")

    try:
        # 2. 파일 열기
        with open(input_file, 'r', encoding='utf-8') as f:
            
            # 3. 파일의 모든 줄을 위에서부터 한 줄씩 읽어옵니다.
            for line in f:
                line = line.strip()

                if not line:
                    continue

                # [요구사항 1] 전체 로그 줄 수 1 증가
                total_lines += 1

                # 4. 로그는 ' | ' 기호를 기준으로 작성되어 있으므로 이를 기준으로 쪼갭니다.
                parts = line.split(' | ')

                if len(parts) >= 5:
                    severity = parts[2].strip()
                    event = parts[3].strip()

                    # [요구사항 2] 심각도(Severity)별 개수 세기
                    severity_counts[severity] = severity_counts.get(severity, 0) + 1

                    # [요구사항 3] 이벤트(Event)별 개수 세기
                    event_counts[event] = event_counts.get(event, 0) + 1

                    # [요구사항 4] WARNING 또는 CRITICAL 로그 수집 (ERROR 포함)
                    if severity in ['WARNING', 'CRITICAL', 'ERROR']:
                        warning_critical_list.append(line)

                    # [요구사항 5] 특정 키워드가 포함된 주요 이벤트 요약
                    line_lower = line.lower()
                    for term in key_terms:
                        if term in line_lower:
                            major_event_list.append(line)
                            break 

    except FileNotFoundError:
        print(f"에러: '{input_file}' 파일을 찾을 수 없습니다.")
        return

    print("로그 분석이 끝났습니다. 이제 보고서 파일을 생성합니다...")

    # 5. 결과를 Markdown(.md) 파일로 저장하기
    with open(output_file, 'w', encoding='utf-8') as out_f:
        out_f.write("# 교육용 DCO 샘플 로그 분석 요약 보고서\n\n")

        out_f.write("## 1. 전체 로그 통계\n")
        out_f.write(f"- **총 로그 수:** {total_lines} 줄\n\n")

        out_f.write("## 2. 심각도별 발생 횟수\n")
        for sev, count in sorted(severity_counts.items()):
            out_f.write(f"- {sev}: {count}건\n")
        out_f.write("\n")

        out_f.write("## 3. 이벤트별 발생 횟수\n")
        for evt, count in sorted(event_counts.items(), key=lambda x: x[1], reverse=True):
            out_f.write(f"- {evt}: {count}건\n")
        out_f.write("\n")

        out_f.write("## 4. 주의 요망 로그 (WARNING / CRITICAL / ERROR)\n")
        for log_line in warning_critical_list:
            out_f.write(f"- `{log_line}`\n")
        out_f.write("\n")

        out_f.write("## 5. 주요 이벤트 요약\n")
        out_f.write("> **검출 키워드:** CRC_ERROR, LINK_DOWN, TICKET_ESCALATED\n\n")
        for log_line in major_event_list:
            out_f.write(f"- `{log_line}`\n")

    print(f"작업 완료! '{output_file}' 결과 파일을 확인해 보세요.")

if __name__ == "__main__":
    analyze_dco_log("sample_dco_log.txt", "incident_summary.md")
