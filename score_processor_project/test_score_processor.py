import os
import tempfile
import pytest

from score_processor import ScoreProcessor


def test_process_score_file_success():
    processor = ScoreProcessor()

    with tempfile.NamedTemporaryFile(
        mode="w",
        delete=False,
        encoding="utf-8"
    ) as temp_file:
        temp_file.write("7")
        temp_file_path = temp_file.name

    try:
        result = processor.process_score_file(temp_file_path)

        assert result == 70

    finally:
        os.remove(temp_file_path)


def test_process_score_file_missing_file():
    processor = ScoreProcessor()

    with pytest.raises(FileNotFoundError):
        processor.process_score_file("missing_file.txt")


def test_process_score_file_invalid_data():
    processor = ScoreProcessor()

    with tempfile.NamedTemporaryFile(
        mode="w",
        delete=False,
        encoding="utf-8"
    ) as temp_file:
        temp_file.write("abc")
        temp_file_path = temp_file.name

    try:
        with pytest.raises(ValueError):
            processor.process_score_file(temp_file_path)

    finally:
        os.remove(temp_file_path)