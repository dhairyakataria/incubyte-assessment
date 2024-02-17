class StringCalculator:
    def add_str(self, str_numbers: str) -> int:
        if not str_numbers:
            return 0
        
        delimiter = ","

        # Split the numbers using delimiter or newline
        numbers_list = str_numbers.split(",")
        
        # Remove the extra white spaces before and after the number if any
        numbers_list = [num.strip() for num in numbers_list]
        
        # Convert numbers to integers and filter out empty strings
        numbers_list = [int(num) for num in numbers_list if num]
        return sum(numbers_list)