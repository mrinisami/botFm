import unittest

from src.deserializer.exchange_craft_results import deserialize_4294
from src.protocol.fm_results import FmResults, ObjectEffect
from src.socket.buffer import Buffer
from src.message.app_message import AppMessage, parseMsgs


class ParseMessagesTests(unittest.TestCase):
    def test__parse_messages(self):
        buffer = Buffer.from_str(
            "43190f01e55a0001143e7c12ce97a72201014a090f003fe55a0001143e7c12ce97a72201441905a318fa840116a4")
        expected = [AppMessage(id=4294, msg=Buffer.from_str("01e55a0001143e7c12ce97a7220101"), len_data=15),
                    AppMessage(id=4738, msg=Buffer.from_str("003fe55a0001143e7c12ce97a72201"), len_data=15),
                    AppMessage(id=4358, msg=Buffer.from_str("a318fa8401"), len_data=5)]

        result = parseMsgs(buffer)

        self.assertEqual(expected, result)

