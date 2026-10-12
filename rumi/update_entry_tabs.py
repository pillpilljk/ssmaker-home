# -*- coding: utf-8 -*-
import re

with open(r'C:\Users\pillp\.gemini\antigravity\scratch\rumi-unplugged-edu\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update filter chips
old_chips = """        <!-- 단원별 필터 칩 -->
        <div class="filter-chips">
          <button class="chip-btn active" data-unit="all">전체 차시 보기 (14)</button>
          <button class="chip-btn" data-unit="video" style="background:#fee2e2; color:#b91c1c; border-color:#fca5a5; font-weight:800;">🎬 시연 영상 있는 모드 (12)</button>
          <button class="chip-btn" data-unit="1단원">1단원: 로봇 기초 & 무선 조종기 (감정/정지/RC/페어링)</button>
          <button class="chip-btn" data-unit="2단원">2단원: 반응 로봇 & 스마트 펫 (회피/일정간격/척력)</button>
          <button class="chip-btn" data-unit="3단원">3단원: 스스로 생각하는 자율주행 (오토센싱/5mm·2cm 라인/스모)</button>
          <button class="chip-btn" data-unit="4단원">4단원: 로봇 창의 음악회 & 예술 (STEAM)</button>
          <button class="chip-btn" data-unit="5단원">5단원 & 마스터: 게임 & 경로 코딩 (기억/역산)</button>
        </div>"""

new_chips = """        <!-- 단원별 필터 칩 -->
        <div class="filter-chips">
          <button class="chip-btn active" data-unit="all">
            <span class="ko-txt">전체 차시 보기 (14)</span>
            <span class="mn-txt">Бүх хичээл (14)</span>
          </button>
          <button class="chip-btn" data-unit="video" style="background:#fee2e2; color:#b91c1c; border-color:#fca5a5; font-weight:800;">
            <span class="ko-txt">🎬 시연 영상 있는 모드 (12)</span>
            <span class="mn-txt">🎬 Бичлэгтэй горимууд (12)</span>
          </button>
          <button class="chip-btn" data-unit="1단원">
            <span class="ko-txt">1단원: 로봇 기초 & 무선 조종기 (감정/정지/RC/페어링)</span>
            <span class="mn-txt">1-р бүлэг: Роботын үндэс & Удирдлага (Сэтгэл хөдлөл/Зогсох/RC/Хослолт)</span>
          </button>
          <button class="chip-btn" data-unit="2단원">
            <span class="ko-txt">2단원: 반응 로봇 & 스마트 펫 (회피/일정간격/척력)</span>
            <span class="mn-txt">2-р бүлэг: Хариу үйлдэлт робот & Тэжээвэр амьтан (Бултах/Зай барих/Түлхэлцэх)</span>
          </button>
          <button class="chip-btn" data-unit="3단원">
            <span class="ko-txt">3단원: 스스로 생각하는 자율주행 (오토센싱/5mm·2cm 라인/스모)</span>
            <span class="mn-txt">3-р бүлэг: Бие даасан жолоодлого (Auto-Sensing/5мм·2см шугам/Сүмо)</span>
          </button>
          <button class="chip-btn" data-unit="4단원">
            <span class="ko-txt">4단원: 로봇 창의 음악회 & 예술 (STEAM)</span>
            <span class="mn-txt">4-р бүлэг: Робот хөгжмийн тоглолт & Урлаг (STEAM)</span>
          </button>
          <button class="chip-btn" data-unit="5단원">
            <span class="ko-txt">5단원 & 마스터: 게임 & 경로 코딩 (기억/역산)</span>
            <span class="mn-txt">5-р бүлэг: Тоглоом & Санах ойн зам кодчлол (Санах ой/Урвуу тооцоолол)</span>
          </button>
        </div>"""

if old_chips in text:
    text = text.replace(old_chips, new_chips)

# 2. Update Tab-Entry Section Header & Subtitle
old_entry_header = """        <div class="section-header">
          <div>
            <h2 class="section-title">💻 [초등부 & 중등 저학년] 엔트리 블록코딩 실습 매뉴얼</h2>
            <p class="section-sub">USB 연결부터 모터, 네오픽셀 RGB LED, 라인트레이서(line/lt/rt) 정밀 교차로 제어 및 격자 미션</p>
          </div>
          <span class="badge-entry">Target: 초등 3~6학년 & 중등 1~2학년</span>
        </div>"""

new_entry_header = """        <div class="section-header">
          <div>
            <h2 class="section-title">
              <span class="ko-txt">💻 [초등부 & 중등 저학년] 엔트리 블록코딩 실습 매뉴얼</span>
              <span class="mn-txt">💻 [Дунд & Ахлах анги] Entry блок кодчлолын дадлагын гарын авлага</span>
            </h2>
            <p class="section-sub">
              <span class="ko-txt">USB 연결부터 모터, 네오픽셀 RGB LED, 라인트레이서(line/lt/rt) 정밀 교차로 제어 및 격자 미션</span>
              <span class="mn-txt">USB Bluetooth холболтоос мотор, NeoPixel RGB LED, шугам дагагч (line/lt/rt) нарийн удирдлага ба тор замын даалгавар</span>
            </p>
            <div class="mn-sub">🇲🇳 Дунд, ахлах анги: Entry блок кодчлолоор 루미 роботыг удирдах практик дадлагын заавар</div>
          </div>
          <span class="badge-entry">Target: 9~14 нас (3~8-р анги)</span>
        </div>"""

if old_entry_header in text:
    text = text.replace(old_entry_header, new_entry_header)

# 3. Update Entry Steps
old_entry_steps = """        <!-- 2. 개발환경 설정 5단계 -->
        <h3 style="font-size: 1.2rem; font-weight:800; color:var(--gray-900); margin: 28px 0 14px; display:flex; align-items:center; gap:8px;">
          <span>🔌</span> 1. 개발환경 설정과 무선 연결 5단계
        </h3>

        <div class="entry-setup-steps">
          <div class="setup-step-box">
            <span class="step-badge">STEP 1</span>
            <h4>USB 드라이버 설치</h4>
            <p>로봇과 컴퓨터 간 통신을 위해 <strong>CH340 / CH341 드라이버</strong>(CH341SER.exe)를 실행하여 설치합니다. (오류 시 UNINSTALL 후 재설치)</p>
          </div>

          <div class="setup-step-box">
            <span class="step-badge">STEP 2</span>
            <h4>엔트리 오프라인 설치</h4>
            <p><strong>playentry.org</strong>에서 PC용 엔트리 프로그램과 함께 <strong>'엔트리 하드웨어 연결 프로그램'</strong>을 다운로드하여 설치합니다.</p>
          </div>

          <div class="setup-step-box">
            <span class="step-badge">STEP 3</span>
            <h4>동글 연결 & 루미 전원 ON</h4>
            <p><strong>블루투스 동글</strong>을 컴퓨터 USB에 꽂고 루미 전원을 켭니다. <em>(동글을 꽂고 바로 루미를 켜면 페어링 속도가 가장 빠릅니다!)</em></p>
          </div>

          <div class="setup-step-box">
            <span class="step-badge">STEP 4</span>
            <h4>하드웨어 '라인코딩' 선택</h4>
            <p>엔트리 하드웨어 창에서 <strong>[라인코딩]</strong>을 찾아 선택하고 연결된 <strong>COM 포트</strong>를 연결합니다. (연결 성공 후 창 최소화)</p>
          </div>

          <div class="setup-step-box">
            <span class="step-badge">STEP 5</span>
            <h4>초록색 블록 & 스피커 테스트</h4>
            <p>엔트리 블록 메뉴에 초록색 라인코딩 블록들이 나타나면 성공! <strong>[스피커 5 옥타브 도 음 0.25초 연주]</strong> 블록으로 첫 소리 테스트를 진행합니다.</p>
          </div>
        </div>"""

new_entry_steps = """        <!-- 2. 개발환경 설정 5단계 -->
        <h3 style="font-size: 1.2rem; font-weight:800; color:var(--gray-900); margin: 28px 0 14px; display:flex; align-items:center; gap:8px;">
          <span>🔌</span> 
          <span class="ko-txt">1. 개발환경 설정과 무선 연결 5단계</span>
          <span class="mn-txt">1. Хөгжүүлэлтийн орчин ба 5 алхамт утасгүй холболт</span>
        </h3>
        <div class="mn-sub">🇲🇳 Entry програм болон Bluetooth Dongle-оор роботоо компьютертэй холбох 5 алхам</div>

        <div class="entry-setup-steps">
          <div class="setup-step-box">
            <span class="step-badge">STEP 1</span>
            <h4>
              <span class="ko-txt">USB 드라이버 설치</span>
              <span class="mn-txt">USB Драйвер суулгах</span>
            </h4>
            <p>
              <span class="ko-txt">로봇과 컴퓨터 간 통신을 위해 <strong>CH340 / CH341 드라이버</strong>(CH341SER.exe)를 실행하여 설치합니다.</span>
              <span class="mn-txt">Компьютер ба робот хоорондын холболтод зориулж <strong>CH340 / CH341 драйвер</strong> (CH341SER.exe) ажиллуулан суулгана.</span>
            </p>
            <div class="mn-sub">🇲🇳 Алхам 1: CH340 драйвер суулгах</div>
          </div>

          <div class="setup-step-box">
            <span class="step-badge">STEP 2</span>
            <h4>
              <span class="ko-txt">엔트리 오프라인 설치</span>
              <span class="mn-txt">Entry офлайн програм суулгах</span>
            </h4>
            <p>
              <span class="ko-txt"><strong>playentry.org</strong>에서 PC용 엔트리 프로그램과 함께 <strong>'엔트리 하드웨어 연결 프로그램'</strong>을 다운로드하여 설치합니다.</span>
              <span class="mn-txt"><strong>playentry.org</strong> сайтаас PC-д зориулсан Entry програм ба <strong>'Entry техник хангамж холболтын програм'</strong>-ыг татаж суулгана.</span>
            </p>
            <div class="mn-sub">🇲🇳 Алхам 2: Entry програм татах</div>
          </div>

          <div class="setup-step-box">
            <span class="step-badge">STEP 3</span>
            <h4>
              <span class="ko-txt">동글 연결 & 루미 전원 ON</span>
              <span class="mn-txt">Dongle холбох & Асаах</span>
            </h4>
            <p>
              <span class="ko-txt"><strong>블루투스 동글</strong>을 컴퓨터 USB에 꽂고 루미 전원을 켭니다. <em>(동글 꽂고 바로 켜면 페어링이 가장 빠릅니다!)</em></span>
              <span class="mn-txt"><strong>Bluetooth Dongle</strong>-ийг USB-д залгаад Румиг асаана. <em>(Залгаад шууд асаахад хамгийн хурдан холбогдоно!)</em></span>
            </p>
            <div class="mn-sub">🇲🇳 Алхам 3: Bluetooth Dongle холбож роботоо асаах</div>
          </div>

          <div class="setup-step-box">
            <span class="step-badge">STEP 4</span>
            <h4>
              <span class="ko-txt">하드웨어 '라인코딩' 선택</span>
              <span class="mn-txt">'Шугам кодчлол' сонгох</span>
            </h4>
            <p>
              <span class="ko-txt">엔트리 하드웨어 창에서 <strong>[라인코딩]</strong>을 찾아 선택하고 연결된 <strong>COM 포트</strong>를 연결합니다.</span>
              <span class="mn-txt">Entry техник хангамжийн цонхноос <strong>[Line Coding]</strong>-г хайж сонгоод харгалзах <strong>COM портыг</strong> холбоно.</span>
            </p>
            <div class="mn-sub">🇲🇳 Алхам 4: Төхөөрөмжүүд дундаас '라인코딩' сонгох</div>
          </div>

          <div class="setup-step-box">
            <span class="step-badge">STEP 5</span>
            <h4>
              <span class="ko-txt">초록색 블록 & 스피커 테스트</span>
              <span class="mn-txt">Ногоон блок & Дуу шалгах</span>
            </h4>
            <p>
              <span class="ko-txt">엔트리 블록 메뉴에 초록색 블록들이 나타나면 성공! <strong>[스피커 5 옥타브 도 음 0.25초 연주]</strong> 블록으로 첫 소리 테스트를 진행합니다.</span>
              <span class="mn-txt">Entry цэсэнд ногоон өнгийн блокууд гарч ирвэл амжилттай! <strong>[5-р октавын До эгшгийг 0.25 сек дуугаргах]</strong> блокоор анхны дуугаа шалгана.</span>
            </p>
            <div class="mn-sub">🇲🇳 Алхам 5: Ногоон блокоор анхны дууг шалгах</div>
          </div>
        </div>"""

if old_entry_steps in text:
    text = text.replace(old_entry_steps, new_entry_steps)

with open(r'C:\Users\pillp\.gemini\antigravity\scratch\rumi-unplugged-edu\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Entry tabs and filter chips updated with Mongolian translations!")
