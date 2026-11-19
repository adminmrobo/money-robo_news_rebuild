# Money-Robo 발행인 로드맵 브리핑 — 단일 HTML 빌드
import json, os, datetime as dt, html

BASE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'base.css'), encoding='utf-8').read()
D = dt.date
def d(s): return D(*map(int, s.split('-')))
NOTION = 'https://app.notion.com/p/'

# ---------------- 스테이지 ----------------
STAGES = [
 dict(k='s1', n=1, name='기업개황 LLM 데이터', st='done', stl='완료', s='2025-11-18', e='2025-11-27',
  gate='G1 — 상장사 기업개황을 검색 결과에 붙인다', gres='통과 · 11/20 연동, 11/27 결측 340건 보충',
  out='검색 결과의 [기업 개황]·[보고서 원문] 버튼, 상장사 개황 데이터',
  say='검색창에 회사 이름을 넣으면 그 회사가 무슨 일을 하는지 바로 읽히게 됐습니다. Money-Robo가 “공시 목록”에서 “회사 이야기”로 넘어가는 첫걸음입니다.',
  did=['사업보고서의 [사업의 개요]만 뽑아 GPT-4o-mini로 정리하고, 회사별 최신 1건만 남겨 CSV로 보관',
       '검색 결과에 [기업 개황] 버튼 추가 — 누르면 미리 정리한 개황 텍스트 표시, 없으면 “개황 없음”',
       '삼성전자·카카오·NAVER 등 개황이 빠진 상장사 340건을 추가 수집으로 보충',
       '[보고서 원문] 버튼 신설, 굵은 글씨 표시 방식 정리'],
  issue='보충 과정에서 회사와 개황이 엇갈리는 문제(카카오에 리츠 개황이 붙는 식)가 나왔습니다. 이후 공시 요약 단계에서 원문 대조 검증을 늘린 출발점입니다.',
  refs=[('2025-11-18','기업개황 - LLM 데이터 처리','2af17a4520ed80eba5a8d37c4810daf9'),
        ('2025-11-20','기업개황 데이터 - LLM 처리 후 연동 성공','2b117a4520ed80e99f8dcabb0176a5ec'),
        ('2025-11-27','‘사업의 개요’ 결측치 보충 완료','2b817a4520ed80bc8100d0bf17699bd9')]),
 dict(k='s2', n=2, name='공시 요약 자동화 1차 (6유형)', st='done', stl='완료', s='2025-12-02', e='2026-01-22',
  gate='G2 — 주요 공시를 사람 손 없이 요약해 검색에 올린다', gres='통과 · 1/22 6개 유형 자동화 완료',
  out='단일판매·배당·분기·반기·사업보고서·손익구조30% 변동의 LLM 요약 자동화',
  say='단일판매·공급계약 하나로 시작해 두 달 만에 6개 유형이 사람 손 없이 돌기 시작했습니다. 비용이 하루 1달러 안쪽이라는 숫자를 처음 받아 본 것도 이때입니다.',
  did=['단일판매·공급계약 2022~2025년 데이터 수집, 2026년부터는 실시간 수집봇이 자동 적재',
       '5분에 한 번 돌며 새 공시를 요약해 검색 엔진에 반영 — 실시간 공시 검색 성공 (12/9)',
       '현금·현물배당(12/11), 분기보고서(12/16), 반기보고서(12/31), 손익구조 30% 변동(1/13), 사업보고서(1/22) 순으로 확장',
       '사업보고서 재무제표 인식 실패를 고쳐 6개 유형 모두 검색 결과에 표시'],
  issue='12월에 토큰 한도(Billing)로 검색·요약이 멈췄고, 1월에는 사업보고서 크롤링 중 DART 접속 차단으로 추정되는 장애가 있었습니다. 둘 다 당일 복구됐습니다.',
  refs=[('2025-12-09','공급계약-단일판매 자동화 완료','2c417a4520ed8014a969d69a4d8a7af1'),
        ('2025-12-17','OpenAI API 평균 비용 : $0.9/일','2cc17a4520ed80fba5dcda1686ed5323'),
        ('2026-01-22','현재까지 작업한 모든 공시 자동화 완료','2f017a4520ed801cb870fb9cedb2c53f')]),
 dict(k='s3', n=3, name='공시 유형 확대 (주요사항·주총 시즌)', st='done', stl='완료', s='2026-01-27', e='2026-04-02',
  gate='G3 — 투자 판단에 쓰이는 주요 공시까지 요약 범위를 넓힌다', gres='통과 · 23번째 유형(투자판단관련주요경영사항)까지 진행',
  out='최대주주변동·유상/무상증자·주식소각·조회공시 7종·주총 관련·감사보고서·기업가치제고계획 등',
  say='주총 시즌을 앞두고 유형을 하나씩 늘려 갔습니다. 이틀에 한 유형을 끝내는 속도가 나오면서, “유형마다 코드를 새로 짜는 방식은 오래 못 간다”는 문제도 함께 보였습니다.',
  did=['최대주주변동(1/27~29), 유상증자(2/3~5), 무상증자(2/10~11), 주식소각결정(2/12)',
       '조회공시(풍문 또는 보도) 관련 9개 세부 유형(2/19~3/3)',
       '주주총회소집결의(3/4), 주주총회 집중일 개최사유신고(3/17), 감사보고서(3/19), 정기주주총회결과(3/25)',
       '기업가치제고계획(3/31) — 2024년 5월에 새로 생긴 유형, 투자판단관련주요경영사항(4/1~2)'],
  issue='주주총회소집공고는 LLM 요약을 보류(PENDING)하고 플랜 B로 돌렸습니다. 2025년 11월 말부터 2026년 3월까지 OpenAI 지출은 78.54달러(약 12만 원)로 집계됐습니다.',
  refs=[('2026-01-28','최대주주변동 DB 수집 완료','2f617a4520ed805d8601d4e97c4b50b5'),
        ('2026-02-25','풍문또는보도 관련 공시요구 관련 4개 완료','31217a4520ed80279e0ae3a90881d2d8'),
        ('2026-04-01','투자판단관련주요경영사항 (유형 23종 일정표·비용)','33517a4520ed807a917bfea3eb224ba5')]),
 dict(k='s4', n=4, name='AX·MCP 구조 전환', st='done', stl='완료', s='2026-04-07', e='2026-05-28',
  gate='G4 — 기존 서비스를 멈추지 않고 새 구조로 옮길 길을 낸다', gres='통과 · 11단계 계획 5/8 완료, 응답 30초대 → 1~5초',
  out='공시 2분류(단순 공시형·복합 보고서형), 라우터, DB 캐시 분기, MCP 경로 + 자동 fallback, 운영 로그',
  say='여기가 이 1년의 허리입니다. 공시를 “유형”이 아니라 “문서 구조”로 다시 나눴고, 새 MCP 경로가 실패하면 예전 방식으로 저절로 돌아가게 만들었습니다. 서비스를 세우지 않고 엔진을 갈아 끼운 셈입니다.',
  did=['현재 구조 파악 → Git·DB·환경설정 백업 → Cursor + Remote SSH 개발 환경 (4/7~14)',
       '공시를 단순 공시형(본문 하나)과 복합 보고서형(목차→섹션)으로 2분류 확정 (4/28)',
       '단순형 모듈 분리, 복합형 목차·섹션·요약 서비스, 자동 분기 라우터, 요약이 있으면 DB에서 바로 꺼내는 캐시 분기 (4/29~30)',
       'FastAPI → MCP tool 호출, 실패 시 legacy 자동 전환, 환경변수 하나로 켜고 끄는 feature flag, 운영 로그 (5/7~8)',
       '첫 클릭 지연 28초 → 126ms, 요약 대기 30초대 → 캐시 1초 이내·재요약 4~5초, 진행 막대 추가 (5/20~28)'],
  issue='MCP 호출마다 별도 프로세스를 띄우는 방식이라 트래픽이 늘면 느려질 수 있고, 검색 흐름 전체는 아직 MCP로 옮기지 않았습니다(중간보고서의 리스크 항목).',
  refs=[('2026-04-07','MCP 전환 계획','33b17a4520ed80e297bdd9e76ec3f67a'),
        ('2026-04-28','AX 플랜 재수립 및 공시 2종으로 분류','35017a4520ed8013a37dea358378f52c'),
        ('2026-05-06','AX/MCP 요약 전환 중간보고서','35817a4520ed80b1bccdd445a1df5cc7'),
        ('2026-05-28','LLM 반응 소요시간 대폭 감소','36e17a4520ed80ea9c88cbafc4aabbb2')]),
 dict(k='s5', n=5, name='서비스 화면·회원·관리자', st='done', stl='완료', s='2026-06-02', e='2026-07-22',
  gate='G5 — 요약 엔진을 사람이 쓰는 서비스로 만든다', gres='통과 · 7/13 관리자 페이지 오픈',
  out='홈·랜딩, 우측 패널 기사 자동 생성, 기업별 공시 모음, 회원가입·로그인, 관리자 대시보드',
  say='엔진 위에 처음으로 “가게”가 섰습니다. 공시가 들어오면 기사가 저절로 쓰이고, 방문자와 LLM 사용량을 관리자 화면에서 볼 수 있게 됐습니다.',
  did=['사업·분기·반기보고서 오류 수정(6/2), 홈페이지 고도화(6/9), 랜딩페이지(6/18)',
       '오른쪽 패널에서 새 공시 기사 자동 생성 — 6/10 이후 공시 2,220건을 훑어 누락분 50건을 작업 대기열에 등록',
       '“매수” 단어 하나까지 막던 금칙어를 투자 권유 표현만 막도록 바로잡음',
       '기업 상세 페이지·공시 히스토리(6/23~7/2), 공시 본문을 못 가져올 때의 대체 처리(7/7)',
       '이메일 회원가입·인증번호(7/8~9), 관리자 대시보드 — 고객·비회원 방문자·OpenAI 사용량·시스템 상태 (7/13)'],
  issue='소셜 로그인(구글·네이버·카카오)은 보류했습니다. 운영이 아직 HTTP라서 관리자 쿠키의 Secure 옵션을 꺼 둔 상태이고, HTTPS로 옮길 때 켜야 합니다.',
  refs=[('2026-06-16','우측 패널 기사 요약 자동화 완성','38117a4520ed801abe67d2513bc1dd85'),
        ('2026-07-08','로그인/회원가입 기능 추가','39717a4520ed80d080f2c84dbebfe43e'),
        ('2026-07-14','admin 관리자 페이지 개설','39c17a4520ed8072a790f9ebda6f56bc')]),
 dict(k='s6', n=6, name='공시 카드화·실적 구조화', st='done', stl='완료', s='2026-07-23', e='2026-09-10',
  gate='G6 — 요약 문장 대신 숫자가 보이는 카드로 바꾼다', gres='통과 · 카드 지원 105종, 카드 가치 유형 97.93%',
  out='사업·반기·분기보고서 실적 카드와 과거 데이터 backfill, 실적공시 구조화 파이프라인',
  say='읽는 요약에서 보는 카드로 바뀌었습니다. 원문과 9개 숫자가 모두 맞았다는 대조 결과가 이 단계의 품질 보증서라고 봅니다.',
  did=['사업·반기·분기 공시를 카드로 보여 주고 과거분까지 backfill (7/23~8/19)',
       '실적공시 파이프라인 전체 테스트, 실제 DART 원문 연결 검증, 브라우저 12개 케이스 확인 (8/27)',
       '42개 파일 커밋 — 민감정보·절대경로·디버그 코드 점검 후 정리',
       '카드 지원 유형 77종 → 105종, 카드로 볼 가치가 있는 유형 지원률 77.6% → 97.93% (9/10)'],
  issue='8/27 점검에서 이 코드 저장소에 원격 저장소(origin)가 없는 것이 확인됐습니다. 지금은 회사 서버 한 곳에만 있는 셈이라, 별도 백업 위치를 정해야 합니다.',
  refs=[('2026-08-04','분기보고서 카드형 UI - backfill 완료','3b217a4520ed8067a751e61295b03396'),
        ('2026-08-27','실적공시 구조화 파이프라인 검증 & 커밋 완료','3c917a4520ed80e3a3e1d1026a606aed'),
        ('2026-09-10','공시요약 UI 완성률 97%, 다음 기능 구현 계획','3d717a4520ed80d2b4c8d9d037b59a52')]),
 dict(k='s7', n=7, name='Company Story — 공시 × 주가', st='done', stl='완료', s='2026-09-15', e='2026-10-20',
  gate='G7 — 국내 전체 상장사의 공시와 주가 반응을 한 화면에 잇는다', gres='통과 · 10/16 국내 상장사 2,611개 등록, 10/20 자동 갱신 예약',
  out='Company Story 화면, 기업 소식 캘린더, 공시별 주가 반응(Event Study) 데이터, 자동 갱신 스케줄',
  say='공시를 요약해 읽어 주던 서비스가 “이 공시 뒤에 주가가 어떻게 움직였나”까지 보여 주게 됐습니다. 이름도 Company Story로 붙었습니다.',
  did=['기업 소식 홈·시세(KOSPI·KOSDAQ·원/달러·관심종목), 하이라이트·그리기 도구, 캘린더 (9/15~30)',
       '개발 방식에 Superpowers + Ralph Loop 도입 — 계획→구현→테스트→검증을 반복 (10/1)',
       '약 8년치 일봉으로 공시 후 +1·+3·+5·+10·+20일 수익률 계산, Tier1 10개 종목 11,514건 적재 (10/6)',
       '검색 속도 약 2초 → 10ms, KOSPI 100개 → 500개 → 전체로 확대 (10/13~16)',
       'KOSPI 827개 + KOSDAQ 1,802개, 중복 제외 2,611개 기업 등록 · 신규 상장·상장폐지 자동 관리 (10/20)'],
  issue='9/17에 Cursor 추가 사용 한도(10달러)를 다 써서 개발이 며칠 멈췄습니다. 남은 개발에 5천만~1억 토큰이 더 든다는 김 연구원의 추정이 있어, 개발 도구 예산을 따로 잡아야 합니다.',
  refs=[('2026-09-17','기업 소식 서비스 확장 및 Cursor 사용량','3de17a4520ed805a9efff0b902ffef36'),
        ('2026-10-01','Superpowers + Ralph Loop 도입','3ec17a4520ed80f4b539eb8871691da4'),
        ('2026-10-06','주가 x 공시 시각화','3f117a4520ed808195aacb2ca3c5de06'),
        ('2026-10-20','국장 상장기업 all ready + 미장 준비','3fa17a4520ed808e9348eb5434c079cb')]),
 dict(k='s8', n=8, name='money-robo.com 정리 · LLM 기사 자동 발행', st='run', stl='진행 중', s='2026-10-21', e='2026-11-18',
  gate='G8 — 검증을 통과한 LLM 기사만 money-robo.com에 자동으로 싣는다', gres='진행 중 · 11/18 기준 51종 자동 발행 대상',
  out='공시봇 23개 정상화, 블로그 전체 백업·분류, 기사 검증 게이트, WordPress 자동 게시',
  say='드디어 엔진이 money-robo.com 본지에 닿았습니다. 새 기사를 싣기 전에 옛 기사부터 백업하고, 숫자가 원문과 다르면 아예 싣지 않는 검증 게이트를 먼저 세운 순서가 마음에 듭니다.',
  did=['공시봇 23개·DART 수집·이메일 발송 정상화, 코스피·코스닥 시황 메일링 복구 (10/21~29)',
       'WordPress 게시물 61,767건 백업(누락·중복·오류 0건), 2025년 이전 27,262건 분류 — 비공개 추천 1,210 · 공개 유지 8,877 · 수동 검토 17,175 (10/28)',
       'LLM 기사 1,000건 검증 중 998건 정상, 운영 기준 5,197건 중 5,101건 통과 — 계약금액 1,147억을 114억으로 쓴 기사는 자동 차단 (10/29)',
       '단일판매·공급계약 자동 게시 시작 — 30분 주기, 하루 최대 5건, 정정공시는 전후 대조 필수 (11/5)',
       '신규 14종 공개 게시(11/17) → 기존 31종 + 신규 20종 = 51종 자동 발행 대상, 발행 조건 15개 항목 모두 통과 (11/18)'],
  issue='Cafe24 서버의 이미지 업로드 오류(HTTP 500)가 아직 풀리지 않아, 메일로는 나갔지만 블로그에 못 실린 공시 13건이 대기 중입니다. 오래된 기사 비공개 전환은 아직 시범 10건 검증까지만 했습니다.',
  refs=[('2026-10-27','블로그 정리 및 공시 서비스 개편 계획 (~11/02)','40617a4520ed8045b0a2f71cd712d420'),
        ('2026-10-28','기존 콘텐츠 백업·아카이브 / 신규 공시 서비스 개편 준비','40717a4520ed80d2b115d41185f11a6d'),
        ('2026-10-29','LLM 기사 검증·WP 연동','40817a4520ed800b89c6e6247c3e46da'),
        ('2026-11-05','단일판매공급계약 ← LLM 자동 포스팅 완료','40f17a4520ed80ba8af7f140e56a8c2f'),
        ('2026-11-17','LLM 자동 포스팅 14개 유형 완','41817a4520ed80d3ae10ddca3e13aefe'),
        ('2026-11-18','LLM 자동 포스팅 51종 완(51/108)','41c17a4520ed80228f27ec3c1b315bb3')]),
]

