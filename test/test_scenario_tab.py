import unittest
from unittest.mock import patch, MagicMock
from gradio import Radio, Chatbot, ChatInterface, Tab, Markdown
import gradio as gr
# 将 src 目录添加到模块搜索路径
import sys
sys.path.insert(0, '/mnt/teacherCode/LanguageMentor/src')

from tabs.scenario_tab import create_scenario_tab

class TestScenarioTab(unittest.TestCase):
    @patch('tabs.scenario_tab.gr.Tab')
    @patch('tabs.scenario_tab.gr.Radio')
    def test_create_scenario_tab(self, mock_radio, mock_tab):
       # 返回一个实际的 Radio 组件实例
        mock_radio.return_value = Radio(
            choices=[
                ("求职面试", "job_interview"),
                ("酒店入住", "hotel_checkin"),
            ],
            label="场景"
        )
        with gr.Blocks(title="LanguageMentor 英语私教") as language_mentor_app:
            # 调用函数
            create_scenario_tab()

        # 验证 Tab 是否被创建
        mock_tab.assert_called_once_with("场景")

        # 验证 Radio 是否被调用
        mock_radio.assert_called_once()

if __name__ == '__main__':
    unittest.main()