# -*- coding: utf-8 -*-
import json
import re

with open(r'C:\Users\pillp\.gemini\antigravity\scratch\rumi-unplugged-edu\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Load mode translations from update_multilang.py
from update_multilang import mode_translations

# 1. Update lessonsData by injecting the 4 Mongolian fields for each id
for m_id, trans in mode_translations.items():
    # find the object for this id
    pattern = rf'(\{{\s*id:\s*{m_id},.*?)(\btitle:\s*\")'
    def replacer(m):
        prefix = m.group(1)
        suffix = m.group(2)
        extra = f"""mongolFeedback: {json.dumps(trans['feedback'], ensure_ascii=False)},
        mongolOperation: {json.dumps(trans['operation'], ensure_ascii=False)},
        mongolStory: {json.dumps(trans['story'], ensure_ascii=False)},
        mongolTip: {json.dumps(trans['tip'], ensure_ascii=False)},
        """
        # If already present, don't duplicate
        if "mongolFeedback:" in prefix:
            return m.group(0)
        return prefix + extra + suffix

    text = re.sub(pattern, replacer, text, flags=re.DOTALL)

# 2. Update renderAccordion
old_render_block = """                  <!-- 모드 선택 피드백 & 실제 하드웨어 동작 가이드 -->
                  <div class="detail-block block-action">
                    <div class="detail-label">
                      <span>🎮</span> 모드 선택 피드백 및 실제 동작 방법 (Operation Guide)
                    </div>
                    <div class="detail-text" style="display:flex; flex-direction:column; gap:8px;">
                      <div style="background:white; padding:10px 14px; border-radius:8px; border:1px solid #99f6e4; font-weight:700; color:#0f766e; display:flex; align-items:flex-start; gap:8px;">
                        <span style="font-size:1.1rem; line-height:1.2;">🔔</span>
                        <span style="line-height:1.5;">${item.selectFeedback}</span>
                      </div>
                      <div style="line-height:1.65; color:var(--gray-800); padding:2px 4px;">
                        <strong style="color:#0f766e;">▶ 하드웨어 실제 동작 메커니즘:</strong> ${item.operationMethod}
                      </div>
                    </div>
                  </div>

                  ${remoteGuideHtml}

                  ${videoBlockHtml}

                  <div class="detail-block block-principle">
                    <div class="detail-label">
                      <span>⚙️</span> 핵심 원리 (Computer Science Principle)
                    </div>
                    <div class="detail-text">
                      <strong>${item.principle}</strong>
                      <div class="mongol-trans" style="margin-top:6px; color:#15803d; font-weight:500;">🇲🇳 ${item.mongolPrinciple}</div>
                    </div>
                  </div>

                  <div class="detail-block block-story">
                    <div class="detail-label">
                      <span>🗣️</span> 교실 속 스토리텔링 (Storytelling Guide)
                    </div>
                    <div class="detail-text">
                      <blockquote class="story-quote">
                        ${item.storytelling}
                      </blockquote>
                    </div>
                  </div>

                  ${soundDemoHtml}
                  ${remoconBlockHtml}

                  <div class="detail-block block-guide">
                    <div class="detail-label">
                      <span>💡</span> 유치원·초등 저학년 교사용 수업 꿀팁 & 지도 가이드
                    </div>
                    <div class="detail-text">
                      ${item.tip}
                    </div>
                  </div>"""

new_render_block = """                  <!-- 모드 선택 피드백 & 실제 하드웨어 동작 가이드 -->
                  <div class="detail-block block-action">
                    <div class="detail-label">
                      <span>🎮</span>
                      <span class="ko-txt">모드 선택 피드백 및 실제 동작 방법 (Operation Guide)</span>
                      <span class="mn-txt">Горим сонголтын хариу үйлдэл ба бодит ажиллах заавар (Operation Guide)</span>
                    </div>
                    <div class="detail-text" style="display:flex; flex-direction:column; gap:8px;">
                      <div style="background:white; padding:10px 14px; border-radius:8px; border:1px solid #99f6e4; font-weight:700; color:#0f766e; display:flex; align-items:flex-start; gap:8px;">
                        <span style="font-size:1.1rem; line-height:1.2;">🔔</span>
                        <div style="line-height:1.5;">
                          <span class="ko-txt">${item.selectFeedback}</span>
                          <span class="mn-txt">${item.mongolFeedback || item.selectFeedback}</span>
                          <div class="mn-sub">🇲🇳 ${item.mongolFeedback || ''}</div>
                        </div>
                      </div>
                      <div style="line-height:1.65; color:var(--gray-800); padding:2px 4px;">
                        <strong style="color:#0f766e;">
                          <span class="ko-txt">▶ 하드웨어 실제 동작 메커니즘:</span>
                          <span class="mn-txt">▶ Төхөөрөмжийн бодит ажиллах зарчим:</span>
                        </strong> 
                        <span class="ko-txt">${item.operationMethod}</span>
                        <span class="mn-txt">${item.mongolOperation || item.operationMethod}</span>
                        <div class="mn-sub">🇲🇳 ${item.mongolOperation || ''}</div>
                      </div>
                    </div>
                  </div>

                  ${remoteGuideHtml}

                  ${videoBlockHtml}

                  <div class="detail-block block-principle">
                    <div class="detail-label">
                      <span>⚙️</span>
                      <span class="ko-txt">핵심 원리 (Computer Science Principle)</span>
                      <span class="mn-txt">Үндсэн зарчим (Computer Science Principle)</span>
                    </div>
                    <div class="detail-text">
                      <strong class="ko-txt">${item.principle}</strong>
                      <strong class="mn-txt">${item.mongolPrinciple}</strong>
                      <div class="mn-sub">🇲🇳 ${item.mongolPrinciple}</div>
                    </div>
                  </div>

                  <div class="detail-block block-story">
                    <div class="detail-label">
                      <span>🗣️</span>
                      <span class="ko-txt">교실 속 스토리텔링 (Storytelling Guide)</span>
                      <span class="mn-txt">Анги дахь өгүүллэг (Storytelling Guide)</span>
                    </div>
                    <div class="detail-text">
                      <blockquote class="story-quote">
                        <span class="ko-txt">${item.storytelling}</span>
                        <span class="mn-txt">${item.mongolStory || item.storytelling}</span>
                        <div class="mn-sub">🇲🇳 ${item.mongolStory || ''}</div>
                      </blockquote>
                    </div>
                  </div>

                  ${soundDemoHtml}
                  ${remoconBlockHtml}

                  <div class="detail-block block-guide">
                    <div class="detail-label">
                      <span>💡</span>
                      <span class="ko-txt">유치원·초등 저학년 교사용 수업 꿀팁 & 지도 가이드</span>
                      <span class="mn-txt">Цэцэрлэг, бага ангийн багшид зориулсан хичээлийн зөвлөмж</span>
                    </div>
                    <div class="detail-text">
                      <span class="ko-txt">${item.tip}</span>
                      <span class="mn-txt">${item.mongolTip || item.tip}</span>
                      <div class="mn-sub">🇲🇳 ${item.mongolTip || ''}</div>
                    </div>
                  </div>"""

if old_render_block in text:
    text = text.replace(old_render_block, new_render_block)

# 3. Update header inside accordion item: title with ko-txt and mn-txt
old_header_title = """                  <div class="lesson-title-text">${item.title}</div>
                  <div class="mongol-trans">🇲🇳 ${item.mongolTitle}</div>"""

new_header_title = """                  <div class="lesson-title-text">
                    <span class="ko-txt">${item.title}</span>
                    <span class="mn-txt">${item.mongolTitle}</span>
                  </div>
                  <div class="mn-sub inline">🇲🇳 ${item.mongolTitle}</div>"""

if old_header_title in text:
    text = text.replace(old_header_title, new_header_title)

# 4. Update the bottom script handlers for langSubtitleBtn and langConvertBtn
old_script_lang = """      const langToggleBtn = document.getElementById("langToggleBtn");
      langToggleBtn.addEventListener("click", () => {
        document.body.classList.toggle("show-mongol");
        const isShown = document.body.classList.contains("show-mongol");
        langToggleBtn.innerHTML = isShown 
          ? `<span>🌐</span> 몽골어 보조 자막 끄기` 
          : `<span>🌐</span> 몽골어 보조 자막 켜기`;
      });"""

new_script_lang = """      const subtitleBtn = document.getElementById("langSubtitleBtn");
      const convertBtn = document.getElementById("langConvertBtn");

      function updateLanguageUI() {
        const isFullMn = document.body.classList.contains("lang-mongol-full");
        const isSubOn = document.body.classList.contains("show-mongol-sub");

        if (convertBtn) {
          if (isFullMn) {
            convertBtn.innerHTML = `<span>🇰🇷</span> 한국어로 보기 (Солонгос хэл)`;
            convertBtn.classList.add("active");
          } else {
            convertBtn.innerHTML = `<span>🇲🇳</span> Монгол хэлээр харах`;
            convertBtn.classList.remove("active");
          }
        }

        if (subtitleBtn) {
          if (isSubOn) {
            subtitleBtn.innerHTML = `<span>🌐</span> 몽골어 보조자막 끄기`;
            subtitleBtn.classList.add("active");
          } else {
            subtitleBtn.innerHTML = `<span>🌐</span> 몽골어 보조자막 켜기`;
            subtitleBtn.classList.remove("active");
          }
        }

        const searchInput = document.getElementById("lessonSearch");
        if (searchInput) {
          searchInput.placeholder = isFullMn 
            ? "Хичээлийн нэр, зарчим, мэдрэгч, горимын дугаараар хайх (жишээ: теремин, санах ой, 12-р горим)..."
            : "차시 제목, 핵심 원리, 센서, 모드 번호 검색 (예: 테레민, 메모리, 모드 12, 역산, 오토센싱)...";
        }

        const expandBtn = document.getElementById("expandAllBtn");
        const collapseBtn = document.getElementById("collapseAllBtn");
        if (expandBtn) expandBtn.innerHTML = isFullMn ? `<span>📂</span> Бүгдийг дэлгэх` : `<span>📂</span> 모두 펼치기`;
        if (collapseBtn) collapseBtn.innerHTML = isFullMn ? `<span>📁</span> Бүгдийг хураах` : `<span>📁</span> 모두 접기`;
      }

      if (subtitleBtn) {
        subtitleBtn.addEventListener("click", () => {
          document.body.classList.toggle("show-mongol-sub");
          updateLanguageUI();
        });
      }

      if (convertBtn) {
        convertBtn.addEventListener("click", () => {
          document.body.classList.toggle("lang-mongol-full");
          updateLanguageUI();
        });
      }"""

if old_script_lang in text:
    text = text.replace(old_script_lang, new_script_lang)

with open(r'C:\Users\pillp\.gemini\antigravity\scratch\rumi-unplugged-edu\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied full multilang integration successfully!")