PLANS = [
 dict(k='p1', name='105종 자동 포스팅 체계', src='11/17·11/18 리포트의 “최종 목표”',
  body='Company Story가 카드로 지원하는 105종 전체를 자동 포스팅으로 잇습니다. 남은 것은 기사 생성 경로가 아직 없는 52종, 실적 별도 경로 2종, 그리고 잠정실적·경영권 분쟁·기술 라이선스 같은 우선 유형입니다.'),
 dict(k='p2', name='관심종목 피드 · 이전 공시와 비교', src='9/10 리포트의 “다음 기능”',
  body='관심 기업만 골라 공시를 시간순으로 모아 보고, 같은 회사의 같은 유형 공시를 50억 → 80억 → 120억처럼 이어서 보여 줍니다. 공시를 “읽어 주는” 서비스에서 기업의 변화를 “추적하는” 서비스로 가는 단계입니다.'),
 dict(k='p3', name='미국 증시로 Company Story 확장', src='10/20 리포트의 “향후 작업”',
  body='SEC 공시와 미국 주가 수집 구조를 검토하고 주요 상장사부터 넓힙니다. money-robo.com의 기존 미국 주식시장 메뉴(개미의 주판, 미국 증시 Brief)와 만나는 지점입니다.'),
 dict(k='p4', name='money-robo.com 구조 레노베이션', src='발행인 구상 — 10/27 개편 계획과 위 세 가지를 묶음',
  body='오래된 단순 전달형 기사는 비공개로 돌리고 원천 데이터는 남기며, 23개 뉴스봇은 단계적으로 줄이고, 증권기사·기업 페이지·관심종목을 Company Story와 한 동선으로 잇습니다. 아래 “사이트 구조 레노베이션”에 지금 메뉴와 바꿀 방향을 나란히 놓았습니다.'),
]

