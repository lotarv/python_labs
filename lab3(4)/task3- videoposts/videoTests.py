import pytest
import time
from video import split_videos
def test_positive_cases():
    assert split_videos(6, 3, [3, 3, 1, 4, 1, 6]) == "Да\n2 3 1"
    assert split_videos(3, 3, [1, 1, 1]) == "Да\n1 1 1"
    assert split_videos(3, 1, [1, 10, 100]) == "Да\n3"


def test_negative_cases():
    assert split_videos(3,3,[1,1,2]) == "Нет"
    assert split_videos(10,7,[1,2,3,4,5,6,7,8,9,10]) == "Нет"
    assert split_videos(2,2,[1,4]) == "Нет"

def test_performance():
    n = 100000
    k = 10
    durations = [10]*n
    start_time = time.time()
    result = split_videos(n,k,durations)
    time_passed = time.time() - start_time
    assert time_passed < 3 #Укладывается ли в 3 секунды
    assert result.startswith("Да")