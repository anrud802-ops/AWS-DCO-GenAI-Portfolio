# [교육용 샘플 데이터 사용] 가상 인프라 장애 티켓

## 1. 티켓 정보 (Ticket Information)
- **티켓 ID**: SAMPLE-TICKET-2026-0707
- **심각도 (Severity)**: Medium (EDU-LEVEL-2)
- **발생 시간**: 2026-07-07 15:09:40 KST (가상 시간)
- **샘플 장비명**: SAMPLE_TOR_SW_01 (가상 Top of Rack 스위치)
- **대상 이벤트**: CRC Error Count Increase & Link Down

## 2. 관찰 내용 및 시스템 로그 샘플 (Observations)
- **증상**: 
  - `SAMPLE_TOR_SW_01` 스위치의 특정 인터페이스에서 CRC(Cyclic Redundancy Check) 에러 수가 급격히 증가함.
  - CRC 에러 누적 이후 해당 포트의 링크가 다운되는 `Link Down` 이벤트가 관찰됨.
- **가상 로그 출력 예시**:
  ```log
  [2026-07-07 15:00:00 KST] SAMPLE_TOR_SW_01: %ETHPORT-5-IF_DOWN_LINK_FAILURE: Interface Ethernet1/1 is down (Link failure)
  [2026-07-07 15:00:05 KST] SAMPLE_TOR_SW_01: %PORT-4-ERR_DISABLE: Ethernet1/1 keepalive failure
  [2026-07-07 15:00:10 KST] SAMPLE_TOR_SW_01: %IFMGR-5-PORT_DOWN: Interface Ethernet1/1 is down
  ```

## 3. 에스컬레이션 필요 여부 (Escalation Required)
- **Escalation**: 필요 (Yes)
  - **이유**: 단순 일시적 에러가 아닌 물리 계층(Cabling, SFP Module) 또는 하드웨어 인터페이스 불량 가능성이 존재함. 원격 조치로 링크 복구가 불가하여 현장 DCO 엔지니어의 물리적 점검 및 에스컬레이션이 요구됨.

## 4. 보안 주의사항 (Security & Compliance Guidelines)
- 본 티켓은 오직 가상의 실습 환경을 위해 작성된 **교육용 샘플 데이터**입니다.
- **절대 주의**: 실제 인프라의 IP 주소, 물리적 장비의 실제 시리얼 번호(Serial Number), 계정 정보(Credentials) 및 고객 정보를 본 문서에 기재하거나 외부로 유출하지 마십시오.