REPS = {'s1': ['상장사 기업개황을 LLM으로 정리해 검색 결과에 붙이는 작업이 완료됐습니다. 11/20에 [기업 개황] 버튼을 연동했고, 11/27에 빠져 있던 340건을 보충했습니다. 이를 보고합니다.'], 's2': ['단일판매·배당·분기·반기·사업보고서·손익구조 30% 변동, 6개 유형의 공시 요약 자동화가 완료됐습니다. 5분마다 새 공시를 요약해 검색에 올립니다. 이를 보고합니다.', '운영 비용은 2개 유형이 돌던 12월 기준 하루 약 0.9달러입니다.'], 's3': ['최대주주변동부터 투자판단관련주요경영사항까지, 23번째 유형의 요약 자동화가 완료됐습니다. 주주총회소집공고는 LLM 요약을 보류했습니다. 이를 보고합니다.'], 's4': ['공시를 단순 공시형과 복합 보고서형으로 나누고 MCP 경로와 자동 fallback을 붙이는 11단계 전환이 5/8에 완료됐습니다. 이를 보고합니다.', '이어서 요약 대기 시간을 30초대에서 1~5초로, 첫 클릭 지연을 28초에서 126ms로 줄였습니다.'], 's5': ['공시가 들어오면 기사가 저절로 쓰이는 우측 패널, 이메일 회원가입·로그인, 관리자 페이지 개설이 완료됐습니다. 관리자 페이지는 7/13에 열었습니다. 이를 보고합니다.'], 's6': ['사업·반기·분기보고서 실적 카드화와 과거 데이터 backfill이 완료됐습니다. 카드 지원 유형은 105종입니다. 이를 보고합니다.', '삼성생명·삼성화재·DSR제강의 매출·영업이익·순이익 9개 지표를 DART 원문과 대조해 모두 일치함을 확인했습니다.'], 's7': ['국내 KOSPI·KOSDAQ 상장사 2,611개를 Company Story에 등록하고 공시·주가 자동 갱신 예약까지 완료됐습니다. 이를 보고합니다.', '공시 뒤 주가 반응은 Tier1 10개 종목 11,514건을 먼저 계산해 두었습니다.'], 's8': ['money-robo.com 게시물 61,767건 백업, LLM 기사 검증 게이트, WordPress 자동 게시가 완료됐습니다. 11/18 기준 51종이 자동 발행 대상입니다. 이를 보고합니다.', '다만 Cafe24 이미지 업로드 오류로 메일로만 나간 공시 13건은 아직 블로그에 싣지 못했습니다.']}
# ---------------- 렌더 도우미 ----------------
def esc(s): return html.escape(s, quote=True)
def chip(st, stl): return f'<span class="st {st}">{esc(stl)}</span>'
AV = {
 'kim': ('김 연구원', '#2f6f9e', '<rect x="18" y="20" width="28" height="20" rx="3" fill="#fff"/><path d="M22 35 L28 29 L33 33 L42 24" stroke="#2f6f9e" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/><rect x="27" y="42" width="10" height="4" rx="1.5" fill="#fff"/>'),
 'pub': ('발행인', '#0b5c7a', '<path d="M32 13 L41 30 L32 52 L23 30 Z" fill="#fff"/><circle cx="32" cy="31" r="3.2" fill="#0b5c7a"/><path d="M32 34 L32 52" stroke="#0b5c7a" stroke-width="1.6"/>'),
 'q':   ('처음 보는 독자', '#b4532a', '<text x="32" y="44" text-anchor="middle" font-size="30" font-weight="700" fill="#fff" font-family="sans-serif">?</text>'),
 'rec': ('기록 데스크', '#3d6b2f', '<rect x="20" y="16" width="24" height="32" rx="3" fill="#fff"/><path d="M25 25h14M25 31h14M25 37h9" stroke="#3d6b2f" stroke-width="2.4" stroke-linecap="round"/>'),
 'box': ('요청 접수함', '#6b4fa0', '<path d="M17 30 L22 18 H42 L47 30 V45 H17 Z" fill="#fff"/><path d="M17 30 H26 L28 35 H36 L38 30 H47" stroke="#6b4fa0" stroke-width="2.4" fill="none" stroke-linejoin="round"/>'),
}
def avatar(w, size=64):
    nm, col, g = AV[w]
    return f'<svg class="who" width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="31" fill="{col}"/>{g}</svg>'
def say(w, txt):
    return f'<div class="say" data-who="{w}">{avatar(w)}<div class="bub"><b class="name">{AV[w][0]}</b><p>{txt}</p></div></div>'
def talk(*lines):
    return '<div class="talk">' + ''.join(say(w, t) for w, t in lines) + '</div>'
REP = '이를 보고합니다.'
def lv(id_, title, inner, req=True):
    pin = f'<button type="button" class="rqpin" data-sec="{esc(title)}" aria-label="이 부분 수정 요청">요청</button>' if req else ''
    return f'<section class="level" id="{id_}"><div class="wrap"><h2>{esc(title)}{pin}</h2>{inner}</div></section>'

# ---------------- 일정 막대 (SVG) ----------------
def gantt():
    t0, t1 = D(2025, 11, 1), D(2027, 3, 31)
    W, L, R, top, rh = 1000, 210, 20, 34, 30
    span = (t1 - t0).days
    X = lambda day: L + (W - L - R) * (day - t0).days / span
    rows = STAGES
    H = top + rh * len(rows) + 54
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="2025년 11월부터 2026년 11월까지 스테이지별 일정 막대">']
    m = D(2025, 11, 1)
    while m <= t1:
        x = X(m)
        o.append(f'<line x1="{x:.1f}" y1="{top-6}" x2="{x:.1f}" y2="{H-40}" stroke="#e3e8ee"/>')
        lab = f'{str(m.year)[2:]}.{m.month:02d}' if m.month in (1, 11) or m == D(2025, 11, 1) else f'{m.month}월'
        o.append(f'<text x="{x+3:.1f}" y="{top-12}" font-size="11.5" fill="#5b6874">{lab}</text>')
        m = D(m.year + (m.month == 12), m.month % 12 + 1, 1)
    for i, s in enumerate(rows):
        y = top + i * rh
        x1, x2 = X(d(s['s'])), X(d(s['e']) + dt.timedelta(days=1))
        col = '#13733a' if s['st'] == 'done' else '#1e55c8'
        o.append(f'<text x="8" y="{y+19}" font-size="13" fill="#16212b"><tspan font-weight="700">S{s["n"]}</tspan> {esc(s["name"][:15])}{"…" if len(s["name"])>15 else ""}</text>')
        o.append(f'<a href="#{s["k"]}"><rect x="{x1:.1f}" y="{y+5}" width="{max(x2-x1,4):.1f}" height="19" rx="5" fill="{col}" opacity=".88"><title>S{s["n"]} {esc(s["name"])} · {s["s"]} ~ {s["e"]}</title></rect></a>')
    # 예정 띠
    y = top + len(rows) * rh
    xs = X(D(2026, 11, 19))
    o.append(f'<rect x="{xs:.1f}" y="{y+5}" width="{W-R-xs:.1f}" height="19" rx="5" fill="#fff" stroke="#8a96a3" stroke-dasharray="5 4"/>')
    o.append(f'<text x="8" y="{y+19}" font-size="13" fill="#5b6874">다음 단계 (날짜 미정)</text>')
    o.append(f'<text x="{xs+8:.1f}" y="{y+19}" font-size="12" fill="#5b6874">105종·관심종목·미장·개편</text>')
    xt = X(D(2026, 11, 18))
    o.append(f'<line x1="{xt:.1f}" y1="{top-4}" x2="{xt:.1f}" y2="{H-34}" stroke="#c9302c" stroke-width="2"/>')
    o.append(f'<text x="{xt-4:.1f}" y="{H-18}" font-size="12" fill="#c9302c" text-anchor="end">기준일 2026-11-18</text>')
    o.append('</svg>')
    return ''.join(o)

