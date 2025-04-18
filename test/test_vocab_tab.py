import unittest
from unittest.mock import patch, MagicMock
import gradio as gr
# 将 src 目录添加到模块搜索路径
import sys
sys.path.insert(0, '/mnt/teacherCode/LanguageMentor/src')

from tabs.vocab_tab import create_vocab_tab

class TestVocabTab(unittest.TestCase):
    @patch('tabs.vocab_tab.gr.Tab')
    @patch('tabs.vocab_tab.gr.ChatInterface')
    def test_create_vocab_tab(self, mock_chat_interface, mock_tab):
        with gr.Blocks(title="LanguageMentor 英语私教") as language_mentor_app:
            # 调用函数
            create_vocab_tab()

        # 验证 Tab 是否被创建
        mock_tab.assert_called_once_with("单词")

        # 验证 ChatInterface 是否被调用
        mock_chat_interface.assert_called_once()

if __name__ == '__main__':
    unittest.main()