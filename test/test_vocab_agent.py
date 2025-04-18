import unittest
from unittest.mock import patch, MagicMock

# 将 src 目录添加到模块搜索路径
import sys
sys.path.insert(0, '/mnt/teacherCode/LanguageMentor/src')

from agents.vocab_agent import VocabAgent

class TestVocabAgent(unittest.TestCase):
    @patch('agents.vocab_agent.get_session_history')
    def test_restart_session(self, mock_get_session_history):
        # 模拟会话历史
        mock_history = MagicMock()
        mock_get_session_history.return_value = mock_history

        agent = VocabAgent()
        result = agent.restart_session()

        # 验证会话历史是否被清除
        mock_history.clear.assert_called_once()

if __name__ == '__main__':
    unittest.main()