# ---------------- 본문 조립 ----------------
B = []
NAV = [('#concl', '결론'), ('#map', '로드맵 지도'), ('#status', '스테이지 현황'), ('#timeline', '일정 막대'), ('#flow', '엔진 흐름'),
       ('#nums', '숫자로 본 변화'), ('#stages', 'S1~S8'), ('#next', '다음 단계'), ('#reno', '사이트 개편'), ('#risk', '확인할 것'),
       ('#review', '발행인 판단'), ('#reqs', '요청 모음'), ('#kg', '찾아보기'), ('#src', '출처')]
B.append('<nav class="top" aria-label="이 쪽 차례"><div class="wrap"><a class="logo" href="#top">Money-Robo 로드맵</a>'
         + ''.join(f'<a class="l" href="{h}">{t}</a>' for h, t in NAV) + '</div></nav><div id="prog" aria-hidden="true"></div>')

KPI = [('139', '데일리 리포트 (2025-11-18 ~ 2026-11-18)', 'i'), ('8', '스테이지 — 7개 완료, 1개 진행 중', 'g'),
       ('2,611', '검색에 등록한 국내 상장사', 'i'), ('105종', 'Company Story 카드 지원 공시 유형', 'm'),
       ('51종', 'money-robo.com 자동 발행 대상 (11/18)', 'g'), ('61,767', '백업을 마친 기존 블로그 게시물', 'a')]
B.append('<header class="hero" id="top"><div class="wrap"><div class="hero-text">'
 '<div class="eyebrow">PUBLISHER BRIEFING · 01 · 기준일 2026-11-18</div>'
 '<h1>공시봇에서 Company Story까지 — 발행인이 본 1년의 로드맵</h1>'
 '<p class="coreq">Money-Robo 발행인이 김 연구원의 데일리 리포트 139건(2025-11-18 「기업개황 - LLM 데이터 처리」부터 2026-11-18 「LLM 자동 포스팅 51종」까지)을 여덟 개 스테이지로 묶어 읽었습니다. 큰 그림은 하나입니다. money-robo.com을 공시 데이터 위에서 다시 짓는 일입니다.</p>'
 '</div><div class="kpis">' + ''.join(f'<div class="kpi {c}"><b>{v}</b><span>{t}</span></div>' for v, t, c in KPI) + '</div>'
 '<p class="fn">숫자는 모두 김 연구원의 노션 데일리 리포트에 적힌 값입니다. 발행인이 새로 계산한 값은 없고, 표기가 서로 다른 곳은 “확인할 것”에 따로 모았습니다.</p>'
 '</div></header>')

B.append(lv('concl', '결론 먼저 — 오늘 보고의 세 줄',
 '<div class="box3"><h3>발행인의 세 줄</h3><ol>'
 '<li><b>엔진은 섰습니다.</b> 공시를 받아 요약하고, 카드로 바꾸고, 원문 숫자와 대조해 틀리면 막는 흐름이 국내 상장사 2,611개 위에서 돌아갑니다 (S1~S7).</li>'
 '<li><b>이제 본지에 닿았습니다.</b> 검증을 통과한 LLM 기사가 money-robo.com에 자동으로 실리기 시작했고, 11/18 기준 51종이 자동 발행 대상입니다 (S8).</li>'
 '<li><b>남은 일은 “사이트를 다시 짓는 것”입니다.</b> 105종 전체 연결, 관심종목·이전 공시 비교, 미국 증시, 그리고 오래된 기사 정리와 메뉴 개편을 한 동선으로 묶어야 합니다 (다음 단계).</li></ol></div>'
 + talk(('kim', '2025-11-18 기업개황 작업부터 2026-11-18 LLM 자동 포스팅 51종까지, 데일리 리포트 139건 분량의 작업이 정리됐습니다. 이를 보고합니다.'),
        ('pub', '이 쪽은 김 연구원의 결과물을 “평가”하려는 문서가 아닙니다. 1년 동안 무엇이 어떤 순서로 쌓였는지 발행인이 한눈에 보고, 다음 관문에서 무엇을 정해야 하는지 고르려는 지도입니다.'))
 + talk(('q', '공시봇은 원래 있지 않았나요? 무엇이 달라진 건가요?'),
        ('kim', '예전 공시봇 23개는 정해진 틀에 숫자를 끼워 기사를 찍었습니다. 지금은 LLM이 원문을 읽고 쓰되, 숫자는 원문과 기계로 대조해 하나라도 다르면 싣지 않도록 바꾸는 작업이 완료됐습니다. 이를 보고합니다.'),
        ('pub', '그 대조가 핵심입니다. 그리고 결과가 기사 한 편으로 끝나지 않고 회사별 이야기(Company Story)로 쌓인다는 점이 예전과 가장 다릅니다.'))
 + '</div>'))

# 로드맵 지도
cards = []
for s in STAGES:
    cards.append(f'<a class="card" href="#{s["k"]}">{chip(s["st"], s["stl"])}<b>S{s["n"]} {esc(s["name"])}</b><span class="d">{s["s"][2:].replace("-",".")} ~ {s["e"][2:].replace("-",".")} · {esc(s["out"])}</span></a>')
for p in PLANS:
    cards.append(f'<a class="card plan" href="#{p["k"]}">{chip("plan","예정")}<b>{esc(p["name"])}</b><span class="d">{esc(p["src"])}</span></a>')
B.append(lv('map', '로드맵 지도 — 어디부터 보시면 되나',
 '<p class="lead">초록은 끝난 단계, 파랑은 진행 중, 점선은 김 연구원의 리포트에 “다음에 할 일”로 적힌 단계입니다. 카드를 누르면 해당 스테이지로 갑니다. 처음이라면 <a href="#s4">S4 AX·MCP 구조 전환</a>과 <a href="#s8">S8 자동 발행</a> 두 장만 보셔도 흐름이 잡힙니다.</p>'
 '<div class="mapc">' + ''.join(cards) + '</div>'))

# 현황 표
rows = ''.join(f'<tr><td><a href="#{s["k"]}"><b>S{s["n"]}</b> {esc(s["name"])}</a></td><td>{chip(s["st"], s["stl"])}</td><td class="num nw">{s["s"][2:].replace("-",".")} ~ {s["e"][2:].replace("-",".")}</td><td>{esc(s["gate"])}<br><span class="small muted">{esc(s["gres"])}</span></td></tr>' for s in STAGES)
rows += ''.join(f'<tr><td><a href="#{p["k"]}">{esc(p["name"])}</a></td><td>{chip("plan","예정")}</td><td class="muted">날짜 미정</td><td class="small muted">{esc(p["src"])}</td></tr>' for p in PLANS)
B.append(lv('status', '스테이지 현황 — 2026-11-18 기준',
 '<div class="tw"><table class="tb"><thead><tr><th>스테이지</th><th>상태</th><th>기간</th><th>관문과 결과</th></tr></thead><tbody>' + rows + '</tbody></table></div>'
 '<p class="fn">기간은 각 스테이지에 속한 데일리 리포트의 첫 날짜와 마지막 날짜입니다. 관문(G1~G8) 이름은 발행인이 결과물을 보고 붙였습니다.</p>'))

B.append(lv('timeline', '일정 막대 — 1년이 어떻게 쓰였나',
 '<div class="flowbox panel">' + gantt() + '</div>'
 + say('rec', '빈칸 없이 이어져 있습니다. 가장 길었던 것은 S2(공시 요약 1차, 약 7주)와 S3(유형 확대, 약 9주)이고, 구조를 갈아엎은 S4는 7주 남짓에 끝났습니다. 12/23~24 휴무와 9/17~21 개발 도구 한도 소진으로 쉰 날이 있습니다.')))

