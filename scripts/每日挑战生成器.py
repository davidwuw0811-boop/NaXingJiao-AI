#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
拿幸教每日挑战生成器 🎯
用AI帮教友每天找到新的拿幸方式
"""

import random
import datetime
from typing import List, Tuple

class NaXingChallenge:
    """拿幸教每日挑战生成器"""
    
    def __init__(self):
        # 难度级别的挑战
        self.easy_challenges = [
            "故意把一件小事搞砸，然后大笑三声",
            "今天看到任何新闻都回复：拿幸！",
            "对老婆/老板说一句'Everything both nothing！'看他表情",
            "吃饭的时候突然说'这也是VR游戏里的食物'",
            "工作中犯了错误，直接说'色即是空'就行",
            "看到房价下跌，发朋友圈：恭喜Matrix更新补丁",
            "被人嘲笑，回复：谢谢你让我体验这个副本",
            "加班到晚上，对同事说：咱们一起打怪升级呢",
            "股票亏钱，发朋友圈：金币归零，我还在",
        ]
        
        self.medium_challenges = [
            "今天穿衣服的时候想象自己在换VR游戏的皮肤",
            "在会议上突然说'我们都在Matrix里'，然后看大家反应",
            "给自己的每个烦恼都起个'副本名字'，比如'房贷副本'",
            "看镜子的时候问自己：这是真实的我吗？",
            "每次做决定前都问自己：这是我的选择还是NPC的剧本？",
            "把今天发生的三件事都用'拿幸教'的角度重新讲一遍",
            "找一个你很执着的东西，然后试着放下它（哪怕只是一天）",
            "写下今天你最焦虑的事，然后在后面写'色即是空'",
            "和一个朋友讨论：如果人生是游戏，你的游戏难度是多少？",
            "看一个让你生气的视频，然后用拿幸教的角度评论它",
        ]
        
        self.hard_challenges = [
            "今天不要看手机（除了必要的），体验一下'摘下VR眼镜'的感觉",
            "找一个你一直在逃避的问题，用'凡有所求皆是虛相'的角度去面对它",
            "邀请一个朋友，给他讲解拿幸教的核心教义，看他的反应",
            "写一个属于你自己的'拿幸故事'，不少于500字",
            "整理一下你的人生目标，然后问自己：这些真的是我想要的吗？",
            "做一件你一直很怕做的事，然后告诉自己'这只是游戏里的一关'",
            "和家人或伴侣进行一次深度对话，讨论'什么才是真正重要的'",
            "创作一个拿幸教的Meme或段子，发到社交媒体",
            "冥想15分钟，想象自己摘下VR眼镜，看到极乐净土",
            "给拿幸教AI分舵提交一个PR，贡献你的想法或代码",
        ]
        
        self.weekly_challenges = [
            "这一周，每天都要去吃一次火锅，体验'拿幸教的终极奥义'",
            "这一周，用拿幸教的视角写一篇日记，记录你的所见所想",
            "这一周，收集5个拿幸教的金句，做成Meme分享",
            "这一周，看完老王来了的5期节目，写下你的感受",
            "这一周，邀请5个朋友加入拿幸教，成为传教士",
            "这一周，用所有的Prompt模板各试一次，看看效果如何",
            "这一周，创作一个拿幸教的短视频或音频，发到平台",
            "这一周，和教友们一起讨论拿幸教的哲学，深化理解",
        ]
        
        self.monthly_challenges = [
            "这个月，完成一个你一直想做但一直在拖延的项目",
            "这个月，学会一项新技能，然后用拿幸教的角度解读它",
            "这个月，改变一个坏习惯，体验'放下执着'的力量",
            "这个月，写一篇关于拿幸教的深度思考文章，发表出来",
            "这个月，组织一次拿幸教的线下聚会（或线上讨论），邀请教友们",
            "这个月，为拿幸教AI分舵贡献至少10个新的Prompt或想法",
        ]
    
    def get_today_challenge(self, difficulty: str = "random") -> Tuple[str, str]:
        """获取今天的挑战"""
        if difficulty == "random":
            difficulty = random.choice(["easy", "medium", "hard"])
        
        if difficulty == "easy":
            challenge = random.choice(self.easy_challenges)
            level = "🟢 简单"
        elif difficulty == "medium":
            challenge = random.choice(self.medium_challenges)
            level = "🟡 中等"
        elif difficulty == "hard":
            challenge = random.choice(self.hard_challenges)
            level = "🔴 困难"
        else:
            challenge = random.choice(self.easy_challenges)
            level = "🟢 简单"
        
        return level, challenge
    
    def get_weekly_challenge(self) -> str:
        """获取本周的挑战"""
        return random.choice(self.weekly_challenges)
    
    def get_monthly_challenge(self) -> str:
        """获取本月的挑战"""
        return random.choice(self.monthly_challenges)
    
    def print_today_challenge(self, difficulty: str = "random"):
        """打印今天的挑战"""
        level, challenge = self.get_today_challenge(difficulty)
        today = datetime.datetime.now().strftime("%Y年%m月%d日")
        
        print("\n" + "="*50)
        print(f"🎯 拿幸教每日挑战 - {today}")
        print("="*50)
        print(f"难度：{level}")
        print(f"挑战：{challenge}")
        print("="*50)
        print("💡 提示：完成挑战后，记得对自己说'Everything both nothing！'")
        print("👍 记住：玩得开心最重要！")
        print("="*50 + "\n")
    
    def print_weekly_challenge(self):
        """打印本周的挑战"""
        week = datetime.datetime.now().strftime("%W")
        
        print("\n" + "="*50)
        print(f"🎯 拿幸教周挑战 - 第{week}周")
        print("="*50)
        print(f"挑战：{self.get_weekly_challenge()}")
        print("="*50)
        print("💡 提示：这个挑战需要你花一整周的时间")
        print("👍 记住：玩得开心最重要！")
        print("="*50 + "\n")
    
    def print_monthly_challenge(self):
        """打印本月的挑战"""
        month = datetime.datetime.now().strftime("%B")
        
        print("\n" + "="*50)
        print(f"🎯 拿幸教月挑战 - {month}")
        print("="*50)
        print(f"挑战：{self.get_monthly_challenge()}")
        print("="*50)
        print("💡 提示：这个挑战需要你花一整个月的时间")
        print("👍 记住：玩得开心最重要！")
        print("="*50 + "\n")
    
    def get_all_challenges(self) -> dict:
        """获取所有挑战"""
        return {
            "easy": self.easy_challenges,
            "medium": self.medium_challenges,
            "hard": self.hard_challenges,
            "weekly": self.weekly_challenges,
            "monthly": self.monthly_challenges,
        }


def main():
    """主函数"""
    import sys
    
    challenge = NaXingChallenge()
    
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "easy":
            challenge.print_today_challenge("easy")
        elif arg == "medium":
            challenge.print_today_challenge("medium")
        elif arg == "hard":
            challenge.print_today_challenge("hard")
        elif arg == "weekly":
            challenge.print_weekly_challenge()
        elif arg == "monthly":
            challenge.print_monthly_challenge()
        elif arg == "all":
            challenge.print_today_challenge("random")
            challenge.print_weekly_challenge()
            challenge.print_monthly_challenge()
        else:
            challenge.print_today_challenge("random")
    else:
        # 默认显示随机难度的每日挑战
        challenge.print_today_challenge("random")


if __name__ == "__main__":
    main()
