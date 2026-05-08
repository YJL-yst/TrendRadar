import os
import requests
from datetime import datetime

# 企业微信机器人Webhook
WEBHOOK_URL = os.getenv("WECOM_WEBHOOK")

def send_wecom_review(content):
    """发送复盘消息到企业微信群"""
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }
    response = requests.post(WEBHOOK_URL, json=data)
    print(f"推送结果: {response.status_code}, {response.text}")

def generate_markdown_review():
    """生成晚间复盘Markdown内容模板"""
    today = datetime.now().strftime("%Y年%m月%d日")
    content = f"""📅 {today} 20:00 晚间复盘

【市场总览】
沪指：待更新
深成指：待更新 | 创业板：待更新
成交额：待更新
涨跌家数：待更新
涨停：待更新 | 跌停：待更新 | 炸板率：待更新

【北向资金】
当日净流入：待更新
十大成交活跃股：待更新

【主线板块】
1. 商业航天：待更新
2. 人形机器人：待更新
3. 国防军工：待更新

【市场情绪】
- 连板高度：待更新
- 连板梯队：待更新
- 首板数量：待更新
- 炸板率：待更新

【龙虎榜动向】
- 机构净买入TOP3：待更新
- 游资动向：待更新

【晚间重要公告/新闻】
待更新

【次日前瞻】
- 主线延续性：待更新
- 风险提示：待更新
- 关注方向：待更新
"""
    return content

if __name__ == "__main__":
    print("开始生成晚间复盘内容...")
    review_content = generate_markdown_review()
    send_wecom_review(review_content)
    print("复盘推送完成！")
