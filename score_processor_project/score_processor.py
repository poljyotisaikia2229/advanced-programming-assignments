from typing import Final


class ScoreProcessor:
    """
    Utility class responsible for safely reading,
    validating, and processing score data from a file.
    """

    MULTIPLIER: Final[int] = 10

    def process_score_file(self, file_path: str) -> int:
        """
        Reads a numeric score from a file, multiplies it by 10,
        and returns the processed result.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                raw_value = file.read().strip()
                score = int(raw_value)

        except FileNotFoundError as error:
            print(f"Error: File not found -> {file_path}")
            raise error

        except ValueError as error:
            print(
                f"Error: Invalid numeric data encountered in file -> {file_path}"
            )
            raise error

        else:
            processed_score = score * self.MULTIPLIER
            print("Data processed successfully")
            return processed_score

        finally:
            print("File cleanup completed")