# 엔진 흐름
FLOW = [('DART 공시', '5분 주기 수집 · 2,611개 상장사', 'S2·S7'), ('구조로 나누기', '단순 공시형 / 복합 보고서형 라우터', 'S4'),
        ('요약·카드', 'LLM 요약 + 105종 카드 · DB 캐시', 'S2·S6'), ('검증 게이트', '금액·수치·필수 항목 원문 대조', 'S8'),
        ('내보내기', 'Company Story · money-robo.com · 메일', 'S5·S7·S8')]
fl = ''.join(f'<div class="st4"><h5><i>{i+1}</i>{esc(a)}</h5><p>{esc(b)}</p><p><span class="tag">{c}</span></p></div>' for i, (a, b, c) in enumerate(FLOW))
B.append(lv('flow', '엔진 흐름 — 지금 공시 한 건이 지나가는 길',
 '<p class="lead">1년의 결과물을 공시 한 건의 여정으로 다시 그리면 다섯 칸입니다. 칸 아래 꼬리표는 그 칸을 만든 스테이지입니다.</p>'
 '<div class="sm4 sm5">' + fl + '</div>'
 + '<div class="pair"><div><span class="tag d">예전 방식 (legacy)</span><p class="small">FastAPI가 요약 함수를 직접 부름 → 새 공시 유형마다 서비스 코드를 고침 → 고치다 기존 기능이 깨질 위험</p></div>'
 '<div><span class="tag m">지금 방식 (MCP 경유 + 자동 fallback)</span><p class="small">FastAPI → gateway → MCP tool. 실패하면 예전 방식으로 저절로 돌아가고, 환경변수 하나로 끄고 켭니다. 새 유형은 tool을 하나 더 붙이는 일이 됩니다.</p></div></div>'
 + talk(('kim', '공시 한 건이 수집 → 구조 분류 → 요약·카드 → 검증 → 내보내기 다섯 칸을 지나는 구조가 완성됐습니다. 이를 보고합니다.'),
        ('kim', '검증 단계에서는 계약금액 1,147억 원을 114억 원으로 쓴 기사를 실제로 잡아 게시를 막았습니다.'),
        ('pub', '발행인이 가장 높이 사는 대목이 바로 그 검증 게이트입니다. 언론사에게 이 칸은 기능이 아니라 신뢰입니다.'))))

# 숫자
def bar(lbl, a, b, unit, mx, note, better='down'):
    pa, pb = 100 * a / mx, 100 * b / mx
    return (f'<div class="nb"><div class="nh"><b>{esc(lbl)}</b><span class="small muted">{esc(note)}</span></div>'
            f'<div class="nrow"><span class="nl">전</span><div class="track"><div class="fill" style="width:{pa:.1f}%;background:#c9b8a8"></div></div><span class="num nv">{a:,}{unit}</span></div>'
            f'<div class="nrow"><span class="nl">후</span><div class="track"><div class="fill" style="width:{max(pb,0.6):.1f}%;background:#13733a"></div></div><span class="num nv">{b:,}{unit}</span></div></div>')
cov = [('자동 발행 활성', 51, '#13733a'), ('실적 별도 경로', 2, '#1e55c8'), ('기사 경로 미연결', 52, '#c8cfd6')]
covbar = '<div class="covbar">' + ''.join(f'<div style="flex:{n};background:{c}" title="{t} {n}종"></div>' for t, n, c in cov) + '</div>' + \
         '<div class="covleg">' + ''.join(f'<span><i style="background:{c}"></i>{t} <b class="num">{n}종</b></span>' for t, n, c in cov) + '</div>'
B.append(lv('nums', '숫자로 본 변화 — 리포트에 적힌 전후 값',
 '<div class="nums">'
 + bar('첫 클릭 지연', 28000, 126, 'ms', 28000, 'S4 · 5/20 캐시 미리 올리기')
 + bar('공시 요약 대기', 30, 5, '초', 30, 'S4 · 5/28 (캐시 hit는 1초 이내)')
 + bar('Company Story 검색', 2000, 10, 'ms', 2000, 'S7 · 10/6')
 + bar('카드 지원 공시 유형', 77, 105, '종', 105, 'S6 · 9/10', 'up')
 + '</div>'
 '<h3>자동 발행으로 이어진 정도 — 관리 대상 105종 중</h3>' + covbar
 + '<p class="fn">11/18 리포트 본문 표 기준(51 + 2 + 52 = 105종). 같은 리포트 제목에는 “51/108”로 적혀 있어 분모가 다릅니다 — “확인할 것” 참조.</p>'
 '<div class="kpis k5" style="margin-top:16px">'
 '<div class="kpi g"><b>5,101</b><span>LLM 기사 검증 통과 / 운영 기준 5,197건 (10/29)</span></div>'
 '<div class="kpi i"><b>998</b><span>1,000건 표본 검증 중 정상 (10/29)</span></div>'
 '<div class="kpi a"><b>27,262</b><span>분류를 마친 2025년 이전 게시물 (10/28)</span></div>'
 '<div class="kpi m"><b>11,514</b><span>공시별 주가 반응 계산 건수, Tier1 10종목 (10/6)</span></div>'
 '<div class="kpi r"><b>$78.54</b><span>OpenAI 지출, 25년 11월 말 ~ 26년 3월 (4/1)</span></div></div>'))

# 스테이지 상세
sd = []
for s in STAGES:
    refs = ''.join(f'<li><span class="num">{a}</span> <a href="{NOTION}{u}" target="_blank" rel="noopener">{esc(t)}</a></li>' for a, t, u in s['refs'])
    sd.append(f'<article class="stg" id="{s["k"]}"><div class="lvhead"><span class="hexno">S{s["n"]}</span><div><h3 style="margin:0">{esc(s["name"])} {chip(s["st"], s["stl"])}</h3>'
              f'<div class="small muted num">{s["s"]} ~ {s["e"]}</div></div></div>'
              + talk(*([('kim', esc(x)) for x in REPS[s['k']]] + [('pub', esc(s['say']))])) +
              f'<div class="shead"><dl><dt>관문</dt><dd>{esc(s["gate"])}</dd><dt>결과</dt><dd>{esc(s["gres"])}</dd><dt>산출물</dt><dd>{esc(s["out"])}</dd></dl></div>'
              '<h4>김 연구원이 한 일</h4><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in s['did']) + '</ul>'
              f'<div class="insight"><p class="a"><b>걸린 점 · </b>{esc(s["issue"])}</p></div>'
              f'<details class="abbr"><summary>원문 데일리 리포트 {len(s["refs"])}건 (사내 노션)</summary><ul class="refsm">{refs}</ul></details></article>')
B.append(lv('stages', '스테이지별 보기 — S1부터 S8까지', ''.join(sd)))

# 다음 단계
nx = ''.join(f'<div class="planbox" id="{p["k"]}"><h4>{chip("plan","예정")} {esc(p["name"])}</h4><p>{esc(p["body"])}</p><p class="small muted">근거 · {esc(p["src"])}</p></div>' for p in PLANS)
B.append(lv('next', '다음 단계 — 리포트에 적힌 “앞으로 할 일”', nx
 + talk(('kim', '다음 작업으로 105종 자동 포스팅, 관심종목 피드·이전 공시 비교, 미국 증시 확장의 방향 정리가 완료됐습니다. 일정은 아직 정하지 않았습니다. 이를 보고합니다.'),
        ('pub', '방향은 있지만 일정표가 없어서, 발행인이 여기서 날짜를 지어내지 않았습니다. 사이트 구조 개편까지 네 갈래의 순서와 날짜를 다음 관문에서 함께 정하겠습니다.'))))

