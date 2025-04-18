import unittest
from unittest.mock import patch, mock_open, MagicMock

# 将 src 目录添加到模块搜索路径
import sys
sys.path.insert(0, '/mnt/teacherCode/LanguageMentor/src')

from agents.scenario_agent import ScenarioAgent

class TestScenarioAgent(unittest.TestCase):

    @patch('agents.scenario_agent.random.choice')
    def test_start_new_session(self, mock_random_choice):
        # 模拟文件内容
        with patch('builtins.open', mock_open(read_data='{"as":"zhaowang"}')):
            agent = ScenarioAgent(scenario_name="job_interview")

        # 模拟随机选择初始消息
        mock_random_choice.return_value = "Initial message"

        # 调用函数
        result = agent.start_new_session()

        # 验证初始消息是否正确
        self.assertEqual(result, "Initial message")

if __name__ == '__main__':
    unittest.main()