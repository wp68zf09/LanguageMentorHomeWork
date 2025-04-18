import unittest
from unittest.mock import patch, MagicMock

# 将 src 目录添加到模块搜索路径
import sys
sys.path.insert(0, '/mnt/teacherCode/LanguageMentor/src')

from tabs.conversation_tab import create_conversation_tab

class TestConversationTab(unittest.TestCase):
    @patch('tabs.conversation_tab.gr.Tab')
    @patch('tabs.conversation_tab.gr.ChatInterface')
    def test_create_conversation_tab(self, mock_chat_interface, mock_tab):
        # 调用函数
        create_conversation_tab()

        # 验证 Tab 是否被创建
        mock_tab.assert_called_once_with("对话")

        # 验证 ChatInterface 是否被调用
        mock_chat_interface.assert_called_once()

if __name__ == '__main__':
    unittest.main()