# 사이트 개편
RENO = [
 ('증권기사 (유가증권·코스닥)', '공시봇 23개가 틀에 맞춰 찍은 짧은 기사', '검증 게이트를 통과한 LLM 공시기사 · 51종 → 105종', 'S8 · p1'),
 ('(없음)', '—', '기업 페이지 = Company Story — 공시 타임라인·주가 반응·카드', 'S7'),
 ('(없음)', '—', '관심종목 피드 · 이전 공시와 비교', 'p2'),
 ('과거 공시기사', '2025년 이전 27,262건이 그대로 공개', '1,210건 비공개 추천 · 원천 데이터와 백업은 보존 · 시범 10건 검증 완료', 'S8'),
 ('주가지수 (코스피·코스닥)', '지수 페이지·시세 위젯', '시세와 공시 반응을 Company Story와 한 화면에서', 'S7'),
 ('미국 주식시장', '개미의 주판 · 미국 증시 Brief · 디지털자산', 'SEC 공시와 미국 주가로 Company Story 확장', 'p3'),
 ('메일링', '공시봇 메일 · 코스피·코스닥 시황 메일 (구독자 4명)', '유지하면서 단계적 경량화', 'S8'),
 ('인사이트 · Index Report · Project', '키워드 해설 · 지표 리포트 · 실험 프로젝트', '이번 리포트 범위 밖 — 개편 범위는 발행인이 정함', '—'),
]
rr = ''.join(f'<tr><td><b>{esc(a)}</b></td><td>{esc(b)}</td><td>{esc(c)}</td><td class="small muted">{esc(e)}</td></tr>' for a, b, c, e in RENO)
B.append(lv('reno', 'money-robo.com 구조 레노베이션 — 지금 메뉴와 바꿀 방향',
 '<p class="lead">장기 목표는 money-robo.com 사이트 구조를 다시 짓는 것입니다. 왼쪽은 지금 사이트(2026-11-19 확인)의 메뉴, 오른쪽은 김 연구원의 결과물이 그 자리를 어떻게 바꿀 수 있는지입니다. 오른쪽 칸은 확정안이 아니라 발행인의 구상(안)입니다.</p>'
 '<div class="tw"><table class="tb"><thead><tr><th>지금 메뉴</th><th>지금 모습</th><th>바꿀 방향 (안)</th><th>근거</th></tr></thead><tbody>' + rr + '</tbody></table></div>'
 + talk(('q', '오래된 기사를 지우면 검색 유입이 줄지 않나요?'),
        ('kim', '같은 내용을 Company Story에서 볼 수 있는 1,210건만 비공개 추천으로 골랐고, 시범 10건의 사전 실행과 되돌리기 검증이 완료됐습니다. 실제 전환은 아직 한 건도 하지 않았습니다. 이를 보고합니다.'),
        ('pub', '삭제가 아니라 비공개 전환이고 원본은 남습니다. 기존 기사 URL과 검색 유입에 주는 영향을 확인한 다음 넓힐지 정하겠습니다.'))))

# 확인할 것
RISK = [
 ('이미지 업로드 장애', 'Cafe24 WordPress 미디어 업로드 HTTP 500이 10/28부터 이어짐. 블로그에 못 실린 공시 13건 대기. 외부(호스팅) 복구 대기 중.', 'r'),
 ('코드 원격 저장소 없음', '8/27 점검에서 서비스 코드 저장소에 원격(origin)이 없음을 확인. 서버 한 곳에만 있는 상태라 백업 위치 결정이 필요.', 'r'),
 ('HTTP 운영', '관리자 쿠키 Secure 옵션을 꺼 둔 상태. HTTPS로 옮길 때 함께 켜야 함 (7/14).', 'a'),
 ('개발 도구·LLM 비용', 'Cursor 추가 한도 10달러 소진(9/17), 남은 개발에 5천만~1억 토큰 추정. OpenAI 사용량은 서버 자체 로그 기준이며 조직 Usage API는 미연동.', 'a'),
 ('보류한 공시', '주주총회소집공고(3/11 PENDING), 단기차입금 감소(필수 정보 부족), 감자 완료 1건(해석 기준 차이)은 검증을 위해 발행 보류.', 'a'),
 ('표기 불일치', '11/18 리포트 제목은 “51/108”, 본문 표는 전체 105종. 9/10 리포트는 카드 가치 유형 지원률을 97.93%와 96.94% 두 값으로 적음. 기준을 하나로 맞출 필요.', 'm'),
 ('계정 정보 기록', '일부 데일리 리포트 본문에 운영 계정 정보가 그대로 적혀 있음. 이 쪽에는 옮기지 않았고, 노션 원문 정리와 비밀번호 교체를 권함.', 'r'),
]
rk = ''.join(f'<p class="{c}"><b>{esc(a)} · </b>{esc(b)}</p>' for a, b, c in RISK)
B.append(lv('risk', '확인할 것 — 발행인이 짚어 둔 위험과 빈칸', '<div class="insight rk">' + rk + '</div>'))

# 발행인 판단
REV = [
 ('r1', '다음 단계 네 갈래(105종·관심종목·미장·개편)의 우선순위를 정한다', '김 연구원 리포트에는 방향만 있고 날짜가 없음'),
 ('r2', '과거 공시기사 1,210건 비공개 전환을 시범 10건 다음 단계로 넓힌다', '검색 유입 영향 확인 후'),
 ('r3', '서비스 코드의 원격 백업 저장소를 정한다', '회사 GitHub 조직 또는 별도 백업 서버'),
 ('r4', 'Cafe24 이미지 업로드 장애의 대안(호스팅 이전 또는 외부 이미지 저장소)을 검토한다', '미게시 13건이 걸려 있음'),
 ('r5', '개발 도구·LLM 월 예산을 따로 잡는다', 'Cursor 한도 소진으로 개발이 멈춘 전례'),
 ('r6', '자동 발행 하루 한도(expansion 4건, 단일판매 5건)를 유지할지 늘릴지 정한다', '품질 게이트는 그대로 두는 전제'),
]
rv = ''.join(f'<div class="ri" data-id="{i}"><div class="rqq">{esc(q)}<small>{esc(n)}</small></div><div class="ro">'
             '<button type="button" data-v="agree" aria-pressed="false">동의</button><button type="button" data-v="fix" aria-pressed="false">수정 필요</button>'
             '<button type="button" data-v="talk" aria-pressed="false">논의</button><input type="text" placeholder="한 줄 메모" aria-label="메모"></div></div>' for i, q, n in REV)
B.append(lv('review', '발행인 판단 — 다음 관문에서 정할 것',
 talk(('kim', '11/18 기준 미해결 사항 정리가 완료됐습니다. 이미지 업로드 장애로 13건 대기, 단기차입금 감소 등 보류 공시, 개발 도구 비용이 남아 있습니다. 이를 보고합니다.'),
        ('pub', '아래 여섯 가지를 다음 회의 안건으로 올립니다. 단추를 누르면 이 브라우저에만 저장되고, 아래 “판단 내보내기”로 글로 옮길 수 있습니다.'))
 + '<div class="review"><h4>안건 6개</h4>' + rv + '</div>'
 '<div class="ctrl"><button type="button" class="bt" id="revCopy">판단 내보내기 (복사)</button><button type="button" class="bt" id="revReset">초기화</button><span class="small muted" id="revMsg"></span></div>'))

# 요청 모음
B.append(lv('reqs', '요청 모음 — 이 쪽을 고칠 곳',
 say('box', '고칠 곳이 보이면 적어 주세요. 제목 옆 “요청” 단추를 누르면 어느 부분인지 자동으로 채워집니다. 요청은 이 브라우저에만 저장됩니다.')
 + '<div class="rq" id="rqForm"><div class="step"><b>어디</b><div><select id="rqSec" class="bt" style="width:100%"></select></div></div>'
 '<div class="step"><b>무엇을</b><div class="opts" id="rqKind"></div></div>'
 '<div class="step"><b>내용</b><div><textarea id="rqText" placeholder="예: S8 기간을 11/19까지로 늘려 주세요."></textarea></div></div>'
 '<div class="step"><b></b><div class="opts"><button type="button" class="bt primary" id="rqAdd">요청 추가</button><button type="button" class="bt" id="rqCopy">전체 복사</button></div></div></div>'
 '<ul class="rqlist" id="rqList"></ul>', req=False))

# 지식 색인
KG = [
 ('Company Story', '서비스', '기업별 공시 타임라인·카드·주가 반응을 한 화면에 모은 새 서비스. S7에서 이름이 붙음.', 's7'),
 ('MCP', '기술', 'AI가 기능을 “도구(tool)”로 불러 쓰게 하는 연결 방식. S4에서 공시 요약을 tool로 감쌈.', 's4'),
 ('fallback', '기술', '새 경로가 실패하면 예전 방식으로 저절로 돌아가는 안전장치. S4.', 's4'),
 ('feature flag', '기술', '코드를 고치지 않고 환경변수로 기능을 켜고 끄는 스위치. USE_MCP_SUMMARY 등.', 's4'),
 ('단순 공시형', '구조', '본문 한 쪽을 읽고 표·문장을 뽑아 요약하는 공시. 단일판매·증자·CB 등.', 's4'),
 ('복합 보고서형', '구조', '목차 → 섹션을 골라 읽는 공시. 사업·반기·분기보고서.', 's4'),
 ('structured card', '화면', '요약 문장 대신 핵심 숫자를 칸에 넣어 보여 주는 공시 카드. 105종 지원.', 's6'),
 ('backfill', '데이터', '새 기능을 만든 뒤 과거 공시에도 거슬러 적용하는 작업.', 's6'),
 ('Event Study', '분석', '공시 뒤 +1·+3·+5·+10·+20일 주가 수익률을 재는 분석. Tier1 10종목 11,514건.', 's7'),
 ('검증 게이트', '품질', 'LLM 기사의 금액·수치·필수 항목을 원문과 대조해 틀리면 게시를 막는 단계.', 's8'),
 ('expansion 버킷', '운영', '자동 발행을 유형 묶음별로 나눈 단위. 버킷별·전체 일일 한도가 있음.', 's8'),
 ('아카이브 정책', '운영', '오래된 공시기사를 지우지 않고 비공개로 돌리며 원본은 보존하는 원칙.', 's8'),
 ('Superpowers + Ralph Loop', '개발 방식', '계획→구현→테스트→검증을 반복시키는 AI 개발 방식. 10/1 도입.', 's7'),
 ('DART', '데이터', '금융감독원 전자공시시스템. 모든 공시 원문의 출처.', 's2'),
 ('GPT-4o-mini', '모델', 'S1 기업개황 정리에 쓴 OpenAI 모델.', 's1'),
]
B.append(lv('kg', '찾아보기 — 이 쪽에 나온 말',
 '<div class="kgbar"><input type="search" id="kgQ" placeholder="낱말로 찾기 (예: MCP, 카드, 검증)" aria-label="낱말 찾기"></div>'
 '<div class="kglist" id="kgList">' + ''.join(f'<div class="kgitem" data-k="{esc((a+" "+b+" "+c).lower())}"><div class="t"><b>{esc(a)}</b><span class="ty">{esc(b)}</span><a class="small" href="#{s}">{s.upper()}</a></div><p>{esc(c)}</p></div>' for a, b, c, s in KG) + '</div>', req=False))

