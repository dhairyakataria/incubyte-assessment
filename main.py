class StringCalculator:
    def add_str(self, str_numbers: str) -> int:
        if not str_numbers:
            return 0
        
        # Check for trailing comma followed by newline
        if ",\n" in str_numbers:
            raise ValueError("Invalid input format: trailing comma followed by newline")

        # Strip leading and trailing whitespaces in str if any
        str_numbers = str_numbers.strip()

        # Default delimiter
        delimiter = ","
        
        # Check for custom delimiter
        if str_numbers.startswith("//"):
            delimiter_line, str_numbers = str_numbers.split("\n", 1)
            delimiter = delimiter_line[2:]

        # Split numbers using delimiter and new line
        split_numbers = []
        for part in str_numbers.split(delimiter):
            if "\n" in part:
                split_numbers.extend(part.split("\n"))
            else:
                split_numbers.append(part)

        # Convert numbers to integers and filter out empty strings
        numbers_list = [int(num) for num in split_numbers if num]
        return sum(numbers_list)
    