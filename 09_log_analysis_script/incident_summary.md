# 교육용 DCO 샘플 로그 분석 요약 보고서

## 1. 전체 로그 통계
- **총 로그 수:** 140 줄

## 2. 심각도별 발생 횟수
- ERROR: 2건
- INFO: 135건
- WARNING: 3건

## 3. 이벤트별 발생 횟수
- Normal heartbeat: 125건
- Ticket opened: 3건
- Ticket escalated: 3건
- Maintenance completed: 3건
- Fan Alert: 1건
- Temperature warning: 1건
- SSD failure warning: 1건
- CRC error 증가: 1건
- Link Down: 1건
- Link Up: 1건

## 4. 주의 요망 로그 (WARNING / CRITICAL / ERROR)
- `2026-07-03 01:05:00 | DEMO_CORE_SW_02 | WARNING | Fan Alert | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2`
- `2026-07-03 02:05:00 | EDU_SRV_R04_N12 | WARNING | Temperature warning | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12`
- `2026-07-03 02:10:00 | EDU_SRV_R04_N12 | ERROR | SSD failure warning | Drive Slot 3 SSD wearout indicator FAILING (SMART wear 96%). IP: 192.0.2.12`
- `2026-07-03 03:05:00 | SAMPLE_TOR_SW_01 | WARNING | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1`
- `2026-07-03 03:06:00 | SAMPLE_TOR_SW_01 | ERROR | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost.`

## 5. 주요 이벤트 요약
> **검출 키워드:** CRC_ERROR, LINK_DOWN, TICKET_ESCALATED

- `2026-07-03 01:10:00 | DEMO_CORE_SW_02 | INFO | Ticket escalated | Ticket EDU-TKT-2026-0001 escalated to Local Infrastructure Team.`
- `2026-07-03 02:15:00 | EDU_SRV_R04_N12 | INFO | Ticket escalated | Ticket EDU-TKT-2026-0002 escalated to DCO Hardware Support.`
- `2026-07-03 03:05:00 | SAMPLE_TOR_SW_01 | WARNING | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1`
- `2026-07-03 03:06:00 | SAMPLE_TOR_SW_01 | ERROR | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost.`
- `2026-07-03 03:12:00 | SAMPLE_TOR_SW_01 | INFO | Ticket escalated | Ticket EDU-TKT-2026-0003 escalated to Onsite Cabling Team.`
- `2026-07-03 03:30:00 | SAMPLE_TOR_SW_01 | INFO | Normal heartbeat | System status is healthy. Interface Gi0/1 running with 0 CRC errors. IP: 192.0.2.1`
