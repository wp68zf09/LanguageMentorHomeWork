import unittest
from unittest.mock import patch, mock_open, MagicMock

# 将 src 目录添加到模块搜索路径
import sys
sys.path.insert(0, '/mnt/teacherCode/LanguageMentor/src')

from agents.agent_base import AgentBase

class TestAgentBase(unittest.TestCase):
    @patch('agents.agent_base.get_session_history')
    @patch('agents.agent_base.ChatOllama')
    def test_agent_initialization(self, mock_chat_ollama, mock_get_session_history):
        # 模拟文件内容
        mock_open_data = {'prompts/test_prompt.txt': 'Test prompt'}
        with patch('builtins.open', mock_open(read_data='Test prompt')):
            agent = AgentBase(name="test", prompt_file="prompts/test_prompt.txt")

        # 验证初始化
        self.assertEqual(agent.name, "test")
        self.assertEqual(agent.prompt, "Test prompt")

        # 验证 ChatOllama 是否被调用
        mock_chat_ollama.assert_called_once()

    @patch('agents.agent_base.LOG.debug')
    def test_chat_with_history(self, mock_log_debug):
        # 模拟会话历史
        mock_history = MagicMock()
        mock_history.messages = []
        with patch('agents.agent_base.get_session_history', return_value=mock_history):
            agent = AgentBase(name="test", prompt_file="prompts/test_prompt.txt")
            response = agent.chat_with_history("你是谁")

        # 验证日志记录
        mock_log_debug.assert_called()

if __name__ == '__main__':
    unittest.main()