# 출처
allrefs = sorted({(a, t, u) for s in STAGES for a, t, u in s['refs']})
TITLE_ONLY = {'2f617a4520ed805d8601d4e97c4b50b5','31217a4520ed80279e0ae3a90881d2d8','39717a4520ed80d080f2c84dbebfe43e','3b217a4520ed8067a751e61295b03396'}
nbody = sum(1 for a,t,u in allrefs if u not in TITLE_ONLY)
B.append(lv('src', '출처와 읽는 법',
 '<p>이 쪽의 모든 사실과 숫자는 김 연구원의 노션 데일리 리포트(M-Robo : Report › #2 › 데일리 리포트)에서 왔습니다. 2025-11-18부터 2026-11-18까지 139건 가운데 아래 '
 f'{len(allrefs)}건을 스테이지의 근거로 골랐습니다. 그중 {nbody}건은 본문을 읽었고, {len(allrefs)-nbody}건은 제목과 날짜만 썼습니다. 나머지 리포트도 제목과 날짜로 스테이지를 나누는 데 썼습니다. 노션 링크는 사내 워크스페이스 권한이 있어야 열립니다.</p>'
 '<div class="tw"><table class="tb"><thead><tr><th>날짜</th><th>리포트</th><th>읽은 범위</th></tr></thead><tbody>'
 + ''.join(f'<tr><td class="num">{a}</td><td><a href="{NOTION}{u}" target="_blank" rel="noopener">{esc(t)}</a></td><td class="small">{"제목·날짜" if u in TITLE_ONLY else "본문"}</td></tr>' for a, t, u in allrefs)
 + '</tbody></table></div>'
 '<ul class="small muted"><li>사이트 메뉴 구조: <a href="https://money-robo.com/" target="_blank" rel="noopener">money-robo.com</a> (2026-11-19 확인)</li>'
 '<li>“김 연구원” 말풍선은 해당 데일리 리포트의 내용을 발행인이 한두 문장으로 요약한 것입니다. 원문 표현 그대로가 아닙니다.</li>'
 '<li>개편 방향 표의 오른쪽 칸과 관문 이름은 발행인의 해석입니다. 원 리포트에 없는 날짜·수치는 넣지 않았습니다.</li>'
 '<li>테스트 서버 주소, 관리자·개발 도구 계정 정보는 의도적으로 옮기지 않았습니다.</li></ul>', req=False))

B.append('<footer><div class="wrap"><p><b>공시봇에서 Company Story까지 — 발행인이 본 1년의 로드맵</b><br>글 · Money-Robo 발행인 &nbsp;|&nbsp; 결과물 · 김 연구원 (데일리 리포트 2025-11-18 ~ 2026-11-18) &nbsp;|&nbsp; 기준일 2026-11-18</p></div></footer>'
         '<button type="button" id="roboFab" aria-label="요청 모음으로 가기">' + avatar('box', 40) + '<span>수정 요청</span></button>')

EXTRA = r"""
:root{--accent:#0b5c7a;--c-robo:#6b4fa0}
.say svg.who{width:64px;height:64px;flex:none;border-radius:50%}
.talk .say svg.who{width:52px;height:52px}
.say[data-who=kim] .name{color:#2f6f9e}.say[data-who=pub] .name{color:#0b5c7a}.say[data-who=q] .name{color:#b4532a}.say[data-who=rec] .name{color:#3d6b2f}.say[data-who=box] .name{color:#6b4fa0}
header.hero::after{background:repeating-linear-gradient(0deg,rgba(11,92,122,.07) 0 6px,transparent 6px 12px),repeating-linear-gradient(90deg,rgba(19,115,58,.06) 0 6px,transparent 6px 12px)}
.st{display:inline-block;font-size:12px;font-weight:700;padding:2px 9px;border-radius:999px;border:1.5px solid;vertical-align:middle;white-space:nowrap;line-height:1.5}
.st.run{color:#1e55c8;border-color:#1e55c8;background:#e6eefb}.st.plan{color:#5b6874;border-color:#8a96a3;border-style:dashed;background:#fff}
.st.done{color:#fff;border-color:#13733a;background:#13733a}
.mapc{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin:16px 0}
.mapc a.card{display:block;border:1px solid var(--rule);border-radius:14px;padding:16px 18px;text-decoration:none;color:var(--text);background:#fff;transition:border-color .15s,transform .15s}
.mapc a.card:hover,.mapc a.card:focus-visible{border-color:#1e55c8;transform:translateY(-2px)}
.mapc a.card b{display:block;font-size:16px;margin:6px 0 4px}.mapc a.card span.d{font-size:14px;color:var(--muted);line-height:1.6;display:block}
.mapc a.card.plan{border-style:dashed;background:#fbfcfd}
.shead{border:1px solid var(--rule);border-radius:14px;padding:14px 18px;margin:14px 0;background:#fbfcfd}
.shead dl{display:grid;grid-template-columns:80px 1fr;gap:6px 14px;margin:0}.shead dt{font-weight:700;color:var(--muted)}.shead dd{margin:0}
.planbox{border:1.5px dashed #8a96a3;border-radius:14px;padding:16px 18px;margin:14px 0;background:#fbfcfd;scroll-margin-top:70px}
.planbox h4{margin:0 0 6px;font-size:17px}
.stg{border-top:1px dashed var(--rule);padding:28px 0 18px;scroll-margin-top:60px}.stg:first-child{border-top:0;padding-top:6px}
.stg h4{margin:14px 0 4px;font-size:15px;color:var(--muted)}.stg ul{margin:4px 0 8px;padding-left:22px}
.refsm{font-size:14px;margin-top:6px}
.sm4{display:grid;grid-template-columns:repeat(5,1fr);gap:22px;margin:14px 0}
.sm4 .st4{position:relative;border:1px solid var(--rule);border-radius:12px;padding:12px;background:#fff}
.sm4 .st4:not(:last-child)::after{content:"→";position:absolute;right:-19px;top:40%;font-size:20px;font-weight:800;color:#0b5c7a}
.sm4 .st4 h5{margin:0 0 6px;font-size:15px}.sm4 .st4 h5 i{font-style:normal;display:inline-block;width:22px;height:22px;line-height:22px;text-align:center;border-radius:50%;background:#0b5c7a;color:#fff;font-size:12px;margin-right:6px}
.sm4 p{font-size:13.5px;line-height:1.6;margin:6px 0 0;color:var(--muted)}
.flowbox.panel svg{min-width:820px}
.nums{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0 18px}
.nb{border:1px solid var(--rule);border-radius:12px;padding:12px 16px;background:#fff}
.nh{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;margin-bottom:6px}
.nrow{display:grid;grid-template-columns:22px 1fr 90px;gap:8px;align-items:center;margin:4px 0;font-size:14px}
.nrow .track{height:14px;background:#f1f4f7;border-radius:4px;position:relative;overflow:hidden}
.nrow .fill{position:absolute;top:0;bottom:0;left:0;border-radius:4px}
.nrow .nv{text-align:right;font-weight:700}.nl{color:var(--muted);font-size:13px}
.covbar{display:flex;height:26px;border-radius:8px;overflow:hidden;border:1px solid var(--rule);margin:8px 0}
.covleg{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:14px}.covleg i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.rk p{margin:6px 0}
.review .rqq{font-weight:500;margin-bottom:6px}.review .rqq small{display:block;font-weight:400;color:var(--muted);font-size:13.5px}
td.nw{white-space:nowrap}
.rqpin{display:inline-flex;align-items:center;margin-left:10px;vertical-align:middle;font:inherit;font-size:12px;font-weight:600;color:var(--c-robo);background:#fff;border:1px solid var(--c-robo);border-radius:999px;padding:1px 10px;cursor:pointer;line-height:1.6}
.rqpin:hover,.rqpin:focus-visible{background:#f1ecf9}
.rq{border:1.5px solid var(--c-robo);border-radius:16px;padding:18px 20px;background:#faf8fd;margin:14px 0}
.rq .step{display:grid;grid-template-columns:80px 1fr;gap:10px;align-items:start;margin:10px 0}
.rq .step>b{font-size:14px;color:var(--c-robo);padding-top:6px}
.rq .opts{display:flex;flex-wrap:wrap;gap:6px}
.rq .bt.rqc[aria-pressed="true"]{background:var(--c-robo);border-color:var(--c-robo);color:#fff}
.rq .bt.primary{background:var(--c-robo);border-color:var(--c-robo)}
.rq textarea{width:100%;min-height:70px;border:1px solid var(--rule);border-radius:10px;padding:10px 12px;font:inherit;font-size:15px;background:#fff}
.rqlist{list-style:none;padding:0;margin:10px 0}.rqlist li{border:1px solid var(--rule);border-radius:10px;padding:10px 12px;margin:6px 0;background:#fff;font-size:14.5px;line-height:1.7}
.rqlist li .rqb{display:flex;gap:6px;margin-top:6px}.rqlist li.done{opacity:.55}
#roboFab{position:fixed;right:16px;bottom:16px;z-index:60;display:flex;align-items:center;gap:8px;background:#fff;border:2px solid var(--c-robo);border-radius:999px;padding:4px 14px 4px 4px;font:inherit;font-weight:700;color:var(--c-robo);box-shadow:0 4px 16px rgba(107,79,160,.22);cursor:pointer;font-size:14px}
#roboFab svg{width:40px;height:40px;border-radius:50%}
section.level{scroll-margin-top:56px}
@media (max-width:980px){.sm4{grid-template-columns:1fr 1fr}.sm4 .st4::after{display:none}}
@media (max-width:760px){.nums{grid-template-columns:1fr}}
@media (max-width:600px){#roboFab span{display:none}#roboFab{padding:4px}.rq .step{grid-template-columns:1fr}.shead dl{grid-template-columns:1fr}}
@media print{nav.top,#roboFab,#prog,.rqpin{display:none}}
"""

