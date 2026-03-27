#!/usr/bin/env python3
"""
Platform Intelligence 数据爬虫
自动抓取 B站花火、巨量星图、小红书蒲公英、快手磁力聚星 的最新动态
"""

import re
import json
import subprocess
from datetime import datetime

# ============================================================
# 数据源配置 - 你可以在这里修改/添加数据源
# ============================================================

DATA_SOURCE = {
    "bilibili_huohuo": {
        "name": "B站花火",
        "color": "#00A1D6",
        "updates": [
            {
                "title": "B站花火平台开放全行业商业合作，全链路线上化交易升级",
                "url": "https://huahuo.bilibili.com/",
                "summary": "哔哩哔哩花火平台面向全行业开放，助力品牌批量触达、筛选、匹配意向合作UP主，提供安全高效的全链路线上化交易。",
                "source": "B站花火官网",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            # 可以添加更多新闻...
        ],
        "feedback": [
            {
                "title": "花火平台不向UP主收取提成，差异化优势持续吸引创作者入驻",
                "url": "https://socialbeta.com/campaign/13105",
                "summary": "平台不向UP主收提成而向品牌方收费的模式，是其区别于同类平台的核心差异化优势。",
                "source": "SocialBeta"
            },
        ],
        "strengths": [
            "Z世代核心用户群体，社区信任度极高",
            "UP主粉丝粘性强，中长视频种草转化效果突出",
            "弹幕互动文化独特，品牌植入接受度高",
        ],
        "roadmap": ["UP主商业化工具升级", "X火计划营销闭环", "效果分成模式"],
        "insight": "B站花火持续迭代，X火计划实现种草-转化闭环，效果分成和评论区蓝链强化电商转化。"
    },

    "douyin_xingtu": {
        "name": "巨量星图",
        "color": "#FE2C55",
        "updates": [
            {
                "title": "巨量星图持续进化，AIGC工具链不断丰富",
                "url": "https://5gcenter.huanqiu.com/article/4ANBnu4JfCt",
                "summary": "从2018年9月上线以来持续进化，从转化组件上线到明星入驻，再到AIGC创作工具，已成为达人营销领域最成熟的产品平台。",
                "source": "环球网",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
        ],
        "feedback": [
            {
                "title": "关于抖音星图的达人评价：连接创作者和广告主、平台背书安全性高",
                "url": "https://zhuanlan.zhihu.com/p/563562680",
                "summary": "星图是达人接单、获取收益、内容变现的服务平台。达人普遍反映接单流程规范，但头部达人竞争激烈。",
                "source": "知乎"
            },
        ],
        "strengths": [
            "抖音日活超7亿，达人库规模行业第一",
            "算法推荐精准，达人匹配效率行业领先",
            "巨量引擎全域营销整合，一站式投放体验",
        ],
        "roadmap": ["AIGC创作工具", "全域营销闭环", "星广联投升级"],
        "insight": "巨量星图持续深化AIGC工具建设，星广联投、看后搜等新功能显著提升投放效率。"
    },

    "xiaohongshu_pugongying": {
        "name": "小红书蒲公英",
        "color": "#FF2442",
        "updates": [
            {
                "title": "小红书2026年平台功能大更新：合作广场、撬客管理、KOS员工号等10项调整",
                "url": "https://help.reditorapp.com/content/260104",
                "summary": "涵盖广告投放、客户管理、合作广场、撬客管理、KOS员工号等10项重要功能调整，进一步完善商业化基础设施。",
                "source": "Reditor帮助",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
        ],
        "feedback": [
            {
                "title": "新手必看！蒲公英品牌合作下单全流程拆解",
                "url": "https://zhuanlan.zhihu.com/p/1914386362947314623",
                "summary": "接收合作邀约→确认合作条款→创作内容→提交审核→发布上线→等待结算。整体流程较规范。",
                "source": "知乎"
            },
        ],
        "strengths": [
            "种草心智最强的生活方式社区，消费决策影响力突出",
            "搜索转化率高，用户主动获取品牌信息的首选平台",
            "女性用户占比高，美妆/时尚/家居等垂类内容领先",
        ],
        "roadmap": ["种草直达", "KOS员工号", "合作广场升级"],
        "insight": "小红书蒲公英商业化强势加速，2026年正式进入商业流量时代，付费内容获得流量优先权。"
    },

    "kuaishou_cilijuXing": {
        "name": "快手磁力聚星",
        "color": "#FF6900",
        "updates": [
            {
                "title": "快手磁力聚星产品全面升级：重塑平台体验，全周期服务提升达人与品牌连接效率",
                "url": "https://tech.huanqiu.com/article/403EkZOcxlH",
                "summary": "升级后的磁力聚星重塑了平台体验，为客户提供全周期服务，基于全域分发优质内容，助力内容和生意一拍即合。",
                "source": "环球网",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
        ],
        "feedback": [
            {
                "title": "快手磁力聚星团长申请开通指南：条件与注意事项",
                "url": "https://www.zhihu.com/question/638477542",
                "summary": "磁力聚星平台是快手官方唯一达人生态营销平台。创作者普遍认可平台安全性。",
                "source": "知乎"
            },
        ],
        "strengths": [
            "下沉市场渗透率最高，三四线城市用户基础深厚",
            "老铁经济社区信任度高，电商复购率突出",
            "短视频+直播双栖生态，达人变现路径短",
        ],
        "roadmap": ["AI技术落地", "品聚营销", "公私域打通"],
        "insight": "快手磁力聚星产品全面升级，达人数突破460万。公私域流量打通取得显著成果。"
    }
}


def generate_platform_section(platform_key: str, data: dict) -> str:
    """生成单个平台的HTML内容"""

    update_count = len(data.get("updates", []))
    feedback_count = len(data.get("feedback", []))

    updates_html = ""
    for i, item in enumerate(data.get("updates", []), 1):
        updates_html += f'''
                  <div class="news-item">
                    <div class="news-num">{i:02d}</div>
                    <div class="news-content">
                      <a class="news-title-link" href="{item['url']}" target="_blank">{item['title']}</a>
                      <p class="news-summary">{item['summary']}</p>
                      <div class="news-footer">
                        <span class="news-source-tag">{item['source']}</span>
                        <span class="news-date">{item['date']}</span>
                      </div>
                    </div>
                  </div>'''

    feedback_html = ""
    for i, item in enumerate(data.get("feedback", []), 1):
        feedback_html += f'''
                  <div class="news-item">
                    <div class="news-num">{i:02d}</div>
                    <div class="news-content">
                      <a class="news-title-link" href="{item['url']}" target="_blank">{item['title']}</a>
                      <p class="news-summary">{item['summary']}</p>
                      <div class="news-footer">
                        <span class="news-source-tag">{item['source']}</span>
                      </div>
                    </div>
                  </div>'''

    strengths_html = ""
    for s in data.get("strengths", []):
        strengths_html += f'<div class="strength-item"><span class="strength-dot" style="background:{data["color"]}"></span>{s}</div>'

    roadmap_html = ""
    for tag in data.get("roadmap", []):
        roadmap_html += f'<span class="dir-tag" style="border-color:rgba{tuple(int(data["color"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))},.25);color:{data["color"]};background:rgba{tuple(int(data["color"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))},.06)">{tag}</span>'

    return f'''
      <div class="section" id="{platform_key}">
        <div class="section-head">
          <h2>{data['name']}</h2>
          <span class="section-tag">{update_count} 条动态 · {feedback_count} 条反馈</span>
        </div>
        <div class="section-divider"></div>
        <div class="platform-block">
          <div class="platform-header">
            <div class="platform-icon">📺</div>
            <div class="platform-meta">
              <h3>{data['name']}</h3>
              <a href="#" target="_blank" class="url">
                <svg width="10" height="10" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 2H2a1 1 0 00-1 1v7a1 1 0 001 1h7a1 1 0 001-1V7M8 1h3m0 0v3m0-3L5 7"/></svg>
                {data['name']}
              </a>
            </div>
            <div class="platform-stats">
              <span class="stat-pill"><span class="text-green">●</span> {update_count} Updates</span>
              <span class="stat-pill"><span style="color:var(--accent)">●</span> {feedback_count} Feedback</span>
            </div>
          </div>
          <div class="platform-body">
            <div class="platform-main">
              <div class="sub-card">
                <div class="sub-card-title">
                  <svg width="11" height="11" viewBox="0 0 12 12" fill="currentColor" opacity=".5"><circle cx="6" cy="6" r="5"/></svg>
                  Latest Updates
                </div>
                <div class="news-list">
                  {updates_html}
                </div>
              </div>
              <div class="sub-card-divider"></div>
              <div class="sub-card">
                <div class="sub-card-title">
                  <svg width="11" height="11" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".5"><path d="M6 1v5l3 3"/><circle cx="6" cy="6" r="5"/></svg>
                  User Feedback
                </div>
                <div class="news-list">
                  {feedback_html}
                </div>
              </div>
            </div>
            <div class="platform-sidebar">
              <div class="sub-card">
                <div class="sub-card-title">Core Strengths</div>
                <div class="strength-list">
                  {strengths_html}
                </div>
              </div>
              <div class="sub-card-divider"></div>
              <div class="sub-card">
                <div class="sub-card-title">Product Roadmap</div>
                <div class="tag-cloud">
                  {roadmap_html}
                </div>
              </div>
              <div class="sub-card-divider"></div>
              <div class="insight" style="border-left-color:{data['color']}">
                {data['insight']}
              </div>
            </div>
          </div>
        </div>
      </div>'''


def main():
    """主函数 - 生成更新的HTML"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始生成数据...")

    # 保存数据到JSON文件（方便后续读取和更新）
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump({
            "last_updated": datetime.now().isoformat(),
            "platforms": DATA_SOURCE
        }, f, ensure_ascii=False, indent=2)

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 数据已保存到 data.json")

    # 如果需要自动提交到Git
    # subprocess.run(["git", "add", "."])
    # subprocess.run(["git", "commit", "-m", f"Update data: {datetime.now().strftime('%Y-%m-%d')}"])
    # subprocess.run(["git", "push"])

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 完成!")


if __name__ == "__main__":
    main()