JS = r"""
(function(){
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var KEY='mrobo_roadmap_v1',M={};
try{M=JSON.parse(localStorage.getItem(KEY)||'{}')||{}}catch(e){M={}}
function save(){try{localStorage.setItem(KEY,JSON.stringify(M))}catch(e){}}
function copy(t,msg){if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(function(){msg&&msg('복사했습니다.')},function(){fallback()})}else fallback();
 function fallback(){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy');msg&&msg('복사했습니다.')}catch(e){msg&&msg('복사하지 못했습니다.')}a.remove()}}
// 진행 막대
var pg=$('#prog');window.addEventListener('scroll',function(){var h=document.documentElement;pg.style.width=(100*h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight))+'%'},{passive:true});
// 판단
M.rev=M.rev||{};
$$('.review .ri').forEach(function(ri){var id=ri.dataset.id,st=M.rev[id]||{};
 $$('button',ri).forEach(function(b){b.setAttribute('aria-pressed',st.v===b.dataset.v);b.onclick=function(){st.v=(st.v===b.dataset.v)?'':b.dataset.v;M.rev[id]=st;save();$$('button',ri).forEach(function(x){x.setAttribute('aria-pressed',st.v===x.dataset.v)})}});
 var inp=$('input',ri);inp.value=st.m||'';inp.oninput=function(){st.m=inp.value;M.rev[id]=st;save()}});
var LB={agree:'동의',fix:'수정 필요',talk:'논의'};
$('#revCopy').onclick=function(){var out=['[발행인 판단] Money-Robo 로드맵 (기준일 2026-11-18)'];
 $$('.review .ri').forEach(function(ri,i){var st=M.rev[ri.dataset.id]||{};out.push((i+1)+'. '+$('.rqq',ri).firstChild.textContent+' — '+(LB[st.v]||'미정')+(st.m?' / '+st.m:''))});
 copy(out.join('\n'),function(t){$('#revMsg').textContent=t})};
$('#revReset').onclick=function(){M.rev={};save();$$('.review button').forEach(function(b){b.setAttribute('aria-pressed','false')});$$('.review input').forEach(function(i){i.value=''});$('#revMsg').textContent='초기화했습니다.'};
// 요청
var KINDS=[['fix','내용 수정'],['add','내용 추가'],['num','숫자·근거 확인'],['easy','더 쉽게'],['date','날짜·일정'],['ask','질문']];
M.req=M.req||[];var kind='fix';
var secs=['이 쪽 전체'];$$('section.level h2').forEach(function(h){var t=h.firstChild.textContent.trim();if(secs.indexOf(t)<0)secs.push(t)});
$$('.stg').forEach(function(a){secs.push($('h3',a).firstChild.textContent.trim())});
$('#rqSec').innerHTML=secs.map(function(s){return '<option>'+s.replace(/</g,'&lt;')+'</option>'}).join('');
function paintK(){$('#rqKind').innerHTML=KINDS.map(function(k){return '<button type="button" class="bt rqc" data-k="'+k[0]+'" aria-pressed="'+(kind===k[0])+'">'+k[1]+'</button>'}).join('');
 $$('#rqKind button').forEach(function(b){b.onclick=function(){kind=b.dataset.k;paintK()}})}
paintK();
function lab(k){for(var i=0;i<KINDS.length;i++)if(KINDS[i][0]===k)return KINDS[i][1];return k}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function paintL(){var L=$('#rqList');if(!M.req.length){L.innerHTML='<li class="muted">아직 요청이 없습니다.</li>';return}
 L.innerHTML=M.req.map(function(r,i){return '<li class="'+(r.done?'done':'')+'"><b>#'+(i+1)+' '+esc(r.sec)+'</b> · '+lab(r.kind)+'<br>'+esc(r.text)+'<div class="rqb"><button type="button" class="bt sm" data-a="done" data-i="'+i+'">'+(r.done?'되살리기':'처리 완료')+'</button><button type="button" class="bt sm" data-a="del" data-i="'+i+'">지우기</button></div></li>'}).join('');
 $$('#rqList button').forEach(function(b){b.onclick=function(){var i=+b.dataset.i;if(b.dataset.a==='del')M.req.splice(i,1);else M.req[i].done=!M.req[i].done;save();paintL()}})}
paintL();
$('#rqAdd').onclick=function(){var t=$('#rqText').value.trim();if(!t){$('#rqText').focus();return}M.req.push({sec:$('#rqSec').value,kind:kind,text:t,at:new Date().toISOString().slice(0,10)});save();$('#rqText').value='';paintL()};
function reqText(){return ['[수정·보완 요청] Money-Robo 로드맵'].concat(M.req.map(function(r,i){return '#'+(i+1)+(r.done?' (처리 완료)':'')+' ['+r.sec+'] '+lab(r.kind)+' — '+r.text+' ('+r.at+')'})).join('\n')}
$('#rqCopy').onclick=function(){copy(reqText())};
$$('.rqpin').forEach(function(p){p.onclick=function(){var s=p.dataset.sec;$('#rqSec').value=s;document.getElementById('reqs').scrollIntoView();setTimeout(function(){$('#rqText').focus()},400)}});
$('#roboFab').onclick=function(){document.getElementById('reqs').scrollIntoView();setTimeout(function(){$('#rqText').focus()},400)};
// 찾아보기
$('#kgQ').oninput=function(){var q=this.value.trim().toLowerCase();$$('#kgList .kgitem').forEach(function(it){it.style.display=(!q||it.dataset.k.indexOf(q)>=0)?'':'none'})};
})();
"""

page = ('<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
 '<title>공시봇에서 Company Story까지 — 발행인이 본 1년의 로드맵</title>'
 '<meta name="description" content="Money-Robo 발행인이 김 연구원의 데일리 리포트(2025-11-18 ~ 2026-11-18)를 여덟 스테이지 로드맵으로 정리한 브리핑">'
 '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">'
 '<style>' + BASE + EXTRA + '</style></head><body>' + ''.join(B) + '<script>' + JS + '</script></body></html>')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'), 'w', encoding='utf-8').write(page)
print(len(page), 'bytes;', len(allrefs), 'refs')
